def avanzar():
    print("Hola, estoy avanzando")

#Verifica si se esta ejecutando en el propio modulo o estq siendo llamado en otro modulo
#Si esta siendo llamado desde otro modulo lo siguiente no se ejecutara
#Si es ejecutado el propio modulo entonces si se ejecturará
if __name__ == "__main__":
    avanzar()