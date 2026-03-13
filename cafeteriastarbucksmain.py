from cafeteria import *

productos = [
    Producto("Caramel Macchiato", 75, 60),
    Producto("Frappuccino Mocha", 85, 45),
    Producto("Latte Vainilla", 70, 50),
    Producto("Cold Brew", 65, 55, es_vegano=True),
    Producto("Pumpkin Spice Latte", 80, 40),
    Producto("Panini de Pavo", 90, 20),
    Producto("Cheesecake", 95, 15, sin_gluten=True),
    Producto("Blueberry Muffin", 55, 30)
]
    

print("----------------- MENÚ STARBUCKS  ------------------")
for i in range(len(productos)):
    p = productos[i]

    info = f"({'V' if p.es_vegano else ''}{'SG' if p.sin_gluten else ''})"
    print(f"{i + 1} - {p.nombre} (${p.precio}) {info if info != '()' else ''}")

opcion = int(input("\nElige un producto (1-8): ")) - 1
producto_elegido = productos[opcion]


control_suministros = Inventario()


ingrediente = "Harina" if "Panini" in producto_elegido.nombre or "Muffin" in producto_elegido.nombre or "Cheesecake" in producto_elegido.nombre else "Cafe"

if control_suministros.reducir_stock(ingrediente, 1):
    
    instrucciones = input("¿Instrucciones especiales?: ")
    desea_extra = input("¿Desea agregar un extra por $15? (si/no): ")
    precio_extra = 15 if desea_extra.lower() == "si" else 0

    
    empleado1 = Empleado(101, "Monse", "Monnn@cafe.com", "E-500", "Barista")
    nombre_c = input("Tu nombre: ")
    cliente1 = Persona(1, nombre_c, "correo@ejemplo.com")

    
    pedido1 = Pedido(800, cliente1.nombre)
    
    if pedido1.agregar_producto(producto_elegido, instrucciones, precio_extra):
        
        
        empleado1.cambiar_estado_pedido(pedido1, "PREPARANDO")
        empleado1.cambiar_estado_pedido(pedido1, "ENTREGADO")

        
        print("\n----------------- TICKET DE VENTA ------------------")
        print("Atendido por:", empleado1.nombre)
        print("Cliente:", cliente1.nombre)
        print("Producto:", producto_elegido.nombre)
        print("Notas:", instrucciones)
        print("Total a pagar: $", pedido1.total)
        print("Estado final:", pedido1.estado)
        print("----------------------------------------------------")
        
    
        print(f"Suministros restantes de {ingrediente}: {control_suministros.ingredientes[ingrediente]}")

else:
    print(f"No se puede preparar: falta {ingrediente} en inventario.")
