from math import sin


print("filip")

my_list = [12, 13]

my_touple = (12, 13)

print(my_touple)

# dictionary 
my_dict =  {"Filip Kaminski": 23,
            "Tomasz Kania": 50,
            (1,2): 20,
            }
print( my_dict["Tomasz Kania"])
print ( my_dict[(1,2)])

print(my_touple.__hash__())


my_set = {1, 2, 3, 4, 5}

print(ord("a"))

dog_list = list("dog")
print(dog_list)



funny_cubes = [x**3 for x in range(1,11) if x%3 ==0]

funny_sines = list(map(sin, funny_cubes))



print (funny_cubes)

print(funny_sines)

def ceasar_cipher(message: str, shift: int) -> str:
    message = message.lower()
    message_list = list(message)
    

