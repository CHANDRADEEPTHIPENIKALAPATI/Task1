class Employee:
    def work(self):
        print("work done")
class Manager(Employee):
    def manage(self):
        print("manage done")
m=Manager()
m.work()
m.manage()