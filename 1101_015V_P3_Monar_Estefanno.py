import os
os.system('cls')

Lista_NIF=[]
nacimiento = []
estado_conyugal = []
nombre= []

def grabar():
    print("grabe sus datos NIF")
    
    v_nif = input("ingrese su nif: ")
    v_estado_conyugal = input('ingrese su estado conyugal: ')
    v_nombre = input("ingrese su nombre: ")
    v_fecha_de_nacimiento = input('ingrese su fecha de nacimiento: ')
    v_edad = int(input("ingrese su edad: "))
    v_union_europea = input('eres de la unio europea: ')
       


    nif={
        'nif' : v_nif,
        'estado conyugal' : v_estado_conyugal,
        'fecha de nacimineto': v_fecha_de_nacimiento,
        'edad' : v_edad,
        'nombre' : v_nombre,
        'union europea' : v_union_europea 
                            }
    
    estadoconyugal={ v_estado_conyugal
                                        }                    
    
    vnacimento={
                'fecha de nacimiento':v_fecha_de_nacimiento
                }
                                
    
    vnombre={'nombre':v_nombre}

    nombre.append(vnombre)
    nacimiento.append(vnacimento)
    estado_conyugal.append(estadoconyugal)
    Lista_NIF.append(nif)

def buscar():
    print('Ingrese NIF de la persona que esta buscando')
    v_nif = input('ingrese NIF: ' )
    v_encontrado = False
    for nif in Lista_NIF:
        if nif ['nif'] == v_nif :
            print(nif)
            v_encontrado = True

def imprimir():
    while True:
         v_nif = input('ingrese NIF: ' )
         v_encontrado2 = False
         for nif in Lista_NIF:
            if nif ['nif'] == v_nif :
                print('porfavor escoja que tados desea inprimir ')
                v_encontrado2= True

                print('''
                1.-acta de nacimineto
                2.-Estado conyugal
                3.-pertenecia a la Union Europea
                4.-salir
                ''')
            try:
                op= int(input('ingrese opcion deseada: '))
            except:
                op = 0
            if op < 1 or op > 4:
                print('opcion no valida')
            else:
                if op == 1:
                    print('nacimiento')
                    print('enesta acta de nacimiento', (nacimiento), 'esta con sus fecha de nacimiento actualizado')
                elif op == 2:
                    print('estado conyugal')
                    print('el estado conyugal del sr/sra ', (nombre), 'es', (estado_conyugal))
                elif op == 3:
                    print('pertenencia en la union europea')
                    print('el/la sr/sra', (nombre), 'si pertenece a la union europea')
                elif op == 4:
                    salir()
                    break


def salir():
    print('salistes del programa')





while True:
    print('Menu De opciones')

    print('''
        1.-Grabar datos
        2.-Buscar datos
        3.-Impirmir
        4.-salir
          ''')
    try:
        op=int(input('ingrese una opcion: '))
    except:
        op = 0
    if op < 1 or op > 4:
        print('opcion no valida')
    else:
        if op == 1:
            grabar()
        elif op == 2:
            buscar()
        elif op == 3:
            imprimir()
        else:
            salir()
            break
