# Función para sumar dos números
def suma(a, b):
    return a + b

# Función para restar dos números
def resta(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicacion(a, b):
    return a * b

# Función para dividir dos números
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"

# Solicitar al usuario que ingrese dos números y la operación deseada
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Selecciona la operación (+, -, *, /): ")

# Realizar la operación seleccionada
if operacion == '+':
    print("Resultado:", suma(num1, num2))
elif operacion == '-':
    print("Resultado:", resta(num1, num2))
elif operacion == '*':
    print("Resultado:", multiplicacion(num1, num2))
elif operacion == '/':
    print("Resultado:", division(num1, num2))
else:
    print("Operación no válida")