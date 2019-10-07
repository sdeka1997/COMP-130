"""
Swapnav Deka (sd55)
COMP 130
Fondren Library
Thursday, April 28, 2016

This is the second exam for COMP 130.

Honor Code: On my honor, I have neither given nor received any unauthorized
aid on this exam.
-Swapnav Deka
"""
# Points:
# 1) path_distance()                    40 points
# 2) Coin World                   total 60 points
# 2a)  World.__init__()                 12 points
# 2b)  World.pickup_coin()               5 points
# 2c)  Person.__init__()                12 points
# 2d)  Person.lose_coins()               5 points
# 2e)  Person.check_location()          14 points
# 2f)  Person.north(), Person.south(),  12 points
#      Person.east(), Person.west()




# Given a directed graph with edge distances and a path
# as a list of nodes, return the total distance of that path if it
# exists, or None if it doesn't.
# The path distance is simply the sum of the distances of each edge
# in the path.  As a special case, the distance of an empty path is 0.
# Paths are allowed to repeat nodes and edges.
#
# The function should not mutate graph or path.
#
# For this problem, a graph is a dictionary that maps source nodes
# to dictionaries that maps target nodes to distances.
# All nodes in the graph should be listed as a source node, even if
# no edges exist from it.
# An edge from a node to itself with zero cost is assumed to exist if
# no self-edge is explicitly present.
# See the examples after the function for more details.
#
# The tests after the code test all of the expected cases.

def path_distance(graph, path):
    """
    Returns the distance of the path in the graph, if the
    path exists, and None, if it doesn't.
    """
    for node in path:
        if node not in graph.keys():
            return None
    if len(path) == 0:
        return 0
    path_pairs = []
    idx = 0
    while idx < (len(path) - 1):
        path_pairs.append((path[idx],path[idx+1]))
        idx = idx + 1
    all_paths = []
    for pair in path_pairs:
        for elem in pair:
            all_paths.append(elem)
    num = []
    count = 0
    while count < (len(all_paths)):
        if all_paths[count+1] in graph[all_paths[count]]:
            num.append(graph[all_paths[count]][all_paths[count+1]])
        elif all_paths[count] == all_paths[count+1]:
            num.append(0)
        count = count + 2
    if len(path) - 1 != len(num):
        return None
    return sum(num)
    


# Sample directed graph for path_distance
# E.g., d->e exists, but e->d doesn't.  a->b has distance 1, while b->a has distance 4.
graph = {"a": {"b": 1, "c": 2, "e": 3},
         "b": {"a": 4, "d": 3},
         "c": {"a": 2, "b": 5, "c": 3},
         "d": {"b": 7, "e": 5},
         "e": {"a": 1, "c": 3, "z": 8}}

existent_path1 = ["b", "d", "e", "a", "b", "d", "b"]  # Edges b->d, d->e, e->a, a->b, b->d, d->b.
existent_path2 = ["a", "b", "b"] # Edges a->b, b->b.  b->b exists implicitly with distance 0.
existent_path3 = ["a", "c", "c"] # Edges a->c, c->c.  c->c exists explicitly with non-zero distance.
existent_path4 = ["b"] # Node b exists, but path is empty.
existent_path5 = [] # Considered an empty path.
nonexistent_path1 = ["d", "e", "b", "a", "b"]    # No edge exists from e to b.
nonexistent_path2 = ["d", "x"] # No edge d->x exists and no node x exists.
nonexistent_path3 = ["x"] # No node x exists.
nonexistent_path4 = ["a", "e", "z"] # Edges a->e, e->z exist, but there's no node z in the graph.


print "=Path test==================================="
print path_distance(graph, existent_path1), "should be", 3+5+1+1+3+7
print path_distance(graph, existent_path2), "should be", 1+0
print path_distance(graph, existent_path3), "should be", 2+3
print path_distance(graph, existent_path4), "should be", 0
print path_distance(graph, existent_path5), "should be", 0
print path_distance(graph, nonexistent_path1), "should be", None
print path_distance(graph, nonexistent_path2), "should be", None
print path_distance(graph, nonexistent_path3), "should be", None
print path_distance(graph, nonexistent_path4), "should be", None






# Complete the following code that models a simple multi-player
# game.  We can have multiple worlds, each with multiple people.
# Coins are scattered probabilistically in the world.  As people
# move around, they automatically pick up any coins at their location.
# When one person bumps into another, the bumper steals all the bumpee's
# coins.
#
# In the following, docstrings describe what each method should do.
# In particular, the __init__() docstrings describe what data each
# object should store.
#
# As always, use methods to get data from other objects, even
# though Python allows you to directly access another object's data.
#
# The following problem uses typical 2D (x,y) spatial coordinates.
# The x axis extends horizontally, increasing right/east.
# The y axis extends vertically, increasing up/north.
#
# The tests after the code test much (but not all) of the expected
# functionality.

from random import random

class World:
    def __init__(self, width, height, coin_probability):
        """
        Initialize world as a 2D matrix of the given dimensions.
        Location coordinates are numbered 0..width-1 and 0..height-1.
        Each location either contains a coin or it doesn't.
        Each location is initialized to have a coin with
        the given probability.
        
        The world keeps track of what people are in it.
        It initially has no people.  The world does not keep
        track of the people's locations -- the people do themselves.
        Multiple people can be in the same location.
        
        Assume that width and height are positive integers and
        that coin_probability is in the range [0,1].
        """
        
        self.width = width
        self.height = height
        self.people = set()  # Initially no people
        
        # CHANGE THIS LINE
        # self.coins should be the 2D matrix described above.
        self.coins = [[1 if random() <= coin_probability else 0 for dummy_col in range(self.width)]
                      for dummy_row in range(self.height)]
        
    def add_person(self, person):
        """
        Adds the given person (object) to the world's people.
        """
        
        self.people.add(person)
        
    def get_people(self):
        """
        Returns a new set of the people in the world.
        """
        
        return set(self.people)
            
    def get_dimensions(self):
        """
        Returns the width and height of the world.
        """
        
        return (self.width, self.height)

    def pickup_coin(self, x, y):
        """
        If a coin is at location (x,y), it removes it from the location.
        It returns the number of coins that were there.
        
        Assume location (x,y) is within the world boundary.
        """
        
        # ADD CODE HERE
        if self.coins[y][x] > 0:
            coins = self.coins[y][x]
            self.coins[y][x] = 0
            return coins
        else:
            return 0        

    
class Person:
    def __init__(self, name, x, y, coins, world):
        """
        Initializes a person with the given name, number of coins, and world.
        Initializes a person to have the given location (x,y) in the given world,
        except that if those coordinates are outside the bounds of the world,
        then the nearest location inside the bounds is used.

        It adds the person to the world, and uses the check_location method
        to look for coins or people at the initial location.
        """
        
        self.name = name
        self.coins = coins
        self.world = world

        # CHANGE THIS CODE
        # Initialize self.x and self.y as described above.
        # Put the person in the world.
        # Use check_location.
        self.x = x
        self.y = y
        
        x_bdry = self.world.get_dimensions()[0] - 1
        y_bdry = self.world.get_dimensions()[1] - 1
        
        if x < 0:
            self.x = 0
        elif x > x_bdry:
            self.x = x_bdry

        if y < 0:
            self.y = 0
        elif y > y_bdry:
            self.y = y_bdry
            
        self.world.add_person(self)
        self.check_location()
        
    def get_name(self):
        """
        Returns the person's name.
        """
        
        return self.name
        
    def get_coordinates(self):
        """
        Returns the person's (x,y) location.
        """
        
        return (self.x, self.y)
        
    def get_coins(self):
        """
        Returns how many coins the person has.
        """
        
        return (self.coins)
        
    def lose_coins(self):
        """
        Changes the person's number of coins to zero.
        Returns the number of coins the person had.
        """
        
        # CHANGE THIS CODE
        coins = self.coins
        self.coins = 0
        return coins
        
    def check_location(self):
        """
        If a coin is at the person's new location, the person picks it up and keeps it.
        If other people are already there, this person steals all their coins.
        
        This method should only be called by other Person methods, after moving.
        """
        
        # CHANGE THIS CODE
        existing_coins = self.world.pickup_coin(self.x, self.y)        
        people = self.world.get_people()
        for person in people:
            if person != self:
                location = person.get_coordinates()
                if location == self.get_coordinates():
                    people_coins = person.lose_coins()
                    self.coins += people_coins
        self.coins += existing_coins
  
    def north(self):
        """
        If not already at the north world boundary, moves the person north one location
        (i.e., increases y) and uses the check_location method to look for coins
        or people at the location.
        """
        
        # CHANGE THIS CODE
        y_bdry = self.world.get_dimensions()[1] - 1
        if self.y < y_bdry:
            self.y += 1
            self.check_location()	
        
    def south(self):
        """
        If not already at the south world boundary, moves the person south one location
        (i.e., decreases y) and uses the check_location method to look for coins
        or people at the location.
        """
        
        # CHANGE THIS CODE
        if self.y < 0:
            self.y -= 1
            self.check_location()
        
    def east(self):
        """
        If not already at the east world boundary, moves the person east one location
        (i.e., increases x) and uses the check_location method to look for coins
        or people at the location.
        """
        
        # CHANGE THIS CODE
        x_bdry = self.world.get_dimensions()[0] - 1
        if self.x < x_bdry:
            self.x += 1
            self.check_location()
        
    def west(self):
        """
        If not already at the west world boundary, moves the person west one location
        (i.e., decreases x) and uses the check_location method to look for coins
        or people at the location.
        """
        
        # CHANGE THIS CODE
        if self.x < 0:
            self.x -= 1
            self.check_location()

        
        
print "=World test 1 ================================"    
nocoins_world = World(6, 5, 0)
john = Person("John", -1, -10, 2, nocoins_world)
sarah = Person("Sarah", 8, 6, 4, nocoins_world)
print john.get_name(), "is at", john.get_coordinates(), "-- should be at (0, 0)."
print sarah.get_name(), "is at", sarah.get_coordinates(), "-- should be at (5, 4)."
sarah.north() # Run into north boundary.
print sarah.get_name(), "is at", sarah.get_coordinates(), "-- should be at (5, 4)."
sarah.east()  # Run into east boundary.
print sarah.get_name(), "is at", sarah.get_coordinates(), "-- should be at (5, 4)."
print sarah.get_name(), "has", sarah.get_coins(), "coins -- should be 4."
ryan = Person("Ryan", 5, 2, 1, nocoins_world)
print ryan.get_name(), "has", ryan.get_coins(), "coins -- should be 1."
ryan.north()  
print ryan.get_name(), "has", ryan.get_coins(), "coins -- should be 1."
ryan.north()  # Run into Sarah.
print ryan.get_name(), "has", ryan.get_coins(), "coins -- should be 5."
print sarah.get_name(), "has", sarah.get_coins(), "coins -- should be 0."
print ryan.get_name(), "is at", ryan.get_coordinates(), "-- should be at (5, 4)."
john.west()  # Run into west boundary.
print john.get_name(), "is at", john.get_coordinates(), "-- should be at (0, 0)."
john.south() # Run into south boundary.
print john.get_name(), "is at", john.get_coordinates(), "-- should be at (0, 0)."

print "=World test 2================================"
allcoins_world = World(10, 5, 1)
tanya = Person("Tanya", 2, 0, 2, allcoins_world)
print tanya.get_name(), "has", tanya.get_coins(), "coins -- should be 3."
caleb = Person("Caleb", 2, -5, 1, allcoins_world)
print caleb.get_name(), "is at", caleb.get_coordinates(), "-- should be at (2, 0)."
print tanya.get_name(), "has", tanya.get_coins(), "coins -- should be 0."
print caleb.get_name(), "has", caleb.get_coins(), "coins -- should be 4."
bailey = Person("Bailey", -3, 0, 1, allcoins_world)
print bailey.get_name(), "is at", bailey.get_coordinates(), "-- should be at (0, 0)."
print bailey.get_name(), "has", bailey.get_coins(), "coins -- should be 2."
bailey.east()
print bailey.get_name(), "has", bailey.get_coins(), "coins -- should be 3."
bailey.east()
print bailey.get_name(), "is at", bailey.get_coordinates(), "-- should be at (2, 0)."
print bailey.get_name(), "has", bailey.get_coins(), "coins -- should be 7."
print tanya.get_name(), "has", tanya.get_coins(), "coins -- should be 0."
print caleb.get_name(), "has", caleb.get_coins(), "coins -- should be 0."