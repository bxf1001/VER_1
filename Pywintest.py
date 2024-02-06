import subprocess
import time
from pywinauto import Desktop, Application
number = 8056099417
app = Application(backend='uia').start(r"cmd.exe /c start shell:appsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App", create_new_console=True, wait_for_idle=False)
app = Application(backend='uia').connect(title_re=".*WhatsApp.*") # Replace with the actual path
url = f"whatsapp://send?phone=+91{number}"
subprocess.Popen(["cmd", "/C", f"start {url}"], shell=True)
time.sleep(0.25)
subprocess.Popen(["cmd", "/C", f"start {url}"], shell=True)
time.sleep(1)
while True:
    try:
        time.sleep(2)
        app.WhatsAppDialog.VideoCallButton.click() 
        break
    except:
        time.sleep(1)
        continue
