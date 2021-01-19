import time 
from plyer import notification #pip install plyer
if __name__ == "__main__":
    while True:
        notification.notify(
            title="****Please Drink Water Now****",
            message="the national acadmies of sciences, engineering and medicine determined that an adequate daily fluid intake is: about 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women".title(),
            app_icon="glass.png",
            timeout=10
        )
        time.sleep(60*60)