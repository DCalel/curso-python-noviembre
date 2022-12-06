# While
i = 0
while i<=10:
    print(i)
    i+=1
print('ciclo roto')

# For
alumnos = ['Adan', 'Eva', 'Jorge','Gaby','Eva']

for alumno in alumnos:
    if alumno == 'Eva':
        print('Encontramos a Eva')
        continue
    print(alumno)