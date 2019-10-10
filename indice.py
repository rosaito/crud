print ("------------------------------")
print ("1.Agregar")
print ("2.Eliminar")
print ("3.Listar")
print ("4.Modificar")
print ("5.Salir")
print ("------------------------------")


seleccion = None
nombre = None
apellido = None
edad = None
while seleccion != 5:
    seleccion = input("Ingrese un valor: ")
    if seleccion == "1":
        print("Agregar")
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        edad = input("Ingresa tu edad: ")
        print("Tus datos son: "+nombre+" "+apellido+" "+edad+" años")
    elif seleccion == "2":
        print("Eliminar")
        print("Datos a eliminar: "+nombre+" "+apellido+" "+edad+" años")
    elif seleccion == "3":
        print("Listar")
        print("Los datos actuales son: ")
        print (nombre+" "+apellido+" "+edad+" años")
    elif seleccion == "4":
        print("Modificar")
    elif seleccion=="5":
        print("Salir")
        break
exit()