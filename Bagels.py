import random

NUM_DIGITADOS = 3 # (!) intenta cambiar esto del 1 o 10.
MAX_SUPOSICIONES = 10 # (!) intenta cambiar esto del 1 o 100

def main():
    print("""Bagels, el juego de logica deductiva
Estoy pensando en un {}- numero digital que no repite los mismos numeros.
trata de adivinar cual es. aqui ay algunas pistas:
Cuando digo:  Eso significa:
 Pico        Un digito es correcto pero es incorrecta la posicion.
 Fermi       Un digito es correcto y la posicion es Correcta.
 Bagels      El digito no es correcto.
 
 Por ejemplo, si el numero secreto es 248 y el numero que elejiste es 843, la pista 
 deberia ser Fermi Pico.""".format(NUM_DIGITADOS))
    
    while True: # Bucle del juego.
        # Esto almacena el número secreto que el jugador necesita adivinar:
        secretNum = getSecretNum()
        print('Tengo pensado un numero.')
        print('Tu tienes {} que adivinar.'.format(MAX_SUPOSICIONES))
        
        numSuposiciones = 1
        while numSuposiciones <= MAX_SUPOSICIONES:
            suposicion = ''
            # Seguir con el bucle hasta que la suposicion sea valida:
            while len(suposicion) != NUM_DIGITADOS or not suposicion.isdecimal():
                print('Suposicion #{}: '.format(numSuposiciones))
                suposicion = input('> ')

            Pistas = obtPistas(suposicion, secretNum)
            print(Pistas)
            numSuposiciones += 1

            if suposicion == secretNum:
                break # Esta en lo correcto, asi que rompe el bucle.
            if numSuposiciones > MAX_SUPOSICIONES:
                print('Te quedaste sin suposiciones.')
                print('La respuesta era {}.'.format(secretNum))

            
        # Pregunta al jugador si quiere jugar de nuevo.
        print('Quieres jugar Una vez mas? (Yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Gracias por jugar UwU!')


def getSecretNum():
    """Devuelve una cadena formada por NUM_DIGITADOS digitos aleatorios unicos"""
    numeros = list('0123456789') # Crea una lista de digitos del 0 al 9.
    random.shuffle(numeros) # Para estar en random los digitos.

    # Tomar el primero NUM_DIGITADOS digito en la lista del numero secreto:

    secretNum = ''
    for i in range(NUM_DIGITADOS):
        secretNum += str(numeros[i])
    return secretNum

def obtPistas(suposicion, secretNum):
    """"Devuelve una cadena con las pistas pico, fermi, bagels 
    para una conjetura y un par de números secretos"""
    if suposicion == secretNum:
        return 'Lo tienes!'

    Pistas = []

    for i in range(len(suposicion)):
        if suposicion[i] == secretNum[i]:
            # Un dígito correcto está en el lugar correcto.
            Pistas.append('Fermi ')
        elif suposicion[i] in secretNum:
            # Un digito correcto en el lugar incorrecto.
            Pistas.append('Pico ')
    if len(Pistas) == 0:
        return 'Bagels' # No hay dígitos correctos en absoluto.
    else:
        # Clasifica las pistas en orden alfabético para que su orden original.
        # No da informacion.
        Pistas.sort()
        # Haz una sola cadena de la lista de pistas de cadenas.
        return ''.join(Pistas)

# Si se ejecuta el programa (en lugar de importarlo), ejecute el juego:
if __name__ == '__main__':
    main()
