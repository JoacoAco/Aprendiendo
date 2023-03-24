print("CIFRAX 0.01")
num = input("""
            Ingresa el número a cifrar: """)
passcode = num
passcode_1 = passcode*2
passcode_2 = int(passcode_1)
passcode_2 *=3.14159

if type(passcode_2) == int:
    print(f"Su número en el sistema de cifrado CIFRAX 0.01 es {passcode_2} y es un número entero")
elif passcode_2 >= 150:
    print (f"Su número en el sistema de cifrado CIFRAX 0.01 es {passcode_2} y es un número recomendado")
elif type(passcode_2) == float:   
    print(f"Su número en el sistema de cifrado CIFRAX 0.01 es {passcode_2} y es un número decimal no recomendado")


