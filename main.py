import time
import psutil
from plyer import notification

if __name__ == "__main__":
    while True:
        # Check if Google Chrome is running
        for proc in psutil.process_iter():
            if proc.name() == "MSIAfterburner.exe":
                # Display the notification
                notification.notify(
                    title = "Focus Asshole",
                    message = "Focus on your work And and stop playing games. Also close MSI Afterburner",
                    app_icon = "D:\Python-Projects\Cornmanthe3rd-Plex-Other-python.ico",
                    timeout = 5
                )
                # Wait for 10 minutes before displaying the notification again
                time.sleep(5)
        # Wait for 5 seconds before checking again
        time.sleep(1)
