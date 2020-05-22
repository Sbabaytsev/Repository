import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(Loggable, list):
    def append(self, element):
        list.append(self, element)
        self.log(element)


x = LoggableList()
x.append('qwerty')
