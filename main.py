import time
import psutil
from plyer import notification

if __name__ == "__main__":
    while True:
        # Check if file is running
        for proc in psutil.process_iter():
            if proc.name() == "addYourFileName.exe":
                # Display the notification
                notification.notify(
                    title = "This is the title of the notification",
                    message = "The message you want in it",
                    app_icon = "path\to\your\icon",
                    timeout = 5 # how long you want the message to be seen? (in seconds)
                )
                # Wait for 10 minutes before displaying the notification again
                time.sleep(5)
        # Wait for 5 seconds before checking again
        time.sleep(1)
