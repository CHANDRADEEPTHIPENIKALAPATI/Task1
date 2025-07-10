class Cat(Animal):
    def make_sound(self):
        print("cat sounds")
class Dog(Animal):
    def make_sound(self):
        print("Dog sounds")
for a in [Cat(), Dog()]:
    a.make_sound()