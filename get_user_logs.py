from pathlib import Path
import subprocess
import os.path
import time

def get_user_android_logs():
    # filename = input("Enter File Name: ")
    filename = "boxOfficeTycoon"
    filename = filename + (".txt")
    with open(filename, 'w') as f:
        #
        # proc = subprocess.Popen(['adb','logcat','-s', 'IntegrationHelper'],
        proc = subprocess.Popen(['adb','logcat','-s', 'IntegrationHelper'],
        stdout=f,stderr=subprocess.STDOUT)
        print("Connect device...")
        time.sleep(2)
        print("Waiting for logs...")
        try:
            errs = proc.communicate(timeout = 20)

        except subprocess.TimeoutExpired:
            proc.kill()
            errs = proc.communicate()
            return filename

def get_user_ios_logs():
    filename = "ios"
    filename = filename + (".txt")
    with open(filename, 'w') as f:
        proc = subprocess.Popen(["cfgutil syslog | grep -r IntegrationHelper"], stdin = subprocess.PIPE, shell = True,
               stdout=f,
               stderr=subprocess.STDOUT)
        print("Connect device...")
        time.sleep(2)
        print("Waiting for logs...")
        try:
            errs = proc.communicate(timeout = 40)

        except subprocess.TimeoutExpired:
            proc.kill()
            errs = proc.communicate()
            return filename
