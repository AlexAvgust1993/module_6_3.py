class Horse:  # Лошадь
    def __init__(self):
        self.x_distance = 0  # пройденный путь.
        self.sound = 'Frrr'  # звук, который издаёт лошадь.

    def run(self, dx):
        self.x_distance += dx


class Eagle:  # Орёл
    def __init__(self):
        self.y_distance = 0  # высота
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):  # Пегас
    def __init__(self):
        super().__init__()
        Eagle.__init__(self)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)
    # def move(self, dx, dy):
    #     return self.fly(dy), self.run(dx)

    def get_pos(self):
        return self.x_distance, self.y_distance



    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()









# class Human:
#     def __init__(self, name, group):
#         self.name = name
#         super().__init__(group)
#         super().about()
#
#     def info(self):
#         print(f'Привет, меня зовут {self.name}')
#
#
# class StudentGroup:
#     def __init__(self, group):
#         self.group = group
#
#     def about(self):
#         print(f'{self.name} учится в группе {self.group}')
#
#
# class Student(Human, StudentGroup):
#     def __init__(self, name, place, group):
#         super().__init__(name, group)  # Метод super позволяет нам обращаться сразу к родителю и вызывать его методы.
#         # Human.__init__(self, name)
#         self.place = place
#         super().info()
#
#
# # human = Human("Alex")
# # print(human.name)
# student = Student('Oleg', 'Urban', 'Питон 1')
# student.about()
# print(Student.mro())
