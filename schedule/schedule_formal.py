import os
import sys
import yaml

FILEPATH = os.path.expanduser('~') + '/.schedule.yml'

class Schedule(object):
    tasks = None

    # - method
    def __init__(self):
        if os.path.isfile(FILEPATH):
            with open(FILEPATH, 'r+') as f:
                self.tasks = yaml.load(f)
        else:
            self.tasks = {}

    def _save_to_file(self):
        with open(FILEPATH, 'w+') as f:
            yaml.dump(self.tasks, f)

    def add_task(self, name, content, priority, due_hour=1):
        if name in self.tasks.keys():
            print('Task with name %s already exists' % name)
        new_task = [name, content, priority, due_hour]
        self.tasks.update({name : new_task})
        self._save_to_file()

    def remove_task(self, name):
        if name not in self.tasks.keys():
            print('Cannot delete a non-exist task %s' % name)
        self.tasks.pop(name, None)
        self._save_to_file()

    def display(self):
        if self.tasks:
            print 'Here are your tasks:'
            for task in self.tasks.values():
                print('%-10s %-5s %-5s %-50s' % (task[0], task[1], task[2], task[3]))

if __name__ == '__main__':
    schedule = Schedule()

    action = sys.argv[1]
    args = sys.argv[2:]

    def add(name, content, priority, due_hour):
        schedule.add_task(name, content, priority, due_hour)
        schedule.display()

    def delete(name):
        schedule.remove_task(name)
        schedule.display()

    def display():
        schedule.display()

    options = {
        'add': add,
        'delete': delete,
        'display': display
    }

    options[action](*args)



