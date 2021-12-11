# # Examples 1
# class partyanimal:
#     x = 0
#     def party(self):
#         self.x = self.x + 1
#         print("So far", self.x)
#
# an = partyanimal()
# an.party()
# an.party()
# an.party()
# print(an.x)
# print(type(an))
# print(dir(an))


# Example 2
# Constructor and Destructor
# class partyanimal:
#     x = 0
#     # object constructor
#     def __init__(self):
#         print("I am constructed.")
#     def party(self):
#         self.x = self.x + 1
#         print("So far", self.x)
#     # object destructor
#     def __del__(self):
#         print("I am destructed at", self.x)
# an = partyanimal()
# an.party()
# an.party()
# an = 30
# print(an)

# Example 3
# Independent instances local scope variable
class partyanimal:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name, "is constructed")
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)
# s = partyanimal("Tiger")
# s.party()
# li = partyanimal("Lion")
# li.party()
# s.party()

# Example 3, inheritance
class childclass(partyanimal):
    points = 0
    def touchdown(self):
        self.points = self.points +7
        self.party()
        print(self.name, "points", self.points)

s = partyanimal("Tiger")
s.party()
try:
    s.touchdown()
except:
    print("Parent has limited functionality")
j = childclass("Lion")
j.party()
j.touchdown()
