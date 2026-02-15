from nicegui import ui
from datetime import datetime
from controllers.ventas_controller import VentasController
from views.prueba_tarjeta import VentasApp
from views.ventas_card import VentaCard
from controllers.productos_controller import ProductoController

controller = ProductoController()

controller_ventas = VentasController()


@ui.refreshable
def render_lista_pendientes(container_cards):
    """Refresca solo las tarjetas que vienen de la Base de Datos"""
    container_cards.clear()
    ventas_db = controller_ventas.listar_ventas_pendientes()

    with container_cards:
        if not ventas_db:
            ui.label('No hay ventas activas en el local').classes('text-grey-5 italic m-4')

        for v in ventas_db:
            # Instanciamos la tarjeta con ID existente
            # Pasamos render_lista_pendientes.refresh como callback para actualizar al pagar/cancelar
            card =  Venta() #VentaCard(controller_ventas, id_venta=v['id_venta'], al_finalizar=render_lista_pendientes.refresh)
            card.render(container_cards)

def render_ventas(container):
    container.clear()

    # El contenedor principal DEBE tener h-screen o una altura definida para que flex-grow funcione
    with container.classes('w-full h-full flex flex-col p-4 gap-4'):
        ui.label('Gestión de Caja').classes('text-h4') 

        # 1. Definición de las Pestañas
        with ui.tabs().classes('w-full shadow-lg rounded-t-lg') as tabs:
            tab_pendientes = ui.tab('VENTAS EN CURSO', icon='pending_actions')
            tab_finalizadas = ui.tab('FINALIZADAS HOY', icon='assignment_turned_in')

        # 2. Contenedor de los Paneles
        # Quitamos 'no-wrap' aquí, no es necesario en el contenedor de paneles
        with ui.tab_panels(tabs, value=tab_pendientes).classes('w-full flex-grow border border-gray-200 rounded-b-lg'):

            # PANEL 1: VENTAS EN CURSO
            # 'p-0' es vital para que el contenido interno llegue a los bordes si es necesario
            with ui.tab_panel(tab_pendientes).classes('h-full flex flex-col p-0'):

                # --- SECCIÓN SUPERIOR ESTÁTICA ---
                VentasApp()
"""              n Curso').classes('text-xl font-bold')


                        #### Formulario nueva venta ####


                        with ui.expansion('Añadir Nueva Venta', icon='add_circle').classes('w-full') as expansion:
                               with ui.column().classes('w-full p-4 gap-3'):
                                   # Campos del formulario
                                   nuevo_cliente = ui.input('Cliente (ej: Jacinto)').classes('w-full')

                                   with ui.row().classes('w-full justify-between items-center p-4'):
                                       ui.label('Productos').classes('text-xl font-bold w-full text-center')

                                   with ui.row().classes('w-full justify-between items-center p-4'):
                                       datos = controller.listar_productos_para_ui()
                                       print(datos)

                                         #[{'codigo': str(i), 'nombre': f'Opción {i}'} for i in range(1, 350)] 
                                       # Función para filtrar los datos según el texto ingresado 
                                       def filtrar_opciones(valor_input): 
                                           if not valor_input or not isinstance(valor_input, str):
                                               return {} 
                                       # Filtra diccionarios donde el 'codigo' comience con el texto ingresado 
                                           filtrados = [d for d in datos if str(d['codigo']).startswith(valor_input)]
                                       # Retorna un diccionario {valor: etiqueta} para el ui.select 
                                           return {d['codigo']: f"{d['codigo']} - {d['nombre']}" for d in filtrados}
                                           # Elemento de selección con búsqueda 
                                       selector = ui.select( options={}, with_input=True, label='Ingrese código', on_change=lambda e: ui.notify(f'Seleccionado: {e.value}') ).classes('w-60') 
                                       # Evento que se dispara al escribir en el input del select 
                                       # Usamos 'input-value' (propiedad de Quasar) para capturar lo que el usuario escribe 
                                       selector.on('input-value', lambda e: selector.set_options(filtrar_opciones(e.args)))


                                       def selector_cantidad(): 
                                           with ui.row().classes('items-center gap-0 border rounded-lg overflow-hidden'): 
                                       # Botón Menos 
                                               ui.button(icon='remove', on_click=lambda: selector.set_value(max(0, selector.value - 1))).props('flat square').classes('bg-grey-2') 
                                       # Input de número (readonly impide que el usuario escriba directamente
# PANEL 2: FINALIZADAS
            with ui.tab_panel(tab_finalizadas).classes('p-4'):
                ui.label('Historial de Ventas - Hoy').classes('text-xl font-bold mb-4')
                container_finalizadas = ui.column().classes('w-full')
                render_historial_hoy(container_finalizadas, controller_ventas)


"""
