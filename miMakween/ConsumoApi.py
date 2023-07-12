import requests
import os

os.system('cls')

# Obtener la lista de servicios desde la API
url = 'http://127.0.0.1:8000/servicio/'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Mostrar los servicios disponibles
    print("SERVICIOS DISPONIBLES:")
    print("---------------------")
    for i, servicio in enumerate(data, start=1):
        print(f"{i}. Nombre: {servicio['nombre']}")
        print(f"   Precio: {servicio['precio']}")

    # Solicitar al usuario seleccionar un servicio
    selected_service = int(input("Seleccione un servicio: "))

    # Verificar la selección del servicio
    if 1 <= selected_service <= len(data):
        servicio_elegido = data[selected_service - 1]

        # Mostrar la información del servicio elegido
        print("\nDETALLES DEL SERVICIO:")
        print("----------------------")
        print(f"Nombre: {servicio_elegido['nombre']}")
        print(f"Precio: {servicio_elegido['precio']}")
        print(f"Foto: {servicio_elegido['foto']}")
        
        # Aquí puedes agregar más lógica, como solicitar información adicional al usuario,
        # procesar el pedido, etc.
    else:
        print("Selección inválida.")
else:
    print('Error al hacer la solicitud:', response.status_code)
