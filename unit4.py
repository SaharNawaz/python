#ex 1
favorite=['Tikka', 'supreme','crown crust']
for pizza in favorite:
    print(pizza)
for pizza in favorite:
    print(f"I like{pizza}pizza")

print('I love pizza')  

#ex9
cubes=[number**3 for number in range(1,11)]
for cube in cubes:
    print(cube)