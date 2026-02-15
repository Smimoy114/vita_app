from nicegui import ui
from views.config import render_config_panel
from views.productos_ui import render_productos
from views.ventas_ui import render_ventas

def create_header(target_container):
    """Crea una barra de navegación superior personalizada."""
    
    # Usamos ui.row en lugar de ui.header para permitir anidamiento dentro del canvas
    # 'shrink-0' es vital para que el header no se achique al hacer scroll
    with ui.row().classes('w-full bg-primary items-center justify-between px-4 py-2 shrink-0 shadow-lg z-10') as header:
        
        # Lado Izquierdo: Logo y Título
        with ui.row().classes('items-center gap-3'):
            ui.image('/statics/logo_vita_595px.png').style('width: 50px; height: 50px;')
            ui.label('Vita App').classes('text-white text-xl font-bold')
            
        # Centro: Botones Principales
        with ui.row().classes('gap-2'):       
            ui.button('Productos', 
                      on_click=lambda: render_productos(target_container)).props('flat color=white icon=inventory')
            
            ui.button('Ventas', 
                      on_click=lambda: render_ventas(target_container)).props('flat color=white icon=shopping_cart')
        
        # Lado Derecho: Utilidades
        with ui.row().classes('gap-2 items-center'):
            # Menú rápido para otros módulos
            with ui.button(icon='more_vert').props('flat color=white'):
                with ui.menu():
                    ui.menu_item('Caja', on_click=lambda: ui.notify('Abriendo Caja...'))
                    ui.menu_item('Informes', on_click=lambda: ui.notify('Abriendo Informes...'))
            
            # Configuración
            ui.button(icon='settings', 
                      on_click=lambda: render_config_panel(target_container)).props('flat color=white')
            
    return header
