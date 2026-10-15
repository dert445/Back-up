class Animals:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Genaric animal sound")

class Dog(Animals):
    def speak(self):
        super().speak()
        print("Woof!")

# a=Animals("Dog")
# a.speak()
a=Dog("ASS")
a.speak()