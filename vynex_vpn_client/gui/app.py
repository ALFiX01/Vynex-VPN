from __future__ import annotations

import ctypes
import sys

from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QColor, QFont, QPalette
from PySide6.QtNetwork import QAbstractSocket, QLocalServer, QLocalSocket
from PySide6.QtWidgets import QApplication, QSystemTrayIcon

from vynex_vpn_client.constants import APP_NAME, APP_VERSION

from . import design_tokens as tokens
from .main_window import MainWindow


SINGLE_INSTANCE_SERVER_NAME = "VynexVPNClient.SingleInstance"
SINGLE_INSTANCE_ACTIVATE_MESSAGE = b"activate\n"


class SingleInstanceServer(QObject):
    activate_requested = Signal()

    def __init__(self, server_name: str, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self._server_name = server_name
        self._server = QLocalServer(self)
        self._server.setSocketOptions(QLocalServer.SocketOption.UserAccessOption)
        self._server.newConnection.connect(self._handle_new_connection)

    def listen(self) -> bool:
        return self._server.listen(self._server_name)

    def server_error(self) -> QAbstractSocket.SocketError:
        return self._server.serverError()

    def remove_stale_server(self) -> None:
        QLocalServer.removeServer(self._server_name)

    def close(self) -> None:
        self._server.close()
        QLocalServer.removeServer(self._server_name)

    def _handle_new_connection(self) -> None:
        while self._server.hasPendingConnections():
            socket = self._server.nextPendingConnection()
            if socket is None:
                continue
            socket.setParent(self)
            socket.readyRead.connect(lambda socket=socket: self._handle_socket_ready(socket))
            socket.disconnected.connect(socket.deleteLater)
            if socket.bytesAvailable() > 0:
                self._handle_socket_ready(socket)

    def _handle_socket_ready(self, socket: QLocalSocket) -> None:
        message = bytes(socket.readAll()).strip()
        if message == SINGLE_INSTANCE_ACTIVATE_MESSAGE.strip():
            self.activate_requested.emit()
        socket.disconnectFromServer()


def _notify_existing_instance(server_name: str, *, timeout_ms: int = 250) -> bool:
    socket = QLocalSocket()
    socket.connectToServer(server_name)
    if not socket.waitForConnected(timeout_ms):
        socket.abort()
        return False
    socket.write(SINGLE_INSTANCE_ACTIVATE_MESSAGE)
    socket.flush()
    socket.waitForBytesWritten(timeout_ms)
    socket.disconnectFromServer()
    return True


def _set_windows_app_user_model_id() -> None:
    if sys.platform != "win32":
        return
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            f"Vynex.VPNClient.{APP_VERSION}"
        )
    except Exception:
        pass


def _apply_base_style(app: QApplication) -> None:
    app.setStyle("Fusion")
    app.setFont(QFont(tokens.FONT_FAMILY, tokens.FONT_POINT_SIZE))

    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(tokens.COLOR_BG))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(tokens.COLOR_TEXT_PRIMARY))
    palette.setColor(QPalette.ColorRole.Base, QColor(tokens.COLOR_SURFACE_ALT))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(tokens.COLOR_SURFACE))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(tokens.COLOR_SURFACE))
    palette.setColor(QPalette.ColorRole.ToolTipText, QColor(tokens.COLOR_TEXT_PRIMARY))
    palette.setColor(QPalette.ColorRole.Text, QColor(tokens.COLOR_TEXT_PRIMARY))
    palette.setColor(QPalette.ColorRole.Button, QColor(tokens.COLOR_SURFACE))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(tokens.COLOR_TEXT_PRIMARY))
    palette.setColor(QPalette.ColorRole.BrightText, QColor(tokens.COLOR_TEXT_INVERSE))
    palette.setColor(QPalette.ColorRole.Link, QColor(tokens.COLOR_PRIMARY))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(tokens.COLOR_SELECTION))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(tokens.COLOR_TEXT_INVERSE))
    palette.setColor(QPalette.ColorRole.PlaceholderText, QColor(tokens.COLOR_TEXT_DISABLED))
    app.setPalette(palette)

    app.setStyleSheet(tokens.app_stylesheet())


def run_gui(argv: list[str] | None = None) -> int:
    _set_windows_app_user_model_id()
    app = QApplication(argv if argv is not None else sys.argv)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setOrganizationName("Vynex")
    if _notify_existing_instance(SINGLE_INSTANCE_SERVER_NAME):
        return 0
    single_instance_server = SingleInstanceServer(SINGLE_INSTANCE_SERVER_NAME, app)
    if not single_instance_server.listen():
        if (
            single_instance_server.server_error() == QAbstractSocket.SocketError.AddressInUseError
            and _notify_existing_instance(SINGLE_INSTANCE_SERVER_NAME, timeout_ms=1000)
        ):
            return 0
        single_instance_server.remove_stale_server()
        if _notify_existing_instance(SINGLE_INSTANCE_SERVER_NAME):
            return 0
        single_instance_server.listen()
    if QSystemTrayIcon.isSystemTrayAvailable():
        app.setQuitOnLastWindowClosed(False)
    _apply_base_style(app)

    window = MainWindow()
    single_instance_server.activate_requested.connect(window.show_normal)
    app.aboutToQuit.connect(single_instance_server.close)
    window.show()
    return app.exec()


def main() -> int:
    return run_gui()


if __name__ == "__main__":
    raise SystemExit(main())
