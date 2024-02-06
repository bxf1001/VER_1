from pywinauto.application import Application
app = Application().start("C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2401.5.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")  # Replace with the actual path
app.WhatsAppDialog.VideoCallButton.click()  # Replace with actual control names
app.WhatsAppDialog.VideoCallButton.click_input()  # Simulates cursor movement and clicks
