###create a function to tell the date,time,day... try to use numbering in list

from datetime import datetime
from datetime import date
#from datetime import time

#create a function
def main():
    # date objects
    # keep () method empty from date
    today = date.today()
    print("today's date is", today)

    # print out day, month, year using today
    print("date is", today.day, today.month, today.year)

    #print out time right now
    today = datetime.now()
    print("the time is", today)

    #days of the week will by where the date  is in the list starting from 0 - 6
    print ("# day in the week", today.weekday())
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    print("today is " + days[today.weekday()])

    tnow = datetime.time(datetime.now())
    print("current time is ", tnow)

if __name__ == "__main__":
    main();

