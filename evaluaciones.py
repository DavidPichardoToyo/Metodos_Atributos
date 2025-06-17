from pizza import Pizza

# Print para mostrar en pantalla los atributos de clase
print(f" El tamaño de la pizza es: {Pizza.tamaño} y su precio es de: {Pizza.precio}")

#Print para mostrar si un elemento se encuentra en la lista
print(Pizza.validar("salsa de tomate",["salsa de tomate", "salsa bqq"]))

pizza1 = Pizza()

pizza1.realizar_pedido()

Pizza.validar