# List exercise

carmakes = ['BMW', 'Honda', 'Toyota', 'Ford', 'Rivian', 'Audi']

slice1 = (carmakes[0:2])
slice2 = (carmakes[2:4])

message1 = f"The first two items in the list are: {slice1}"
message2 = f"The middle two items in the list are: {slice2}"
message3 = f"The first and last items in the list are: {carmakes[0]}, {carmakes[-1]}"

print(carmakes)
print(message1)
print(message2)
print(message3)

print("\n")

# Tuple Exercise

menuitems = ("Tuna crudo", "Tacos", "Steak", "Redfish almondine", "Bread pudding")


for food in menuitems:
    print(food.title())

print("\n")

newmenuitems = ("Tuna crudo", "Gumbo", "Steak", "Redfish almondine", "Beignets")

for food in newmenuitems:
    print(food.title())