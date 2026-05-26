from __future__ import annotations

import socket
from types import SimpleNamespace
from unittest.mock import Mock, patch

import psutil

from vynex_vpn_client.utils import _powershell_utf8_command
from vynex_vpn_client.utils import RunningProcessDetails, terminate_running_processes, wait_for_tun_interface_details


def test_powershell_utf8_command_forces_utf8_io() -> None:
    command = _powershell_utf8_command("Get-NetAdapter | ConvertTo-Json -Compress")

    assert "[Console]::InputEncoding = [System.Text.Encoding]::UTF8" in command
    assert "[Console]::OutputEncoding = [System.Text.Encoding]::UTF8" in command
    assert "$OutputEncoding = [System.Text.Encoding]::UTF8" in command
    assert command.endswith("Get-NetAdapter | ConvertTo-Json -Compress")


def test_terminate_running_processes_falls_back_to_taskkill_when_wait_access_is_denied() -> None:
    process_info = RunningProcessDetails(pid=12552, name="winws2.exe")
    process = Mock()
    process.pid = process_info.pid
    process.name.return_value = process_info.name
    process.wait.side_effect = psutil.AccessDenied(pid=process_info.pid, name=process_info.name)

    with (
        patch("vynex_vpn_client.utils.psutil.Process", return_value=process),
        patch("vynex_vpn_client.utils.time.sleep"),
        patch("vynex_vpn_client.utils._is_running_process_match", side_effect=[True, False]),
        patch("vynex_vpn_client.utils.subprocess.run") as run,
    ):
        failed = terminate_running_processes([process_info], timeout=0.0, kill_timeout=0.0)

    assert failed == []
    process.terminate.assert_called_once_with()
    process.kill.assert_called_once_with()
    run.assert_called_once()
    assert run.call_args.args[0] == ["taskkill", "/PID", str(process_info.pid), "/T"]


def test_terminate_running_processes_reports_failure_when_taskkill_does_not_stop_process() -> None:
    process_info = RunningProcessDetails(pid=12552, name="winws2.exe")
    process = Mock()
    process.pid = process_info.pid
    process.name.return_value = process_info.name
    process.wait.side_effect = psutil.AccessDenied(pid=process_info.pid, name=process_info.name)

    with (
        patch("vynex_vpn_client.utils.psutil.Process", return_value=process),
        patch("vynex_vpn_client.utils.time.sleep"),
        patch("vynex_vpn_client.utils._is_running_process_match", return_value=True),
        patch("vynex_vpn_client.utils.subprocess.run") as run,
    ):
        failed = terminate_running_processes([process_info], timeout=0.0, kill_timeout=0.0)

    assert failed == [process_info]
    assert run.call_count == 2
    assert run.call_args_list[0].args[0] == ["taskkill", "/PID", str(process_info.pid), "/T"]
    assert run.call_args_list[1].args[0] == ["taskkill", "/PID", str(process_info.pid), "/T", "/F"]


def test_wait_for_tun_interface_details_uses_fast_psutil_path() -> None:
    with (
        patch(
            "vynex_vpn_client.utils.psutil.net_if_stats",
            return_value={"VynexTun": SimpleNamespace(isup=True)},
        ),
        patch(
            "vynex_vpn_client.utils.psutil.net_if_addrs",
            return_value={
                "VynexTun": [
                    SimpleNamespace(family=socket.AF_INET, address="169.254.10.5"),
                ],
            },
        ),
        patch("vynex_vpn_client.utils.socket.if_nametoindex", return_value=17),
        patch("vynex_vpn_client.utils.get_interface_details") as slow_details,
    ):
        details = wait_for_tun_interface_details("vynextun", timeout=0.0)

    assert details is not None
    assert details.alias == "VynexTun"
    assert details.index == 17
    assert details.ipv4 == "169.254.10.5"
    slow_details.assert_not_called()
