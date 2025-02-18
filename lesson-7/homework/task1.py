import math

class Vector:
    def __init__(self, *args):
        self._coords = list(args)

    def __str__(self):
        values = ', '.join(map(str, self._coords))
        return f"Vector({values})"

    def __eq__(self, other):
        return isinstance(other, Vector) and self._coords == other._coords

    def __add__(self, other):
        if len(self._coords) != len(other._coords):
            raise ValueError("Dimension mismatch")
        return Vector(*(a + b for a, b in zip(self._coords, other._coords)))

    def __sub__(self, other):
        if len(self._coords) != len(other._coords):
            raise ValueError("Dimension mismatch")
        return Vector(*(a - b for a, b in zip(self._coords, other._coords)))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*(c * other for c in self._coords))
        if isinstance(other, Vector):
            if len(self._coords) != len(other._coords):
                raise ValueError("Dimension mismatch")
            return sum(a * b for a, b in zip(self._coords, other._coords))
        raise TypeError("Invalid multiplication")

    def __rmul__(self, other):
        return self.__mul__(other)

    def magnitude(self):
        return math.sqrt(sum(c ** 2 for c in self._coords))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Zero vector cannot be normalized")
        return Vector(*(c / mag for c in self._coords))
