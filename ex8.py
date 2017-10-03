formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("One", "Two", "Three", "Four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Roses are red,",
    "I have a box,",
    "My nanny was unfortunate,", 
    "Got impailed by an ox"
))
