import math
class Vector:
    def __init__(self, *args):
        self.dimensions = [*args]

    def __add__(self, other):
        try:
            if len(self) == len(other):
                new_vector = Vector()
                for i in self.dimensions:
                    new_vector.dimensions.append(i + other.dimensions[self.dimensions.index(i)])
                return new_vector
            else:
                raise TypeError
        except TypeError:
            raise Exception("Vectors of different dimensions can't be added")

    def __sub__(self, other):
        try:
            if len(self) == len(other):
                new_vector = Vector()
                for i in self.dimensions:
                    new_vector.dimensions.append(i - other.dimensions[self.dimensions.index(i)])
                return new_vector
            else:
                raise TypeError
        except TypeError:
            raise Exception("Vectors of different dimensions can't be substructed")

    def __mul__(self, other):
        try:
            if type(other) == Vector:
                if len(self) == len(other):
                    dot_product = 0
                    for i in self.dimensions:
                        dot_product += i * other.dimensions[self.dimensions.index(i)]
                    return dot_product
                else:
                    raise TypeError
            else:
                new_vector = Vector()
                for i in self.dimensions:
                    new_vector.dimensions.append(i * other)
                return new_vector
        except TypeError:
            raise Exception("Vectors of different dimensions can't be dot producted")

    def magnitude(self):
        vector_magnitude = 0
        for i in self.dimensions:
            vector_magnitude += i**2
        return math.sqrt(vector_magnitude)

    def normalize(self):
        new_vector = Vector()
        for i in self.dimensions:
            new_vector.dimensions.append(round((i / self.magnitude()), 3))
        return new_vector

    def __len__(self):
        return len(self.dimensions)

    def __str__(self):
        dimensions = ""
        for i in self.dimensions:
            dimensions += f"{i}, "
        return f"Vector({dimensions[:-2]})"

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8)

print(v1 + v2)
# print(v1 + v3)

print(v1 - v2)
# print(v1 - v3)

print(v1 * v2)
# print(v1 * v3)
print(v1 * 3)

print(v1.magnitude())

print(v1.normalize())