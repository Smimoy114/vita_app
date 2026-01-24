from nicegui import ui
from datetime import datetime
from controllers.ventas_ctr import VentasController
from views.ventas_card import VentaCard

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
            card = VentaCard(controller_ventas, id_venta=v['id_venta'], al_finalizar=render_lista_pendientes.refresh)
            card.render(container_cards)
            

def render_ventas(container):
    container.clear()
    
    # El contenedor principal usa flex-col y ocupa toda la altura disponible
    with container.classes('w-full h-full flex flex-col p-4 gap-4'): # Añadimos 'p-4 gap-4' para mejor espaciado
        ui.label('Gestión de Caja').classes('text-h4') 
            
    
        # 1. Definición de las Pestañas
        with ui.tabs().classes('w-full shadow-lg rounded-t-lg') as tabs:
            tab_pendientes = ui.tab('VENTAS EN CURSO', icon='pending_actions')
            tab_finalizadas = ui.tab('FINALIZADAS HOY', icon='assignment_turned_in')

        # 2. Contenedor de los Paneles
        with ui.tab_panels(tabs, value=tab_pendientes).classes('w-full flex-grow border border-gray-200 rounded-b-lg'):

            with ui.tab_panel(tab_pendientes).classes('h-full flex flex-col p-0'):
       
        # --- SECCIÓN SUPERIOR ESTÁTICA (La tarjeta azul que NO hace scroll) --- 
        # Esta tarjeta ahora solo contiene el label y el botón
                
                with ui.card().classes('w-full bg-blue-50 shadow-md'):
                     with ui.row().classes('w-full justify-between items-center p-4'):
                            ui.label('Ventas en Curso').classes('text-xl font-bold')
                # El botón se queda como estaba
                            ui.button('NUEVA VENTA', icon='add_shopping_cart', color='green', on_click=lambda: VentaCard(controller_ventas,al_finalizar=render_lista_pendientes.refresh).render(cards_area)).props('size=lg').classes('shadow-lg px-6')

        # --- SECCIÓN DE TARJETAS CON SCROLL (El área que queremos que crezca) --- 
        # Usamos 'flex-grow' aquí para que ocupe todo el espacio vertical restante.
                with ui.scroll_area().classes('w-full flex-grow bg-gray-50 p-4'):
                    cards_area = ui.column().classes('w-full gap-4') 
            
            # Llamada inicial para cargar lo que ya está en DB 
                    render_lista_pendientes(cards_area, controller_ventas)
 
        
        with ui.tab_panel(tab_finalizadas):
            ui.label('Historial de Ventas - Hoy').classes('text-xl font-bold mb-4')
                
                # Espacio para la tabla de historial
            container_finalizadas = ui.column().classes('w-full')
            render_historial_hoy(container_finalizadas, controller_ventas)
               

#def render_ventas(container):
#    container.clear()
#    
#    with container:
#        ui.label('Módulo de Ventas').classes('text-h4 mb-4')

#        # 1. Definición de las Pestañas
#        with ui.tabs().classes('w-full shadow-lg rounded-t-lg') as tabs:
#            tab_pendientes = ui.tab('VENTAS EN CURSO', icon='pending_actions')
#            tab_finalizadas = ui.tab('FINALIZADAS HOY', icon='assignment_turned_in')

#        # 2. Contenedor de los Paneles
#        with ui.tab_panels(tabs, value=tab_pendientes).classes('w-full border border-gray-200 rounded-b-lg'):
#            
#            # --- PANEL 1: VENTAS PENDIENTES ---
#            with ui.tab_panel(tab_pendientes):
#                # Contenedor dinámico de tarjetas 
#                cards_container = ui.column().classes('w-full') 
#                ui.button('Nueva Venta', on_click=lambda: VentaCard(controller_ventas).render(cards_container))
#                # Cargar las que ya están en DB como PENDIENTES al iniciar 
#                pendientes = controller_ventas.listar_ventas_pendientes() 
#                
#                for v in pendientes:
#                    VentaCard(controller_ventas, id_venta=v['id_venta']).render(cards_container) 
#                
#                with ui.row().classes('w-full justify-between items-center mb-4'):
#                    ui.label('Ventas Abiertas').classes('text-xl font-bold')
#                    # Botón para crear una nueva comanda o venta vacía
#                    ui.button('Nueva Venta', icon='add', color='green', 
#                              on_click=lambda: crear_nueva_venta_dialog(controller_ventas, tabs))
#                
#                # Espacio donde se renderizarán las tarjetas colapsables
#                container_pendientes = ui.column().classes('w-full gap-4')
#                render_lista_pendientes(container_pendientes, controller_ventas)

#            # --- PANEL 2: VENTAS FINALIZADAS ---
#            with ui.tab_panel(tab_finalizadas):
#                ui.label('Historial de Ventas - Hoy').classes('text-xl font-bold mb-4')
#                
#                # Espacio para la tabla de historial
#                container_finalizadas = ui.column().classes('w-full')
#                render_historial_hoy(container_finalizadas, controller_ventas)

# --- FUNCIONES DE RENDERIZADO (Prototipos para completar después) ---

#def render_lista_pendientes(container, controller):
#    """Carga las ventas con estado 'PENDIENTE' como tarjetas colapsables."""
#    container.clear()
#    ventas = controller.listar_ventas_pendientes() # Esto lo definiremos en el controlador
#    
#    if not ventas:
#        with container:
#            ui.label('No hay ventas en curso').classes('text-grey-5 italic m-4')
#        return

#    for v in ventas:
#        # Aquí es donde usaremos el ui.expansion que mencionaste
#        with container, ui.expansion(f"Cliente: {v['cliente']} - Total: ${v['total']}", icon='person').classes('w-full border rounded'):
#            ui.label(f"Detalles de la venta #{v['id_venta']}...")
#            # Aquí irá la tabla de productos vendidos de esta venta

#def render_historial_hoy(container, controller):
#    """Carga la tabla de ventas con estado 'PAGADO' filtradas por fecha actual."""
#    container.clear()
#    hoy = datetime.now().strftime("%d-%m-%Y")
#    ventas_hoy = controller.listar_ventas_por_fecha(hoy) # Usará select_by_fecha_ventas
#    
#    with container:
#        columns = [
#            {'name': 'hora', 'label': 'Hora', 'field': 'hora_venta'},
#            {'name': 'cliente', 'label': 'Cliente', 'field': 'cliente'},
#            {'name': 'total', 'label': 'Total', 'field': 'total'},
#            {'name': 'pago', 'label': 'Forma Pago', 'field': 'forma_pago'}
#        ]
#        ui.table(columns=columns, rows=ventas_hoy).classes('w-full')

#def crear_nueva_venta_dialog(controller, tabs):
#    """Diálogo rápido para iniciar una venta con un nombre de cliente."""
#    # Lógica para insertar en VentaModel y refrescar la vista
#    pass
