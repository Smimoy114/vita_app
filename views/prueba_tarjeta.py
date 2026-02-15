from nicegui import ui

# Clase para representar los datos de cada venta
class Venta:
    def __init__(self, cliente, total):
        self.cliente = cliente
        self.total = total

# Clase/Componente para renderizar la tarjeta de cada venta
class VentaCard:
    def __init__(self, venta: Venta):
        with ui.card().classes('w-64 shadow-lg'):
            with ui.row().classes('items-center justify-between w-full'):
                ui.label(venta.cliente).classes('text-bold text-lg')
                ui.label(f'${venta.total}').classes('text-green-600 font-mono')

# Clase principal de la aplicación
class VentasApp:
    def __init__(self):
        self.lista_ventas = []  # Almacena instancias de la clase Venta

        # Interfaz de entrada
        with ui.card().classes('w-full max-w-md m-auto p-8'):
            with ui.expansion('Registrar Nueva Venta').classes('text-2xl mb-4'):
                self.cliente_input = ui.input('Nombre del Cliente')
                self.total_input = ui.number('Total de Venta', format='%.2f')
                ui.button('Guardar Venta', on_click=self.agregar_venta).classes('w-full mt-4')

            ui.separator().classes('my-8')

        # Panel de tarjetas (Sección dinámica)
        ui.label('Historial de Ventas').classes('text-xl mb-4 ml-4')
        self.render_panel()

    @ui.refreshable
    def render_panel(self):
        """Renderiza el contenedor de tarjetas basándose en la lista actual"""
        with ui.row().classes('gap-4 p-4'):
            if not self.lista_ventas:
                ui.label('No hay ventas registradas.').classes('text-gray-400 italic')
            for venta in self.lista_ventas:
                VentaCard(venta)

    def agregar_venta(self):
        # Validar y crear nueva instancia
        if self.cliente_input.value and self.total_input.value:
            nueva_venta = Venta(self.cliente_input.value, self.total_input.value)
            self.lista_ventas.append(nueva_venta)

            # Limpiar campos y refrescar el panel
            self.cliente_input.set_value('')
            self.total_input.set_value(None)
            self.render_panel.refresh()  # <-- Esto actualiza el panel visualmente
            ui.notify(f'Venta de {nueva_venta.cliente} guardada')

# Iniciar la app
#VentasApp()
#ui.run()

