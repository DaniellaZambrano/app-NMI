import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Flet + Flask Example"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Función para obtener datos del backend
    def fetch_data(e):
        try:
            response = requests.get("http://127.0.0.1:5000/api/data")
            if response.status_code == 200:
                data = response.json()
                message.value = data["message"]
                info.value = data["info"]
                page.update()
            else:
                message.value = "Error al obtener datos"
                page.update()
        except Exception as err:
            message.value = f"Error: {err}"
            page.update()

    # Crear elementos de la interfaz
    message = ft.Text()
    info = ft.Text()
    fetch_button = ft.ElevatedButton("Obtener datos del backend", on_click=fetch_data)

    # Agregar elementos a la página
    page.add(fetch_button, message, info)

ft.app(target=main)
