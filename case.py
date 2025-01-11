# Menú del restaurante
print("Bienvenido al Restaurante")
print("Menú:")
print("Categoría 1: Hamburguesas")
print("1.1. Simple - $5.00")
print("1.2. Doble - $7.00")
print("1.3. Doble con Tocino - $9.00")
print("Categoría 2: Pizzas")
print("2.1. Mediana - $8.00")
print("2.2. Grande - $10.00")
print("2.3. Extra Grande - $12.00")
print("Categoría 3: Bebidas")
print("3.1. Pequeña - $2.00")
print("3.2. Grande - $3.00")
print("3.3. Familiar - $4.00")

# Inicialización de variables
subtotal = 0
total_items = 0

# Ciclo para seleccionar platos
while True:
    seleccion = input("\nSeleccione un platillo (o escriba 'fin' para terminar): ")

    if seleccion == 'fin':
        break

    # Uso de match para simular un switch/case
    match seleccion:
        case '1.1':
            subtotal += 5
            total_items += 1
            print("Has seleccionado una Hamburguesa Simple.")
        case '1.2':
            subtotal += 7
            total_items += 1
            print("Has seleccionado una Hamburguesa Doble.")
        case '1.3':
            subtotal += 9
            total_items += 1
            print("Has seleccionado una Hamburguesa Doble con Tocino.")
        
        case '2.1':
            subtotal += 8
            total_items += 1
            print("Has seleccionado una Pizza Mediana.")
        case '2.2':
            subtotal += 10
            total_items += 1
            print("Has seleccionado una Pizza Grande.")
        case '2.3':
            subtotal += 12
            total_items += 1
            print("Has seleccionado una Pizza Extra Grande.")
        
        case '3.1':
            subtotal += 2
            total_items += 1
            print("Has seleccionado una Bebida Pequeña.")
        case '3.2':
            subtotal += 3
            total_items += 1
            print("Has seleccionado una Bebida Grande.")
        case '3.3':
            subtotal += 4
            total_items += 1
            print("Has seleccionado una Bebida Familiar.")
        
        case _:
            print("Selección no válida, por favor intente de nuevo.")

# Cálculo del IVA y total a pagar
iva = subtotal * 0.15
total_pagar = subtotal + iva

# Resumen final de la orden
print("\nResumen de su orden:")
print(f"Número total de platos seleccionados: {total_items}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"IVA (15%): ${iva:.2f}")
print(f"Total a pagar: ${total_pagar:.2f}")

print("\n¡Gracias por su pedido!")
