"""Get number of available updates."""
import subprocess
import urllib.request
import urllib.error

def get_number_of_updates() -> int:
    output = 0

    try:
        urllib.request.urlopen("http://www.example.com")
    except urllib.error.URLError:
        output = 0
    else:
        updates = subprocess.run(["checkupdates"],
                                 capture_output=True, 
                                 encoding="utf-8").stdout.splitlines()

        aur_updates = subprocess.run(["yay", "-Qua"],
                                     capture_output=True,
                                     encoding="utf-8").stdout.splitlines()

        updates.extend(aur_updates)

        output = len(updates)

    return output


subprocess.call(["echo", f"{get_number_of_updates()}"])

