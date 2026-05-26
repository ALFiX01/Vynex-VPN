from __future__ import annotations

import os
import threading

import pytest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
pytest.importorskip("PySide6")
pytest.importorskip("pytestqt")

from PySide6.QtCore import Qt  # noqa: E402
from PySide6.QtWidgets import QLabel, QSizePolicy  # noqa: E402

from vynex_vpn_client.app_service import ComponentsStatus  # noqa: E402
from vynex_vpn_client.gui.main_window import MainWindow  # noqa: E402
from vynex_vpn_client.models import AppSettings, RuntimeState, ServerEntry, SubscriptionEntry  # noqa: E402


class FakeService:
    def __init__(self) -> None:
        self.server = ServerEntry.new(
            name="Alpha",
            protocol="vless",
            host="example.com",
            port=443,
            raw_link="vless://test@example.com:443",
        )
        self.servers = [self.server]
        self.state = RuntimeState()
        self.settings = AppSettings(connection_mode="PROXY", set_system_proxy=True)
        self.connect_started = threading.Event()
        self.release_connect = threading.Event()

    def get_current_state(self) -> RuntimeState:
        return self.state

    def list_servers(self, *, sorted_by_name: bool = False) -> list[ServerEntry]:
        return list(self.servers)

    def list_subscriptions(self):
        return []

    def get_settings(self, *, validated: bool = True) -> AppSettings:
        return self.settings

    def get_components_status(self) -> ComponentsStatus:
        return ComponentsStatus(items=())

    def list_routing_profiles(self):
        return []

    def available_app_update(self):
        return None

    def get_cached_app_update(self):
        return None

    def can_self_update(self) -> bool:
        return False

    def best_tcp_ping_server(self, servers=None):
        return None

    def list_winws_conflicts(self):
        return ()

    def get_runtime_status(self, *, run_healthcheck: bool = False):
        raise RuntimeError("not implemented in fake")

    def connect(self, server_id: str, *, progress_callback=None):
        self.connect_started.set()
        if progress_callback is not None:
            progress_callback("Запуск ядра подключения")
        self.release_connect.wait(timeout=3)
        self.state = RuntimeState(
            pid=1234,
            backend_id="xray",
            mode="PROXY",
            server_id=server_id,
            routing_profile_name="Default",
        )
        return object()

    def disconnect(self):
        self.state = RuntimeState()
        return self.state


def test_main_window_renders_connection_summary(qtbot) -> None:
    service = FakeService()
    service.state = RuntimeState(
        pid=1234,
        backend_id="xray",
        mode="PROXY",
        server_id=service.server.id,
        routing_profile_name="Default",
    )
    window = MainWindow(service=service)
    qtbot.addWidget(window)

    assert window.status_value.text() == "Подключено"
    assert window.active_server_value.text() == "Alpha"
    assert window.mode_value.text() == "PROXY"
    assert window.backend_value.text() == "Xray"
    assert window.pid_value.text() == "1234"
    assert window.connect_button.text() == "Отключиться"


def test_connect_button_runs_connect_in_background(qtbot) -> None:
    service = FakeService()
    window = MainWindow(service=service)
    qtbot.addWidget(window)

    assert window.connect_button.isEnabled() is True
    assert window.servers_table.currentRow() == 0
    assert window.connection_selected_server_value.text() == "Alpha"

    qtbot.mouseClick(window.connect_button, Qt.MouseButton.LeftButton)

    assert service.connect_started.wait(timeout=3)
    assert window.connect_button.isEnabled() is False

    service.release_connect.set()
    qtbot.waitUntil(lambda: window._active_worker is None, timeout=3000)
    assert window.status_value.text() == "Подключено"


def test_connection_page_embeds_server_table_and_details(qtbot) -> None:
    service = FakeService()
    service.servers = [
        ServerEntry.new(
            name=f"Alpha {index}",
            protocol="vless",
            host=f"example{index}.com",
            port=443,
            raw_link=f"vless://test{index}@example.com:443",
        )
        for index in range(10)
    ]
    service.server = service.servers[0]
    window = MainWindow(service=service)
    qtbot.addWidget(window)

    window.resize(1600, 950)
    window.show()

    assert window.servers_table.rowCount() == 10
    assert window.server_detail_labels["address"].text() == "example0.com"
    assert window.server_detail_labels["port"].text() == "443"
    assert window.servers_table.sizePolicy().verticalPolicy() == QSizePolicy.Policy.Expanding


def test_subscriptions_table_counts_actual_owned_servers(qtbot) -> None:
    service = FakeService()
    subscription = SubscriptionEntry.new(url="https://example.com/sub", title="Example")
    subscription.id = "sub-1"
    subscription.server_ids = ["missing-1", "missing-2"]
    service.server.source = "subscription"
    service.server.subscription_id = subscription.id
    service.list_subscriptions = lambda: [subscription]

    window = MainWindow(service=service)
    qtbot.addWidget(window)

    assert window.subscriptions_table.item(0, 2).text() == "1"


def test_connection_empty_state_guides_import(qtbot) -> None:
    service = FakeService()
    service.servers = []
    window = MainWindow(service=service)
    qtbot.addWidget(window)

    assert window.connect_button.isEnabled() is False
    assert window.connection_selected_server_value.text() == "Импортируйте сервер"
    assert window.servers_empty_state is not None
    assert any("Добавить сервер" in label.text() for label in window.servers_empty_state.findChildren(QLabel))
