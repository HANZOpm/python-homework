import math

a = 100_000_000
b = 1e10
c = 1.4e3
print(a)
print(b)
print(c)

d = math.sqrt(2)

print(f"{d:.5f}")

name = "Jonathan"
print(f"{name:<10} - first name")

my_str = "Hello World" # Sequence

# Slicing or Indexing
print(my_str[4:20])
print(my_str[-1])
print(my_str[-5:])
print(my_str[-10:4])

# BEGIN:END:STEP
print(my_str[3:10:2])

# SyntaxError
# TypeError
# ValueError
# IndexError: string index out of range

print("a", "b")
print("a", "b", sep="_")
print("a", end="")
print("b", end="")
print("c")

# Mutable vs Immutable (O'zgaruvchan vs O'zgarmas)

word = "        Hello World        "
print(word.strip(), "check")
print(word.lstrip(), "check")
print(word.rstrip(), "check")

fruits = "apple banana cherry"
print(fruits.split())
fruits2 = "apple*banana*cherry"
print(fruits2.split("*"))