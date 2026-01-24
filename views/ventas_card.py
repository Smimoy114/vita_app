from nicegui import ui
import datetime

class VentaCard:
    def __init__(self, controller, id_venta=None, al_cancelar=None, al_finalizar=None):
        self.ctr = controller
        self.id_venta = id_venta  # Si es None, la venta no existe en DB aún
        self.al_cancelar = al_cancelar
        self.al_finalizar = al_finalizar
        
        # Estado en memoria
        self.cliente = ""
        self.productos_seleccionados = []  # Lista de dicts con datos de ProductoModel + cantidad
        self.total_venta = 0
        
        # Si recibimos un ID, cargamos los datos existentes desde el controlador
        if self.id_venta:
            self._cargar_datos_db()

    def _cargar_datos_db(self):
        venta = self.ctr.obtener_venta_por_id(self.id_venta)
        if venta:
            self.cliente = venta['cliente']
            # Cargar productos ya vinculados a esta venta
            self.productos_seleccionados = self.ctr.obtener_items_por_venta(self.id_venta)
            self._recalcular_total()

    def _recalcular_total(self):
        self.total_venta = sum(item['precio_producto'] * item['cantidad'] for item in self.productos_seleccionados)

    def render(self, container):
        """Genera la UI de la tarjeta dentro de un contenedor"""
        with container, ui.card().classes('w-full mb-4 border-l-4 border-blue-500 shadow-lg') as self.card_ui:
            with ui.expansion().classes('w-full items-center'):
                with ui.row().classes('w-full items-center'): 
                    ui.icon('receipt_long').classes('text-2xl')
                    self.input_cliente = ui.input('Nombre del Cliente', value=self.cliente).classes('flex-grow')
            
                ui.separator()
            
            # --- ÁREA DE PRODUCTOS ---
                with ui.column().classes('w-full'):
                    ui.label('Productos').classes('font-bold text-grey-7')
                    self.lista_ui = ui.column().classes('w-full gap-1')
                    self._dibujar_lista_productos()
                
                    with ui.row().classes('w-full justify-between mt-2'):
                        ui.button('Añadir Producto', icon='add', on_click=self._dialogo_busqueda_productos).props('flat dense')
                        self.label_total = ui.label(f'Total: ${self.total_venta}').classes('text-lg font-bold text-blue-900')

            ui.separator()

            # --- BOTONERA ---
            with ui.row().classes('w-full justify-end gap-2'):
                ui.button('CANCELAR', color='red', icon='delete_sweep', on_click=self.accion_cancelar).props('outline')
                ui.button('GUARDAR', color='blue', icon='save', on_click=self.accion_guardar)
                ui.button('PAGAR', color='green', icon='payments', on_click=self.dialogo_pago)

    def _dibujar_lista_productos(self):
        self.lista_ui.clear()
        with self.lista_ui:
            for i, prod in enumerate(self.productos_seleccionados):
                with ui.row().classes('w-full items-center bg-blue-50 p-1 rounded'):
                    ui.label(f"{prod['nombre_producto']} x{prod['cantidad']}")
                    ui.space()
                    ui.label(f"${prod['precio_producto'] * prod['cantidad']}")
                    ui.button(icon='remove', on_click=lambda idx=i: self._quitar_producto(idx)).props('flat round dense color=red')

    def _dialogo_busqueda_productos(self):
        with ui.dialog() as diag, ui.card().classes('w-80'):
            ui.label('Buscar Producto').classes('text-h6')
            prods = self.ctr.m_productos.select_all_productos()
            with ui.scroll_area().classes('h-64'):
                for p in prods:
                    with ui.row().classes('w-full border-b p-2 items-center'):
                        ui.label(p['nombre_producto'])
                        ui.space()
                        ui.button(icon='add', on_click=lambda p=p: self._agregar_producto_memoria(p)).props('flat')
            ui.button('Cerrar', on_click=diag.close).classes('w-full mt-2')
        diag.open()

    def _agregar_producto_memoria(self, producto):
        # Lógica para sumar cantidad si ya existe o añadir nuevo
        encontrado = next((x for x in self.productos_seleccionados if x['codigo_producto'] == producto['codigo_producto']), None)
        if encontrado:
            encontrado['cantidad'] += 1
        else:
            item = producto.copy()
            item['cantidad'] = 1
            self.productos_seleccionados.append(item)
        
        self._recalcular_total()
        self.label_total.set_text(f'Total: ${self.total_venta}')
        self._dibujar_lista_productos()

    def _quitar_producto(self, index):
        self.productos_seleccionados.pop(index)
        self._recalcular_total()
        self.label_total.set_text(f'Total: ${self.total_venta}')
        self._dibujar_lista_productos()

    # --- ACCIONES DE NEGOCIO ---

    def accion_guardar(self):
        """Crea o actualiza la venta en estado PENDIENTE"""
        datos_venta = {
            'id_venta': self.id_venta,
            'cliente': self.input_cliente.value,
            'total': self.total_venta,
            'estado_pago': 'PENDIENTE'
        }
        # El controlador decide si hace INSERT o UPDATE
        self.id_venta = self.ctr.guardar_venta_completa(datos_venta, self.productos_seleccionados)
        ui.notify('Venta guardada (Pendiente)')
        if self.al_finalizar: self.al_finalizar()

    def accion_cancelar(self):
        """Elimina de DB si existe, o solo de la UI si no"""
        if self.id_venta:
            self.ctr.eliminar_venta_total(self.id_venta)
            ui.notify('Venta eliminada de la base de datos', type='warning')
        else:
            ui.notify('Venta descartada')
        
        self.card_ui.delete() # Elimina la tarjeta de la vista
        if self.al_cancelar: self.al_cancelar()

    def dialogo_pago(self):
        """Diálogo de cierre con cálculo de propina editable"""
        # Primero guardamos cambios antes de pagar
        self.accion_guardar()
        
        with ui.dialog() as diag, ui.card().classes('w-96'):
            ui.label('Finalizar Venta').classes('text-h5')
            ui.label(f'Subtotal: ${self.total_venta}')
            
            with ui.row().classes('items-center w-full'):
                propina_check = ui.checkbox('¿Sugerir 10% propina?', value=True)
                propina_input = ui.number('Propina $', value=int(self.total_venta*0.1)).bind_visibility_from(propina_check, 'value')
            
            total_final = ui.label().classes('text-xl font-bold text-green-700')
            
            def actualizar_pago():
                p = propina_input.value if propina_check.value else 0
                total_final.set_text(f'TOTAL A PAGAR: ${self.total_venta + p}')
            
            propina_input.on('value_change', actualizar_pago)
            propina_check.on('value_change', actualizar_pago)
            actualizar_pago()

            metodo = ui.select(['EFECTIVO', 'TARJETA', 'TRANSFERENCIA'], label='Medio de Pago', value='EFECTIVO').classes('w-full')
            
            ui.button('CONFIRMAR PAGO', color='green', 
                      on_click=lambda: self._finalizar_pago(diag, metodo.value, propina_input.value if propina_check.value else 0))
        diag.open()

    def _finalizar_pago(self, diag, metodo, propina):
        datos_pago = {
            'id_venta': self.id_venta,
            'estado_pago': 'PAGADO',
            'forma_pago': metodo,
            'propina': propina,
            'total': self.total_venta + propina
        }
        self.ctr.finalizar_pago_db(datos_pago)
        diag.close()
        self.card_ui.delete()
        ui.notify('Venta Pagada y Finalizada')
        if self.al_finalizar: self.al_finalizar()
