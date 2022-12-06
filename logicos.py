# Conjución - representado por: and
print(12 > 2 and 5 < 10)

# Disyunción - representado por: or
print(12 > 2 or 5 < 10)
print(9 != 6 or 8 <= 5)

# Negacion - representado por: not
print(not True)

edad = 18
nacionalidad = 'guatemalteco'

if edad >= 18 and nacionalidad == 'guatemalteco':
    print('Puede votar')
else:
    print('No puede votar')

def validar_persona_para_votar(edad, nacionalidad):
    if edad >= 18:
        if nacionalidad == 'guatemalteco':
            print('Puede votar')
        else:
            print('No puede votar por nacionalidad')
    else:
        print('No puede votar por la edad')

def validar_persona_para_votar_refactor(edad, nacionalidad):
    if not edad >= 18:
        print('No puede votar por la edad')
        return

    if not nacionalidad == 'guatemalteco':
        print('No puede votar por nacionalidad')
        return


validar_persona_para_votar(18,'colombiano')

validar_persona_para_votar_refactor(17,'guatemaltec')