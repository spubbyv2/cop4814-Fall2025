"""Week 3 - Object Oriented Paradigm in Python"""

"""Class - blueprint"""
"""Object - representation of a real world"""

#Example 1
class Car:
    def __init__(self, x, y):
        self.color = x
        self.maker = y

    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")

myCar = Car("White", "Honda")
print(myCar)
myCar.start_engine()
myCar.stop_engine()
print(myCar.color)
print(myCar.maker)

#Example 2
class FIUStudent():
    minimum_grade = 93
    def __init__(self, firstName, lastName, pid, email, grade):
        self.firstName = firstName
        self.lastName = lastName
        self.pid = pid
        self.email = email
        self.grade = grade

    def current_grade(self):
        return f"{self.firstName.title()} {self.lastName.title()}\'s current grade is {self.grade}"

    def student_credentials(self):
        return f"{self.firstName.title()} {self.lastName.title()}\'s email is {self.email}, and their panther ID is {self.pid}"

Student1 = FIUStudent("Richard", "Smith", 1234567, "email@fiu.edu", 83)
print(Student1.current_grade())
print(Student1.student_credentials())
Student2 = FIUStudent("Jon", "Jones", 7654321, "email2@fiu.edu", 95)
print(Student2.current_grade())
print(Student1.minimum_grade, Student2.minimum_grade)
Student2.minimum_grade = 96
print(Student1.minimum_grade, Student2.minimum_grade)
FIUStudent.minimum_grade = 89
print(Student1.minimum_grade, Student2.minimum_grade)

#Example 3

class Robot():
    def __init__(self, name, weight, battery_life, price):
        self.name = name
        self.weight = weight
        self.battery_life = battery_life
        self.price = price

    def introduce(self):
        return f"I'm {self.name.title()} and my battery life lasts {self.battery_life} hours."


Robot1 = Robot("zig", 50, 4, 399.99)
print(Robot1.introduce())

class AquaticRobot(Robot):
    def __init__(self, name, weight, battery_life, price, sensors, motors, isAutonomous):
        super().__init__(name, weight, battery_life, price)
        self.sensors = sensors
        self.motors = motors
        self.isAutonomous = isAutonomous

    def environment(self, water):
        return f"I'm {self.name.title()} and I am an aquatic robot that operates in "f"{water} water"

Robot2 = AquaticRobot("Eco", 170, 8, 140000, ["temp", "pH"], 3, True)
print(Robot2.environment("fresh"))
print(Robot2.introduce())

#Example 4

from abc import abstractmethod, ABC

class StreamingService(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def add_subscriber(self, username):
        pass

    @abstractmethod
    def remove_subscriber(self, username):
        pass

    @abstractmethod
    def display(self):
        pass


class VideoStreamingService(StreamingService):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.subscribersList = []

    def play(self):
        print("I am a rich streaming service and production company")

    def add_subscriber(self, username):
        self.subscribersList.append(username)

    def remove_subscriber(self, username):
        try:
            self.subscribersList.remove(username)
        except ValueError:
            pass

    def display(self):
        print("I provide tv shows and movies to my subscribers.")

Netflix = VideoStreamingService("Netflix", 15.99)
Netflix.display()
print(Netflix.add_subscriber("Sebas"))
print(Netflix.add_subscriber("John"))
print(Netflix.subscribersList)
print(Netflix.subscribersList[0])
print(Netflix.subscribersList[1])

