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

    # TODO: write the set_quack_behavior method
    def set_quack_behavior(self, new_quack_behavior):
        self.quack_behavior = new_quack_behavior

    # TODO: write the set_fly_behavior method
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

    # TODO: write the init method
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()

    # TODO: write the display method
    def display(self):
        print("I'm a Decoy duck, not a real duck")

class RubberDuck(Duck):

    # TODO: write the init method
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()

    # TODO: write the display method
    def display(self):
        print("I'm a Rubber duck, not a real duck")

class RedHeadDuck(Duck):

    # TODO: write the init method
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()


    # TODO: write the display method
    def display(self):
        print("I'm a real Red Head duck")

# TODO: write the ModelDuck class

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

# TODO: write the MuteQuack class
class MuteQuack(QuackBehavior):
    def quack(self):
        print("...")

# TODO: write the Squeak class
class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")
# TODO: write the FakeQuack class
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


# TODO: write the FlyNoWay class
class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I cannot fly!!")

# TODO: write the FlyRocketPowered class
class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying like a rocket!!")

if __name__ == '__main__':
    # TODO: instantiate an object of MallardDuck
    Duck1 = MallardDuck()

    # TODO: instantiate an object of RedHeadDuck
    Duck2 = RedHeadDuck()

    # TODO: instantiate an object of ModelDuck
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