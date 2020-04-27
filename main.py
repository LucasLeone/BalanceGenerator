from tkinter import ttk
from tkinter import *
import sqlite3



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
        self.listbox1 = Listbox(frame, width=35, height=28)
        activos = ['Caja', 'Banco', 'Valores a depositar','Moneda extranjera',"Fondo fijo", "Titulos y acciones", "Deudores varios","Deudores por venta","Deudores morosos","Deudores en litigio","Documentos a cobrar", "Concepto pagado poadelantado", "Hipotecas a cobrar","Anticipios proveedores", "Accionistas", "Mercaderias", "Materias primas", "Productos en proceso de elaboracion","Productos terminados", "Rodados", "Instalaciones", "Muebles y utiles", "Inmuebles", "Maquinarias", "Llave de negocio", "Marcas y patentes", "Derechos de autor", "Gastos de organizacion"]
        self.listbox1.insert(0, *activos)
        self.listbox1.grid(row=3, column=0)
        

        self.listbox2 = Listbox(frame, width=35, height=28)
        pasivos = ["Proveedores", "Acreedores varios", "Documentos a pagar", "Intereses a pagar", "Obligaciones negociables", "Prestamos a pagar", "Acreedores prendarios e hipotecarios", "Adelantos en cuenta corriente", "Honorarios a pagar", "Sueldos a pagar", "Anses a pagar", "Retencion impuesto a las ganancias", "Retencion IVA", "Dividendos", "Concepto cobrado por adelantado", "Anticipo de clientes", "Cuentas por pagar", "Previsiones"]
        self.listbox2.insert(0, *pasivos)
        self.listbox2.grid(row=3, column=1)

        self.listbox3 = Listbox(frame, width=35, height=28)
        resultados = ['Gastos Luz','Descuento obtenido','Descuento otorgado','Interes otorgado','Interes obtenido', 'Ventas','CMV', 'Alquileres cobrados', 'Comision Cobrada', 'Impuestos', 'Alquileres pagados', 'Sueldos y jornales', 'Gastos generales', 'Comisiones pagadas', 'Publicidad', 'Seguros']
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


    def run_query(self, query, parameters = ()):
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                result = cursor.execute(query, parameters)
                conn.commit()
            return result


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
            self.balance_wind, height=10, columns=[f"#{n}" for n in range(1, 11)]
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
        self.tree.heading('#9', text='Positivo', anchor=CENTER)
        self.tree.heading('#10', text='Negativo', anchor=CENTER)

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


    def validation(self):
        return len(self.price_debe.get()) == 0 and len(self.price_haber.get()) == 0 and len(self.nro_cuenta.get()) == 0


    def add_product(self):
        try:
            if (rows:= self.listbox1.selection_get() or self.listbox2.selection_get()):
                query = 'INSERT INTO balance (id, cuenta, debe, haber) VALUES (?, ?, ?, ?)'
                parameters = (self.nro_cuenta.get(), rows, self.price_debe.get(), self.price_haber.get())
                self.run_query(query, parameters)
                self.price_debe.delete(0, END)
                self.price_debe.insert(0, int(0))
                self.price_haber.delete(0, END)
                self.price_haber.insert(0, int(0))
                self.nro_cuenta.delete(0, END)
                self.mesagge['text'] = 'Se guardo con exito'
            elif (rows:= self.listbox3.selection_get()):
                query = 'INSERT INTO balance (id, cuenta, debe, haber) VALUES (?, ?, ?, ?)'
                parameters = (self.nro_cuenta.get(), rows, self.price_debe.get(), self.price_haber.get())
                self.run_query(query, parameters)
                self.price_debe.delete(0, END)
                self.price_haber(0, END)
                self.nro_cuenta.delete(0, END)
                self.mesagge['text'] = 'Resultado de ejercicio guardado'
            else:
                self.mesagge['text'] = 'No hay rubro'
        except (sqlite3.IntegrityError, TclError):
            self.mesagge['text'] = 'No hay datos o ya esta cargado'




if __name__ == "__main__":
    window = Tk()
    Program(window)
    window.mainloop()




    