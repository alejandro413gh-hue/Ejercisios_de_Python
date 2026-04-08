import tkinter as Ventana
#zona de funciones
def inicio_sesion(dato_usuario):
    print("..........se esta buscando en la base de datos.........")
    print("se a iniciado la sesion del usuario....")
    print(dato_usuario)
    print(type(dato_usuario))
    
#crear ventana
obj_ventana = Ventana.Tk()
obj_ventana.title("inicio de Sesión")
obj_ventana.geometry("800x800")
obj_ventana.config(bg="red")

#crear los Widgets -- Elementos de interaccion con el usuario
label_usuario = Ventana.Label(obj_ventana , text="Escriba el usuario: ")
label_usuario.pack()
entry_usuario = Ventana.Entry(obj_ventana)
entry_usuario.pack()
dato_usuario = entry_usuario.get()

label_contraseña = Ventana.Label(obj_ventana , text="Escriba la contraseña: ")
label_contraseña.pack()
entry_contraseña = Ventana.Entry(obj_ventana)
entry_contraseña.pack()

boton_inicio = Ventana.Button(obj_ventana, text="Inicio de sesión" , command = lambda :inicio_sesion(dato_usuario))
boton_inicio.pack()

obj_ventana.mainloop() # <--- Esto va al final del proyecto