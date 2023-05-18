# test
import time

def focus_timer(duration):
    start_time = time.time()
    end_time = start_time + duration * 60

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        time_format = "{:02d}:{:02d}".format(minutes, seconds)
        print("Remaining time:", time_format, end="\r")
        time.sleep(1)

    print("Time's up! Stay focused!")

# 设置专注时长（单位：分钟）
duration = int(input("请输入专注时长（分钟）："))
focus_timer(duration)
