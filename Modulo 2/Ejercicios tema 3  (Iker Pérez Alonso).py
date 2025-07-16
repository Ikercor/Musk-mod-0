# 1. Haz un programa que lea un número decimal por pantalla, lo convierta a entero y lo imprima.
     # 4.8 numero que da el ejercicio 

x =float(input('Dime un numero decimal para pasartelo a entero' ))

print(int(x))


# 2. Haz un programa que lea un número decimal por pantalla e imprima su tipo y su valor redondeado en la misma línea.
     # 4.8 numero que da el ejercicio 

y = float(input('Dime un número decimal '))
tip = type(y)
redondeado = round(y) #este comndo se usa para redondear los numeros 

print(f'el tipo es {tip} y el valor redondeado es {redondeado}' )


# 3. Haz un programa que lea dos números por pantalla e imprima su diferencia en valor absoluto.
     #  14 y 37 son los numeros que nos proporciona el ejercicio 
num1 = float(input('Dime un numero'))
num2 = float(input('Dime otro numero'))
diferen = abs(num1 - num2) #  Este comando devuelve el valor absoluto del numero indicado

print(f'la diferencia entre {num1} y {num2} es de {diferen}')
