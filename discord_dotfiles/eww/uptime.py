"""Uptime script"""
import subprocess

uptime = subprocess.run(["uptime", "-p"], capture_output=True, encoding="utf-8").stdout

subprocess.call(["echo", "Uptime: " + " ".join(uptime.split()[1:])])

