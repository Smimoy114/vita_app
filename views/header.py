from nicegui import ui
from views.config import render_config_panel
from views.productos_ui import render_productos

def create_header(target_container):
    with ui.header().classes('bg-primary items-center justify-between') as header:
        with ui.row().classes('items-center gap-3'):
            ui.image('/statics/logo_vita_595px.png').style('width: 100px; height: 100px;')
            ui.label('Vita App').classes('text-white text-xl font-bold')
            
            ui.button('Productos', on_click=lambda: render_productos(target_container))
        
        with ui.row().classes('gap-4'):
            for nombre in ['Ventas', 'Caja', 'Informes']:
                ui.button(nombre)
            
        # Llamada directa a la función modularizada
        ui.button(icon='settings', on_click=lambda: render_config_panel(target_container))
    return header

#def show_panel(container, name):
#    container.clear()
#    with container:
#        if name == 'Productos':
#            label
#            
