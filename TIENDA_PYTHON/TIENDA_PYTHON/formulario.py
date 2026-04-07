
import tkinter as Ventana

class Interfaz:
    def __init__(self,color,titulo):
        self.color = color
        self.titulo = titulo

    def crear_formulario(self):
        formulario = Ventana.Tk()
        formulario.title(self.titulo)
        formulario.geometry("500x605")
        formulario.config(bg=self.color)
        
        #Menu opciones
        menu_opciones = Ventana.Menu(formulario)
        menu_opciones.add_command(label="Guardar", command=self.registrar)
        menu_opciones.add_command(label="Salir", command=formulario.quit)
        formulario.config(menu=menu_opciones)

        meubtn= Ventana.Menubutton(formulario, text="Opciones")
        menu = Ventana.Menu(meubtn, tearoff=0)
        menu.add_command(label="Guardar", command=self.registrar)
        menu.add_command(label="Salir", command=formulario.quit)
        meubtn.config(menu=menu)
        meubtn.pack(anchor="w")
        
        return formulario
    
    def registrar(self):
        print("guardando datos...")

        seleccion_nombre = self.entry_r1.get()
        print("Nombre ingresado:", seleccion_nombre)

        seleccion_nit = self.entry_r2.get()
        print("NIT ingresado:", seleccion_nit)

        seleccion_genero = self.genero.get()
        print("Género seleccionado:", seleccion_genero)

        seleccion = self.pais.get(self.pais.curselection())
        print("Seleccionó:", seleccion)

        seleccion_terminos = self.opcion1.get()
        print("Aceptó términos:", seleccion_terminos)




    def borrar_campos(self):
        print("borrando campos...")
        self.entry_r1.delete(0, 'end')
        self.entry_r2.delete(0, 'end')

    def crear_preguntas(self, formulario, preguntal, pregunta2):

        #Message
        frame7 = Ventana.Frame(formulario, width=300, height=100)
        frame7.pack()
        frame7.pack_propagate(False)
        mensaje = Ventana.Message(frame7, text="Bienvenido al sistema", font=("Arial", 27))
        mensaje.pack()

        #Frame 1 (contenedor de preguntas)

        frame1 = Ventana.Frame(formulario, width=300, height=100)
        frame1.pack()
        frame1.pack_propagate(False)

        label_p1 = Ventana.Label (frame1, text=preguntal)
        label_p1.pack()
        self.entry_r1 = Ventana.Entry (frame1)
        self.entry_r1.pack()
        label_p2 = Ventana.Label (frame1, text=pregunta2)
        label_p2.pack()
        self.entry_r2 = Ventana.Entry (frame1)
        self.entry_r2.pack()

        
        frame2 = Ventana.Frame(formulario, width=300, height=60)
        frame2.pack()
        frame2.pack_propagate(False)

        #radiobuttons para seleccionar el género
        self.genero = Ventana.StringVar()
        radio1 = Ventana.Radiobutton(frame2,text="Masculino",variable=self.genero, value="M")
        radio1.pack()
        radio2 = Ventana.Radiobutton(frame2,text="Femenino",variable=self.genero, value="F")
        radio2.pack()



        # LISTBOX para seleccionar el país
        frame3 = Ventana.Frame(formulario, width=300, height=90)
        frame3.pack()
        frame3.pack_propagate(False)
        self.pais = Ventana.Listbox(frame3)

        self.pais.insert(1, "Colombia")
        self.pais.insert(2, "México")
        self.pais.insert(3, "Argentina")

        self.pais.pack()

        frame8 = Ventana.Frame(formulario, width=300, height=20)
        frame8.pack()

        #checkbox para aceptar términos
        frame4 = Ventana.Frame(formulario, width=300, height=50)
        frame4.pack()
        frame4.pack_propagate(False)
        self.opcion1 = Ventana.IntVar()
        check1 = Ventana.Checkbutton(frame4, text="Acepto términos", variable=self.opcion1)
        check1.pack()



        #Boton para enviar el formulario
        frame5 = Ventana.Frame(formulario, width=300, height=40)
        frame5.pack()
        frame5.pack_propagate(False)
        boton_enviar = Ventana.Button(frame5, text="Registrar", command=self.registrar)
        boton_enviar.pack()

        frame6 = Ventana.Frame(formulario, width=300, height=40)
        frame6.pack()
        frame6.pack_propagate(False)
        boton_borrar = Ventana.Button(frame6, text="Borrar campos", command=self.borrar_campos)
        boton_borrar.pack()



        #CANVAS 
        canvas = Ventana.Canvas(formulario, width=300, height=100, bg="white")
        canvas.pack()
        canvas.create_rectangle(50, 20, 150, 80, fill="red")
        canvas.create_text(100, 50, text="¡Bienvenido!", fill="white")






