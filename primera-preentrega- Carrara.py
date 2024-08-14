usuarios={}

def agregar_usuario():
    while True:
        try:
         
         usuario= input('Ingrese nombre de usuario o coloque x para volver al menu: ')
         if usuario=='x' :
          break
         elif usuario in usuarios:
             print (f'Usuario {usuario} ya se encuentra registrado, por favor, intente otro nombre')
             return agregar_usuario()
         elif usuario not in usuarios: 
           clave= input('ingrese contraseña: ')
           usuarios[usuario]=clave
           print(f'Usuario {usuario} creado con exito!')
           break
        finally:
            pass


def login():
     while True:
        try:
             usuario= input('Ingrese su usuario o coloque x para volver al menu: ')
             if usuario=='x' :
                break
             elif usuario in usuarios:
              clave= input(f' Hola {usuario}, ingresa tu clave: ')
              if usuarios[usuario]==clave:
               print('Inicio de sesion exitoso')
              else:
               print('Combinacion de clave y usuario incorrecta, intente nuevamente')
               return login()
             else: 
                print('Usuario no se encuentra en la base, intente nuevamente')
                return login()
        finally:
            pass



while True:     
    try:
        accion=int(input('Bienvenido! \n Por favor, selecciona la acción que queres realizar: \n 1- Iniciar sesión  \n 2-Crear Usuario \n 3-Ver lista de usuarios \n 4-Salir\n'))
        if accion == 1:
            print('Inicio de sesión')
            login()
            
        elif accion == 2:
            print('Creación de usuario')
            agregar_usuario()   
            
        elif accion == 3:
             if not usuarios :
                print ('No hay usuarios creados')
             else:
                 print('Listado de ususarios')
                 print(usuarios) 
            
        elif accion == 4:
             print('Programa finalizado. Adios!')
             break
        elif  1>accion or accion>4:
          print('Numero invalido.\n Por favor, coloca un numero entre 1 y 4')
    except ValueError:
       print('Por favor, intenta de nuevo ingrasando un numero')
  
    finally:
        pass


