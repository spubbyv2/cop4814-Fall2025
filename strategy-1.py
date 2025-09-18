"""
The SimUDuck App - Strategy Design Pattern

Joe works for a company that makes a highly successful duck
pond simulation game, SimUDuck. The game can show a large
variety of duck species swimming and making quacking sounds.
"""

###############################################################################
# Ducks
###############################################################################

# Abstract class Duck
class Duck:
    fly_behavior = None
    quack_behavior = None

    def display(self):
        pass

    def fly(self):
        self.fly_behavior.fly()

    def quack(self):
        self.quack_behavior.quack()

    def set_quack_behavior(self, new_quack_behavior):
        self.quack_behavior = new_quack_behavior

    def set_fly_behavior(self, new_fly_behavior):
        self.fly_behavior = new_fly_behavior

    def swim(self):
        print("All ducks float, even decoys!!")

class MallardDuck(Duck):

    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a real Mallard duck")

class DecoyDuck(Duck):

    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()

    def display(self):
        print("I'm a Decoy duck, not a real duck")

class RubberDuck(Duck):


    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()


    def display(self):
        print("I'm a Rubber duck, not a real duck")

class RedHeadDuck(Duck):


    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a real Red Head duck")

class ModelDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyRocketPowered()
        self.quack_behavior = FakeQuack()

    def display(self):
        print("I'm a Model duck")

###############################################################################
# Quack behaviors
###############################################################################

class QuackBehavior:
    def quack(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        print("Quack")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("...")

class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")

class FakeQuack(QuackBehavior):
    def quack(self):
        print("Queek")

###############################################################################
# Fly behaviors
###############################################################################
class FlyBehavior():
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I cannot fly!!")

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying like a rocket!!")

if __name__ == '__main__':

    Duck1 = MallardDuck()

    Duck2 = RedHeadDuck()

    Duck3 = ModelDuck()

    Duck4 = DecoyDuck()

    print(Duck1,Duck2,Duck3)
    Duck1.display()
    Duck1.fly()

    Duck2.display()
    Duck2.quack()

    Duck3.display()
    Duck3.fly()

    Duck4.display()
    Duck4.fly()

    Duck4.set_fly_behavior(FlyRocketPowered())
    Duck4.fly()
    Duck4.quack()

"""
References:
This lecture was designed by Dr Gregory Reis based on the book
Elisabeth Freeman, Eric Freeman, Bert Bates, and Kathy Sierra. 2004
Head First Design Patterns. O' Reilly & Associates, Inc.,
Dr Kip Irvine's class notes, and using the simuduck.py written
by Miguel Alba and modified by Dr Gregory Reis
"""