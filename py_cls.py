one = 'Today is a happy day.'
two = 'Finding happiness is such a nice thing.'

length_one = len(one)
length_two = len(two)
py = 22/7
radius = length_one**2

print('1.',length_one)
print('2.',length_two)

area_sphere = 4 * py * radius

print('Area of Sphere is:',area_sphere)

if (length_one > length_two):
    print('The highest Value is:', length_one)
elif(length_two > length_one):
    print('The highest Value is:', length_two)