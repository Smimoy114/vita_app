#from nicegui import ui
#from controllers.productos_ctr import ProductoController # Importamos el controlador

# #Inicializamos el controlador
#controller = ProductoController()

#columns = [
#    {'name': 'codigo', 'label': 'Código', 'field': 'codigo', 'required': True, 'align': 'left'},
#    {'name': 'nombre', 'label': 'Nombre', 'field': 'nombre', 'align': 'left'},
#    {'name': 'precio', 'label': 'Precio ($)', 'field': 'precio', 'align': 'right'},
#    {'name': 'descripcion', 'label': 'Descripción', 'field': 'descripcion', 'align': 'left'},
#    {'name': 'formato', 'label': 'Formato', 'align': 'left', 'field': 'formato'},
#]

#def render_productos(container):
#    """Renderiza el panel completo de gestión de productos."""
#    container.clear()
#    with container:
#        ui.label('Gestión de Productos').classes('text-h4 mb-4')


#        # --- SECCIÓN 1: AGREGAR PRODUCTOS (Formulario) ---
#        with ui.card().classes('w-full max-w-lg mb-6'):
#            with ui.expansion() as expansion:
#                expansion.classes('w-full')
#                
#                # HEADER del expansion
#                with expansion.add_slot('header'):
#                    with ui.row().classes('items-center justify-between w-full'):
#                        ui.label('Añadir Nuevo Producto').classes('text-lg font-semibold')
#                        # Nota: bind_visibility_from es más estándar para esto
#                        ui.icon('add').classes('text-3xl').bind_visibility_from(expansion, 'value', value=False)
#                        ui.icon('remove').classes('text-3xl').bind_visibility_from(expansion, 'value', value=True)

#                # CONTENIDO del expansion (Indentado un nivel adentro)
#                # Al estar dentro del 'with expansion', se ocultará/mostrará automáticamente
#                with ui.column().classes('w-full p-4'):
#                    codigo_input = ui.number('Código', value=None, format='%.0f').props('clearable full-width')
#                    nombre_input = ui.input('Nombre').props('clearable full-width')
#                    precio_input = ui.number('Precio', value=None).props('suffix="$" clearable full-width')
#                    descripcion_input = ui.textarea('Descripción').props('clearable full-width')
#                    formato_input = ui.input('Formato').props('clearable full-width')

#                    def add_product_action():
#                        try:
#                            data = {
#                                'codigo': codigo_input.value,
#                                'nombre': nombre_input.value,
#                                'precio': precio_input.value or 0,
#                                'descripcion': descripcion_input.value or '',
#                                'formato': formato_input.value or '',
#                            }
#                            controller.guardar_nuevo_producto(data) 
#                            products_table.rows = controller.listar_productos_para_ui()
#                            products_table.update()
#                            ui.notify(f'Producto "{data["nombre"]}" añadido', type='positive')
#                            
#                            # Limpiar campos
#                            codigo_input.value = None
#                            nombre_input.value = None
#                            precio_input.value = None
#                            descripcion_input.value = None
#                            formato_input.value = None
#                        except Exception as e:
#                            ui.notify(f'Error: {e}', type='negative')

#                    ui.button('Guardar Producto', on_click=add_product_action).classes('mt-4')
#                    
#                    

#        # --- SECCIÓN 2: TABLA DE REGISTROS ---
#        ui.label('Registros de Productos Existentes').classes('text-lg font-bold mb-2')
#        # Cargar datos iniciales desde el controlador
#        initial_rows = controller.listar_productos_para_ui()
#        products_table = ui.table(columns=columns, rows=initial_rows, row_key='codigo').classes('w-full')


# ... # --- SECCIÓN 2: TABLA DE REGISTROS --- 
#            ui.label('Registros de Productos Existentes').classes('text-lg font-bold mb-2')
#            initial_rows = controller.listar_productos_para_ui()
#            products_table = ui.table(columns=columns, rows=initial_rows, row_key='codigo').classes('w-full')
#            def handle_edit(row):
#                 ui.notify(f'Editar producto: {row["nombre"]} (Código: {row["codigo"]})')
#            def handle_delete(row):
#                ui.notify(f'Eliminar producto: {row["nombre"]} (Código: {row["codigo"]})')
#          
#            with products_table.add_slot('body-cell-actions') as slot:
#                      with slot.cell():
#                          with ui.row().classes('flex flex-nowrap'):
#                              ui.button(icon='edit', on_click=lambda props=slot.props: handle_edit(props.row)).props('flat round dense color=blue')
#                              ui.button(icon='delete', on_click=lambda props=slot.props: handle_delete(props.row)).props('flat round dense color=red')

#def render_productos(container):
#    """Renderiza el panel completo de gestión de productos."""
#    container.clear()
#    with container:
#        ui.label('Gestión de Productos').classes('text-h4 mb-4')

#        # --- SECCIÓN 1: AGREGAR PRODUCTOS (Formulario) ---
#        with ui.card().classes('w-full max-w-lg mb-6'):
#            with ui.expansion() as expansion:
#                expansion.classes('w-full')
#                
#                # HEADER del expansion
#                with expansion.add_slot('header'):
#                    # ... (código del header sin cambios) ...
#                    with ui.row().classes('items-center justify-between w-full'):
#                        ui.label('Añadir Nuevo Producto').classes('text-lg font-semibold')
#                        ui.icon('add').classes('text-3xl').bind_visibility_from(expansion, 'value', value=False)
#                        ui.icon('remove').classes('text-3xl').bind_visibility_from(expansion, 'value', value=True)

#                # CONTENIDO del expansion (Inputs y botón Guardar)
#                with ui.column().classes('w-full p-4'):
#                    # ... (código de inputs y add_product_action sin cambios) ...
#                    codigo_input = ui.number('Código', value=None, format='%.0f').props('clearable full-width')
#                    nombre_input = ui.input('Nombre').props('clearable full-width')
#                    precio_input = ui.number('Precio', value=None).props('suffix="$" clearable full-width')
#                    descripcion_input = ui.textarea('Descripción').props('clearable full-width')
#                    formato_input = ui.input('Formato').props('clearable full-width')

#                    def add_product_action():
#                        try:
#                            data = {
#                                'codigo': codigo_input.value,
#                                'nombre': nombre_input.value,
#                                'precio': precio_input.value or 0,
#                                'descripcion': descripcion_input.value or '',
#                                'formato': formato_input.value or '',
#                            }
#                            controller.guardar_nuevo_producto(data) 
#                            products_table.rows = controller.listar_productos_para_ui()
#                            products_table.update()
#                            ui.notify(f'Producto "{data["nombre"]}" añadido', type='positive')
#                            
#                            # Limpiar campos
#                            codigo_input.value = None
#                            nombre_input.value = None
#                            precio_input.value = None
#                            descripcion_input.value = None
#                            formato_input.value = None
#                        except Exception as e:
#                            ui.notify(f'Error: {e}', type='negative')

#                    ui.button('Guardar Producto', on_click=add_product_action).classes('mt-4')

#        # --- SECCIÓN 2: TABLA DE REGISTROS ---
#        # ESTAS LÍNEAS DEBEN ESTAR ALINEADAS CON 'ui.card()' y 'ui.label("Gestión de Productos")'
#        ui.label('Registros de Productos Existentes').classes('text-lg font-bold mb-2')
#        
#        # Cargar datos iniciales desde el controlador
#        initial_rows = controller.listar_productos_para_ui()
#        products_table = ui.table(columns=columns, rows=initial_rows, row_key='codigo').classes('w-full')

#        # Funciones de manejo DEBEN estar al mismo nivel que la definición de 'products_table'
#        def handle_edit(row):
#                ui.notify(f'Editar producto: {row["nombre"]} (Código: {row["codigo"]})')
#        def handle_delete(row):
#            ui.notify(f'Eliminar producto: {row["nombre"]} (Código: {row["codigo"]})')
#        
#        # ADICIÓN DEL SLOT DE ACCIONES: DEBE ESTAR AL MISMO NIVEL QUE LA TABLA
#        products_table.add_column({'name': 'actions', 'label': 'Acciones', 'field': 'actions'}) # Asegúrate de añadir la columna primero
#        with products_table.add_slot('body-cell-actions') as slot:
#                    with slot.cell():
#                        with ui.row().classes('flex flex-nowrap'):
#                            ui.button(icon='edit', on_click=lambda props=slot.props: handle_edit(props.row)).props('flat round dense color=blue')
#                            ui.button(icon='delete', on_click=lambda props=slot.props: handle_delete(props.row)).props('flat round dense color=red')

from nicegui import ui
from controllers.productos_ctr import ProductoController

# Inicializamos el controlador
controller = ProductoController()

columns = [
    {'name': 'codigo', 'label': 'Código', 'field': 'codigo', 'required': True, 'align': 'left'},
    {'name': 'nombre', 'label': 'Nombre', 'field': 'nombre', 'align': 'left'},
    {'name': 'precio', 'label': 'Precio ($)', 'field': 'precio', 'align': 'right'},
    {'name': 'descripcion', 'label': 'Descripción', 'field': 'descripcion', 'align': 'left'},
    {'name': 'formato', 'label': 'Formato', 'align': 'left', 'field': 'formato'},
    # AÑADIMOS LA COLUMNA DE ACCIONES AQUÍ
    {'name': 'actions', 'label': 'Acciones', 'field': 'actions', 'align': 'center'},
]

def render_productos(container):
    """Renderiza el panel completo de gestión de productos."""
    container.clear()
    with container:
        ui.label('Gestión de Productos').classes('text-h4 mb-4')

        # --- SECCIÓN 1: AGREGAR PRODUCTOS (Formulario) ---
        with ui.card().classes('w-full max-w-lg mb-6'):
            # ... (El código de la expansión y el formulario de añadir producto no cambia) ...
            with ui.expansion() as expansion:
                expansion.classes('w-full')
                with expansion.add_slot('header'):
                    with ui.row().classes('items-center justify-between w-full'):
                        ui.label('Añadir Nuevo Producto').classes('text-lg font-semibold')
                        ui.icon('add').classes('text-3xl').bind_visibility_from(expansion, 'value', value=False)
                        ui.icon('remove').classes('text-3xl').bind_visibility_from(expansion, 'value', value=True)

                with ui.column().classes('w-full p-4'):
                    # ... (Inputs y función add_product_action aquí) ...
                    codigo_input = ui.number('Código', value=None, format='%.0f').props('clearable full-width')
                    nombre_input = ui.input('Nombre').props('clearable full-width')
                    precio_input = ui.number('Precio', value=None).props('suffix="$" clearable full-width')
                    descripcion_input = ui.textarea('Descripción').props('clearable full-width')
                    formato_input = ui.input('Formato').props('clearable full-width')

                    def add_product_action():
                        try:
                            data = {
                                'codigo': codigo_input.value,
                                'nombre': nombre_input.value,
                                'precio': precio_input.value or 0,
                                'descripcion': descripcion_input.value or '',
                                'formato': formato_input.value or '',
                            }
                            controller.guardar_nuevo_producto(data) 
                            products_table.rows = controller.listar_productos_para_ui()
                            products_table.update()
                            ui.notify(f'Producto "{data["nombre"]}" añadido', type='positive')
                            
                            codigo_input.value = None
                            nombre_input.value = None
                            precio_input.value = None
                            descripcion_input.value = None
                            formato_input.value = None
                        except Exception as e:
                            ui.notify(f'Error: {e}', type='negative')

                    ui.button('Guardar Producto', on_click=add_product_action).classes('mt-4')

        # --- SECCIÓN 2: TABLA DE REGISTROS ---
        # TODO ESTE BLOQUE ESTÁ AHORA ALINEADO CORRECTAMENTE CON 'ui.card()'
        ui.label('Registros de Productos Existentes').classes('text-lg font-bold mb-2')
        
        # Cargar datos iniciales desde el controlador
        initial_rows = controller.listar_productos_para_ui()
        products_table = ui.table(columns=columns, rows=initial_rows, row_key='codigo').classes('w-full')

        # Definiciones de funciones para los botones (AL MISMO NIVEL QUE products_table)
        def handle_edit(row):
             ui.notify(f'Editar producto: {row["nombre"]} (Código: {row["codigo"]})')
        
        def handle_delete(row):
            ui.notify(f'Eliminar producto: {row["nombre"]} (Código: {row["codigo"]})')
        
        # ADICIÓN DEL SLOT: DEBE ESTAR AL MISMO NIVEL QUE LA TABLA
 #       with products_table.add_slot('body-cell-actions') as slot:
#            with slot.cell():
#                with ui.row().classes('flex flex-nowrap'):
#                    # Pasamos props.row a las funciones lambda
#                    ui.button(icon='edit', on_click=lambda props=slot.props: handle_edit(props.row)).props('flat round dense color=blue')
#                    ui.button(icon='delete', on_click=lambda props=slot.props: handle_delete(props.row)).props('flat round dense color=red')

# ... (código previo sin cambios) ...
# ... (código previo sin cambios) ...

        # ADICIÓN DEL SLOT: DEBE ESTAR AL MISMO NIVEL QUE LA TABLA
        with products_table.add_slot('body-cell-actions') as slot:
            with ui.row().classes('flex flex-nowrap'):
                
                # Botón EDITAR: Usamos .on() para pasar los datos explícitamente
                ui.button(icon='edit').props('flat round dense color=blue').on(
                    'click',
                    # 1. js_handler (Frontend): Emite un evento 'edit_click' con los datos de la fila (props.row)
                    js_handler='() => emit("edit_click", props.row)',
                    # 2. handler (Backend): Recibe el evento y llama a nuestra función Python
                    handler=lambda e: handle_edit(e.args)
                )

                # Botón ELIMINAR: Usamos .on() para pasar los datos explícitamente
                ui.button(icon='delete').props('flat round dense color=red').on(
                    'click',
                    # 1. js_handler (Frontend): Emite un evento 'delete_click' con los datos de la fila (props.row)
                    js_handler='() => emit("delete_click", props.row)',
                    # 2. handler (Backend): Recibe el evento y llama a nuestra función Python
                    handler=lambda e: handle_delete(e.args)
                )
