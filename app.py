import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__)) 
if current_dir not in sys.path: 
    sys.path.append(current_dir)

from nicegui import app, ui
from views.layout import show_splash


# Configuración de rutas y almacenamiento
current_dir = os.path.dirname(os.path.abspath(__file__))
static_path = os.path.join(current_dir, 'statics')
app.add_static_files('/statics', static_path) 
os.environ['NICEGUI_STORAGE_PATH'] = os.path.join(current_dir, 'vita_storage_data')

def aplicar_estilos_guardados():
    s = app.storage.user
    
    if not s:
        return

    ui.run_javascript(f'''
        document.body.style.setProperty("--q-primary", "{s.get('primary_color', '#1976d2')}");
        document.body.style.fontSize = "{s.get('font_size', 16)}px";
        document.body.style.fontFamily = "{s.get('font_family', 'Arial')}";
        
        // Para las tarjetas, creamos o actualizamos un estilo dinámico
        let style = document.getElementById("custom-persistence-styles");
        if (!style) {{
            style = document.createElement("style");
            style.id = "custom-persistence-styles";
            document.head.appendChild(style);
        }}
        style.innerHTML = ".q-card {{ background-color: {s.get('card_color', '#ffffff')} !important; }}";
    ''')


@ui.page('/')
async def main_page(client):
    await client.connected()
    s = app.storage.user
    
    aplicar_estilos_guardados()
    
    
    show_splash(client)

favicon_path = os.path.join(os.getcwd(),'statics', 'logo_vita_220px.png')
ui.run(
    storage_secret='clave_vita_2026', 
    title='Vita App',
    port=8080,
    favicon=favicon_path
)
