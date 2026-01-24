#import asyncio
#from nicegui import ui
#from views.header import create_header

#def show_splash(client):
#    ui.add_head_html('''
#        <style>
#            @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
#            @keyframes fadeOut { from { opacity: 1; } to { opacity: 0; } }
#            .fade-in { animation: fadeIn 4s forwards; }
#            .fade-out { animation: fadeOut 1s forwards; }
#            @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(-360deg); } } 
#            .rotating-image { animation: spin 5s linear infinite; }
#        </style>
#    ''')

#    # Contenedor de Splash
#    splash = ui.element('div').classes('fixed-center z-[100] w-full h-full flex items-center justify-center bg-white')
#    with splash:
#        ui.image('/statics/logo_vita_595px.png').classes('fade-in rotating-image').style('width: 595px')


#    content_body = ui.column().classes('w-full h-screen items-center gap-0')
#    content_body.set_visibility(False)
#    with content_body:
#        ui.label('Seleccione un módulo arriba para comenzar.').classes('text-grey')


#    header_el = create_header(content_body)
#    header_el.set_visibility(False)

#    async def transition():
#        await asyncio.sleep(3) 
#        splash.classes(add='fade-out')
#        await asyncio.sleep(1)
#        splash.delete()
#        header_el.set_visibility(True)
#        content_body.set_visibility(True)

#    ui.timer(0, transition, once=True)

import asyncio
from nicegui import ui
from views.header import create_header

def build_main_layout():
    """Define la estructura base de la aplicación y los estilos globales."""
    
    ui.add_head_html('''
        <style>
            @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
            @keyframes fadeOut { from { opacity: 1; } to { opacity: 0; } }
            .fade-in { animation: fadeIn 2s forwards; }
            .fade-out { animation: fadeOut 0.8s forwards; }
            @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(-360deg); } } 
            .rotating-image { animation: spin 8s linear infinite; }
            
            /* Clase CRÍTICA para heredar estilos globales en la tabla */            .inherit-font-styles table,
            .inherit-font-styles th,
            .inherit-font-styles td {
                font-size: inherit !important;
                font-family: inherit !important; 
            } 

            /* Evita scroll elástico en navegadores móviles/tablets */
            body { 
                margin: 0; 
                padding: 0; 
                height: 100vh; 
                width: 100vw; 
                background-color: #f5f5f5;
                font-size: 16px; /* Asegúrate de tener un valor base aquí */
                font-family: Arial, sans-serif; 
            }
        </style>
    ''')

    # CONTENEDOR PRINCIPAL: Ocupa el 100% de la pantalla sin desbordarse
    # Se inicia oculto (display: none) para esperar al Splash
    main_container = ui.column().classes('w-full h-screen gap-0 no-wrap').style('display: none;')

    with main_container:
        # 1. Contenedor de destino (Donde se cargan las tarjetas de Ventas/Productos)
        # flex-grow permite que use todo el espacio sobrante debajo del header
        # overflow-y-auto habilita scroll solo dentro de esta área
        target_container = ui.column().classes('w-full flex-grow overflow-y-auto p-4 items-center gap-4') 
        #target_container = ui.column().classes('w-full flex-grow overflow-y-auto p-4 items-center gap-4')
        
        with target_container:
            # Mensaje de bienvenida inicial
            ui.label('Seleccione un módulo arriba para comenzar.').classes('text-grey mt-20').props('id=initial_message')

        # 2. El Header (Se crea y se mueve al inicio de la columna principal)
        header_el = create_header(target_container)
        header_el.move(target_index=0)

    return {
        'container': main_container,
        'target': target_container,
        'header': header_el
    }

async def start_splash_transition(elements):
    """Controla la animación del logo y la revelación de la app."""
    
    # Capa de Splash a pantalla completa
    splash = ui.element('div').classes('fixed inset-0 z-[100] flex items-center justify-center bg-white')
    with splash:
        ui.image('/statics/logo_vita_595px.png').classes('fade-in rotating-image').style('width: 450px')

    # Duración del splash (3 segundos + animación de salida)
    await asyncio.sleep(3) 
    splash.classes(add='fade-out')
    await asyncio.sleep(0.8)
    
    # Destruir el splash para liberar memoria y mostrar el layout
    splash.delete()
    elements['container'].style('display: flex;')
