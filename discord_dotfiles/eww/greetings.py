"""Greeting script."""
from datetime import datetime
import subprocess

username = subprocess.run(["whoami"], capture_output=True, encoding="utf-8").stdout.replace("\n", "")


def current_day_stage() -> str:
    """Improvised shit."""
    day_stage = ""

    if datetime.now().hour in range(0, 12):
        day_stage = "morning"
    elif datetime.now().hour in range(12, 19):
        day_stage = "afternoon"
    elif datetime.now().hour in range(19, 24):
        day_stage = "night"

    return day_stage


subprocess.call(["echo", f"Good {current_day_stage()}, {username}"])

