from win10toast import ToastNotifier
import sys
import subprocess
import os
import webbrowser

IP_DEVICE = "192.168.1.82"

# proc = subprocess.Popen(["ping", IP_NETWORK], stdout=subprocess.PIPE)
proc = subprocess.Popen(["ping", "-t", IP_DEVICE], stdout=subprocess.PIPE)

while True:
    line = proc.stdout.readline()
    if not line:
        break
    else:
        None
    try:
        connected_ipp = line.decode("utf-8").split()[2].replace(":", "")
        if connected_ipp == IP_DEVICE:
            print("device is connected")
            webbrowser.open_new_tab("www.gmail.com")
            webbrowser.open_new_tab("www.linkedin.com")
            subprocess.call("D:\\Program Files (x86)\\Steam\\steam.exe")
            toaster = ToastNotifier()
            toaster.show_toast("Alert", "Shakti's iPhone Connected!", duration=200)
            break
        else:
            print("Your Device still not  Connected")
            # toaster = ToastNotifier()
            # toaster.show_toast("Alert", "Your Phone Not Nearby", duration=200)

    except:
        pass