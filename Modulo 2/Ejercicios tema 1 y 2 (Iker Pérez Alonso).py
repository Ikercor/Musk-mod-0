# 1. Haz un programa que escriba una línea con el mensaje “Buenos días a todo el mundo!”.

print('Buenos días a todo el mundo!')


# 2. Haz un programa que declare tres palabras a, b y c, y que escriba una línea con c, b y a en este orden.

a = 'a todos'
b = 'días'
c = 'Buenos'

print(f'{c} {b} {a}')


# 3. Haz un programa que declare dos números y que escriba la suma.

num1 = 10
num2 = 20

print(num1 + num2)


# 4. Haz un programa que declare dos números y que escriba el máximo.

num3 = 20
num4 = 10

print(max(num3,num4)) # este comando se usa para declarar el maximo entre una serie de numeros seleccionados 


# 5. Haz un programa que declare tres números, todos diferentes, y que escriba el máximo.

num5 = 10
num6 = 20
num7 = 30

print(max(num5,num6,num7))


# 6. Hacer un programa que dado un valor calcule su cuadrado y el cubo. 

num8 = 10

print(num8 ** 2)
print(num8 ** 3)


# 7. Haz un programa que devuelva el valor absoluto de un número.

num9 = -10

print(abs(-10)) # Este comando devuelve el valor absoluto del numero indicado

# 8. Haz un programa que lea dos naturales a y b, con b > 0, y que escriba la división entera d y el residuo r de a entre b. Recordad que, por definición, d y r tienen que ser los únicos enteros tales que 0 ≤ r < b y d · b + r = a. Ejemplo: a=32, b=5, d=6, r=2 ya que 32 = 5 * 6 + 2

a = 32
b = 5
d = a//b
r = a%b

print(f'numeros naturales a dividir son {a,b} la division entera {d} y el residuo {r}')


# 9. Haz un programa que, dada una cantidad de segundos, diga cuántas horas, minutos y segundos representa.

x = int(input('Dime un numero de segundos '))
horas = x / 3600
minuts = x / 60
segun = x

print(f'{segun} segundos son {minuts} minutos y {horas} horas' )


# 10. Haz un programa que dada una temperatura en grados Celsius la muestre en grados Fahrenheit y en grados Kelvin. (F= 1.8C + 32 y  ºK =°C + 273ºK).

y = int(input('Dime una temperatura en grados '))
f = y * 1.8 + 32
k = y + 273

print(f'{y} grados Celsius son {f} grados Fahrenheit y tambien {k} grados Kelvin' )