from tkinter import Tk, Menu, messagebox, simpledialog
import pandas as pd

class MenuApp:
    def __init__(self, master):
        self.master = master
        self.create_menu()
        self.nombreArchivo = "/home/quinto/Descargas/Calculadoras/pueba.xls"
        self.estudiantes = pd.read_exel(self.nombreArchivo)

        #crear un area de texto para mostrar los resultados
        self.text_area = Text(master, wrap='word', height=20, width=60)
        self.text_area.pack(side='left', fill='both', expand=True)

    def create_menu(self):

        barra_menus = Menu(self.master)

        menu_excel = Menu(barra_menus, tearoff=0)
        menu_calculo = Menu(barra_menus, tearoff=0)
        menu_salir = Menu(barra_menus, tearoff=0)
        barra_menus.add_cascade(label="Excel", menu=menu_excel)
        barra_menus.add_cascade(label="Calculos", menu=menu_calculo)
        barra_menus.add_cascade(label="Salir", menu=menu_salir)

        menu_excel.add_command(label="Todos", command=self.show_all)
        menu_excel.add_command(label="Nombre", command=self.show_name)
        menu_excel.add_command(label="Mayores de 18", command=self.show_over_18)
        
        menu_calculo.add_command(label="Promedio", command=self.show_pro)
        menu_calculo.add_command(label="Mediana", command=self.show_med)
        menu_calculo.add_command(label="Moda", command=self.show_mod)

        menu_salir.add_command(label="Cerrar", command=self.show_sal)
        
        self.master.config(menu=barra_menus)
        
    def clear_text_area(self):
        """"Limpia el area de texto antes de mostrar nuevos resultados."""
        self.clear_text_area.delete(1.0,'end')
    
    def show_all(self):
        self.clear_text_area()
        self.text_area.insert('end', str(self.estudiantes))
        
    def show_name(self):
        #self.clear_text_area()
        #nombres = self.estudiantes[]
        name = simpledialog.askstring("Nombre", "Introduce tu nombre:")
        if name:
            messagebox.showinfo("Nombre ingresado", f"Tu nombre es: {name}")

    def show_over_18(self):
        age = simpledialog.askinteger("Edad", "Introduce tu edad:")
        if age is not None:
            if age >= 18:
                messagebox.showinfo("Acceso permitido", "Eres mayor de 18 años.")
            else:
                messagebox.showwarning("Acceso denegado", "Eres menor de 18 años.")

    def show_pro(self):
        messagebox.showinfo("Opción seleccionada", "Mostrar todos los datos.")
    def show_med(self):
        messagebox.showinfo("Opción seleccionada", "Mostrar todos los datos.")   
    def show_mod(self):
        messagebox.showinfo("Opción seleccionada", "Mostrar todos los datos.")
    
    def show_sal(Self):
        messagebox.showinfo("Opción seleccionada", "Mostrar todos los datos.")
        
class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Aplicación con Menú Excel")

        self.menu_app = MenuApp(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()