es_adulto = True

if es_adulto:
    print("Bienvenido adulto")
else:
    print("No eres bienvenido niño")


edad = input("Ingresa tu edad: ")
edad = int(edad)

if edad > 18:
    print("Bienvenido adulto")
elif edad == 18:
    print("Justo empiezas a ser un adulto")
else:
    print("No eres bienvenido niño")