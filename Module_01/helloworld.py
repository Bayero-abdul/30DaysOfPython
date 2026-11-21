print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)

print("Abdulkadir")
print("Bayero")
print("Nigeria")
print("I am enjoying 30 days of python")

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(['Asabeneh', 'Python', 'Finland'])
print(type("Abdulkadir"))
print(type("Bayero"))
print(type("Nigeria"))

### integer: 3
### float: 9.8
### Complex: 4 - 4j
### String: "Abdulkadir", "Bayero", "Nigeria"
### Boolean: True, False
### List: ['Asabeneh', 'Python', 'Finland']
### Tuple: ('Abdulkadir', 'Bayero', 'Nigeria')
### Set: {'Abdulkadir', 'Bayero', 'Nigeria'}
### Dictionary: {'first_name': 'Abdulkadir', 'last_name': 'Bayero', 'country': 'Nigeria', 'city': 'Lagos'}

# find an euclidean distance between two points (2, 3) and (10, 8)
import math
point1 = (2, 3)
point2 = (10, 8)
distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
print(distance)
