class Item:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Ration(Item):

    def __init__(self, quantity):
        super(Ration, self).__init__("Ration", quantity)

    def eat_ration(self):

        if self.quantity > 0:
            self.quantity -= 1
            return True  # able to move 1 Location
        else:
            return False  # unable to move, out of food


class Bandage(Item):

    def __init__(self, quantity):
        super(Bandage, self).__init__("Bandage", quantity)

    def use_bandage(self):

        if self.quantity > 0:
            self.quantity -= 1
            return 10  # 10 health returned to player
        else:
            return 0   # no bandages left, not healed


class Weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Fist(Weapon):

    def __init__(self):
        super(Fist, self).__init__("Fist", 3)


class Cudgel(Weapon):

    def __init__(self):
        super(Cudgel, self).__init__("Cudgel", 10)


class Spear(Weapon):

    def __init__(self):
        super(Spear, self).__init__("Spear", 20)


class Sword(Weapon):

    def __init__(self):
        super(Sword, self).__init__("Sword", 40)


class WizardStaff(Weapon):

    def __init__(self):
        super(WizardStaff, self).__init__("Wizard's Staff", 75)
