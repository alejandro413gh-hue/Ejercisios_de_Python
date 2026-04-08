import tkinter as Ventana

# zona de funciones +++++
def inicio_sesion(dato):
    print("se a iniciado la sesion del usuario.....")
    print(type(dato.get()))


# crear la ventana
obj_ventana = Ventana.Tk()
obj_ventana.title("Inicio de Sesión")
obj_ventana.geometry("800x808")
obj_ventana.config(bg="red")

# crear los widget elementos de interaccion con el usuario
label_usuario = Ventana.Label(obj_ventana, text="Escriba el usuario: ")
label_usuario.pack()

entry_usuario = Ventana.Entry(obj_ventana)
entry_usuario.pack()

label_contraseña = Ventana.Label(obj_ventana, text="Escriba la contraseña:")
label_contraseña.pack()

entry_contraseña = Ventana.Entry(obj_ventana)
entry_contraseña.pack()

# lambda [params] expresión_a_ejecutar
boton_inicio = Ventana.Button(obj_ventana, text="Inicio Sesión", command=lambda: inicio_sesion(entry_usuario))
boton_inicio.pack()

obj_ventana.mainloop()  # ir al final proyecto