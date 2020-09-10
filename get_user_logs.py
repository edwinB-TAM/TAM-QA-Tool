from pathlib import Path
import subprocess
import os.path
import time


# Create with UNIX time stamp
# filename = input("Enter File Name: ")
filename = input("Enter File Name: ")
filename = filename + (".txt")


with open(filename, 'w+') as f:
    print("Waiting for logs...")
    proc = subprocess.Popen(['adb','logcat','-s', 'IntegrationHelper'],
           stdout=subprocess.PIPE,
           stderr=subprocess.STDOUT).communicate()
    # filename = stdout

    # proc.terminate()
    print("-----------here------------", filename)


    for line in proc.stdout:
        print ("Check Post-Read: ", line)
        if "(use this for test devices)" in line:
            print ("Check Pre-Kill")
            proc.kill('/Users/edwinbetancourt/edwinB-TAM/TAM-QA-Tool/test1.txt')
            print ("Check Post-Kill")
            close(filename,'.txt')
            break
        else:
            print ("In else")

proc.wait()
