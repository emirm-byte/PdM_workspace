# -*- coding: cp1252 -*-

# AUTOR: EMILIANO EDUARDO RODRIGUEZ

import serial
import time
import openpyxl
from openpyxl import Workbook
import serial.tools.list_ports
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from threading import Thread
import threading
import _thread
from pathlib import Path

ventana = Tk()
ventana.title('PRESSURE SENSOR MONITOR')

ancho=600
alto=670

ventana.minsize(width=ancho, height=alto)
ventana.maxsize(width=ancho, height=alto)
ventana.configure(background = "gray71")


##**************************SELECCION DE PUERTO*****************************##

hilos=list()
ports = list(serial.tools.list_ports.comports())
puertos = list()
puertos.append("Seleccione Puerto UART")
conectado=0

for p in ports:
    port1=str(p)
    puertos.append(port1)


selec_puerto = ttk.Combobox(values=puertos, style='My.TCombobox', state="readonly")
selec_puerto.set("Seleccione Puerto UART")
selec_puerto.configure(width=35)
selec_puerto.grid(row=1,column=1,columnspan=1,rowspan=1,sticky=N+S,padx=10,pady=15)


def conectar_puerto():
    global conectado
    global puerto_damper
    
    puerto_amortiguador = selec_puerto.get()[:5]
    if puerto_amortiguador != "Selec":
        canvas.delete("all")
        ejes()
        if conectado == 0:
            puerto_damper = serial.Serial(puerto_amortiguador, 57600, timeout=0)
            boton_conectar.configure(text="Desconectar")
            conectado = 1
            thread1 = Thread(target=leer_damper)
            hilos.append(thread1)
            thread1.start()
        else:        
            boton_conectar.configure(text="Conectar")
            conectado = 0
            _thread.exit
            puerto_damper.close()
    else:
        canvas.create_text(135,15,fill="red", font="Times 15 italic bold",text="Seleccione Puerto del Sensor")


registrando = 0

def iniciar_registro():
    global ruta_registro
    global registrando
    global conectado
    
    file = filedialog.asksaveasfilename(initialdir='C:\\',title="seleccionar archivo",filetypes = (("Excel Files","*.xlsx"),("All files","*.*")))
    if len(file)==0:
        registrando = 0
    else:
        ruta_registro = Path(file + ".xlsx")
        if conectado == 1:
            label_info.configure(text="ESTADO: REGISTRANDO DATOS")
            registrando = 1
        else:
            label_info.configure(text="ESTADO: SENSOR DESCONECTADO - CONECTE EL PUERTO")
            registrando = 0


def detener_registro():
    global registrando
    global ruta_registro
    global cont
    
    registrando = 0
    label_info.configure(text="ESTADO: NO REGISTRANDO")
    cont=0
    wb.save(ruta_registro)


def ejes():
    canvas.create_line(0,alto_canvas,ancho_canvas,alto_canvas, fill="black")
    canvas.create_line(0,alto_canvas-50,ancho_canvas,alto_canvas-50, fill="black")
    canvas.create_line(0,alto_canvas-100,ancho_canvas,alto_canvas-100, fill="black")
    canvas.create_line(0,alto_canvas-150,ancho_canvas,alto_canvas-150, fill="black")
    canvas.create_line(0,alto_canvas-200,ancho_canvas,alto_canvas-200, fill="black")
    canvas.create_line(0,alto_canvas-250,ancho_canvas,alto_canvas-250, fill="black")
    canvas.create_line(0,alto_canvas-298,ancho_canvas,alto_canvas-298, fill="black")

    canvas.create_line(33,0,33,alto_canvas, fill="black")

    xtexto=16

    canvas.create_text(xtexto,alto_canvas-10,fill="black",font="Arial 9 italic bold", text="0 Hz")
    canvas.create_text(xtexto,alto_canvas-10-50,fill="black",font="Arial 9 italic bold", text="10 Hz")
    canvas.create_text(xtexto,alto_canvas-10-100,fill="black",font="Arial 9 italic bold", text="20 Hz")
    canvas.create_text(xtexto,alto_canvas-10-150,fill="black",font="Arial 9 italic bold", text="30 Hz")
    canvas.create_text(xtexto,alto_canvas-10-200,fill="black",font="Arial 9 italic bold", text="40 Hz")
    canvas.create_text(xtexto,alto_canvas-10-250,fill="black",font="Arial 9 italic bold", text="50 Hz")
    

boton_conectar = Button(ventana, text="Conectar",width=15,height=1,command=conectar_puerto)
boton_conectar.grid(row=1,column=2,columnspan=1,rowspan=1,sticky=N+S,padx=10,pady=15)

boton_directorio_registro = Button(ventana, text="Iniciar Registro",width=15,height=1,command=iniciar_registro, bg="sea green")
boton_directorio_registro.grid(row=2,column=1,columnspan=1,rowspan=1,sticky=N+S,padx=10,pady=15)

boton_detener_registro = Button(ventana, text="Detener Registro",width=15,height=1,command=detener_registro,bg="red")
boton_detener_registro.grid(row=2,column=2,columnspan=1,rowspan=1,sticky=W+N+S,padx=10,pady=15)

label_info=Label(ventana,text="ESTADO: NO REGISTRANDO",font=("Helvetica", 12),bg="gray71",fg="blue")
label_info.grid(row=3,column=1,columnspan=1, rowspan=1,sticky=W, padx=10,pady=5)

label_frecuencia=Label(ventana,text="FRECUENCIA = 0",font=("Helvetica", 15),bg="gray71")
label_frecuencia.grid(row=4,column=1,columnspan=2, rowspan=1,sticky=W, padx=10,pady=5)

ancho_canvas = 580
alto_canvas = 300

canvas = Canvas(width=ancho_canvas,height=alto_canvas,bg="white")
canvas.grid(row=5,column=1,columnspan=2,sticky=W,padx=10,pady=5)

ejes()

label_frec1=Label(ventana,text="F1 = 0",font=("Helvetica", 12),bg="gray71")
label_frec1.grid(row=6,column=1,columnspan=2, rowspan=1,sticky=W, padx=10,pady=5)

label_frec2=Label(ventana,text="F2 = 0",font=("Helvetica", 12),bg="gray71")
label_frec2.grid(row=7,column=1,columnspan=2, rowspan=1,sticky=W, padx=10,pady=5)

label_frec3=Label(ventana,text="F3 = 0",font=("Helvetica", 12),bg="gray71")
label_frec3.grid(row=8,column=1,columnspan=2, rowspan=1,sticky=W, padx=10,pady=5)

label_frec4=Label(ventana,text="F4 = 0",font=("Helvetica", 12),bg="gray71")
label_frec4.grid(row=9,column=1,columnspan=2, rowspan=1,sticky=W, padx=10,pady=5)

label_frec5=Label(ventana,text="F5 = 0",font=("Helvetica", 12),bg="gray71")
label_frec5.grid(row=10,column=1,columnspan=2, rowspan=1,sticky=W, padx=10,pady=5)

label_frec6=Label(ventana,text="F6 = 0",font=("Helvetica", 12),bg="gray71")
label_frec6.grid(row=6,column=2,columnspan=2, rowspan=1,sticky=W, padx=10,pady=5)

label_frec7=Label(ventana,text="F7 = 0",font=("Helvetica", 12),bg="gray71")
label_frec7.grid(row=7,column=2,columnspan=2, rowspan=1,sticky=W, padx=10,pady=5)

label_frec8=Label(ventana,text="F8 = 0",font=("Helvetica", 12),bg="gray71")
label_frec8.grid(row=8,column=2,columnspan=2, rowspan=1,sticky=W, padx=10,pady=5)

label_frec9=Label(ventana,text="F9 = 0",font=("Helvetica", 12),bg="gray71")
label_frec9.grid(row=9,column=2,columnspan=2, rowspan=1,sticky=W, padx=10,pady=5)

label_frec10=Label(ventana,text="F10 = 0",font=("Helvetica", 12),bg="gray71")
label_frec10.grid(row=10,column=2,columnspan=2, rowspan=1,sticky=W, padx=10,pady=5)

##*************************************************************************##

cont=0
wb = Workbook()
planilla=wb.active

planilla['A1'].value = "MUESTRA"
#planilla['A1'].font = planilla['A1'].font.copy(bold=True)
planilla['B1'].value = "FRECUENCIA DAMPER"
#planilla['B1'].font = planilla['B1'].font.copy(bold=True)


def leer_damper():
    global freq_damper
    global cont
    global puerto_damper
    global registrando

    escala = -5
    eje = alto_canvas

    cont_grafico = 33
    muestras=list()
    for i in range(0,580):
        muestras.append(0)

    
    if conectado == 1:
        puerto_damper.flushInput()                 #borra el buffer de entrada del puerto del tramimetro ego
        puerto_damper.flushOutput()
        
        while conectado:

            trama = puerto_damper.readline()
            trama = trama.decode("utf-8")

            if trama.split('=')[0]=='frec':
                freq_damper = int(trama.split('=')[1])
            
                if registrando == 1:
                    planilla['A'+str(cont+2)].value = (cont+1)
                    planilla['B'+str(cont+2)].value = float(freq_damper)
                    cont=cont+1
                label_frecuencia.config(text="FRECUENCIA = "+str(float(freq_damper)))
                muestras.insert(cont_grafico,(int(float(freq_damper))))
                
                if cont_grafico >=1:
                    canvas.create_line((cont_grafico-1),(escala*muestras[cont_grafico-1])+eje,cont_grafico,(escala*muestras[cont_grafico])+eje,fill="blue")

                cont_grafico = cont_grafico+1

                if cont_grafico >=580:
                    canvas.delete("all")
                    ejes()
                    cont_grafico = 33

            elif trama.split('=')[0]=='store':
                print("PROCESO DE STORE: "+trama.split('=')[1])






ventana.mainloop()


        
