#Condicional simple:

#a = int(input("coloca un numero entero A:"))
#b = int(input("coloca un numero entero B:"))

#if b != 0:
    #division = a // b
    #print("El resultado de la divison es:",division)
#print("Chau")

#Condicional doble:

#a = int(input("coloca un numero entero A:"))
#b = int(input("coloca un numero entero B:"))

#if b != 0:
    #division = a // b
    #print("El resultado de la divison es:",division)
#else:
    #print("No se puede dividir por 0")    
#print("Chau")

#Condicionales Anidados:

#x = int(input("Coloca un numero entero:"))

#if x == 0:
    #resultado ="neutro" 
#elif x > 0:
    #resultado = "positivo"
#else:
    #resultado = "negativo"

#print(x,"es",resultado)

#Condicionales multiples:

print("MENU DE VENTAS")
print("[1] Ventas")
print("[2] Soporte")
print("[3] Administración")
opción = int(input("Seleccione una opción:"))

match opción:
    case 1:
        print("Usted a seleccionado Ventas")
    case 2:
        print("Usted a seleccionado Soporte")
    case 3:
        print("Usted a seleccionado Administración")
    case _:
        print("opción inexistente")
        



#SIN EL MATCH-CASE
#if opción ==1:
    #print("Ventas")
#elif opción ==2:
    #print("Soporte")
#elif opción ==3:
    #print("Administración")
