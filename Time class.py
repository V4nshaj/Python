class Time():
    def __init__(self, hours, mins):
        self.hours = hours
        self.mins = mins


    def addTime(t1, t2):
        t3 = Time(0, 0)
        if t1.mins+t2.mins > 60:
            t3.hours = t3.hours+1
            t3.mins = t1.mins+t2.mins-60
        t3.hours = t3.hours+t1.hours+t2.hours
        return t3


    def displayTime(self):
        print("Time in Hours:", self.hours, "hours and ", self.mins, " mins")


    def displayMinute(self):
        print("Time in Minutes: ", (self.hours*60)+self.mins)


a = Time(2, 50)
b = Time(1, 20)
c = Time.addTime(a, b)
c.displayTime()
c.displayMinute()
