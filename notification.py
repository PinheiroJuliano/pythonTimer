import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="ATENÇÃO",
            message="Você não é um relógio, tire um período de descanso.",
            app_icon="./iconi.ico",  
            timeout=10
        )
        time.sleep(3600) 