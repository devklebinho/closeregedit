# fechar_regedit.py
import psutil
import os
import time
import datetime
from pathlib import Path

LOG_PATH = Path(os.getenv("LOCALAPPDATA")) / "RegBlock" / "regedit_log.txt"
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

def log(msg):
    try:
        with LOG_PATH.open("a", encoding="utf-8") as f:
            f.write(f"[{datetime.datetime.now()}] {msg}\n")
    except Exception:
        pass

def fechar_regedit():
    for proc in psutil.process_iter(["name", "pid"]):
        try:
            if proc.info["name"] and proc.info["name"].lower() == "regedit.exe":
                pid = proc.info["pid"]
                proc.terminate()
                log(f"Regedit (PID {pid}) detectado e encerrado.")
                #print(f"Regedit (PID {pid}) detectado e encerrado.")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

if __name__ == "__main__":
    log("Monitor de Regedit iniciado.")
    while True:
        fechar_regedit()
        time.sleep(0.2)