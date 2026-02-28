#  generalized class example (troubleshooting data.py with AJ)
class Dog:
    def __init__(self, dog_age, dog_name, dog_breed):
        self.age = dog_age
        self.name = dog_name
        self.breed = dog_breed

    def bark (self, volume):
        print("Bark!")

    def run(self):
        return "Ran"
# now we have a dog  class

gerald = Dog(5,"Gerald","Corgi")

gerald.bark(5)
gerald.run()