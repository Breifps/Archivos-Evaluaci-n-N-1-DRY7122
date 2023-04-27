#Crear un script en Python que imprima el texto “Evaluación N°1 Programación y Redes Virtualizadas” y los nombres de los integrantes de la evaluación.
#Script Utilizado:
print("Evaluación N°1 Programación y Redes Virtualizadas")
print("Integrantes:Bastian Rodriguez")


#Crear un script en Python que solicite información como el nombre, apellido, Código-sección y sede. La información debe aparecer en pantalla.
#Script Utilizado:
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
codigo_seccion = input("Ingrese su Código-sección: ")
sede = input("Ingrese su sede: ")

print("Su nombre es",nombre, apellido,"su seccion es", codigo_seccion, "y su sede en Duoc es",sede)


#Crear un script en Python que al momento que un usuario introduzca el número de ACL IPv4, señale si es una ACL Estándar, Extendida o el número no corresponde a una lista de acceso.
acl_num = int(input("Ingrese el número de ACL IPv4: "))
if 1 <= acl_num <= 99 or 1300 <= acl_num <= 1999:
  print("El número de ACL IPv4 corresponde a una ACL Estándar.")
elif 100 <= acl_num <= 129 or 2000 <= acl_num <= 2699:
  print("El número de ACL IPv4 corresponde a una ACL Extendida.")
else:
  print("El número de ACL IPv4 no corresponde a una lista de acceso.")

