from .time import time
class ylist():
    @staticmethod
    def year() -> list:
        new = []
        for i in range(1, 4):
            new.append(int(time.current()) - i)
        return new
