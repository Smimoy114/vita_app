import json
from nicegui import ui
from controllers.productos_controller import ProductoController

controller = ProductoController()

# 1. MANEJADORES DE EVENTOS (Fuera de la renderización para mayor claridad)
def handle_edit(row_data, edit_fields, edit_dialog):
    print(f"DATOS RECIBIDOS PARA EDITAR: {row_data}") 
    edit_fields['codigo'].value = row_data.get('codigo')
    edit_fields['nombre'].value = row_data.get('nombre')
    edit_fields['precio'].value = row_data.get('precio')
    edit_fields['formato'].value = row_data.get('formato')
    edit_fields['descripcion'].value = row_data.get('descripcion')
    edit_dialog.open()

def confirmar_eliminacion_dialog(row_data, products_table):
    
    with ui.dialog() as dialog, ui.card().classes('p-4'):
        with ui.column().classes('items-center w-full'):
            ui.icon('warning', color='warning').classes('text-5xl')
            ui.label(f'¿Eliminar "{row_data.get("nombre")}"?').classes('text-lg font-bold')
            ui.label('Esta acción no se puede deshacer y fallará si el producto tiene ventas asociadas.').classes('text-center mb-4')
            
            with ui.row().classes('w-full justify-end'):
                ui.button('Cancelar', on_click=dialog.close).props('flat')
                # Al confirmar, llamamos a la lógica real de borrado
                ui.button('Eliminar', color='red', 
                          on_click=lambda: ejecutar_borrado_real(dialog, row_data, products_table))
    
    dialog.open()


async def ejecutar_borrado_real(dialog, row_data, products_table):
    try:
        controller.eliminar_producto(row_data['codigo'])
        products_table.rows = controller.listar_productos_para_ui()
        ui.notify(f'Producto {row_data.get("nombre")} eliminado', type='warning')
        dialog.close()
    except Exception as e:
        # Aquí capturarás el BusinessError que definimos anteriormente
        ui.notify(f'{e}', type='negative')
        dialog.close()
        
        

# 2. CONFIGURACIÓN DEL DIÁLOGO
def setup_edit_dialog(products_table):
    with ui.dialog() as dialog, ui.card().classes('w-full max-w-lg'):
        ui.label('Editar Producto').classes('text-lg font-bold mb-2')
        fields = {
            'codigo': ui.number('Código', format='%.0f').props('readonly'),
            'nombre': ui.input('Nombre').classes('w-full'),
            'precio': ui.number('Precio').classes('w-full'),
            'formato': ui.input('Formato').classes('w-full'),
            'descripcion': ui.textarea('Descripción').classes('w-full')
        }
        async def save():
            data = {k: v.value for k, v in fields.items()}
            controller.actualizar_producto(data)
            products_table.rows = controller.listar_productos_para_ui()
            dialog.close()
            ui.notify(f'Producto {data["nombre"]} actualizado', type='positive')
            #ui.notify('Actualizado con éxito')
        
        ui.button('Guardar', on_click=save)
    return dialog, fields

# 3. RENDERIZADO PRINCIPAL
def render_productos(container):
    container.clear()
    with container:
        ui.label('Gestión de Productos').classes('text-h4 mb-4')
        
                # --- SECCIÓN: FORMULARIO DE REGISTRO COLAPSABLE ---
        with ui.card().classes('w-full max-w-lg mb-6 shadow-md'):
            with ui.expansion('Añadir Nuevo Producto', icon='add_circle').classes('w-full') as expansion:
                with ui.column().classes('w-full p-4 gap-3'):
                    # Campos del formulario
                    nuevo_codigo = ui.number('Código', format='%.0f').classes('w-full')
                    nuevo_nombre = ui.input('Nombre').classes('w-full')
                    nuevo_precio = ui.number('Precio', format='%.0f').props('suffix="$"').classes('w-full')
                    nuevo_formato = ui.input('Formato (ej: unidad)').classes('w-full')
                    nueva_desc = ui.textarea('Descripción').classes('w-full')

                    def agregar_y_limpiar():
                        try:
                            # 1. Recopilar datos
                            data = {
                                'codigo': nuevo_codigo.value,
                                'nombre': nuevo_nombre.value,
                                'precio': nuevo_precio.value or 0,
                                'formato': nuevo_formato.value or '',
                                'descripcion': nueva_desc.value or '',
                            }
                            
                            # 2. Guardar mediante el controlador
                            controller.guardar_nuevo_producto(data)
                            
                            # 3. Actualizar la tabla y notificar
                            products_table.rows = controller.listar_productos_para_ui()
                            ui.notify(f'Producto {data["nombre"]} guardado', type='positive')
                            
                            # 4. Limpiar campos y cerrar colapsable
                            nuevo_codigo.value = nuevo_nombre.value = nuevo_precio.value = None
                            nuevo_formato.value = nueva_desc.value = None
                            expansion.value = False 
                            
                        except Exception as e:
                            ui.notify(f'Error: {e}', type='negative')

                    ui.button('Guardar Producto', on_click=agregar_y_limpiar).classes('w-full mt-2')

        # --- SECCIÓN: TABLA ---
        ui.label('Registros Existentes').classes()

        # 1. Definimos columnas 
        columns = [
            {'name': 'acciones', 'label': 'Acciones', 'field': 'acciones', 'align': 'center'},
            {'name': 'codigo', 'label': 'Código', 'field': 'codigo', 'align': 'left'},
            {'name': 'nombre', 'label': 'Nombre', 'field': 'nombre', 'align': 'left'},
            {'name': 'precio', 'label': 'Precio', 'field': 'precio', 'align': 'right'},
            {'name': 'formato', 'label': 'Formato', 'field': 'formato', 'align': 'right'},
            {'name': 'descripcion', 'label': 'Descripción', 'field': 'descripcion', 'align': 'left'},
        ]

        initial_rows = controller.listar_productos_para_ui()
        
        # 2. Creamos la tabla
        products_table = ui.table(columns=columns, rows=initial_rows, row_key='codigo').classes('w-full inherit-font-styles')
        
        # 3. Setup del diálogo
        edit_dialog, edit_fields = setup_edit_dialog(products_table)

        # 4.SLOT
        products_table.add_slot('body-cell-acciones', '''
            <q-td :props="props">
                <q-btn flat round dense color="blue" icon="edit" @click="$parent.$emit('editar', props.row)" />
                <q-btn flat round dense color="red" icon="delete" @click="$parent.$emit('borrar', props.row)" />
            </q-td>
        ''')

        # 5. Escuchamos los eventos desde Python
        products_table.on('editar', lambda msg: handle_edit(msg.args, edit_fields, edit_dialog))
        products_table.on('borrar', lambda msg: handle_delete(msg.args, products_table))

# --- FUNCIONES DE MANEJO ---
def handle_edit(row_data, edit_fields, edit_dialog):
    
    
    edit_fields['codigo'].value = row_data.get('codigo')
    edit_fields['nombre'].value = row_data.get('nombre')
    edit_fields['precio'].value = row_data.get('precio')
    edit_fields['formato'].value = row_data.get('formato')
    edit_fields['descripcion'].value = row_data.get('descripcion')
    edit_dialog.open()

def handle_delete(row_data, products_table):
    
    # En lugar de borrar, abrimos el diálogo de confirmación
    confirmar_eliminacion_dialog(row_data, products_table)

