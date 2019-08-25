# Base location class. Each tile of the game map is a single location
import numpy as np
import curses


class Location:

    def __init__(self, name, map_char):
        self.name = name
        self.traversable = False
        self.is_city = False
        self.map_char = map_char
        self.odds_of_bandit = 0
        self.odds_of_trader = 0
        self.x = -1
        self.y = -1


class Laketown(Location):

    def __init__(self, y, x):
        super(Laketown, self).__init__("Laketown", "L")
        self.traversable = True
        self.is_city = True
        self.x = x
        self.y = y


class Plainstown(Location):

    def __init__(self, y, x):
        super(Plainstown, self).__init__("Plainstown", "P")
        self.traversable = True
        self.is_city = True
        self.x = x
        self.y = y


class Treetop(Location):

    def __init__(self, y, x):
        super(Treetop, self).__init__("Treetop City", "T")
        self.traversable = True
        self.is_city = True
        self.x = x
        self.y = y


class Shorepoint(Location):

    def __init__(self, y, x):
        super(Shorepoint, self).__init__("Shorepoint City", "S")
        self.traversable = True
        self.is_city = True
        self.x = x
        self.y = y


class Portal(Location):

    def __init__(self, y, x):
        super(Portal, self).__init__("Portal", " ")
        self.discovered = False
        self.traversable = True
        self.x = x
        self.y = y

    def discover(self):
        if not self.discovered:
            self.discovered = True
            self.map_char = "0"


class Path(Location):

    def __init__(self, y, x):
        super(Path, self).__init__("Path", "#")
        self.traversable = True
        self.x = x
        self.y = y
        self.odds_of_trader = 10
        self.odds_of_bandit = 0


class Grass(Location):

    def __init__(self, y, x):
        super(Grass, self).__init__("Grass", ".")
        self.traversable = True
        self.x = x
        self.y = y
        self.odds_of_trader = 30
        self.odds_of_bandit = 10


class Forest(Location):

    def __init__(self, y, x):
        super(Forest, self).__init__("Forest", "/")
        self.traversable = True
        self.x = x
        self.y = y
        self.odds_of_trader = 0
        self.odds_of_bandit = 10


class Mountain(Location):

    def __init__(self, y, x):
        super(Mountain, self).__init__("Mountain", "^")
        self.traversable = False
        self.x = x
        self.y = y


class Water(Location):

    def __init__(self, y, x):
        super(Water, self).__init__("Water", "~")
        self.traversable = False
        self.x = x
        self.y = y


class Valley(Location):

    def __init__(self, y, x):
        super(Valley, self).__init__("Valley", " ")
        self.traversable = True
        self.x = x
        self.y = y
        self.odds_of_trader = 0
        self.odds_of_bandit = 15
        self.odds_of_bear = 10


class Map:

    def __init__(self):
        self.row = 31
        self.column = 51
        self.map_grid = np.empty([self.row, self.column], dtype=object)

        for i in range(0, 1):  # first row
            for j in range(self.column):  # every column is Water
                self.map_grid[i][j] = Water(i, j)
        for i in range(1, 2):  # second row
            for j in range(0, 43):
                self.map_grid[i][j] = Water(i, j)  # first 43 Locations are Water
            for j in range(43, 46):
                self.map_grid[i][j] = Grass(i, j)  # Grass for three Locations
            for j in range(46, self.column):
                self.map_grid[i][j] = Water(i, j)  # finish off row with Water
        for i in range(2, 3):
            for j in range(0, 4):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(4, 42):
                self.map_grid[i][j] = Water(i, j)
            for j in range(42, 44):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(44, 45):
                self.map_grid[i][j] = Shorepoint(i, j)
            for j in range(45, 47):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(47, self.column):
                self.map_grid[i][j] = Water(i, j)
        for i in range(3, 4):
            for j in range(0, 1):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(1, 2):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(2, 3):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(3, 14):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(14, 39):
                self.map_grid[i][j] = Water(i, j)
            for j in range(39, 44):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(44, 45):
                self.map_grid[i][j] = Path(i, j)
            for j in range(45, 47):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(47, self.column):
                self.map_grid[i][j] = Water(i, j)
        for i in range(4, 5):
            for j in range(0, 1):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(1, 2):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(2, 4):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(3, 33):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(33, 38):
                self.map_grid[i][j] = Water(i, j)
            for j in range(38, 44):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(44, 45):
                self.map_grid[i][j] = Path(i, j)
            for j in range(45, self.column):
                self.map_grid[i][j] = Grass(i, j)
        for i in range(5, 6):  # 7th row, finished
            for j in range(0, 1):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(1, 4):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(4, 11):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(11, 12):
                self.map_grid[i][j] = Plainstown(i, j)
            for j in range(12, 34):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(34, 38):
                self.map_grid[i][j] = Water(i, j)
            for j in range(38, 43):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(43, 45):
                self.map_grid[i][j] = Path(i, j)
            for j in range(45, self.column):
                self.map_grid[i][j] = Grass(i, j)
        for i in range(6, 7):
            for j in range(0, 2):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(2, 4):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(4, 6):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(6, 11):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(11, 12):
                self.map_grid[i][j] = Path(i, j)
            for j in range(12, 33):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(33, 36):
                self.map_grid[i][j] = Water(i, j)
            for j in range(36, 43):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(43, 44):
                self.map_grid[i][j] = Path(i, j)
            for j in range(44, 48):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(48, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(7, 8):
            for j in range(0, 1):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(1, 2):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(2, 3):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(3, 4):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(4, 5):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(5, 6):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(6, 11):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(11, 13):
                self.map_grid[i][j] = Path(i, j)
            for j in range(13, 31):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(31, 34):
                self.map_grid[i][j] = Water(i, j)
            for j in range(34, 43):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(43, 44):
                self.map_grid[i][j] = Path(i, j)
            for j in range(44, 47):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(47, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(8, 9):
            for j in range(0, 1):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(1, 3):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(3, 6):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(6, 29):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(29, 32):
                self.map_grid[i][j] = Water(i, j)
            for j in range(32, 43):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(43, 44):
                self.map_grid[i][j] = Path(i, j)
            for j in range(44, 46):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(46, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(9, 10):
            for j in range(0, 1):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(1, 2):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(2, 3):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(3, 4):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(4, 5):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(5, 6):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(6, 20):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(20, 28):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(28, 31):
                self.map_grid[i][j] = Water(i, j)
            for j in range(31, 42):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(42, 44):
                self.map_grid[i][j] = Path(i, j)
            for j in range(44, 47):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(47, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(10, 11):
            for j in range(0, 1):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(1, 2):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(2, 6):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(6, 7):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(7, 27):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(27, 30):
                self.map_grid[i][j] = Water(i, j)
            for j in range(30, 38):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(38, 43):
                self.map_grid[i][j] = Path(i, j)
            for j in range(43, 45):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(45, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(11, 12):
            for j in range(0, 1):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(1, 3):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(3, 5):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(5, 6):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(6, 7):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(7, 19):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(19, 20):
                self.map_grid[i][j] = Path(i, j)
            for j in range(20, 28):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(28, 31):
                self.map_grid[i][j] = Water(i, j)
            for j in range(31, 39):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(39, 40):
                self.map_grid[i][j] = Path(i, j)
            for j in range(40, 45):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(45, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(12, 13):  # row 13, finished
            for j in range(0, 1):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(1, 2):
                self.map_grid[i][j] = Portal(i, j)
            for j in range(2, 3):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(3, 5):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(5, 6):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(6, 8):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(8, 19):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(19, 20):
                self.map_grid[i][j] = Path(i, j)
            for j in range(20, 29):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(29, 32):
                self.map_grid[i][j] = Water(i, j)
            for j in range(32, 39):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(39, 40):
                self.map_grid[i][j] = Path(i, j)
            for j in range(40, 43):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(43, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(13, 14):
            for j in range(0, 4):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(4, 6):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(6, 7):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(7, 19):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(19, 20):
                self.map_grid[i][j] = Path(i, j)
            for j in range(20, 28):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(28, 31):
                self.map_grid[i][j] = Water(i, j)
            for j in range(20, 28):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(28, 31):
                self.map_grid[i][j] = Water(i, j)
            for j in range(31, 39):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(39, 40):
                self.map_grid[i][j] = Path(i, j)
            for j in range(40, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(14, 15):
            for j in range(0, 1):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(1, 2):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(2, 3):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(3, 4):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(4, 5):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(5, 6):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(6, 8):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(8, 19):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(19, 24):
                self.map_grid[i][j] = Path(i, j)
            for j in range(24, 26):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(26, 29):
                self.map_grid[i][j] = Water(i, j)
            for j in range(29, 36):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(36, 39):
                self.map_grid[i][j] = Forest(i, j)
            for j in range(39, 40):
                self.map_grid[i][j] = Path(i, j)
            for j in range(40, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(15, 16):
            for j in range(0, 1):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(1, 3):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(3, 5):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(5, 7):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(7, 8):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(8, 23):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(23, 30):
                self.map_grid[i][j] = Path(i, j)
            for j in range(30, 33):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(33, 39):
                self.map_grid[i][j] = Forest(i, j)
            for j in range(39, 40):
                self.map_grid[i][j] = Path(i, j)
            for j in range(40, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(16, 17):
            for j in range(0, 1):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(1, 2):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(2, 3):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(3, 4):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(4, 6):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(6, 7):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(7, 10):
                self.map_grid[i][j] = Water(i, j)
            for j in range(10, 15):
                self.map_grid[i][j] = Path(i, j)
            for j in range(15, 22):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(22, 25):
                self.map_grid[i][j] = Water(i, j)
            for j in range(25, 28):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(28, 29):
                self.map_grid[i][j] = Forest(i, j)
            for j in range(29, 30):
                self.map_grid[i][j] = Path(i, j)
            for j in range(30, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(17, 18):
            for j in range(0, 1):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(1, 3):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(3, 5):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(5, 6):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(6, 8):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(8, 10):
                self.map_grid[i][j] = Water(i, j)
            for j in range(10, 11):
                self.map_grid[i][j] = Path(i, j)
            for j in range(11, 12):
                self.map_grid[i][j] = Water(i, j)
            for j in range(12, 19):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(19, 23):
                self.map_grid[i][j] = Water(i, j)
            for j in range(23, 25):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(25, 29):
                self.map_grid[i][j] = Forest(i, j)
            for j in range(29, 32):
                self.map_grid[i][j] = Path(i, j)
            for j in range(32, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(18, 19):
            for j in range(0, 1):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(1, 2):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(2, 3):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(3, 4):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(4, 5):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(5, 7):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(7, 8):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(8, 10):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(10, 11):
                self.map_grid[i][j] = Path(i, j)
            for j in range(11, 13):
                self.map_grid[i][j] = Water(i, j)
            for j in range(13, 16):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(16, 20):
                self.map_grid[i][j] = Water(i, j)
            for j in range(20, 23):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(23, 29):
                self.map_grid[i][j] = Forest(i, j)
            for j in range(29, 30):
                self.map_grid[i][j] = Path(i, j)
            for j in range(30, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(19, 20):
            for j in range(0, 1):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(1, 3):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(3, 6):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(6, 7):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(7, 10):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(10, 11):
                self.map_grid[i][j] = Laketown(i, j)
            for j in range(11, 18):
                self.map_grid[i][j] = Water(i, j)
            for j in range(18, 21):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(21, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(20, 21):
            for j in range(0, 2):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(2, 3):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(3, 5):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(5, 7):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(7, 8):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(8, 10):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(10, 19):
                self.map_grid[i][j] = Water(i, j)
            for j in range(19, 22):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(22, 40):
                self.map_grid[i][j] = Forest(i, j)
            for j in range(40, 41):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(41, 43):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(43, 44):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(44, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(21, 22):
            for j in range(0, 2):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(2, 6):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(6, 8):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(8, 20):
                self.map_grid[i][j] = Water(i, j)
            for j in range(20, 24):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(24, 39):
                self.map_grid[i][j] = Forest(i, j)
            for j in range(39, 41):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(41, 42):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(42, 43):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(43, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(22, 23):
            for j in range(0, 1):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(1, 3):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(3, 5):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(5, 6):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(6, 7):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(7, 23):
                self.map_grid[i][j] = Water(i, j)
            for j in range(23, 27):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(27, 39):
                self.map_grid[i][j] = Forest(i, j)
            for j in range(39, 40):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(40, 42):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(42, 43):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(43, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(23, 24):
            for j in range(0, 2):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(2, 4):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(4, 5):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(5, 6):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(6, 22):
                self.map_grid[i][j] = Water(i, j)
            for j in range(22, 28):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(28, 39):
                self.map_grid[i][j] = Forest(i, j)
            for j in range(39, 40):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(40, 41):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(41, 42):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(42, 43):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(43, 44):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(44, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(24, 25):
            for j in range(0, 1):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(1, 2):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(2, 3):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(3, 6):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(6, 20):
                self.map_grid[i][j] = Water(i, j)
            for j in range(20, 30):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(30, 35):
                self.map_grid[i][j] = Forest(i, j)
            for j in range(35, 36):
                self.map_grid[i][j] = Treetop(i, j)
            for j in range(36, 38):
                self.map_grid[i][j] = Forest(i, j)
            for j in range(38, 40):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(40, 43):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(43, 44):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(44, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(25, 26):
            for j in range(0, 2):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(2, 5):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(5, 6):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(6, 7):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(7, 18):
                self.map_grid[i][j] = Water(i, j)
            for j in range(18, 32):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(32, 40):
                self.map_grid[i][j] = Forest(i, j)
            for j in range(40, 44):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(43, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(26, 27):
            for j in range(0, 1):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(1, 2):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(2, 4):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(4, 5):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(5, 8):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(8, 15):
                self.map_grid[i][j] = Water(i, j)
            for j in range(15, 34):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(34, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(27, 28):
            for j in range(0, 1):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(1, 3):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(3, 6):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(6, 7):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(7, 9):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(9, 10):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(10, 13):
                self.map_grid[i][j] = Water(i, j)
            for j in range(13, 36):
                self.map_grid[i][j] = Grass(i, j)
            for j in range(36, self.column):
                self.map_grid[i][j] = Forest(i, j)
        for i in range(28, 29):
            for j in range(0, 2):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(2, 4):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(4, 8):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(8, 9):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(9, 11):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(11, self.column):
                self.map_grid[i][j] = Grass(i, j)
        for i in range(29, 30):
            for j in range(0, 1):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(1, 2):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(2, 3):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(3, 6):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(6, 8):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(8, 9):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(9, 12):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(12, self.column):
                self.map_grid[i][j] = Grass(i, j)
        for i in range(30, 31):
            for j in range(0, 2):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(2, 3):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(3, 7):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(7, 8):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(8, 11):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(11, 12):
                self.map_grid[i][j] = Valley(i, j)
            for j in range(12, 13):
                self.map_grid[i][j] = Mountain(i, j)
            for j in range(13, self.column):
                self.map_grid[i][j] = Grass(i, j)

    def is_valid_move(self, current_location, world_map, y_change, x_change):
        if (current_location.y + y_change > -1) and (current_location.y + y_change < 31):  # if y change is valid
            if (current_location.x + x_change > -1) and (current_location.x + x_change < 51):  # if x change is valid
                if world_map.map_grid[current_location.y + y_change][current_location.x + x_change].traversable:
                    return True  # is a traversable location
        else:
            return False

    def draw_map(self, map_scrn, player):
        # map_scrn.erase()
        for i in range(self.row):
            for j in range(self.column):
                if i == player.location.y and j == player.location.x:
                    map_scrn.attron(curses.color_pair(9))
                    map_scrn.addch('@')
                    map_scrn.attroff(curses.color_pair(9))
                else:
                    if self.map_grid[i][j].is_wizard_occupied:
                        map_scrn.attron(curses.color_pair(8))
                        map_scrn.addch('W')
                        map_scrn.attroff(curses.color_pair(8))
                    elif self.map_grid[i][j].name == "Grass":
                        map_scrn.attron(curses.color_pair(1))
                        map_scrn.addch(self.map_grid[i][j].map_char)
                        map_scrn.attroff(curses.color_pair(1))
                    elif self.map_grid[i][j].name == "Forest":
                        map_scrn.attron(curses.color_pair(2))
                        map_scrn.addch(self.map_grid[i][j].map_char)
                        map_scrn.attroff(curses.color_pair(2))
                    elif self.map_grid[i][j].name == "Water":
                        map_scrn.attron(curses.color_pair(3))
                        map_scrn.addch(self.map_grid[i][j].map_char)
                        map_scrn.attroff(curses.color_pair(3))
                    elif self.map_grid[i][j].name == "Path":
                        map_scrn.attron(curses.color_pair(4))
                        map_scrn.addch(self.map_grid[i][j].map_char)
                        map_scrn.attroff(curses.color_pair(4))
                    elif self.map_grid[i][j].name == "Mountain":
                        map_scrn.attron(curses.color_pair(5))
                        map_scrn.addch(self.map_grid[i][j].map_char)
                        map_scrn.attroff(curses.color_pair(5))
                    elif self.map_grid[i][j].name == "Valley":
                        map_scrn.attron(curses.color_pair(6))
                        map_scrn.addch(self.map_grid[i][j].map_char)
                        map_scrn.attroff(curses.color_pair(6))
                    elif self.map_grid[i][j].name == "Portal":
                        if self.map_grid[i][j].discovered:
                            map_scrn.attron(curses.color_pair(8))
                            map_scrn.addch(self.map_grid[i][j].map_char)
                            map_scrn.attroff(curses.color_pair(8))
                        else:
                            map_scrn.attron(curses.color_pair(6))
                            map_scrn.addch(self.map_grid[i][j].map_char)
                            map_scrn.attroff(curses.color_pair(6))

                    else:
                        map_scrn.attron(curses.color_pair(7))
                        map_scrn.addch(self.map_grid[i][j].map_char)
                        map_scrn.attroff(curses.color_pair(7))

        # map_scrn.refresh()
