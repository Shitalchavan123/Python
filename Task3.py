import schedule
import time
import datetime

def Task_minute():
    print("Task based on minutes gets scheduled at:",datetime.datetime.now()

def Task_hour():
        print("Task based on hour gets scheduled at:", datetime.datetime.now())


def Task_day():
    print("Task based on day gets scheduled at:", datetime.datetime.now())


def main():
    print("Inside task scheduler")
    print("Current time is:", datetime.datetime.now())

    schedule.every(1).minutes.do(Task_minute)
    schedule.every(1).hour.do(Task_hour)
    schedule.every().saturday.at("18.00").do(Task_day)



    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__== "__main__":
    main()