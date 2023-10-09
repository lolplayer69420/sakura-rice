"""Get the network interface currently being used."""
import os
import subprocess

interfaces = os.listdir("/sys/class/net")


def get_current_interface() -> str:
    current_interface = ""

    for interface in interfaces:
        with open(f"/sys/class/net/{interface}/operstate", "rt") as interface_operstate:
            if interface_operstate.readlines()[0].removesuffix("\n") == "up":
                current_interface = interface
                break

    return current_interface


subprocess.call(["echo", f" {get_current_interface()}"])

