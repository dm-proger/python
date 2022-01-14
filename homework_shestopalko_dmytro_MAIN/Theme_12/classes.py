# class FirstClass:
#     pass
#
# x = FirstClass()
# print(type(x))

# class FirstClass:
#     class_attr = 1
#
# x = FirstClass()
# y = FirstClass()
#
# print(x==y)
# print(id(x))
# print(id(y))
#
# x.class_attr == y.class_attr

# class_var = FirstClass
# type(class_var)

# Оголошуємо клас
class FirstClass:
    # в цього класа буде атрибут attr, який буде доступний кожному екземпляру класа
    class_attr = 0
    # створюємо метод класа. першим завжди буде self.
    # цей метод завжди приймає першим аргументом екземпляр класу
    def __init__(self, a, b):
        # присвоюємо атрибуту а значення змінної а, з б по аналогії
        self.a = a
        self.b = b

x = FirstClass(1, 2)
y = FirstClass(3, 4)

print(x.a)
print(y.a)
print(x.class_attr, y.class_attr)
