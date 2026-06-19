import inflect

p = inflect.engine()

names = ["Alice", "Bob", "Charlie", "Charlo"]

print(p.join(names))
