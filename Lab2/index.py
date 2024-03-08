# goldbach conjecture

from itertools import filterfalse
from typing import Tuple

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for divisor in range(2,number//2):
        if number % divisor == 0:
            return False
    return True

def get_number(string: str) -> int: 
    components = string.split(sep=" ")
    return int(components[0])

def find_primes(x : int) -> Tuple[int]: 
    if x % 2 == 1:
        raise ValueError(f"The number should be even, but {x} is not.")
    for i in range(3, 1 + x//2):
        h=0
        if is_prime(i) and is_prime(x - i):
            return (str(x), str(i), str(x - i))
    raise RuntimeError("Conjecture falsified!!!")

file = open("Dane_PR2/pary.txt", "r")

contents = file.readlines()
file.close()
contents = list(map(lambda string: string.strip(), contents))
contents = list(map(get_number, contents))
even_numbers = list(filterfalse(lambda number: number % 2, contents))
prime_decompositions = list(map(find_primes, even_numbers))
prime_decompositions = list(map(lambda tup: " ".join(tup), prime_decompositions))


print(prime_decompositions)

answer = open("wynik.txt", "w")
for item in prime_decompositions:
    answer.write(item + "\n")

answer.close()


string = "xxyyyyaxaaa"

def longest_constant_substring(sting: str) -> int:
    max = 0 
    counter = 0 
    priv = ""
    for char in string:
        if (char == priv):
            counter+=1
        else:
            counter = 1
        priv = char
        if (max < counter):
            max = counter

    return max

print(longest_constant_substring(string))