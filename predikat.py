# 7. Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите x: '))
y = int(input('Введите y: '))
z = int(input('Введите z: '))
if (not(x or y or z) == (not x) and (not y) and (not z))==1:
    print('Истина')
else:
    print('Ложь')
