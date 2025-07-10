class User:
    def login(self):
        print("Logging in")
class BusinessUser(User):
    def run_add(self):
        print("run add")
b=BusinessUser()
b.login()
b.run_add()