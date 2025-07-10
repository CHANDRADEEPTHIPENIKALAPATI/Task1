class Marks:
    def __init__(self):
        self.__math_marks = 0

    def update_marks(self, marks):
        if 0 <= marks <= 100:
            self.__math_marks = marks

    def display_marks(self):
        print(f"Math Marks: {self.__math_marks}")
student = Marks()
student.display_marks()
student.update_marks(85)

