import sys
import os
import asyncio
import signal
import subprocess
import platform

def kill_process_on_port(port):
    system = platform.system()
    try:
        if system == "Windows":
            # Busca la línea que contiene el puerto y extrae el PID (última columna)
            cmd = f'netstat -ano | findstr :{port}'
            output = subprocess.check_output(cmd, shell=True).decode()
            for line in output.strip().split('\n'):
                if "LISTENING" in line:
                    pid = line.strip().split()[-1]
                    print(f"Windows: Matando proceso {pid} en puerto {port}")
                    subprocess.run(f"taskkill /F /PID {pid}", shell=True)

        else: # Termux / Linux / macOS
            # lsof -t devuelve solo el PID
            pid = subprocess.check_output(["lsof", "-t", f"-i:{port}"]).decode().strip()
            if pid:
                for p in pid.split('\n'):
                    os.kill(int(p), signal.SIGKILL)

    except subprocess.CalledProcessError:
        # El puerto ya está libre
        pass

# --- Inicio de tu aplicación ---
PORT = 8080
kill_process_on_port(PORT)


# Ajuste de rutas para módulos internos
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from nicegui import app, ui
from views.layout import build_main_layout, start_splash_transition

# Configuración de rutas y almacenamiento
static_path = os.path.join(current_dir, 'statics')
app.add_static_files('/statics', static_path) 
os.environ['NICEGUI_STORAGE_PATH'] = os.path.join(current_dir, 'vita_storage_data')

def aplicar_estilos_guardados():
    s = app.storage.user
    if not s:
        return

    # Inyectamos los estilos guardados por el usuario
    #print(s)

    ui.run_javascript(f'''
        document.body.style.setProperty("--q-primary", "{s.get('primary_color', '#89d6c3')}");
        document.body.style.fontSize = "{s.get('font_size', 16)}px";
        document.body.style.fontFamily = "{s.get('font_family', 'Arial')}";
        
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
    # Esperar conexión del cliente (importante para ejecutar JS)
    await client.connected()

    # 1. Aplicar preferencias visuales
    aplicar_estilos_guardados()

    # 2. Construir la estructura base (Canvas)
    # Esta función devuelve un diccionario con las referencias a los contenedores
    layout_elements = build_main_layout()

    # 3. Ejecutar el Splash Screen y la transición al Layout
    await start_splash_transition(layout_elements)

# Ejecución de la App
if __name__ in {"__main__", "__mp_main__"}:
    favicon_path = os.path.join(os.getcwd(), 'statics', 'logo_vita_220px.png')
    ui.run(
        storage_secret='clave_vita_2026',
        title='Vita App',
        port=8080,
        favicon=favicon_path,
        #reload=False
    )
