# insert(), del(), pop() dont act on tuple
names = ["Swayam", "Eric", "Varun", "Minon", "Soham", "Tatha"]
print(sorted(names))
print(names)
names.insert(1,"Adhil")
print(names)
print(names.pop()) # Shows the popped name
print(names)
del names[1]
print(names)
names.pop()
print(names)
names.pop(1)
print(names)
print(sorted(names))

print("\n")

# only sorted() acts on tuple
name = ("Swayam", "Eric", "Varun", "Minon")
print(name)
print(sorted(name))
