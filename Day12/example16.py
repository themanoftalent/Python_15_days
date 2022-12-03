class Student():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}: {self.age}'

    def __repr__(self):
        return f'Student({self.name}, {self.age})'

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __le__(self, other):
        return self.age <= other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __ne__(self, other):
        return self.name != other.name or self.age != other.age

    def __add__(self, other):
        return self.age + other.age

    def __sub__(self, other):
        return self.age - other.age

    def __mul__(self, other):
        return self.age * other.age

    def __truediv__(self, other):
        return self.age / other.age

# Drive
if __name__ == '__main__':
    s1 = Student('张三', 18)
    s2 = Student('李四', 20)
    print(s1 == s2)
    print(s1 < s2)
    print(s1 > s2)
    print(s1 <= s2)
    print(s1 >= s2)
    print(s1 != s2)
    print(s1 + s2)
    print(s1 - s2)
    print(s1 * s2)
    print(s1 / s2)
