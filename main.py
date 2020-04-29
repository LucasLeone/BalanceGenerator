from tkinter import ttk
from tkinter import *
import sqlite3


RESULTADOS = ['Gastos Luz','Descuento obtenido','Descuento otorgado','Interes otorgado','Interes obtenido', 'Ventas','CMV', 'Alquileres cobrados', 'Comision Cobrada', 'Impuestos', 'Alquileres pagados', 'Sueldos y jornales', 'Gastos generales', 'Comisiones pagadas', 'Publicidad', 'Seguros', 'Gastos bancarios', 'Gastos varios', 'Fletes']


class Program:

    db_name = 'database.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title("Balance")
        
        
        # Menubar
        menubar = Menu(self.wind)
        self.wind.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Opciones', menu=filemenu)
        filemenu.add_command(label='Balance', command=self.balance)
        filemenu.add_separator()
        filemenu.add_command(label='Salir', command = self.wind.quit)


        # Frame
        frame = LabelFrame(self.wind, text='Balance')
        frame.grid(row=0, column=0, columnspan=2, pady=30)


        # Label de listas
        l1 = Label(frame, text='Activos').grid(row=2, column=0)
        l2 = Label(frame, text='Pasivos').grid(row=2, column=1)
        l3 = Label(frame, text='Resultados').grid(row=2, column=2)


        # ListsBoxs
        self.listbox1 = Listbox(frame, width=35, height=31)
        activos = ['Caja', 'Banco', 'Valores a depositar','Moneda extranjera',"Fondo fijo", "Titulos y acciones", "Deudores varios","Deudores por venta","Deudores morosos","Deudores en litigio","Documentos a cobrar", "Concepto pagado poadelantado", "Hipotecas a cobrar","Anticipios proveedores", "Accionistas", "Mercaderias", "Materias primas", "Productos en proceso de elaboracion","Productos terminados", "Rodados", "Instalaciones", "Muebles y utiles", "Inmuebles", "Maquinarias", "Llave de negocio", "Marcas y patentes", "Derechos de autor", "Gastos de organizacion", 'Capital', 'IVA CF', 'IVA Saldo a favor']
        self.listbox1.insert(0, *activos)
        self.listbox1.grid(row=3, column=0)
        

        self.listbox2 = Listbox(frame, width=35, height=31)
        pasivos = ["Proveedores", "Acreedores varios", "Documentos a pagar", "Intereses a pagar", "Obligaciones negociables", "Prestamos a pagar", "Acreedores prendarios e hipotecarios", "Adelantos en cuenta corriente", "Honorarios a pagar", "Sueldos a pagar", "Anses a pagar", "Retencion impuesto a las ganancias", "Retencion IVA", "Dividendos", "Concepto cobrado por adelantado", "Anticipo de clientes", "Cuentas por pagar", "Previsiones", 'Socio A', 'Socio B', 'Socio C', 'IVA DF', 'IVA Saldo a pagar']
        self.listbox2.insert(0, *pasivos)
        self.listbox2.grid(row=3, column=1)

        self.listbox3 = Listbox(frame, width=35, height=31)
        resultados = ['Gastos Luz','Descuento obtenido','Descuento otorgado','Interes otorgado','Interes obtenido', 'Ventas','CMV', 'Alquileres cobrados', 'Comision Cobrada', 'Impuestos', 'Alquileres pagados', 'Sueldos y jornales', 'Gastos generales', 'Comisiones pagadas', 'Publicidad', 'Seguros', 'Gastos bancarios', 'Gastos varios', 'Fletes']
        self.listbox3.insert(0, *resultados)
        self.listbox3.grid(row=3, column=2)
        

        # Input Importes
        Label(frame, text="Importes").grid(row=4, column=1)
        Label(frame, text='Debe').grid(row=7, column=0)
        self.mesagge = Label(frame, text='', fg='red')
        self.mesagge.grid(row=6, column=1)
        Label(frame, text='Haber').grid(row=7, column=2)
        Label(frame, text='Nro cuenta').grid(row=7, column=1)
        

        self.price_debe = Entry(frame)
        self.price_debe.grid(row=8, column=0)
        self.price_debe.insert(0, int(0))

        self.price_haber = Entry(frame)
        self.price_haber.grid(row=8, column=2)
        self.price_haber.insert(0, int(0))

        self.nro_cuenta = Entry(frame)
        self.nro_cuenta.grid(row=8, column=1)
        

        # Button Save
        b1 = Button(frame, text='Guardar', command=self.add_product).grid(row=9, column=1, sticky=W+E)


    # Query para db
    def run_query(self, query, parameters = ()):
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                result = cursor.execute(query, parameters)
                conn.commit()
            return result


    # Llenador de tabla
    def get_products(self):
            # cleaning table
            records = self.tree.get_children()
            for element in records:
                self.tree.delete(element)
            # Query
            query = 'SELECT * FROM balance ORDER BY id DESC'
            db_rows = self.run_query(query)
            # Llenando la tabla
            for row in db_rows:
                self.tree.insert('', 0, text = row[0], values = row[0:10])


    def balance(self):
        # Ventana de balance
        self.balance_wind = Toplevel()
        self.balance_wind.title('Balance de 8 columnas')


        # Table
        self.tree = ttk.Treeview(
            self.balance_wind, height=30, columns=[f"#{n}" for n in range(1, 11)]
        )
        self.tree.config(show='headings')
        
        self.tree.grid(row=0, column=0)
        self.tree.heading('#1', text='Numero', anchor=CENTER)
        self.tree.heading('#2', text='Cuenta', anchor=CENTER)
        self.tree.heading('#3', text='Debe', anchor=CENTER)
        self.tree.heading('#4', text='Haber', anchor=CENTER)
        self.tree.heading('#5', text='Deudor', anchor=CENTER)
        self.tree.heading('#6', text='Acreedor', anchor=CENTER)
        self.tree.heading('#7', text='Activo', anchor=CENTER)
        self.tree.heading('#8', text='Pasivo', anchor=CENTER)
        self.tree.heading('#9', text='Negativo', anchor=CENTER)
        self.tree.heading('#10', text='Positivo', anchor=CENTER)

        self.tree.column('#1', minwidth=55, width = 55, stretch=NO)
        self.tree.column('#2', minwidth=205, width = 205, stretch=NO)
        self.tree.column('#3', minwidth=100, width = 100, stretch=NO)
        self.tree.column('#4', minwidth=100, width = 100, stretch=NO)
        self.tree.column('#5', minwidth=100, width = 100, stretch=NO)
        self.tree.column('#6', minwidth=100, width = 100, stretch=NO)
        self.tree.column('#7', minwidth=100, width = 100, stretch=NO)
        self.tree.column('#8', minwidth=100, width = 100, stretch=NO)
        self.tree.column('#9', minwidth=100, width = 100, stretch=NO)
        self.tree.column('#10', minwidth=100, width = 100, stretch=NO)
        self.get_products()

        # Botones
        ttk.Button(self.balance_wind, text='Eliminar', command = self.delete_product).grid(row=1, column=0, sticky=W+E)
        ttk.Button(self.balance_wind, text='Editar', command = self.edit_product).grid(row=2, column=0, sticky=W+E)
        ttk.Button(self.balance_wind, text='Sumar', command = self.sum_total).grid(row=3, column=0, sticky=W+E)


    # Agregar producto
    def add_product(self):
        try:
            if (rows:= self.listbox1.selection_get()):
                if rows in RESULTADOS:
                    if float(self.price_debe.get()) > float(self.price_haber.get()):
                        negativo_a = (float(self.price_debe.get()) - float(self.price_haber.get()))
                        query = 'INSERT INTO balance (id, cuenta, debe, haber, activo, pasivo, negativo, positivo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
                        parameters = (self.nro_cuenta.get(), rows, self.price_debe.get(), self.price_haber.get(), 0, 0, negativo_a, 0)
                        self.run_query(query, parameters)
                        self.pasivo_negativo(self.nro_cuenta.get())
                        self.mesagge['text'] = 'Se guardo el resultado negativo'
                    else:
                        positivo_a = (float(self.price_haber.get()) - float(self.price_debe.get()))
                        query = 'INSERT INTO balance (id, cuenta, debe, haber, activo, pasivo, negativo, positivo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
                        parameters = (self.nro_cuenta.get(), rows, self.price_debe.get(), self.price_haber.get(), 0, 0, 0, positivo_a)
                        self.run_query(query, parameters)
                        self.pasivo_negativo(self.nro_cuenta.get())
                        self.mesagge['text'] = 'Se guardo el resultado positivo'
                else:
                    if rows == 'Socio A' or rows == 'Socio B' or rows == 'Socio C' or rows == 'IVA CF' or rows == 'IVA DF':
                        query = 'INSERT INTO balance (id, cuenta, debe, haber, deudor, acreedor, activo, pasivo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
                        parameters = (self.nro_cuenta.get(), rows, self.price_debe.get(), self.price_haber.get(), 0, 0, 0, 0)
                        self.run_query(query, parameters)
                        self.price_debe.delete(0, END)
                        self.price_debe.insert(0, int(0))
                        self.price_haber.delete(0, END)
                        self.price_haber.insert(0, int(0))
                        self.nro_cuenta.delete(0, END)
                        self.mesagge['text'] = 'Se guardo con exito'
                    else:
                        query = 'INSERT INTO balance (id, cuenta, debe, haber) VALUES (?, ?, ?, ?)'    
                        parameters = (self.nro_cuenta.get(), rows, self.price_debe.get(), self.price_haber.get())
                        self.run_query(query, parameters)
                        self.price_debe.delete(0, END)
                        self.price_debe.insert(0, int(0))
                        self.price_haber.delete(0, END)
                        self.price_haber.insert(0, int(0))
                        self.nro_cuenta.delete(0, END)
                        self.mesagge['text'] = 'Se guardo con exito'
            else:
                self.mesagge['text'] = 'Hay un error'
        except (sqlite3.IntegrityError, TclError):
            self.mesagge['text'] = 'No hay datos o ya esta cargado'


    # Funcion delete
    def delete_product(self):
        if (rows:= self.tree.selection()):
            name = self.tree.item(rows)['text']
            self.mesagge['text'] = ''
            query = 'DELETE FROM balance WHERE id = ?'
            self.run_query(query, (name, ))
            self.mesagge['text'] = 'El importe fue eliminado'
            self.get_products()
        else:
            self.mesagge['text'] = 'Selecciona un importe'

    
    # Parte visible de editar
    def edit_product(self):
        self.mesagge['text'] = ''
        if (rows:= self.tree.selection()):
            old_debe = self.tree.item(rows)['values'][2]
            old_haber = self.tree.item(rows)['values'][3]
            id_cuenta = self.tree.item(rows)['text']
            cuenta = self.tree.item(rows)['values'][1]
            self.edit_wind = Toplevel()
            self.edit_wind.title("Editar importe")

            # Labels
            Label(self.edit_wind, text='Debe').grid(row=0, column=2)
            Label(self.edit_wind, text='Haber').grid(row=0, column=3)

            # Old Importes
            Label(self.edit_wind, text = 'Importes actual').grid(row=1, column=1)
            Entry(self.edit_wind, textvariable= StringVar(self.edit_wind, value = old_debe), state='readonly').grid(row=1, column=2)
            Entry(self.edit_wind, textvariable= StringVar(self.edit_wind, value = old_haber), state='readonly').grid(row=1,column=3)
            
            # New Importes
            Label(self.edit_wind, text='Nuevos importes').grid(row=2, column=1)
            new_debe = Entry(self.edit_wind)
            new_debe.grid(row=2, column=2)
            new_haber = Entry(self.edit_wind)
            new_haber.grid(row=2, column=3)
            
            # Button
            Button(self.edit_wind, text='Actualizar', command = lambda: self.edit_records(id_cuenta, cuenta, new_debe.get(), new_haber.get())).grid(row=3, column=2, columnspan=2, sticky=W+E)
        else:
            self.mesagge['text'] = 'Selecciona un importe'


    # Funcion editar
    def edit_records(self, id_cuenta, cuenta, new_debe, new_haber):
        query = 'DELETE FROM balance WHERE id = ?'
        #query = 'UPDATE balance SET debe = ?, haber = ? WHERE id = ?'
        parameters = (id_cuenta,)
        self.run_query(query, parameters)
        if cuenta in RESULTADOS:
            self.new_result(id_cuenta, cuenta, new_debe, new_haber)
        else:
            self.new_record(id_cuenta, cuenta, new_debe, new_haber)
        self.edit_wind.destroy()
        self.mesagge['text'] = "El importe fue actualizado"
        self.get_products()


    # Insert Rubro Activo y Pasivo
    def new_record(self, id_cuenta, cuenta, new_debe, new_haber):
        query = 'INSERT INTO balance (id, cuenta, debe, haber) VALUES (?, ?, ?, ?)'
        parameters = (id_cuenta, cuenta, new_debe, new_haber)
        self.run_query(query, parameters)


    # Edit Rubro Resultado
    def new_result(self, id_cuenta, cuenta, new_debe, new_haber):
        if new_debe > new_haber:
            new_negativo = (float(new_debe) - float(new_haber))
            query = 'INSERT INTO balance (id, cuenta, debe, haber, activo, pasivo, negativo, positivo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
            parameters = (id_cuenta, cuenta, new_debe, new_haber, 0, 0, new_negativo, 0)
            self.run_query(query, parameters)
            self.pasivo_negativo(id_cuenta)
        else:
            new_positivo = (float(new_haber) - float(new_debe))
            query = 'INSERT INTO balance (id, cuenta, debe, haber, activo, pasivo, negativo, positivo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
            parameters = (id_cuenta, cuenta, new_debe, new_haber, 0, 0, 0, new_positivo)
            self.run_query(query, parameters)
            self.pasivo_negativo(id_cuenta)
        

    # Set activo y negativo = 0
    def pasivo_negativo(self, nro_cuenta):
        query = 'UPDATE balance SET activo = 0, pasivo = 0 WHERE id = ?'
        parameters = (nro_cuenta,)
        self.run_query(query, parameters)


    # Funcion suma total
    def sum_total(self):
        id_asd = 999
        cuenta_asd = 'TOTAL'
        query = '''INSERT INTO balance
(cuenta, debe, haber, deudor, acreedor,
  activo, pasivo, negativo, positivo)
SELECT 'TOTAL',
       SUM(debe),
       SUM(haber),
       SUM(deudor),
       SUM(acreedor),
       SUM(activo),
       SUM(pasivo),
       SUM(negativo),
       SUM(positivo)
  FROM balance;'''
        self.run_query(query)
        self.get_products()
        


if __name__ == "__main__":
    window = Tk()
    Program(window)
    window.mainloop() 