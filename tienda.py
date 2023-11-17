import random
import string
def tienda():
    class Producto:
        def __init__(self, nombre, precio, unidades):
            self.nombre = nombre
            self.precio = precio
            self.unidades = unidades

    class Cliente:
        def __init__(self, nombre_usuario, contrasena, correo, telefono, direccion, pais):
            self.nombre_usuario = nombre_usuario
            self.contrasena = contrasena
            self.correo = correo
            self.telefono = telefono
            self.direccion = direccion
            self.pais = pais
            self.carrito = {}
            self.iva = ivas_por_pais.get(pais, 0)

        def calcular_total_carrito(self):
            total_sin_iva = sum(producto["precio"] * producto["cantidad"] for producto in self.carrito.values())
            total_con_iva = total_sin_iva * (1 + self.iva / 100)
            return total_con_iva

    def agregar_al_carrito(cliente, producto_seleccionado, cantidad):
        if producto_seleccionado.unidades >= cantidad:
            nombre_producto = producto_seleccionado.nombre
            if nombre_producto in cliente.carrito:
                cliente.carrito[nombre_producto]["cantidad"] += cantidad
            else:
                cliente.carrito[nombre_producto] = {
                    "precio": producto_seleccionado.precio,
                    "cantidad": cantidad,
                }
                producto_seleccionado.unidades -= cantidad
                print(f"{cantidad} unidades de {nombre_producto} añadidas al carrito.")
        else:
            print("No hay suficientes unidades disponibles.")

    class RegistroUsuarios:
        def __init__(self):
            self.clientes_registrados = {}

        def agregar_cliente(self, cliente):
            if cliente.correo not in self.clientes_registrados:  # Cambia a usar el correo como clave
                self.clientes_registrados[cliente.correo] = cliente
                print(f"Cliente '{cliente.nombre_usuario}' registrado exitosamente.")
            else:
                print("El usuario ya existe. Por favor, elija otro correo electrónico.")

        def login(self, correo, contrasena):
            cliente = self.clientes_registrados.get(correo)

            if cliente and cliente.contrasena.strip() == contrasena.strip():
                print(" ")
                print("¡Inicio de sesión exitoso!")
                return cliente
            else:
                print("Credenciales inválidas. No se pudo iniciar sesión.")
                return None

    def solicitar_datos_cliente():
        print("Por favor, complete los siguientes campos para registrarse:")
        nuevo_username = input("Nuevo nombre de usuario: ")
        nuevo_password = input("Nueva contraseña: ")

        while True:
            nuevo_email = input("Correo electrónico: ")
            if '@' in nuevo_email:
                break
            else:
                print("El correo electrónico debe contener el símbolo '@'. Inténtelo de nuevo.")

        while True:
            nuevo_phone = input("Teléfono: ")
            if nuevo_phone.isdigit():
                break
            else:
                print("El número de teléfono debe contener solo dígitos. Inténtelo de nuevo.")

        nueva_address = input("Dirección: ")
        print("\nSeleccione su país:")
        for i, pais in enumerate(ivas_por_pais, start=1):
            print(f"{i}. {pais}")

        while True:
            try:
                seleccion_pais = int(input("Número del país: "))
                if 1 <= seleccion_pais <= len(ivas_por_pais):
                    break
                else:
                    print("Número de país no válido. Inténtelo de nuevo.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        nuevo_pais = list(ivas_por_pais.keys())[seleccion_pais - 1]

        return Cliente(nuevo_username, nuevo_password, nuevo_email, nuevo_phone, nueva_address, nuevo_pais)

    def mostrar_productos(productos):
        print("\n------ LISTA DE PRODUCTOS ------")
        for key, producto in productos.items():
            print(f"{key}. {producto.nombre} - {producto.precio:.2f} € (Disponibles: {producto.unidades})")


    def manejar_tienda(cliente, productos, ivas_por_pais):
        if cliente is None:
            print(" ")
            print("Debes iniciar sesión o registrarte para acceder a la tienda.")
            return

        while True:
            mostrar_productos(productos)
            print("7. Ver Carrito")
            print("8. Pagar")
            opcion_tienda = input("Seleccione una opción para agregar productos al carrito (1-6) o 'q' para salir: ")

            if opcion_tienda == 'q':
                print("Saliendo de la tienda.")
                break
            elif opcion_tienda == '7':
                mostrar_carrito(cliente)
            elif opcion_tienda == '8':
                try:
                    realizar_pago(cliente, productos)
                except ValueError:
                    print("Error: Ingrese una cantidad válida.")
            else:
                try:
                    opcion_tienda = int(opcion_tienda)
                    if 1 <= opcion_tienda <= len(productos):
                        producto_seleccionado = productos[opcion_tienda]
                        cantidad = int(input(f"Ingrese la cantidad de {producto_seleccionado.nombre} que desea agregar al carrito: "))
                        agregar_al_carrito(cliente, producto_seleccionado, cantidad)
                    else:
                        print(
                            "Opción inválida. Por favor, seleccione un número del 1 al 6, '7' para ver el carrito o '8' para pagar.")
                except ValueError:
                    print(
                        "Opción inválida. Por favor, ingrese un número del 1 al 6, '7' para ver el carrito o '8' para pagar.")

    def mostrar_carrito(cliente):
        print("\n------ CARRITO ------")
        if cliente.carrito:
            for nombre_producto, info in cliente.carrito.items():
                print(f"- {nombre_producto} ({info['precio']:.2f} € por unidad) - Cantidad: {info['cantidad']}")
        else:
            print("El carrito está vacío.")

    ivas_por_pais = {
        "España": 21,
        "Francia": 20,
        "Alemania": 19,
        "Italia": 22,
        "Reino Unido": 20,
        "Estados Unidos": 0,
        "Japón": 8,
        "Australia": 10,
        "Canadá": 5,
    }

    def realizar_pago(cliente, productos):
        total_con_iva = cliente.calcular_total_carrito()
        if total_con_iva > 0:
            print(f"Total a pagar (incluyendo IVA): {total_con_iva:.2f} €")
            metodo_pago = input("Seleccione el método de pago (Tarjeta/PayPal): ").lower()

            if metodo_pago == "tarjeta":
                # Solicitar información adicional para el pago con tarjeta
                numero_tarjeta = input("Ingrese el número de tarjeta: ")
                fecha_vencimiento = input("Ingrese la fecha de vencimiento (MM/AA): ")
                codigo_seguridad = input("Ingrese el código de seguridad (CVV): ")

                # Validar la información de la tarjeta (puedes agregar más validaciones según tus necesidades)
                if len(numero_tarjeta) == 16 and fecha_vencimiento.count('/') == 1 and len(codigo_seguridad) == 3:
                    mostrar_carrito(cliente)
                    print("\nInformación de tarjeta válida. Procesando el pago...")
                    print(f"Pago realizado con tarjeta. Se enviará a {cliente.nombre_usuario} la factura en PDF a su correo electrónico: {cliente.correo}.")
                    vaciar_carrito(cliente, productos)
                    generar_y_mostrar_codigo_seguimiento()
                else:
                    print("Información de tarjeta inválida. Operación cancelada.")
            elif metodo_pago == "paypal":
                email_paypal = input("Ingrese su dirección de correo electrónico asociada a PayPal: ")
                password_pago = input("Ingrese una contraseña para este pago en PayPal: ")
                mostrar_carrito(cliente)

                # Simulación de autenticación de PayPal (puedes ajustar según la integración real con PayPal)
                if autenticar_paypal(email_paypal, password_pago):
                    print("\n Autenticación de PayPal exitosa. Procesando el pago...")
                    vaciar_carrito(cliente, productos)
                    generar_y_mostrar_codigo_seguimiento()
                else:
                        print("Autenticación de PayPal fallida. Operación cancelada.")
            else:
                print("Método de pago no válido. Operación cancelada.")
        else:
            print("El carrito está vacío. No hay productos para pagar.")

    # ...

    def autenticar_paypal(email, password):
        return True

    def generar_y_mostrar_codigo_seguimiento():
        longitud_codigo = 10
        codigo_seguimiento = ''.join(random.choices(string.ascii_uppercase + string.digits, k=longitud_codigo))
        print(f"¡Gracias por tu compra! Tu código de seguimiento del pedido es: {codigo_seguimiento}")

    def vaciar_carrito(cliente, productos):
        for nombre, info in cliente.carrito.items():
            # Restaurar las unidades del producto eliminado del carrito
            for prod_id, producto in productos.items():
                if producto.nombre == nombre:
                    producto.unidades += info["cantidad"]
                    break

        cliente.carrito = {}  # Vaciar el carrito del cliente
        print(" ")

    def mostrar_menu():
        print("\n------ MENÚ ------")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Acceder a la tienda")
        print("4. Salir")

    registro = RegistroUsuarios()
    cliente_autenticado = None
    usuario_registrado = False

    productos = {
        1: Producto("Camiseta", 10.50, 8),
        2: Producto("Pantalones", 20.95, 4),
        3: Producto("Sudadera", 60.00, 6),
        4: Producto("Calcetines", 7.50, 9),
        5: Producto("Bufanda", 10.00, 7),
        6: Producto("Guantes", 9.95, 14),
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nuevo_cliente = solicitar_datos_cliente()
            registro.agregar_cliente(nuevo_cliente)
            usuario_registrado = True  # Marca que el usuario ha sido registrado
        elif opcion == "2":
            if usuario_registrado:
                print("Bienvenido a la tienda en línea.")
                print("Por favor, inicie sesión para continuar.")
                correo = input("Ingrese su correo electrónico: ")
                password = input("Ingrese su contraseña: ")

                # Asignar el cliente autenticado a la variable global
                cliente_autenticado = registro.login(correo, password)
                if cliente_autenticado:
                    print(f"¡Bienvenido, {cliente_autenticado.nombre_usuario}!")
            else:
                print("Debes registrarte antes de iniciar sesión.")
        elif opcion == "3":
            if cliente_autenticado is not None:
                manejar_tienda(cliente_autenticado, productos, ivas_por_pais)
            else:
                print("Debes iniciar sesión para acceder a la tienda.")
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")