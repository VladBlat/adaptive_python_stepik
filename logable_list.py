import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, obj):
        list.append(self, obj)
        Loggable.log(self, self[-1])

test = LoggableList()
test.append('1')
test.append('Hellow')