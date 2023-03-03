import time
from plyer import notification
from plyer import bluetooth

if __name__=="__main__":
    while True:
        notification.notify(
            title="Pixelco!!!",
            message="There are new news in technology ",
            timeout=10
        )
        time.sleep(3600)

