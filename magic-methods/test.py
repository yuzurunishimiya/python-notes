# class Storage(float):
#     def __new__(cls, value, unit):
#         instance = super().__new__(cls, value)
#         instance.unit = unit
#         return instance

# storage = Storage(1024, "GB")
# print(storage.unit)
# print(storage)


# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     # def __repr__(self) -> str:
#     #     return f"{type(self).__name__}(name='{self.name}',age='{self.age}')"


# person = Person("John Doe", 25)
# print(person)
# # print(repr(person))



# class Rectangle:
#     def __init__(self, width, height) -> None:
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.height * self.width

#     def __eq__(self, other: 'Rectangle') -> bool:
#         return self.area() == other.area()


# bb = Rectangle(10, 10)
# cc = Rectangle(10, 10)
# print(bb == cc)
