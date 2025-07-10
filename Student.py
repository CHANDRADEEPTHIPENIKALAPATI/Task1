class Student:
    #private
    def __init__(self):
        self.__name=""
        self.__score=0
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            print("Scores must be between 0 and 100")
    def get_score(self):
        return self.__score
s=Student()
s.set_name("Allice")
s.set_score(85)
print("Student Name:",s.get_name())
print("Student marks:",s.get_score())
s.set_score(120)
print("Student marks(After invalid input):",s.get_score())

