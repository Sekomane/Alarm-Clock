import time
import datetime
import pygame

def set_alarmClock(alarm_Time):
    print("Alarm set for "+alarm_Time)
    sound_file = "AUD-20190220-WA0075 - Copy.mp3"
    is_running =  True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_Time:
            print("Wake Up!!!!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play(-1)

            time.sleep(30)
            pygame.mixer.music.stop()

            is_running = False

        time.sleep(1)

if __name__ == "__main__":
        alarm_Time = input("Enter the alarm time  (HH:MM:SS): ")
        set_alarmClock(alarm_Time)

