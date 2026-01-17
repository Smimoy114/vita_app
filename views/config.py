#from nicegui import app, ui

#def Configuracion():
#                try:
#                    s = app.storage.user
#                    # Valores por defecto
#                    defaults = {
#                    'primary_color': '#1976d2', 
#                    'font_size': 16, 
#                    'font_family': 'Arial', 
#                    'card_color': '#ffffff'
#                    }
#                    for k, v in defaults.items():
#                        if k not in s: s[k] = v

#                    ui.label('Configuración del Sitio').classes('text-h4 mb-4')
#                
#                    with ui.card().classes('p-4 w-full max-w-md'):
#                        ui.label('Personalización Visual').classes('text-lg font-bold')
#                    
#                        # --- COLOR PRINCIPAL ---
#                        ui.label('Color Principal:').classes('mt-2')
#                        ui.color_input(on_change=lambda e: (
#                            s.update({'primary_color': e.value}),
#                            ui.run_javascript(f'document.body.style.setProperty("--q-primary", "{e.value}")')
#                        )).bind_value(s, 'primary_color').props('full-width')

#                        # --- TAMAÑO DE FUENTE ---
#                        ui.label('Tamaño de Fuente (px):').classes('mt-4')
#                        ui.slider(min=12, max=30, on_change=lambda e: (
#                            s.update({'font_size': e.value}),
#                            ui.add_head_html(f'<style id="font-size-style">body {{ font-size: {e.value}px !important; }}</style>'))).bind_value(s, 'font_size')

#                        # --- TIPO DE FUENTE  ---
#                        fuentes = [
#                            'Arial', 
#                            'Roboto', 
#                            'Times New Roman', 
#                            'Courier New', 
#                            'Georgia', 
#                            'Trebuchet MS'
#                            ]
#                    
#                        ui.label('Tipo de Fuente:').classes('mt-4')
#                        ui.select(fuentes, on_change=lambda e: (
#                            s.update({'font_family': e.value}),
#                            ui.add_head_html(f'<style id="font-family-style">body {{ font-family: "{e.value}", sans-serif !important; }}</style>')
#                        )).bind_value(s, 'font_family').classes('w-full')

#                        # --- COLOR DE TARJETAS ---
#                        ui.label('Color de Tarjetas:').classes('mt-4')
#                        ui.color_input(on_change=lambda e: (
#                            s.update({'card_color': e.value}),
#                            ui.add_head_html(f'<style id="card-style">.q-card {{ background-color: {e.value} !important; }}</style>')
#                        )).bind_value(s, 'card_color').props('full-width')
#                    
#                except RuntimeError:
#                    ui.notify('Error: Configura storage_secret en ui.run()')


from nicegui import ui, app

def render_config_panel(container):
    container.clear()
    with container:
        try:
            s = app.storage.user
            # Valores por defecto
            defaults = {
                'primary_color': '#1976d2', 
                'font_size': 16, 
                'font_family': 'Arial', 
                'card_color': '#ffffff'
            }
            for k, v in defaults.items():
                if k not in s: s[k] = v

            ui.label('Configuración del Sitio').classes('text-h4 mb-4')
        
            with ui.card().classes('p-4 w-full max-w-md'):
                ui.label('Personalización Visual').classes('text-lg font-bold')
            
                # --- COLOR PRINCIPAL ---
                ui.label('Color Principal:').classes('mt-2')
                ui.color_input(on_change=lambda e: (
                    s.update({'primary_color': e.value}),
                    ui.run_javascript(f'document.body.style.setProperty("--q-primary", "{e.value}")')
                )).bind_value(s, 'primary_color').props('full-width')

                # --- TAMAÑO DE FUENTE ---
                ui.label('Tamaño de Fuente (px):').classes('mt-4')
                ui.slider(min=12, max=30, on_change=lambda e: (
                    s.update({'font_size': e.value}),
                    ui.add_head_html(f'<style id="font-size-style">body {{ font-size: {e.value}px !important; }}</style>'))
                ).bind_value(s, 'font_size')

                # --- TIPO DE FUENTE ---
                fuentes = ['Arial', 'Roboto', 'Times New Roman', 'Courier New', 'Georgia', 'Trebuchet MS']
                ui.label('Tipo de Fuente:').classes('mt-4')
                ui.select(fuentes, on_change=lambda e: (
                    s.update({'font_family': e.value}),
                    ui.add_head_html(f'<style id="font-family-style">body {{ font-family: "{e.value}", sans-serif !important; }}</style>')
                )).bind_value(s, 'font_family').classes('w-full')

                # --- COLOR DE TARJETAS ---
                ui.label('Color de Tarjetas:').classes('mt-4')
                ui.color_input(on_change=lambda e: (
                    s.update({'card_color': e.value}),
                    ui.add_head_html(f'<style id="card-style">.q-card {{ background-color: {e.value} !important; }}</style>')
                )).bind_value(s, 'card_color').props('full-width')
            
        except RuntimeError:
            ui.notify('Error: Configura storage_secret en ui.run()')
