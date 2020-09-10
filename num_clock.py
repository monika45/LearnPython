from time import sleep
import os

class Clock:
    """
    数字时钟
    """
    def __init__(self, hour, minute, second):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """
        走字
        :return:
        """
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0


    def show(self):
        """显示"""
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


if __name__ == '__main__':
    clock = Clock(23, 58, 58)
    while True:
        os.system('cls')
        print(clock.show())
        sleep(1)
        clock.run()

