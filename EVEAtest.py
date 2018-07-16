from tkinter import *
from tkinter import messagebox as MessageBox

def raise_Frame(frame):
	frame.tkraise()

def promediarDepresion():
	global promedioDepre
	promedioDepre = float((opcionTriste.get() + opcionApagado.get() + opcionAlicaido.get() + opcionMelancolico.get())/4)
	pD.set(promedioDepre)

def promediarAnsiedad():
	global promedioAnsi
	promedioAnsi = float((opcionNervios.get() + opcionTenso.get() + opcionAnsioso.get() + opcionIntranquilo.get())/4) 
	pAn.set(promedioAnsi)

def promediarHostilidad():
	global promedioHosti
	promedioHosti = float((opcionIrritado.get() + opcionEnojado.get() + opcionMolesto.get() + opcionEnfadado.get())/4)
	pH.set(promedioHosti)

def promediarAlegria():
	global promedioAleg
	promedioAleg = float((opcionAlegre.get() + opcionOptimista.get() + opcionJovial.get() + opcionContento.get())/4) 
	pAl.set(promedioAleg)

def inclinacion():
	global tend 
	if promedioDepre > promedioAnsi and promedioDepre > promedioHosti and promedioDepre > promedioAleg:
		tend = "D"
		tendencia.set("Depresión")
	elif promedioAnsi > promedioDepre and promedioAnsi > promedioHosti and promedioAnsi > promedioAleg:
		tend = "A"
		tendencia.set("Ansiedad")
	elif promedioHosti > promedioDepre and promedioHosti > promedioAnsi and promedioHosti > promedioAleg:
		tend = "H"
		tendencia.set("Hostilidad")
	elif promedioAleg > promedioDepre and promedioAleg > promedioAnsi and promedioAleg > promedioHosti:
		tend = "a"
		tendencia.set("Alegría")
	else:
		tendencia.set("Contestar nuevamente")

	with open('D:\\Tesis apoco no\\Python\\Scripts EVEA\\resultadosTendecia.txt', "a") as f:
		for t in tend:
			f.write(t + "\n") 

def salir():
	resultado =  MessageBox.askquestion("Salir", "¿Estás seguro que quieres salir?")
	if resultado == 'yes':
		root.destroy()

root = Tk()
root.title("EVEA")
root.resizable(0,0)
root.iconbitmap('perro.ico')

frameUno = Frame(root)
frameDos = Frame(root)
frameTres = Frame(root)
frameCuatro = Frame(root)
frameCinco = Frame(root)
frameSeis = Frame(root)
frameSiete = Frame(root)
frameOcho = Frame(root)
frameNueve = Frame(root)
frameDiez = Frame(root)
frameOnce = Frame(root)
frameDoce = Frame(root)
frameTrece = Frame(root)
frameCatorce = Frame(root)
frameQuince = Frame(root)
frameDiesciseis = Frame(root)
frameResultados = Frame(root)

for frame in (frameUno, frameDos, frameTres, frameCuatro, frameCinco, frameSeis, frameSiete, frameOcho, frameNueve,
	frameDiez, frameOnce, frameDoce, frameTrece, frameCatorce, frameQuince, frameDiesciseis, frameResultados):
    frame.grid(row = 0, column = 0, sticky='news')

#Insertar imágenes
imagen = PhotoImage(file = "cerebro.png")
imagenDos = PhotoImage(file = "Flecha.png")
Label(frameUno, image = imagen).grid(row = 1, column = 1)
Label(frameUno, image = imagenDos).grid(row = 3, column =13)

#Frame pregunta tristeza

opcionTriste = IntVar()

Radiobutton(frameUno, text = "0", variable = opcionTriste, value = 0).grid(row = 2, column = 2)
Radiobutton(frameUno, text = "1", variable = opcionTriste, value = 1).grid(row = 2, column = 3)
Radiobutton(frameUno, text = "2", variable = opcionTriste, value = 2).grid(row = 2, column = 4)
Radiobutton(frameUno, text = "3", variable = opcionTriste, value = 3).grid(row = 2, column = 5)
Radiobutton(frameUno, text = "4", variable = opcionTriste, value = 4).grid(row = 2, column = 6)
Radiobutton(frameUno, text = "5", variable = opcionTriste, value = 5).grid(row = 2, column = 7)
Radiobutton(frameUno, text = "6", variable = opcionTriste, value = 6).grid(row = 2, column = 8)
Radiobutton(frameUno, text = "7", variable = opcionTriste, value = 7).grid(row = 2, column = 9)
Radiobutton(frameUno, text = "8", variable = opcionTriste, value = 8).grid(row = 2, column = 10)
Radiobutton(frameUno, text = "9", variable = opcionTriste, value = 9).grid(row = 2, column = 11)
Radiobutton(frameUno, text = "10", variable = opcionTriste, value = 10).grid(row = 2, column = 12)
Label(frameUno, text = "Me siento triste").grid(row = 1, column = 7)
Button(frameUno, text='Continuar', command=lambda:raise_Frame(frameDos)).grid(row = 3, column = 13)

#Insertar imágenes
imagen2 = PhotoImage(file = "cerebro.png")
imagenDos2 = PhotoImage(file = "Flecha.png")
Label(frameDos, image = imagen2).grid(row = 1, column = 1)
Label(frameDos, image = imagenDos2).grid(row = 3, column =13 )
#Frame pregunta nervios

opcionNervios = IntVar()

Radiobutton(frameDos, text = "0", variable = opcionNervios, value = 0).grid(row = 2, column = 2)
Radiobutton(frameDos, text = "1", variable = opcionNervios, value = 1).grid(row = 2, column = 3)
Radiobutton(frameDos, text = "2", variable = opcionNervios, value = 2).grid(row = 2, column = 4)
Radiobutton(frameDos, text = "3", variable = opcionNervios, value = 3).grid(row = 2, column = 5)
Radiobutton(frameDos, text = "4", variable = opcionNervios, value = 4).grid(row = 2, column = 6)
Radiobutton(frameDos, text = "5", variable = opcionNervios, value = 5).grid(row = 2, column = 7)
Radiobutton(frameDos, text = "6", variable = opcionNervios, value = 6).grid(row = 2, column = 8)
Radiobutton(frameDos, text = "7", variable = opcionNervios, value = 7).grid(row = 2, column = 9)
Radiobutton(frameDos, text = "8", variable = opcionNervios, value = 8).grid(row = 2, column = 10)
Radiobutton(frameDos, text = "9", variable = opcionNervios, value = 9).grid(row = 2, column = 11)
Radiobutton(frameDos, text = "10", variable =opcionNervios, value = 10).grid(row = 2, column = 12)
Label(frameDos, text = "Me siento nervioso").grid(row = 1, column = 7)
Button(frameDos, text='Continuar', command=lambda:raise_Frame(frameTres)).grid(row = 3, column = 13)


#Insertar imágenes
imagen3 = PhotoImage(file = "cerebro.png")
imagenDos3 = PhotoImage(file = "Flecha.png")
Label(frameTres, image = imagen3).grid(row = 1, column = 1)
Label(frameTres, image = imagenDos3).grid(row = 3, column =13 )

#Frame pregunta irritado

opcionIrritado = IntVar()

Radiobutton(frameTres, text = "0", variable = opcionIrritado, value = 0).grid(row = 2, column = 2)
Radiobutton(frameTres, text = "1", variable = opcionIrritado, value = 1).grid(row = 2, column = 3)
Radiobutton(frameTres, text = "2", variable = opcionIrritado, value = 2).grid(row = 2, column = 4)
Radiobutton(frameTres, text = "3", variable = opcionIrritado, value = 3).grid(row = 2, column = 5)
Radiobutton(frameTres, text = "4", variable = opcionIrritado, value = 4).grid(row = 2, column = 6)
Radiobutton(frameTres, text = "5", variable = opcionIrritado, value = 5).grid(row = 2, column = 7)
Radiobutton(frameTres, text = "6", variable = opcionIrritado, value = 6).grid(row = 2, column = 8)
Radiobutton(frameTres, text = "7", variable = opcionIrritado, value = 7).grid(row = 2, column = 9)
Radiobutton(frameTres, text = "8", variable = opcionIrritado, value = 8).grid(row = 2, column = 10)
Radiobutton(frameTres, text = "9", variable = opcionIrritado, value = 9).grid(row = 2, column = 11)
Radiobutton(frameTres, text = "10", variable =opcionIrritado, value = 10).grid(row = 2, column = 12)
Label(frameTres, text = "Me siento irritado").grid(row = 1, column = 7)
Button(frameTres, text='Continuar', command=lambda:raise_Frame(frameCuatro)).grid(row = 3, column = 13)

#Insertar imágenes
imagen4 = PhotoImage(file = "cerebro.png")
imagenDos4 = PhotoImage(file = "Flecha.png")
Label(frameCuatro, image = imagen4).grid(row = 1, column = 1)
Label(frameCuatro, image = imagenDos4).grid(row = 3, column =13)

#Frame pregunta alegre

opcionAlegre = IntVar()

Radiobutton(frameCuatro, text = "0", variable = opcionAlegre, value = 0).grid(row = 2, column = 2)
Radiobutton(frameCuatro, text = "1", variable = opcionAlegre, value = 1).grid(row = 2, column = 3)
Radiobutton(frameCuatro, text = "2", variable = opcionAlegre, value = 2).grid(row = 2, column = 4)
Radiobutton(frameCuatro, text = "3", variable = opcionAlegre, value = 3).grid(row = 2, column = 5)
Radiobutton(frameCuatro, text = "4", variable = opcionAlegre, value = 4).grid(row = 2, column = 6)
Radiobutton(frameCuatro, text = "5", variable = opcionAlegre, value = 5).grid(row = 2, column = 7)
Radiobutton(frameCuatro, text = "6", variable = opcionAlegre, value = 6).grid(row = 2, column = 8)
Radiobutton(frameCuatro, text = "7", variable = opcionAlegre, value = 7).grid(row = 2, column = 9)
Radiobutton(frameCuatro, text = "8", variable = opcionAlegre, value = 8).grid(row = 2, column = 10)
Radiobutton(frameCuatro, text = "9", variable = opcionAlegre, value = 9).grid(row = 2, column = 11)
Radiobutton(frameCuatro, text = "10", variable = opcionAlegre, value = 10).grid(row = 2, column = 12)
Label(frameCuatro, text = "Me siento alegre").grid(row = 1, column = 7)
Button(frameCuatro, text='Continuar', command=lambda:raise_Frame(frameCinco)).grid(row = 3, column = 13)

#Insertar imágenes
imagen5 = PhotoImage(file = "cerebro.png")
imagenDos5 = PhotoImage(file = "Flecha.png")
Label(frameCinco, image = imagen5).grid(row = 1, column = 1)
Label(frameCinco, image = imagenDos5).grid(row = 3, column =13)

#Frame pregunta apagado

opcionApagado = IntVar()

Radiobutton(frameCinco, text = "0", variable = opcionApagado, value = 0).grid(row = 2, column = 2)
Radiobutton(frameCinco, text = "1", variable = opcionApagado, value = 1).grid(row = 2, column = 3)
Radiobutton(frameCinco, text = "2", variable = opcionApagado, value = 2).grid(row = 2, column = 4)
Radiobutton(frameCinco, text = "3", variable = opcionApagado, value = 3).grid(row = 2, column = 5)
Radiobutton(frameCinco, text = "4", variable = opcionApagado, value = 4).grid(row = 2, column = 6)
Radiobutton(frameCinco, text = "5", variable = opcionApagado, value = 5).grid(row = 2, column = 7)
Radiobutton(frameCinco, text = "6", variable = opcionApagado, value = 6).grid(row = 2, column = 8)
Radiobutton(frameCinco, text = "7", variable = opcionApagado, value = 7).grid(row = 2, column = 9)
Radiobutton(frameCinco, text = "8", variable = opcionApagado, value = 8).grid(row = 2, column = 10)
Radiobutton(frameCinco, text = "9", variable = opcionApagado, value = 9).grid(row = 2, column = 11)
Radiobutton(frameCinco, text = "10", variable = opcionApagado, value = 10).grid(row = 2, column = 12)
Label(frameCinco, text = "Me siento apagado").grid(row = 1, column = 7)
Button(frameCinco, text='Continuar', command=lambda:raise_Frame(frameSeis)).grid(row = 3, column = 13)

#Insertar imágenes
imagen6 = PhotoImage(file = "cerebro.png")
imagenDos6 = PhotoImage(file = "Flecha.png")
Label(frameSeis, image = imagen6).grid(row = 1, column = 1)
Label(frameSeis, image = imagenDos6).grid(row = 3, column =13)

#Frame pregunta tenso

opcionTenso = IntVar()

Radiobutton(frameSeis, text = "0", variable = opcionTenso, value = 0).grid(row = 2, column = 2)
Radiobutton(frameSeis, text = "1", variable = opcionTenso, value = 1).grid(row = 2, column = 3)
Radiobutton(frameSeis, text = "2", variable = opcionTenso, value = 2).grid(row = 2, column = 4)
Radiobutton(frameSeis, text = "3", variable = opcionTenso, value = 3).grid(row = 2, column = 5)
Radiobutton(frameSeis, text = "4", variable = opcionTenso, value = 4).grid(row = 2, column = 6)
Radiobutton(frameSeis, text = "5", variable = opcionTenso, value = 5).grid(row = 2, column = 7)
Radiobutton(frameSeis, text = "6", variable = opcionTenso, value = 6).grid(row = 2, column = 8)
Radiobutton(frameSeis, text = "7", variable = opcionTenso, value = 7).grid(row = 2, column = 9)
Radiobutton(frameSeis, text = "8", variable = opcionTenso, value = 8).grid(row = 2, column = 10)
Radiobutton(frameSeis, text = "9", variable = opcionTenso, value = 9).grid(row = 2, column = 11)
Radiobutton(frameSeis, text = "10", variable = opcionTenso, value = 10).grid(row = 2, column = 12)
Label(frameSeis, text = "Me siento tenso").grid(row = 1, column = 7)
Button(frameSeis, text='Continuar', command=lambda:raise_Frame(frameSiete)).grid(row = 3, column = 13)

#Insertar imágenes
imagen7 = PhotoImage(file = "cerebro.png")
imagenDos7 = PhotoImage(file = "Flecha.png")
Label(frameSiete, image = imagen7).grid(row = 1, column = 1)
Label(frameSiete, image = imagenDos7).grid(row = 3, column =13)

#Frame pregunta enojado

opcionEnojado = IntVar()

Radiobutton(frameSiete, text = "0", variable = opcionEnojado, value = 0).grid(row = 2, column = 2)
Radiobutton(frameSiete, text = "1", variable = opcionEnojado, value = 1).grid(row = 2, column = 3)
Radiobutton(frameSiete, text = "2", variable = opcionEnojado, value = 2).grid(row = 2, column = 4)
Radiobutton(frameSiete, text = "3", variable = opcionEnojado, value = 3).grid(row = 2, column = 5)
Radiobutton(frameSiete, text = "4", variable = opcionEnojado, value = 4).grid(row = 2, column = 6)
Radiobutton(frameSiete, text = "5", variable = opcionEnojado, value = 5).grid(row = 2, column = 7)
Radiobutton(frameSiete, text = "6", variable = opcionEnojado, value = 6).grid(row = 2, column = 8)
Radiobutton(frameSiete, text = "7", variable = opcionEnojado, value = 7).grid(row = 2, column = 9)
Radiobutton(frameSiete, text = "8", variable = opcionEnojado, value = 8).grid(row = 2, column = 10)
Radiobutton(frameSiete, text = "9", variable = opcionEnojado, value = 9).grid(row = 2, column = 11)
Radiobutton(frameSiete, text = "10", variable = opcionEnojado, value = 10).grid(row = 2, column = 12)
Label(frameSiete, text = "Me siento enojado").grid(row = 1, column = 7)
Button(frameSiete, text='Continuar', command=lambda:raise_Frame(frameOcho)).grid(row = 3, column = 13)

#Insertar imágenes
imagen8 = PhotoImage(file = "cerebro.png")
imagenDos8 = PhotoImage(file = "Flecha.png")
Label(frameOcho, image = imagen8).grid(row = 1, column = 1)
Label(frameOcho, image = imagenDos8).grid(row = 3, column =13)

#Frame pregunta optimista

opcionOptimista = IntVar()

Radiobutton(frameOcho, text = "0", variable = opcionOptimista, value = 0).grid(row = 2, column = 2)
Radiobutton(frameOcho, text = "1", variable = opcionOptimista, value = 1).grid(row = 2, column = 3)
Radiobutton(frameOcho, text = "2", variable = opcionOptimista, value = 2).grid(row = 2, column = 4)
Radiobutton(frameOcho, text = "3", variable = opcionOptimista, value = 3).grid(row = 2, column = 5)
Radiobutton(frameOcho, text = "4", variable = opcionOptimista, value = 4).grid(row = 2, column = 6)
Radiobutton(frameOcho, text = "5", variable = opcionOptimista, value = 5).grid(row = 2, column = 7)
Radiobutton(frameOcho, text = "6", variable = opcionOptimista, value = 6).grid(row = 2, column = 8)
Radiobutton(frameOcho, text = "7", variable = opcionOptimista, value = 7).grid(row = 2, column = 9)
Radiobutton(frameOcho, text = "8", variable = opcionOptimista, value = 8).grid(row = 2, column = 10)
Radiobutton(frameOcho, text = "9", variable = opcionOptimista, value = 9).grid(row = 2, column = 11)
Radiobutton(frameOcho, text = "10", variable = opcionOptimista, value = 10).grid(row = 2, column = 12)
Label(frameOcho, text = "Me siento optmista").grid(row = 1, column = 7)
Button(frameOcho, text='Continuar', command=lambda:raise_Frame(frameNueve)).grid(row = 3, column = 13)

#Insertar imágenes
imagen9 = PhotoImage(file = "cerebro.png")
imagenDos9 = PhotoImage(file = "Flecha.png")
Label(frameNueve, image = imagen9).grid(row = 1, column = 1)
Label(frameNueve, image = imagenDos9).grid(row = 3, column =13)

#Frame pregunta alicaido

opcionAlicaido = IntVar()

Radiobutton(frameNueve, text = "0", variable = opcionAlicaido, value = 0).grid(row = 2, column = 2)
Radiobutton(frameNueve, text = "1", variable = opcionAlicaido, value = 1).grid(row = 2, column = 3)
Radiobutton(frameNueve, text = "2", variable = opcionAlicaido, value = 2).grid(row = 2, column = 4)
Radiobutton(frameNueve, text = "3", variable = opcionAlicaido, value = 3).grid(row = 2, column = 5)
Radiobutton(frameNueve, text = "4", variable = opcionAlicaido, value = 4).grid(row = 2, column = 6)
Radiobutton(frameNueve, text = "5", variable = opcionAlicaido, value = 5).grid(row = 2, column = 7)
Radiobutton(frameNueve, text = "6", variable = opcionAlicaido, value = 6).grid(row = 2, column = 8)
Radiobutton(frameNueve, text = "7", variable = opcionAlicaido, value = 7).grid(row = 2, column = 9)
Radiobutton(frameNueve, text = "8", variable = opcionAlicaido, value = 8).grid(row = 2, column = 10)
Radiobutton(frameNueve, text = "9", variable = opcionAlicaido, value = 9).grid(row = 2, column = 11)
Radiobutton(frameNueve, text = "10", variable = opcionAlicaido, value = 10).grid(row = 2, column = 12)
Label(frameNueve, text = "Me siento abatido").grid(row = 1, column = 7)
Button(frameNueve, text='Continuar', command=lambda:raise_Frame(frameDiez)).grid(row = 3, column = 13)

#Insertar imágenes
imagen10 = PhotoImage(file = "cerebro.png")
imagenDos10 = PhotoImage(file = "Flecha.png")
Label(frameDiez, image = imagen10).grid(row = 1, column = 1)
Label(frameDiez, image = imagenDos10).grid(row = 3, column =13)

#Frame pregunta ancioso

opcionAnsioso = IntVar()

Radiobutton(frameDiez, text = "0", variable = opcionAnsioso, value = 0).grid(row = 2, column = 2)
Radiobutton(frameDiez, text = "1", variable = opcionAnsioso, value = 1).grid(row = 2, column = 3)
Radiobutton(frameDiez, text = "2", variable = opcionAnsioso, value = 2).grid(row = 2, column = 4)
Radiobutton(frameDiez, text = "3", variable = opcionAnsioso, value = 3).grid(row = 2, column = 5)
Radiobutton(frameDiez, text = "4", variable = opcionAnsioso, value = 4).grid(row = 2, column = 6)
Radiobutton(frameDiez, text = "5", variable = opcionAnsioso, value = 5).grid(row = 2, column = 7)
Radiobutton(frameDiez, text = "6", variable = opcionAnsioso, value = 6).grid(row = 2, column = 8)
Radiobutton(frameDiez, text = "7", variable = opcionAnsioso, value = 7).grid(row = 2, column = 9)
Radiobutton(frameDiez, text = "8", variable = opcionAnsioso, value = 8).grid(row = 2, column = 10)
Radiobutton(frameDiez, text = "9", variable = opcionAnsioso, value = 9).grid(row = 2, column = 11)
Radiobutton(frameDiez, text = "10", variable = opcionAnsioso, value = 10).grid(row = 2, column = 12)
Label(frameDiez, text = "Me siento ancioso").grid(row = 1, column = 7)
Button(frameDiez, text='Continuar', command=lambda:raise_Frame(frameOnce)).grid(row = 3, column = 13)

#Insertar imágenes
imagen11 = PhotoImage(file = "cerebro.png")
imagenDos11 = PhotoImage(file = "Flecha.png")
Label(frameOnce, image = imagen11).grid(row = 1, column = 1)
Label(frameOnce, image = imagenDos11).grid(row = 3, column =13)

#Frame pregunta molesto

opcionMolesto = IntVar()

Radiobutton(frameOnce, text = "0", variable = opcionMolesto, value = 0).grid(row = 2, column = 2)
Radiobutton(frameOnce, text = "1", variable = opcionMolesto, value = 1).grid(row = 2, column = 3)
Radiobutton(frameOnce, text = "2", variable = opcionMolesto, value = 2).grid(row = 2, column = 4)
Radiobutton(frameOnce, text = "3", variable = opcionMolesto, value = 3).grid(row = 2, column = 5)
Radiobutton(frameOnce, text = "4", variable = opcionMolesto, value = 4).grid(row = 2, column = 6)
Radiobutton(frameOnce, text = "5", variable = opcionMolesto, value = 5).grid(row = 2, column = 7)
Radiobutton(frameOnce, text = "6", variable = opcionMolesto, value = 6).grid(row = 2, column = 8)
Radiobutton(frameOnce, text = "7", variable = opcionMolesto, value = 7).grid(row = 2, column = 9)
Radiobutton(frameOnce, text = "8", variable = opcionMolesto, value = 8).grid(row = 2, column = 10)
Radiobutton(frameOnce, text = "9", variable = opcionMolesto, value = 9).grid(row = 2, column = 11)
Radiobutton(frameOnce, text = "10", variable = opcionMolesto, value = 10).grid(row = 2, column = 12)
Label(frameOnce, text = "Me siento molesto").grid(row = 1, column = 7)
Button(frameOnce, text='Continuar', command=lambda:raise_Frame(frameDoce)).grid(row = 3, column = 13)

#Insertar imágenes
imagen12 = PhotoImage(file = "cerebro.png")
imagenDos12 = PhotoImage(file = "Flecha.png")
Label(frameDoce, image = imagen12).grid(row = 1, column = 1)
Label(frameDoce, image = imagenDos12).grid(row = 3, column =13)

#Frame pregunta jovial

opcionJovial = IntVar()

Radiobutton(frameDoce, text = "0", variable = opcionJovial, value = 0).grid(row = 2, column = 2)
Radiobutton(frameDoce, text = "1", variable = opcionJovial, value = 1).grid(row = 2, column = 3)
Radiobutton(frameDoce, text = "2", variable = opcionJovial, value = 2).grid(row = 2, column = 4)
Radiobutton(frameDoce, text = "3", variable = opcionJovial, value = 3).grid(row = 2, column = 5)
Radiobutton(frameDoce, text = "4", variable = opcionJovial, value = 4).grid(row = 2, column = 6)
Radiobutton(frameDoce, text = "5", variable = opcionJovial, value = 5).grid(row = 2, column = 7)
Radiobutton(frameDoce, text = "6", variable = opcionJovial, value = 6).grid(row = 2, column = 8)
Radiobutton(frameDoce, text = "7", variable = opcionJovial, value = 7).grid(row = 2, column = 9)
Radiobutton(frameDoce, text = "8", variable = opcionJovial, value = 8).grid(row = 2, column = 10)
Radiobutton(frameDoce, text = "9", variable = opcionJovial, value = 9).grid(row = 2, column = 11)
Radiobutton(frameDoce, text = "10", variable = opcionJovial, value = 10).grid(row = 2, column = 12)
Label(frameDoce, text = "Me siento jovial").grid(row = 1, column = 7)
Button(frameDoce, text='Continuar', command=lambda:raise_Frame(frameTrece)).grid(row = 3, column = 13)

#Insertar imágenes
imagen13 = PhotoImage(file = "cerebro.png")
imagenDos13 = PhotoImage(file = "Flecha.png")
Label(frameTrece, image = imagen13).grid(row = 1, column = 1)
Label(frameTrece, image = imagenDos13).grid(row = 3, column =13)

#Frame pregunta melancolico

opcionMelancolico = IntVar()

Radiobutton(frameTrece, text = "0", variable = opcionMelancolico, value = 0).grid(row = 2, column = 2)
Radiobutton(frameTrece, text = "1", variable = opcionMelancolico, value = 1).grid(row = 2, column = 3)
Radiobutton(frameTrece, text = "2", variable = opcionMelancolico, value = 2).grid(row = 2, column = 4)
Radiobutton(frameTrece, text = "3", variable = opcionMelancolico, value = 3).grid(row = 2, column = 5)
Radiobutton(frameTrece, text = "4", variable = opcionMelancolico, value = 4).grid(row = 2, column = 6)
Radiobutton(frameTrece, text = "5", variable = opcionMelancolico, value = 5).grid(row = 2, column = 7)
Radiobutton(frameTrece, text = "6", variable = opcionMelancolico, value = 6).grid(row = 2, column = 8)
Radiobutton(frameTrece, text = "7", variable = opcionMelancolico, value = 7).grid(row = 2, column = 9)
Radiobutton(frameTrece, text = "8", variable = opcionMelancolico, value = 8).grid(row = 2, column = 10)
Radiobutton(frameTrece, text = "9", variable = opcionMelancolico, value = 9).grid(row = 2, column = 11)
Radiobutton(frameTrece, text = "10", variable = opcionMelancolico, value = 10).grid(row = 2, column = 12)
Label(frameTrece, text = "Me siento melancolico").grid(row = 1, column = 7)
Button(frameTrece, text='Continuar', command=lambda:raise_Frame(frameCatorce)).grid(row = 3, column = 13)

#Insertar imágenes
imagen14 = PhotoImage(file = "cerebro.png")
imagenDos14 = PhotoImage(file = "Flecha.png")
Label(frameCatorce, image = imagen14).grid(row = 1, column = 1)
Label(frameCatorce, image = imagenDos14).grid(row = 3, column =13)

#Frame pregunta intranquilo

opcionIntranquilo = IntVar()

Radiobutton(frameCatorce, text = "0", variable = opcionIntranquilo, value = 0).grid(row = 2, column = 2)
Radiobutton(frameCatorce, text = "1", variable = opcionIntranquilo, value = 1).grid(row = 2, column = 3)
Radiobutton(frameCatorce, text = "2", variable = opcionIntranquilo, value = 2).grid(row = 2, column = 4)
Radiobutton(frameCatorce, text = "3", variable = opcionIntranquilo, value = 3).grid(row = 2, column = 5)
Radiobutton(frameCatorce, text = "4", variable = opcionIntranquilo, value = 4).grid(row = 2, column = 6)
Radiobutton(frameCatorce, text = "5", variable = opcionIntranquilo, value = 5).grid(row = 2, column = 7)
Radiobutton(frameCatorce, text = "6", variable = opcionIntranquilo, value = 6).grid(row = 2, column = 8)
Radiobutton(frameCatorce, text = "7", variable = opcionIntranquilo, value = 7).grid(row = 2, column = 9)
Radiobutton(frameCatorce, text = "8", variable = opcionIntranquilo, value = 8).grid(row = 2, column = 10)
Radiobutton(frameCatorce, text = "9", variable = opcionIntranquilo, value = 9).grid(row = 2, column = 11)
Radiobutton(frameCatorce, text = "10", variable = opcionIntranquilo, value = 10).grid(row = 2, column = 12)
Label(frameCatorce, text = "Me siento intranquilo").grid(row = 1, column = 7)
Button(frameCatorce, text='Continuar', command=lambda:raise_Frame(frameQuince)).grid(row = 3, column = 13)

#Insertar imágenes
imagen15 = PhotoImage(file = "cerebro.png")
imagenDos15 = PhotoImage(file = "Flecha.png")
Label(frameQuince, image = imagen15).grid(row = 1, column = 1)
Label(frameQuince, image = imagenDos15).grid(row = 3, column =13)

#Frame pregunta enfadado

opcionEnfadado = IntVar()

Radiobutton(frameQuince, text = "0", variable = opcionEnfadado, value = 0).grid(row = 2, column = 2)
Radiobutton(frameQuince, text = "1", variable = opcionEnfadado, value = 1).grid(row = 2, column = 3)
Radiobutton(frameQuince, text = "2", variable = opcionEnfadado, value = 2).grid(row = 2, column = 4)
Radiobutton(frameQuince, text = "3", variable = opcionEnfadado, value = 3).grid(row = 2, column = 5)
Radiobutton(frameQuince, text = "4", variable = opcionEnfadado, value = 4).grid(row = 2, column = 6)
Radiobutton(frameQuince, text = "5", variable = opcionEnfadado, value = 5).grid(row = 2, column = 7)
Radiobutton(frameQuince, text = "6", variable = opcionEnfadado, value = 6).grid(row = 2, column = 8)
Radiobutton(frameQuince, text = "7", variable = opcionEnfadado, value = 7).grid(row = 2, column = 9)
Radiobutton(frameQuince, text = "8", variable = opcionEnfadado, value = 8).grid(row = 2, column = 10)
Radiobutton(frameQuince, text = "9", variable = opcionEnfadado, value = 9).grid(row = 2, column = 11)
Radiobutton(frameQuince, text = "10", variable = opcionEnfadado, value = 10).grid(row = 2, column = 12)
Label(frameQuince, text = "Me siento enfadado").grid(row = 1, column = 7)
Button(frameQuince, text='Continuar', command=lambda:raise_Frame(frameDiesciseis)).grid(row = 3, column = 13)

#Insertar imágenes
imagen16 = PhotoImage(file = "cerebro.png")
imagenDos16 = PhotoImage(file = "Flecha.png")
Label(frameDiesciseis, image = imagen16).grid(row = 1, column = 1)
Label(frameDiesciseis, image = imagenDos16).grid(row = 3, column =13)

#Frame pregunta contento

opcionContento = IntVar()

Radiobutton(frameDiesciseis, text = "0", variable = opcionContento, value = 0).grid(row = 2, column = 2)
Radiobutton(frameDiesciseis, text = "1", variable = opcionContento, value = 1).grid(row = 2, column = 3)
Radiobutton(frameDiesciseis, text = "2", variable = opcionContento, value = 2).grid(row = 2, column = 4)
Radiobutton(frameDiesciseis, text = "3", variable = opcionContento, value = 3).grid(row = 2, column = 5)
Radiobutton(frameDiesciseis, text = "4", variable = opcionContento, value = 4).grid(row = 2, column = 6)
Radiobutton(frameDiesciseis, text = "5", variable = opcionContento, value = 5).grid(row = 2, column = 7)
Radiobutton(frameDiesciseis, text = "6", variable = opcionContento, value = 6).grid(row = 2, column = 8)
Radiobutton(frameDiesciseis, text = "7", variable = opcionContento, value = 7).grid(row = 2, column = 9)
Radiobutton(frameDiesciseis, text = "8", variable = opcionContento, value = 8).grid(row = 2, column = 10)
Radiobutton(frameDiesciseis, text = "9", variable = opcionContento, value = 9).grid(row = 2, column = 11)
Radiobutton(frameDiesciseis, text = "10", variable = opcionContento, value = 10).grid(row = 2, column = 12)
Label(frameDiesciseis, text = "Me siento contento").grid(row = 1, column = 7)
Button(frameDiesciseis, text='Continuar', command=lambda:raise_Frame(frameResultados)).grid(row = 3, column = 13)


pD = StringVar()
pAn = StringVar()
pH = StringVar()
pAl = StringVar()
tendencia = StringVar()

Button(frameResultados, text = "Promedio depresivo", command = promediarDepresion).grid(row = 0, column = 0, padx = 50, pady = 20)
Entry(frameResultados, justify = "center", textvariable = pD, state = "disabled").grid(row = 1, column = 0, padx = 50, pady = 5)
Button(frameResultados, text = "Promedio ansioso", command = promediarAnsiedad).grid(row = 0, column = 1, padx = 50, pady = 20)
Entry(frameResultados, justify = "center", textvariable = pAn, state = "disabled").grid(row = 1, column = 1, padx = 50, pady = 5)
Button(frameResultados, text = "Promedio hostil", command = promediarHostilidad).grid(row = 0, column = 2, padx = 50, pady = 20)
Entry(frameResultados, justify = "center", textvariable = pH, state = "disabled").grid(row = 1, column = 2, padx = 50, pady = 5)
Button(frameResultados, text = "Promedio alegre", command = promediarAlegria).grid(row = 0, column = 3, padx = 50, pady = 20)
Entry(frameResultados, justify = "center", textvariable = pAl, state = "disabled").grid(row = 1, column = 3, padx = 50, pady = 5)
Button(frameResultados, text = "Conocer inclinación del estado de ánimo", command = inclinacion).grid(row = 2, column = 1, columnspan=2, rowspan=1, padx = 50, pady = 10)
Entry(frameResultados, justify = "center", textvariable = tendencia, state = "disabled").grid(row = 3, column = 1, columnspan=2, rowspan=2, padx = 50, pady = 5)
Button(frameResultados, text = "Salir", command =  salir).grid(row = 5, column = 1, columnspan=2, rowspan=2, padx = 50, pady = 5)

raise_Frame(frameUno)
root.mainloop()