import os


menu ="""
    1. Registrar Producto
    2. Buscar producto
    3. Listar productos
    4. Salir

"""

listacodigo =[]
listanombre = []
listacategoria =[]
listaprecio =[]
listacantidad =[]


codnum =[]

nombre= ()


while True:
    try:
        opc=int(input(menu))

        if opc == 4:
            print("A elegido salir")


        elif opc == 1:
            while True:
                try:
                    cod = int(input("codigo de seis digitos a ingresar: "))
                    if cod >= 100000 and cod < 1000000:
                        listacodigo.append(cod)
                        print(listacodigo)          
                        break
                    else:
                        print("error intente nuevamente" )

                except:
                        print("ocurrio una excepcion")


            while True:
                        try:
                            nom = input("nombre del producto: ")
                            if len(nom) >= 2 and len(nom) <=50:
                                listanombre.append(nom)
                                print(listanombre)
                                break
                            else:
                                print("Error, nombre debe tener a lo menos 2 characteres y maximo 50")
                        except:
                            print("excepcion de nombre")


            while True:
                        try:
                            cat = input("Categoria del producto: ")
                            if cat == "Paquete" or cat == "Sobre":
                                listacategoria.append(cat)
                                print(listacategoria)
                                break
                            else:
                                print("La categoria es incorrecta, por favor ingrese categoria valida")  

                        except:
                                print("excepcion de categoria")         


            while True:
                        try:
                            cant =int(input("Stock del producto a ingresar:"))
                            if cant > 0:
                                listacantidad.append(cant)
                                print(listacantidad)
                                break
                            else:
                                print("Intente nuevamente")
                        except:
                            print("Ocurrio una excepcion")
   
            
            while True:
                        try:
                            prec =input("Ingrese Precio :")
                            if prec > 0 and prec <= 100000:
                                listaprecio.append(prec)
                                print(listaprecio)
                                break
                            else:
                                print("Intente nuevamente")
                        except:
                            print("Ocurrio una excepcion")
   
            
            
            
        elif opc == 2:
            buscar= int(input("Codigo de 6 digitos a buscar: "))
            print(f"A seleccionado buscar {buscar} \n")
            print("|   Codigo Numerico    |   Nombre    |  Categoria   |  Cantidad  |")
            print("--+-------------+-------------------+----------------+------------+-")
            for i in range(len(codnum)):
                if buscar == listacodigo[i] and buscar >=100000 and buscar < 1000000:
                    print
                    print(f"|   {listacodigo[i]:9d} |   {listanombre[i]:13s} |  {listacategoria[i]:13s} |   {listacantidad[i]:6s}|  {listaprecio[i]:20d}  ")
                    print("--+-----------------------+------------------------+----------------------+-----------------------+------------")
        elif opc == 3:
            print("|   Codigo Numerico    |   Nombre    |  Categoria   |  Cantidad  |   Precio     | ")
            print("--+-----------------------+------------------------+----------------------+-----------------------+---------------------")
            for i in range(len(codnum)):
                 if listacantidad > 5:
                    st= "Limite de stock no se puede agragar mas de 5 productos"
                    print(f"|   {listacodigo[i]:15d} |   {listanombre[i]:13s} |  {listacategoria[i]:13s} |   {listacantidad[i]:6s}|  {listaprecio[i]:20d}  ")
                    print("--+-----------------------+------------------------+----------------------+-----------------------+------------")
    except:
        print("ocurrio una excepcion")



