from datetime import datetime
import sys

def displaytime_decorator(func):
    def wrapper(*args, **kwargs):
        print(str(datetime.now()))
        return func(*args, **kwargs)
    return wrapper

class Schedule(object):

    name = None
    desp = None
    tasks = None

    # - method
    def __init__(self, n, d):
        self.name = n
        self.desp = d
        self.tasks = {}

    @displaytime_decorator
    def add_task(self, name, content, priority):
        if name not in self.tasks:
            task = [name, content, priority]
            self.tasks.update({name : task})
        self.display()

    @displaytime_decorator
    def remove_task(self, name):
        if name in self.tasks:
            self.tasks.pop(name)
        self.display()

    def display(self):
        if self.tasks:
            print 'Here are your tasks:'
            for task in self.tasks.values():
                print('%-10s %-5s %-50s' % (task[0], task[1], task[2]))

    def __str__(self):
        return 'Schedule %s, %s' % (self.name, self.desp)

if __name__ == '__main__':
    print sys.argv



