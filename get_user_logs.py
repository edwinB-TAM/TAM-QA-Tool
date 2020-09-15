from pathlib import Path
import subprocess
import os.path
import time


def get_user_logs():
    filename = input("Enter File Name: ")
    filename = filename + (".txt")

    with open(filename, 'w') as f:
        print("Waiting for logs...")
        proc = subprocess.Popen(['adb','logcat','-s', 'IntegrationHelper'],
               stdout=f,
               stderr=subprocess.STDOUT)
        try:
            errs = proc.communicate(timeout = 20)
        except subprocess.TimeoutExpired:
            proc.kill()
            errs = proc.communicate()
            return filename
