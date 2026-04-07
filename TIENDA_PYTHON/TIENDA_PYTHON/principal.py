from formulario import Interfaz
#from modelo_usuario import Usuario
#++++ codigo principal ++++



# se consulto en la API los atributos de la interfaz


dato_color = ("DeepSkyBlue4")
dato_titulo = ("fORMULARIO DE REGISTRO")
preguntal = ("Digite su Nombre: ")
pregunta2 = ("Dijite su NIT: ")

obj_formulario = Interfaz (dato_color, dato_titulo)
formulario_usuario = obj_formulario.crear_formulario()

obj_formulario.crear_preguntas (formulario_usuario, preguntal, pregunta2)

formulario_usuario.mainloop() #final del codigo