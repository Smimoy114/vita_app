import asyncio
from nicegui import ui
from views.header import create_header

def show_splash(client):
    ui.add_head_html('''
        <style>
            @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
            @keyframes fadeOut { from { opacity: 1; } to { opacity: 0; } }
            .fade-in { animation: fadeIn 4s forwards; }
            .fade-out { animation: fadeOut 1s forwards; }
            @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(-360deg); } } 
            .rotating-image { animation: spin 5s linear infinite; }
        </style>
    ''')

    # Contenedor de Splash
    splash = ui.element('div').classes('fixed-center z-[100] w-full h-full flex items-center justify-center bg-white')
    with splash:
        ui.image('/statics/logo_vita_595px.png').classes('fade-in rotating-image').style('width: 595px')


    content_body = ui.column().classes('w-full p-4 mt-16')
    content_body.set_visibility(False)
    with content_body:
        ui.label('Seleccione un módulo arriba para comenzar.').classes('text-grey')


    header_el = create_header(content_body)
    header_el.set_visibility(False)

    async def transition():
        await asyncio.sleep(3) 
        splash.classes(add='fade-out')
        await asyncio.sleep(1)
        splash.delete()
        header_el.set_visibility(True)
        content_body.set_visibility(True)

    ui.timer(0, transition, once=True)
