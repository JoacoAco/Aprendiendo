print("""
      CALCUMAX 3000""")
print("""
        1) Suma
        2) Resta
        3) Multiplicación
        4) División
        5) Exponencial""")

operacion_1 = input("Ingrese la operación: ")
operacion_2 = int(operacion_1)
valor1 = input("Ingrese el primer valor: ")
valor2 = input("Ingrese el segundo valor: ")

if operacion_2 == 1:
    resultado = float(valor1) + float(valor2)
    print(f"Su resultado es {resultado}")
elif operacion_2 == 2:
    resultado = float(valor1) - float(valor2)
    print(f"Su resultado es {resultado}")  
elif operacion_2 == 3:
    resultado = float(valor1) * float(valor2)
    print(f"Su resultado es {resultado}")
elif operacion_2 == 4:
    resultado = float(valor1) / float(valor2)
    print(f"Su resultado es {resultado}")
elif operacion_2 == 5:
    resultado = float(valor1) ** float(valor2)
    print(f"Su resultado es {resultado}")
else:
    print("Valor incorrecto. Ingrese de nuevo")
    
