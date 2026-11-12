# Einstein

# c = 300,000,000 will cause an error
# because it will act like a tuple instead of an int

c = 300000000      # m/s
m = int(input("mass: ")) # kg

E = m * (c ** 2)
print(E)
