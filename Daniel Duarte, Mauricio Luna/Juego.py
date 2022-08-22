import tkinter as tk
from tkinter import *
import os
import time
import random
import pygame
from PIL import ImageTk, Image
from threading import Thread
#Variables globales------------------------------------------------------------------------------------------------------------------------------------------------------------
global matriz1 #variable global para guardar los cambios de la matriz del jugador
global matriz2# variable global para guardar los cambios de la matriz del rival
global matriz_pos#variable global en donde se guarda únicamente las posiciones de los barcos del jugador
global matriz_pos_rival#variable global en donde se guarda únicamente las posiciones de los barcos del rival
global hora #variable global en la cual se actualiza las horas del cronómetro de la partida
global segundo#variable global en la cual se actualiza los segundos del cronómetro de la partida
global minuto#variable global en la cual se actualiza los segundos del cronómetro de la partida
global turnos#variable global que sirve para llevar la cuenta de la cantidad de turnos usados por el jugador
global nuf#variable global que guarda el valor obtenido en el entry de la fila del jugador
global nuc#variable global que guarda el valor obtenido en el entry de la columna del jugador
global barcos_selecc#variable global en la que se guarda la cantidad de coordenadas que ha seleccionado el jugador parar sus barcos
global barcos_selecc_m #variable global en la que se guarda la cantidad de coordenadas que ha seleccionado el rival parar sus barcos
global nuft#variable global temporal que guarda el valor de la variable nuf para que de esta manera las coordenadas seleccionadas no se encuentren dispersas en la matriz
global nuct#variable global temporal que guarda el valor de la variable nuc para que de esta manera las coordenadas seleccionadas no se encuentren dispersas en la matriz
global cuadroc #variable global temporal que guarda el valor de la variable nuft para que de esta manera las coordenadas seleccionadas no se encuentren dispersas en la matriz
global cuadrof#variable global temporal que guarda el valor de la variable nuct para que de esta manera las coordenadas seleccionadas no se encuentren dispersas en la matriz
global barco_riv #variable global que lleva la cuenta de cuantas coordenadas faltan por encontrar de la matriz del rival
global turno#variable global que permite que el jugador y el rival ataquen pero no simultaneamente
global barco_jug #variable global que lleva la cuenta de cuantas coordenadas faltan por encontrar de la matriz del jugador
global corre_tiempo#Dependiendo del valor que tenga esta variable global el cronómetro va a correr o se queda pausado
global lista_glob#Esta es una variable global que sirve como lista para guardar las variables globales que nos sirven para guardar partida.
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

matriz_pos_rival = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
matriz_pos = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
matriz1=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
matriz2=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
hora = 0
segundo = 0
minuto = 0
turnos = 0
barcos_jugador = 3
barcos_rival = 3
nuf = None
nuc= None
barcos_selecc=1
barcos_selecc_m=1
nuft = 0
nuct = 0
cuadroc = 0
cuadrof = 0
barco_riv = 6
turno = True
barco_jug = 6
corre_tiempo = None
lista_glob = []




#Clase para el splash animado
class splash:
    def __init__(self):
        #Parámetros ventana del splash animado
        self.splash_animado= Tk()
        self.splash_animado.title("Battle Ship")
        self.splash_animado.geometry("1000x700")
        self.splash_animado.resizable(False,False)

        #Creación y ublicación del canvas del splash
        self.canvas= Canvas(self.splash_animado, width =1000 , height = 700, bg = "#000000")
        self.canvas.place(x=0,y=0)
        #imagen del escenario
        self.imagen_es = Image.open("imagenes\Foni.png")
        self.imagen_es= self.imagen_es.resize((1000,700), Image.ANTIALIAS)
        self.img_es=ImageTk.PhotoImage(self.imagen_es)
        self.canvas.create_image(0,0, image=self.img_es,anchor="nw")
        #imagen del logo
        self.imagen_logo = Image.open("imagenes\Logo.png")
        self.imagen_logo = self.imagen_logo.resize((300, 210), Image.ANTIALIAS)
        self.img_logo = ImageTk.PhotoImage(self.imagen_logo)
        self.canvas.create_image(400, 100, image=self.img_logo, anchor="nw")

        #imagen 1 explosión_gif1
        self.expo1 = Image.open("imagenes\explosiones\Expo1.png")
        self.expo1 = self.expo1.resize((110, 110), Image.ANTIALIAS)
        self.img_expo1 = ImageTk.PhotoImage(self.expo1)
        self.img_expos1 =self.canvas.create_image(800, 450, image=self.img_expo1, anchor="nw")
        #imagen 2 explosión_gif1
        self.expo2 = Image.open("imagenes\explosiones\Expo2.png")
        self.expo2 = self.expo2.resize((110, 110), Image.ANTIALIAS)
        self.img_expo2 = ImageTk.PhotoImage(self.expo2)
        # imagen 3 explosión_gif1
        self.expo3= Image.open("imagenes\explosiones\Expo3.png")
        self.expo3 = self.expo3.resize((110, 110), Image.ANTIALIAS)
        self.img_expo3 = ImageTk.PhotoImage(self.expo3)
        # imagen 4 explosión_gif1
        self.expo4 = Image.open("imagenes\explosiones\Expo4.png")
        self.expo4 = self.expo4.resize((110, 110), Image.ANTIALIAS)
        self.img_expo4 = ImageTk.PhotoImage(self.expo4)
        # imagen 5 explosión_gif1
        self.expo5 = Image.open("imagenes\explosiones\Expo5.png")
        self.expo5 = self.expo5.resize((110, 110), Image.ANTIALIAS)
        self.img_expo5 = ImageTk.PhotoImage(self.expo5)
        # imagen 6 explosión_gif1
        self.expo6 = Image.open("imagenes\explosiones\Expo6.png")
        self.expo6 = self.expo6.resize((110, 110), Image.ANTIALIAS)
        self.img_expo6 = ImageTk.PhotoImage(self.expo6)
        # imagen 7 explosión_gif1
        self.expo7 = Image.open("imagenes\explosiones\Expo7.png")
        self.expo7 = self.expo7.resize((110, 110), Image.ANTIALIAS)
        self.img_expo7 = ImageTk.PhotoImage(self.expo7)
        # imagen 8 explosión_gif1
        self.expo8 = Image.open("imagenes\explosiones\Expo8.png")
        self.expo8 = self.expo8.resize((110, 110), Image.ANTIALIAS)
        self.img_expo8 = ImageTk.PhotoImage(self.expo8)
        # imagen 9 explosión_gif1
        self.expo9 = Image.open("imagenes\explosiones\Expo9.png")
        self.expo9 = self.expo9.resize((110, 110), Image.ANTIALIAS)
        self.img_expo9 = ImageTk.PhotoImage(self.expo9)

        # imagen 1 explosión_gif2
        self.expo1_g2 = Image.open("imagenes\explosiones\Expo1.png")
        self.expo1_g2 = self.expo1_g2.resize((90, 90), Image.ANTIALIAS)
        self.img_expo1_g2 = ImageTk.PhotoImage(self.expo1_g2)
        self.img_expos1_g2 = self.canvas.create_image(610, 400, image=self.img_expo1_g2, anchor="nw")
        # imagen 2 explosión_gif2
        self.expo2_g2 = Image.open("imagenes\explosiones\Expo2.png")
        self.expo2_g2 = self.expo2_g2.resize((90, 90), Image.ANTIALIAS)
        self.img_expo2_g2 = ImageTk.PhotoImage(self.expo2_g2)
        # imagen 3 explosión_gif2
        self.expo3_g2 = Image.open("imagenes\explosiones\Expo3.png")
        self.expo3_g2 = self.expo3_g2.resize((90, 90), Image.ANTIALIAS)
        self.img_expo3_g2 = ImageTk.PhotoImage(self.expo3_g2)
        # imagen 4 explosión_gif2
        self.expo4_g2 = Image.open("imagenes\explosiones\Expo4.png")
        self.expo4_g2 = self.expo4_g2.resize((90, 90), Image.ANTIALIAS)
        self.img_expo4_g2 = ImageTk.PhotoImage(self.expo4_g2)
        # imagen 5 explosión_gif2
        self.expo5_g2 = Image.open("imagenes\explosiones\Expo5.png")
        self.expo5_g2 = self.expo5_g2.resize((90, 90), Image.ANTIALIAS)
        self.img_expo5_g2 = ImageTk.PhotoImage(self.expo5_g2)
        # imagen 6 explosión_gif2
        self.expo6_g2 = Image.open("imagenes\explosiones\Expo6.png")
        self.expo6_g2 = self.expo6_g2.resize((90, 90), Image.ANTIALIAS)
        self.img_expo6_g2 = ImageTk.PhotoImage(self.expo6_g2)
        # imagen 7 explosión_gif2
        self.expo7_g2 = Image.open("imagenes\explosiones\Expo7.png")
        self.expo7_g2 = self.expo7_g2.resize((90, 90), Image.ANTIALIAS)
        self.img_expo7_g2 = ImageTk.PhotoImage(self.expo7_g2)
        # imagen 8 explosión_gif2
        self.expo8_g2 = Image.open("imagenes\explosiones\Expo8.png")
        self.expo8_g2 = self.expo8_g2.resize((90, 90), Image.ANTIALIAS)
        self.img_expo8_g2 = ImageTk.PhotoImage(self.expo8_g2)
        # imagen 9 explosión_gif2
        self.expo9_g2 = Image.open("imagenes\explosiones\Expo9.png")
        self.expo9_g2 = self.expo9_g2.resize((90, 90), Image.ANTIALIAS)
        self.img_expo9_g2 = ImageTk.PhotoImage(self.expo9_g2)

        # imagen 1 explosión_gif3
        self.expo1_g3 = Image.open("imagenes\explosiones\Expo1.png")
        self.expo1_g3 = self.expo1_g3.resize((70, 70), Image.ANTIALIAS)
        self.img_expo1_g3 = ImageTk.PhotoImage(self.expo1_g3)

        # imagen 2 explosión_gif3
        self.expo2_g3 = Image.open("imagenes\explosiones\Expo2.png")
        self.expo2_g3 = self.expo2_g3.resize((70, 70), Image.ANTIALIAS)
        self.img_expo2_g3 = ImageTk.PhotoImage(self.expo2_g3)
        # imagen 3 explosión_gif3
        self.expo3_g3 = Image.open("imagenes\explosiones\Expo3.png")
        self.expo3_g3 = self.expo3_g3.resize((70, 70), Image.ANTIALIAS)
        self.img_expo3_g3 = ImageTk.PhotoImage(self.expo3_g3)
        # imagen 4 explosión_gif3
        self.expo4_g3 = Image.open("imagenes\explosiones\Expo4.png")
        self.expo4_g3 = self.expo4_g3.resize((70, 70), Image.ANTIALIAS)
        self.img_expo4_g3 = ImageTk.PhotoImage(self.expo4_g3)
        # imagen 5 explosión_gif3
        self.expo5_g3 = Image.open("imagenes\explosiones\Expo5.png")
        self.expo5_g3 = self.expo5_g3.resize((70, 70), Image.ANTIALIAS)
        self.img_expo5_g3 = ImageTk.PhotoImage(self.expo5_g3)
        # imagen 6 explosión_gif3
        self.expo6_g3 = Image.open("imagenes\explosiones\Expo6.png")
        self.expo6_g3 = self.expo6_g3.resize((70, 70), Image.ANTIALIAS)
        self.img_expo6_g3 = ImageTk.PhotoImage(self.expo6_g3)
        # imagen 7 explosión_gif3
        self.expo7_g3 = Image.open("imagenes\explosiones\Expo7.png")
        self.expo7_g3 = self.expo7_g3.resize((70, 70), Image.ANTIALIAS)
        self.img_expo7_g3 = ImageTk.PhotoImage(self.expo7_g3)
        # imagen 8 explosión_gif3
        self.expo8_g3 = Image.open("imagenes\explosiones\Expo8.png")
        self.expo8_g3 = self.expo8_g3.resize((70, 70), Image.ANTIALIAS)
        self.img_expo8_g3 = ImageTk.PhotoImage(self.expo8_g3)
        # imagen 9 explosión_gif3
        self.expo9_g3 = Image.open("imagenes\explosiones\Expo9.png")
        self.expo9_g3 = self.expo9_g3.resize((70, 70), Image.ANTIALIAS)
        self.img_expo9_g3 = ImageTk.PhotoImage(self.expo9_g3)

        # primera parte título
        self.imagen_ti1 = Image.open("imagenes\Ti 1.png")
        self.imagen_ti1 = self.imagen_ti1.resize((200, 105), Image.ANTIALIAS)
        self.img_ti1 = ImageTk.PhotoImage(self.imagen_ti1)
        self.canvas.create_image(70, 420, image=self.img_ti1, anchor="nw")

        #segunda parte título
        self.imagen_ti2 = Image.open("imagenes\Ti 2.png")
        self.imagen_ti2 = self.imagen_ti2.resize((200, 60), Image.ANTIALIAS)
        self.img_ti2 = ImageTk.PhotoImage(self.imagen_ti2)
        self.canvas.create_image(70, 530, image=self.img_ti2, anchor="nw")


        #tercera parte título
        self.imagen_ti3 = Image.open("imagenes\Ti 3.png")
        self.imagen_ti3 = self.imagen_ti3.resize((200, 100), Image.ANTIALIAS)
        self.img_ti3 = ImageTk.PhotoImage(self.imagen_ti3)
        self.canvas.create_image(70,590, image=self.img_ti3, anchor="nw")

        self.splash_animado.after(1000, self.play_p1)
        self.gif_expo()
        self.gif2_expo()
        self.gif3_expo()
        self.splash_animado.after(6000, self.start_ventana_menu)
        self.splash_animado.mainloop()

    """
    self.play_p1:Método que agrega sonido al splash
    E:Llamada del self.gif_expo()
    S:Reproducción del audio guerra-civil.mp3
    """

    def play_p1(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Sonidos\guerra-civil.mp3")
        pygame.mixer.music.play(loops=0)

    """
    self.expo_1: método que crea la imagen 1 del gif1
    E:Llamada del self.gif_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_1(self):
        self.img_expo1 = ImageTk.PhotoImage(self.expo1)
        self.img_expos1 = self.canvas.create_image(800, 450, image=self.img_expo1, anchor="nw")

    """
    self.expo_2: método que crea la imagen 2 del gif1
    E:Llamada del self.gif_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_2(self):
        self.img_expo2 = ImageTk.PhotoImage(self.expo2)
        self.img_expos2=self.canvas.create_image(800, 450, image=self.img_expo2, anchor="nw")

    """
    self.expo_3: método que crea la imagen 3 del gif1
    E:Llamada del self.gif_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_3(self):
        self.img_expo3 = ImageTk.PhotoImage(self.expo3)
        self.img_expos3=self.canvas.create_image(800, 450, image=self.img_expo3, anchor="nw")

    """
    self.expo_4: método que crea la imagen 4 del gif1
    E:Llamada del self.gif_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_4(self):
        self.img_expo4 = ImageTk.PhotoImage(self.expo4)
        self.img_expos4=self.canvas.create_image(800, 450, image=self.img_expo4, anchor="nw")

    """
    self.expo_5: método que crea la imagen 5 del gif1
    E:Llamada del self.gif_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_5(self):
        self.img_expo5 = ImageTk.PhotoImage(self.expo5)
        self.img_expos5 = self.canvas.create_image(800, 450, image=self.img_expo5, anchor="nw")
    """
    self.expo_6: método que crea la imagen 6 del gif1
    E:Llamada del self.gif_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_6(self):
        self.img_expo6 = ImageTk.PhotoImage(self.expo6)
        self.img_expos6 = self.canvas.create_image(800, 450, image=self.img_expo6, anchor="nw")
    """
    self.expo_7: método que crea la imagen 7 del gif1
    E:Llamada del self.gif_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_7(self):
        self.img_expo7 = ImageTk.PhotoImage(self.expo7)
        self.img_expos7 = self.canvas.create_image(800, 450, image=self.img_expo7, anchor="nw")
    """
    self.expo_8: método que crea la imagen 8 del gif1
    E:Llamada del self.gif_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_8(self):
        self.img_expo8 = ImageTk.PhotoImage(self.expo8)
        self.img_expos8 = self.canvas.create_image(800, 450, image=self.img_expo8, anchor="nw")
    """
    self.expo_9: método que crea la imagen 9 del gif1
    E:Llamada del self.gif_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_9(self):
        self.img_expo9 = ImageTk.PhotoImage(self.expo9)
        self.img_expos9 = self.canvas.create_image(800, 450, image=self.img_expo9, anchor="nw")

    #Funciones que hacen aparecer imágenes en el segundo gif
    """
    self.expo_1_g2: método que crea la imagen 1 del gif 2
    E:Llamada del self.gif2_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_1_g2(self):
        self.img_expo1_g2 = ImageTk.PhotoImage(self.expo1_g2)
        self.img_expos1_g2 = self.canvas.create_image(610, 400, image=self.img_expo1_g2, anchor="nw")
    """
    self.expo_2_g2: método que crea la imagen 2 del gif 2
    E:Llamada del self.gif2_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_2_g2(self):
        self.img_expo2_g2 = ImageTk.PhotoImage(self.expo2_g2)
        self.img_expos2_g2=self.canvas.create_image(610, 400, image=self.img_expo2_g2, anchor="nw")
    """
    self.expo_3_g2: método que crea la imagen 3 del gif 2
    E:Llamada del self.gif2_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_3_g2(self):
        self.img_expo3_g2 = ImageTk.PhotoImage(self.expo3_g2)
        self.img_expos3_g2=self.canvas.create_image(610, 400, image=self.img_expo3_g2, anchor="nw")
    """
    self.expo_4_g2: método que crea la imagen 4 del gif 2
    E:Llamada del self.gif2_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_4_g2(self):
        self.img_expo4_g2 = ImageTk.PhotoImage(self.expo4_g2)
        self.img_expos4_g2=self.canvas.create_image(610, 400, image=self.img_expo4_g2, anchor="nw")
    """
    self.expo_5_g2: método que crea la imagen 5 del gif 2
    E:Llamada del self.gif2_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_5_g2(self):
        self.img_expo5_g2 = ImageTk.PhotoImage(self.expo5_g2)
        self.img_expos5_g2 = self.canvas.create_image(610, 400, image=self.img_expo5_g2, anchor="nw")
    """
    self.expo_6_g2: método que crea la imagen 6 del gif 2
    E:Llamada del self.gif2_expo()
    S:Creación de la imagen
    R=-
    """

    def expo_6_g2(self):
        self.img_expo6_g2 = ImageTk.PhotoImage(self.expo6_g2)
        self.img_expos6_g2 = self.canvas.create_image(610, 400, image=self.img_expo6_g2, anchor="nw")

    """
    self.expo_7_g2: método que crea la imagen 7 del gif 2
    E:Llamada del self.gif2_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_7_g2(self):
        self.img_expo7_g2 = ImageTk.PhotoImage(self.expo7_g2)
        self.img_expos7_g2 = self.canvas.create_image(610, 400, image=self.img_expo7_g2, anchor="nw")
    """
    self.expo_8_g2: método que crea la imagen 8 del gif 2
    E:Llamada del self.gif2_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_8_g2(self):
        self.img_expo8_g2 = ImageTk.PhotoImage(self.expo8_g2)
        self.img_expos8_g2 = self.canvas.create_image(610, 400, image=self.img_expo8_g2, anchor="nw")
    """
    self.expo_9_g2: método que crea la imagen 9 del gif 2
    E:Llamada del self.gif2_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_9_g2(self):
        self.img_expo9_g2 = ImageTk.PhotoImage(self.expo9_g2)
        self.img_expos9_g2 = self.canvas.create_image(610, 400, image=self.img_expo9_g2, anchor="nw")

    """
    self.expo_1_g3: método que crea la imagen 1 del gif 3
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_1_g3(self):
        self.img_expo1_g3 = ImageTk.PhotoImage(self.expo1_g3)
        self.img_expos1_g3 = self.canvas.create_image(400, 400, image=self.img_expo1_g3, anchor="nw")

    """
    self.expo_2_g3: método que crea la imagen 2 del gif 3
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_2_g3(self):
        self.img_expo2_g3 = ImageTk.PhotoImage(self.expo2_g3)
        self.img_expos2_g3=self.canvas.create_image(400, 400, image=self.img_expo2_g3, anchor="nw")
    """
    self.expo_3_g3: método que crea la imagen 3 del gif 3
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_3_g3(self):
        self.img_expo3_g3 = ImageTk.PhotoImage(self.expo3_g3)
        self.img_expos3_g3=self.canvas.create_image(400, 400, image=self.img_expo3_g3, anchor="nw")
    """
    self.expo_4_g3: método que crea la imagen 4 del gif 3
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_4_g3(self):
        self.img_expo4_g3 = ImageTk.PhotoImage(self.expo4_g3)
        self.img_expos4_g3=self.canvas.create_image(400, 400, image=self.img_expo4_g3, anchor="nw")
    """
    self.expo_5_g3: método que crea la imagen 5 del gif 3
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_5_g3(self):
        self.img_expo5_g3 = ImageTk.PhotoImage(self.expo5_g3)
        self.img_expos5_g3 = self.canvas.create_image(400, 400, image=self.img_expo5_g3, anchor="nw")
    """
    self.expo_6_g3: método que crea la imagen 6 del gif 3
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_6_g3(self):
        self.img_expo6_g3 = ImageTk.PhotoImage(self.expo6_g3)
        self.img_expos6_g3 = self.canvas.create_image(400, 400, image=self.img_expo6_g3, anchor="nw")

    """
    self.expo_7_g3: método que crea la imagen 7 del gif 3
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_7_g3(self):
        self.img_expo7_g3 = ImageTk.PhotoImage(self.expo7_g3)
        self.img_expos7_g3 = self.canvas.create_image(400, 400, image=self.img_expo7_g3, anchor="nw")
    """
    self.expo_8_g3: método que crea la imagen 8 del gif 3
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_8_g3(self):
        self.img_expo8_g3 = ImageTk.PhotoImage(self.expo8_g3)
        self.img_expos8_g3 = self.canvas.create_image(400, 400, image=self.img_expo8_g3, anchor="nw")
    """
    self.expo_9_g3: método que crea la imagen 9 del gif 3
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def expo_9_g3(self):
        self.img_expo9_g3 = ImageTk.PhotoImage(self.expo9_g3)
        self.img_expos9_g3 = self.canvas.create_image(400, 400, image=self.img_expo9_g3, anchor="nw")

    """
    self.el_expo_1: método que elimina la imagen 1 del gif 1
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_1(self):
        self.canvas.delete(self.img_expos1)

    """
    self.el_expo_2: método que elimina la imagen 2 del gif 1
    E:Llamada del self.gif_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_2(self):
        self.canvas.delete(self.img_expos2)
    """
    self.el_expo_3: método que elimina la imagen 3 del gif 1
    E:Llamada del self.gif_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_3(self):
        self.canvas.delete(self.img_expos3)
    """
    self.el_expo_4: método que elimina la imagen 4 del gif 1
    E:Llamada del self.gif_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_4(self):
        self.canvas.delete(self.img_expos4)
    """
    self.el_expo_5: método que elimina la imagen 5 del gif 1
    E:Llamada del self.gif_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_5(self):
        self.canvas.delete(self.img_expos5)
    """
    self.el_expo_6: método que elimina la imagen 6 del gif 1
    E:Llamada del self.gif_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_6(self):
        self.canvas.delete(self.img_expos6)
    """
    self.el_expo_7: método que elimina la imagen 7 del gif 1
    E:Llamada del self.gif_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_7(self):
        self.canvas.delete(self.img_expos7)
    """
    self.el_expo_8: método que elimina la imagen 8 del gif 1
    E:Llamada del self.gif_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_8(self):
        self.canvas.delete(self.img_expos8)
    """
    self.el_expo_9: método que elimina la imagen 9 del gif 1
    E:Llamada del self.gif_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_9(self):
        self.canvas.delete(self.img_expos9)

    """
    self.el_expo_1_g2: método que elimina la imagen 1 del gif 2
    E:Llamada del self.gif2_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_1_g2(self):
        self.canvas.delete(self.img_expos1_g2)
    """
    self.el_expo_2_g2: método que elimina la imagen 2 del gif 2
    E:Llamada del self.gif2_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_2_g2(self):
        self.canvas.delete(self.img_expos2_g2)
    """
    self.el_expo_3_g2: método que elimina la imagen 3 del gif 2
    E:Llamada del self.gif2_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_3_g2(self):
        self.canvas.delete(self.img_expos3_g2)
    """
    self.el_expo_4_g2: método que elimina la imagen 4 del gif 2
    E:Llamada del self.gif2_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_4_g2(self):
        self.canvas.delete(self.img_expos4_g2)
    """
    self.el_expo_5_g2: método que elimina la imagen 5 del gif 2
    E:Llamada del self.gif2_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_5_g2(self):
        self.canvas.delete(self.img_expos5_g2)
    """
    self.el_expo_6_g2: método que elimina la imagen 6 del gif 2
    E:Llamada del self.gif2_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_6_g2(self):
        self.canvas.delete(self.img_expos6_g2)
    """
    self.el_expo_7_g2: método que elimina la imagen 7 del gif 2
    E:Llamada del self.gif2_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_7_g2(self):
        self.canvas.delete(self.img_expos7_g2)
    """
    self.el_expo_8_g2: método que elimina la imagen 8 del gif 2
    E:Llamada del self.gif2_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_8_g2(self):
        self.canvas.delete(self.img_expos8_g2)
    """
    self.el_expo_9_g2: método que elimina la imagen 9 del gif 2
    E:Llamada del self.gif2_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_9_g2(self):
        self.canvas.delete(self.img_expos9_g2)

    """
    self.el_expo_1_g3: método que elimina la imagen 1 del gif 3
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_1_g3(self):
        self.canvas.delete(self.img_expos1_g3)
    """
    self.el_expo_2_g3: método que elimina la imagen 2 del gif 3
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_2_g3(self):
        self.canvas.delete(self.img_expos2_g3)
    """
    self.el_expo_3_g3: método que elimina la imagen 3 del gif 3
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_3_g3(self):
        self.canvas.delete(self.img_expos3_g3)
    """
    self.el_expo_4_g3: método que elimina la imagen 4 del gif 3
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_4_g3(self):
        self.canvas.delete(self.img_expos4_g3)
    """
    self.el_expo_5_g3: método que elimina la imagen 5 del gif 3
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_5_g3(self):
        self.canvas.delete(self.img_expos5_g3)
    """
    self.el_expo_6_g3: método que elimina la imagen 6 del gif 3
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_6_g3(self):
        self.canvas.delete(self.img_expos6_g3)
    """
    self.el_expo_7_g3: método que elimina la imagen 7 del gif 3
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_7_g3(self):
        self.canvas.delete(self.img_expos7_g3)
    """
    self.el_expo_8_g3: método que elimina la imagen 8 del gif 3
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_8_g3(self):
        self.canvas.delete(self.img_expos8_g3)
    """
    self.el_expo_9_g3: método que elimina la imagen 9 del gif 3
    E:Llamada del self.gif3_expo()
    S:Creación de la imagen
    R=-
    """
    def el_expo_9_g3(self):
        self.canvas.delete(self.img_expos9_g3)

    """
    self.gif_expo: Método que reproduce el primer gif llamando a otras funciones
    E: Llamada del init
    S:Reproducción del primer gif
    R:-
    """
    def gif_expo(self):
        self.expo_1()
        self.splash_animado.after(100, self.el_expo_1)
        self.splash_animado.after(100, self.expo_2)
        self.splash_animado.after(200, self.el_expo_2)
        self.splash_animado.after(200, self.expo_3)
        self.splash_animado.after(300, self.el_expo_3)
        self.splash_animado.after(300, self.expo_4)
        self.splash_animado.after(400, self.el_expo_4)
        self.splash_animado.after(400, self.expo_5)
        self.splash_animado.after(500, self.el_expo_5)
        self.splash_animado.after(500, self.expo_6)
        self.splash_animado.after(600, self.el_expo_6)
        self.splash_animado.after(600, self.expo_7)
        self.splash_animado.after(700, self.el_expo_7)
        self.splash_animado.after(700, self.expo_8)
        self.splash_animado.after(800, self.el_expo_8)
        self.splash_animado.after(800, self.expo_9)
        self.splash_animado.after(900, self.el_expo_9)

        self.splash_animado.after(1000, self.gif_expo)

    """
    selfgif2_expo: Método que reproduce el segundo gif llamando a otras funciones
    E: Llamada del init
    S:Reproducción del segundo gif
    R:-
    """
    def gif2_expo(self):
        self.expo_1()
        self.splash_animado.after(200, self.el_expo_1_g2)
        self.splash_animado.after(200, self.expo_2_g2)
        self.splash_animado.after(300, self.el_expo_2_g2)
        self.splash_animado.after(300, self.expo_3_g2)
        self.splash_animado.after(400, self.el_expo_3_g2)
        self.splash_animado.after(400, self.expo_4_g2)
        self.splash_animado.after(500, self.el_expo_4_g2)
        self.splash_animado.after(500, self.expo_5_g2)
        self.splash_animado.after(600, self.el_expo_5_g2)
        self.splash_animado.after(600, self.expo_6_g2)
        self.splash_animado.after(700, self.el_expo_6_g2)
        self.splash_animado.after(700, self.expo_7_g2)
        self.splash_animado.after(800, self.el_expo_7_g2)
        self.splash_animado.after(800, self.expo_8_g2)
        self.splash_animado.after(900, self.el_expo_8_g2)
        self.splash_animado.after(900, self.expo_9_g2)
        self.splash_animado.after(1000, self.el_expo_9_g2)

        self.splash_animado.after(1100, self.gif2_expo)

    """
    self.gif3_expo: Método que reproduce el tercer gif llamando a otras funciones
    E: Llamada del init
    S:Reproducción del tercer gif
    R:-
    """
    def gif3_expo(self):
        self.splash_animado.after(500,self.expo_1_g3)
        self.splash_animado.after(600, self.el_expo_1_g3)
        self.splash_animado.after(600, self.expo_2_g3)
        self.splash_animado.after(700, self.el_expo_2_g3)
        self.splash_animado.after(700, self.expo_3_g3)
        self.splash_animado.after(800, self.el_expo_3_g3)
        self.splash_animado.after(800, self.expo_4_g3)
        self.splash_animado.after(900, self.el_expo_4_g3)
        self.splash_animado.after(900, self.expo_5_g3)
        self.splash_animado.after(1000, self.el_expo_5_g3)
        self.splash_animado.after(1000, self.expo_6_g3)
        self.splash_animado.after(1100, self.el_expo_6_g3)
        self.splash_animado.after(1100, self.expo_7_g3)
        self.splash_animado.after(1200, self.el_expo_7_g3)
        self.splash_animado.after(1200, self.expo_8_g3)
        self.splash_animado.after(1300, self.el_expo_8_g3)
        self.splash_animado.after(1300, self.expo_9_g3)
        self.splash_animado.after(1400, self.el_expo_9_g3)

        self.splash_animado.after(1500, self.gif3_expo)

    """
    self.start_ventana_menu: Método que destruye la ventanta y llama a la clase menu
    E: Llamada por parte del init
    S: Destrucción splash animado y llamada a la clase menu
    R:-
    """
    def start_ventana_menu(self):
        self.splash_animado.destroy()
        menu()

#Clase del menú del juego
class menu:
    def __init__(self):
        # Parámetros ventana del menú
        self.ven_menu = Tk()
        self.ven_menu.title("Battle Ship")
        self.ven_menu.geometry("1000x650")
        self.ven_menu.resizable(False, False)

        # Creación y ublicación del canvas del splash
        self.canvas = Canvas(self.ven_menu, width=1000, height=650, bg="#000000")
        self.canvas.place(x=0, y=0)

        # imagen del escenario
        self.imagen_es = Image.open("imagenes\Fondo 2.png")
        self.imagen_es = self.imagen_es.resize((1000, 650), Image.ANTIALIAS)
        self.img_es = ImageTk.PhotoImage(self.imagen_es)
        self.canvas.create_image(0, 0, image=self.img_es, anchor="nw")
        #imagen del logo
        self.imagen_logo = Image.open("imagenes\Logo.png")
        self.imagen_logo = self.imagen_logo.resize((95, 70), Image.ANTIALIAS)
        self.img_logo = ImageTk.PhotoImage(self.imagen_logo)
        self.canvas.create_image(60, 50, image=self.img_logo, anchor="nw")

        # imagen del panel de botones
        self.panel = Image.open("imagenes\Panel.png")
        self.panel = self.panel.resize((380, 480), Image.ANTIALIAS)
        self.img_panel = ImageTk.PhotoImage(self.panel)
        self.canvas.create_image(640,80, image=self.img_panel, anchor="nw")

        # imagen botón de nueva partida
        self.nueva_p=Image.open("imagenes\Boton_nueva_p.png")
        self.nueva_p = self.nueva_p.resize((115, 70), Image.ANTIALIAS)
        self.img_nueva_p = ImageTk.PhotoImage(self.nueva_p)

        # imagen botón de cargar partida
        self.cargar_p = Image.open("imagenes\Boton_cargar_p.png")
        self.cargar_p = self.cargar_p.resize((115, 70), Image.ANTIALIAS)
        self.img_cargar_p = ImageTk.PhotoImage(self.cargar_p)

        # imagen botón de salón
        self.salon = Image.open("imagenes\Boton_salon.png")
        self.salon = self.salon.resize((115, 70), Image.ANTIALIAS)
        self.img_salon = ImageTk.PhotoImage(self.salon)

        # imagen botón de ayuda
        self.ayuda = Image.open("imagenes\Boton_ayuda.png")
        self.ayuda = self.ayuda.resize((115, 70), Image.ANTIALIAS)
        self.img_ayuda = ImageTk.PhotoImage(self.ayuda)

        #botón nueva partida
        self.btn_n_p= Button(self.ven_menu,image= self.img_nueva_p, borderwidth=0, command= self.nueva_partida)
        self.btn_n_p.place(x=765, y=230)

        #botón cargar partida
        self.btn_n_c = Button(self.ven_menu, image=self.img_cargar_p, borderwidth=0, command= self.cargar_partida)
        self.btn_n_c.place(x=765, y=300)

        #botón salon de fama
        self.btn_salon = Button(self.ven_menu, image=self.img_salon, borderwidth=0, command= self.salon_fama)
        self.btn_salon.place(x=765, y=370)

        #botón ayuda
        self.btn_ayuda = Button(self.ven_menu, image=self.img_ayuda, borderwidth=0,command= self.ayuda_i)
        self.btn_ayuda.place(x=765, y=440)


        self.ven_menu.mainloop()

    """
    self.cargar_partida: Método que llama la ventana de partida cargada y destruye la de menú
    E:Llamada del self.btn_n_c
    R:-
    S:Llamada a la clase Partida_guardada y destrucción de la ventana menú
    """
    def cargar_partida(self):
        self.ven_menu.destroy()
        Partida_cargada()

    """
    self.nueva_partida: Método que llama la ventana de nueva partida y destruye la de menú
    E:Llamada del self.btn_n_p
    R:-
    S:Llamada a la clase Game y destrucción de la ventana menú
    """
    def nueva_partida(self):
        self.ven_menu.destroy()
        Game()

    """
    self.nueva_partida: Método que llama la ventana de Salon y destruye la de menú
    E:Llamada del self.btn_salon
    R:-
    S:Llamada a la clase Salon y destrucción de la ventana menú
    """
    def salon_fama(self):
        self.ven_menu.destroy()
        Salon()
    def ayuda_i(self):
        self.ven_menu.destroy()
        Ven_ayuda1()


# Clase del salon de la fama
class Salon:
    def __init__(self):
        #Parámetros para la ventana del salon
        self.salon_window = Tk()
        self.salon_window.title("Battle Ship")
        self.salon_window.geometry("1000x700")
        self.salon_window.resizable(False, False)
        #Canvas de la ventana
        self.salon_canva = Canvas(self.salon_window, width=1000, height=700, bg="#6E1DF1")
        self.salon_canva.pack()
        #Label para el título de la ventana
        self.title_label = Label(self.salon_window, text= "Salon de la Fama",font= ("Arial", 50), bg = "#6E1DF1")
        self.title_label.place(x= 250, y= 20)
        #Label Nombre
        self.nombre_label = Label(self.salon_window, text= "Nombre",font= ("Arial", 30), bg = "#6E1DF1")
        self.nombre_label.place(x= 200, y= 150)
        # Label Tiempo
        self.tiempo_label = Label(self.salon_window, text= "Tiempo",font= ("Arial", 30), bg = "#6E1DF1")
        self.tiempo_label.place(x= 650, y= 150)

        # Labels para el nombre y tiempo de los jugadores
        self.nombre1_label = Label(self.salon_window, text= "",font= ("Arial", 30), bg = "#6E1DF1")
        self.nombre1_label.place(x= 200, y= 210)

        self.tiempo1_label = Label(self.salon_window, text= "",font= ("Arial", 30), bg = "#6E1DF1")
        self.tiempo1_label.place(x= 650, y= 210)

        self.nombre2_label = Label(self.salon_window, text= "",font= ("Arial", 30), bg = "#6E1DF1")
        self.nombre2_label.place(x= 200, y= 270)

        self.tiempo2_label = Label(self.salon_window, text= "",font= ("Arial", 30), bg = "#6E1DF1")
        self.tiempo2_label.place(x= 650, y= 270)

        self.nombre3_label = Label(self.salon_window, text= "",font= ("Arial", 30), bg = "#6E1DF1")
        self.nombre3_label.place(x= 200, y= 330)

        self.tiempo3_label = Label(self.salon_window, text= "",font= ("Arial", 30), bg = "#6E1DF1")
        self.tiempo3_label.place(x= 650, y= 330)

        self.nombre4_label = Label(self.salon_window, text= "",font= ("Arial", 30), bg = "#6E1DF1")
        self.nombre4_label.place(x= 200, y= 390)

        self.tiempo4_label = Label(self.salon_window, text= "",font= ("Arial", 30), bg = "#6E1DF1")
        self.tiempo4_label.place(x= 650, y= 390)

        self.nombre5_label = Label(self.salon_window, text= "",font= ("Arial", 30), bg = "#6E1DF1")
        self.nombre5_label.place(x= 200, y= 450)

        self.tiempo5_label = Label(self.salon_window, text= "",font= ("Arial", 30), bg = "#6E1DF1")
        self.tiempo5_label.place(x= 650, y= 450)

        self.regresar_btn = Button(self.salon_window, text='Regresar',  bg="#F35757",font=("Arial", 25), command=self.regresar)
        self.regresar_btn.place(x=420, y=550)

        self.principal()

        self.salon_window.mainloop()

    """
    self.principal: Método que lee las lineas del archivo de texto. Además forma una lista con dichas líneas
    E: Llamada por parte del init
    R:-
    S:Lectura de líneas, formación de la lista y llamada a self.obtener_num1()
    """
    #créditos para https://www.youtube.com/watch?v=0EgSo7hsRWM&t=424s#
    def principal(self):
        file = open('Archivos_txt\Salon.txt', 'r')
        f = file.readlines()
        newList=[]
        for line in f:
            if line[-1] == '\n': # Cuando llega al final de una linea
                newList.append(line[:-1])
            else:
                newList.append(line)
        return self.obtener_num1(newList)

    """
    self.obtener_num1: Método que convierte en enteros en una nueva lista a la suma de los segundos de la lista newList
    E:newList
    R:-
    S: newList2 y llamada a self.obtener_num2
    """

    def obtener_num1(self,newList):
        newList2 = [] #Es la misma lista pero la suma de los segundos se vuelven enteros
        n = len(newList)

        for i in range(n):
            if i == 0 or i % 3 == 0:
                try:
                    int(newList[i])
                    newList[i] = int(newList[i])

                except ValueError:
                    return None
                newList2 += [newList[i]]
                i += 1
            else:

                newList2 += [newList[i]]
                i += i
        self.obtener_num2(newList2)
    """
    self.obtener_num2:Método que crea una nueva lista que solamente contiene la suma de los segundos de newList2. Además guarda únicamente los 5 mejores tiempos y los ordena.
    E: newLisT2
    S:newList3 y llamada a self.lista_salon
    R:-
    """
    def obtener_num2(self, newList2):
        n = len(newList2)
        newList3 = [] #Lista que contiene únicamente la suma de los segundos de los puntajes
        for i in range(n):
            if i == 0 or i % 3 == 0:
                newList3 += [newList2[i]]
                i += 1
            else:
                i += i
        newList3.sort()
        newList3 = newList3[0:5]

        self.lista_salon(newList3, newList2)
    """
    self.lista_salon:Método qué compara los elementos de newList2 y newList3 para formar una lista definitiva, con los 5 mejores puntajes, el nombre del juagador y el tiempo.
    E:newList3 y newList2
    R:-
    S.Lista def
    """
    def lista_salon(self, newList3, newList2):
        listaDef = [] #Lista Definitiva
        n = len(newList3)
        i = 0
        j = 0
        while j != n:
            if newList2[i] == newList3[j]:
                listaDef += [newList3[j]] + [newList2[i + 1]] + [newList2[i + 2]]
                j += 1
                i = 0
            else:
                i += 3
        self.modificar_label(listaDef)
    """
    self.modificar_label:Método que se encarga de actualizar los labels de los nombres y los tiempos
    E: Llamada del init
    R:-
    S:Modificación de los Label
    """
    def modificar_label(self,listaDef):
        self.nombre1_label.config(text=str(listaDef[1]))
        self.tiempo1_label.config(text=str(listaDef[2]))
        self.nombre2_label.config(text=str(listaDef[4]))
        self.tiempo2_label.config(text=str(listaDef[5]))
        self.nombre3_label.config(text=str(listaDef[7]))
        self.tiempo3_label.config(text=str(listaDef[8]))
        self.nombre4_label.config(text=str(listaDef[10]))
        self.tiempo4_label.config(text=str(listaDef[11]))
        self.nombre5_label.config(text=str(listaDef[13]))
        self.tiempo5_label.config(text=str(listaDef[14]))
    """
    self.regresar:Método que destruye la ventana del salon y llama a la del menu
    E:Llamada de self.regresar_btn
    R:-
    S: Destrucción de la ventana del salon y llamada la clase menu
    """
    def regresar(self):
        self.salon_window.destroy()
        menu()


class Game:
    def __init__(self):
        #Parámetros para la ventana
        self.game_window = Tk()
        self.game_window.title("Battle Ship")
        self.game_window.geometry("1350x700")
        self.game_window.resizable(False,False)
        #creación del canvas
        self.game_canvas = Canvas(self.game_window, width=1350, height=700)
        self.game_canvas.pack()
        #Imágen del fondo
        self.fondo = Image.open("Media\Fondo_juego.png")
        self.fondo = self.fondo.resize((1350, 700), Image.ANTIALIAS)
        self.img_fondo = ImageTk.PhotoImage(self.fondo)
        self.game_canvas.create_image(0, 0, image=self.img_fondo, anchor="nw")

        #Label para indicar cual es la matriz del jugador
        self.nombre_label = Label(self.game_canvas, text= "Jugador",font= ("Arial", 25), bg = "#EE3E1E")
        self.nombre_label.place(x= 240, y= 20)

        #Label para indicar cual es la matriz del rival
        self.rival_label = Label(self.game_canvas, text= "Rival",font= ("Arial", 25), bg = "#EE3E1E")
        self.rival_label.place(x= 1050, y= 20)

        # Label que muestra la cantidad turnos jugados
        self.turno_label = Label(self.game_canvas, text= "Turnos: "+ str(turnos),font= ("Arial", 25), bg = "#EE3E1E")
        self.turno_label.place(x= 10, y= 650)

        # Label que muestra la cantidad de barcos del jugador
        self.barcos_jugador_label = Label(self.game_canvas, text= "Barcos: 3",font= ("Arial", 25), bg = "#EE3E1E")
        self.barcos_jugador_label.place(x= 10, y= 590)

        # Label que muestra la cantidad de barcos del rival
        self.barcos_rival_label = Label(self.game_canvas, text= "Barcos: 3",font= ("Arial", 25), bg = "#EE3E1E")
        self.barcos_rival_label.place(x= 1150, y= 590)

        # Canvas para la matriz del jugador
        self.img_matriz = Image.open("Media\Cuadricula.png")
        self.matriz_res = self.img_matriz.resize((500,500), Image.ANTIALIAS)
        self.matriz = ImageTk.PhotoImage(self.matriz_res)
        self.game_canvas.create_image(62,78,image=self.matriz,anchor= "nw")

        # Canvas para la matriz del rival
        self.img_matriz_rival = Image.open("Media\Cuadricula.png")
        self.matriz_res_rival = self.img_matriz.resize((500, 500), Image.ANTIALIAS)
        self.matriz_rival_img = ImageTk.PhotoImage(self.matriz_res)
        self.game_canvas.create_image(805,75,image=self.matriz_rival_img,anchor="nw")

        # Texto para la entrada de posicion de barcos Fila
        self.posicionar_label = Label(self.game_canvas, text= "Posición del barco Fila             ",font= ("Arial", 15), bg = "#47EE1E")
        self.posicionar_label.place(x= 170, y= 590)

        # Texto para la entrada de posicion de barcos Columna
        self.posicionar_label = Label(self.game_canvas, text="Posición del barco Columna             ", font=("Arial", 15),bg="#47EE1E")
        self.posicionar_label.place(x=470, y=590)

        # Texto para la entrada de atacar Fila
        self.posicionar_label = Label(self.game_canvas, text= "Atacar Fila             ",font= ("Arial", 15), bg = "#47EE1E")
        self.posicionar_label.place(x= 170, y= 650)

        # Texto para la entrada de atacar Fila
        self.posicionar_label = Label(self.game_canvas, text="Atacar Columna             ", font=("Arial", 15),bg="#47EE1E")
        self.posicionar_label.place(x=380, y=650)

        # Texto para indicar el primer barco
        self.posicionar_label = Label(self.game_canvas, text="Selecciona el primer Barco", font=("Arial", 15),bg="#1ED8EE")
        self.posicionar_label.place(x=563, y=400)

        # Entrada para colocar barcos filas
        self.barcos_entry_f = Entry(width=10)
        self.barcos_entry_f.place(x= 380, y= 595)
        self.barcos_entry_f.get()

        # Entrada para colocar barcos columnas
        self.barcos_entry_c = Entry(width=10)
        self.barcos_entry_c.place(x=720, y=595)
        self.barcos_entry_c.get()

        # Entrada para atacar fila
        self.atacar_entry_f = Entry(width=10)
        self.atacar_entry_f.place(x= 275, y= 655)
        self.atacar_entry_f.get()

        # Entrada para atacar columna
        self.atacar_entry_c = Entry(width=10)
        self.atacar_entry_c.place(x=530, y=655)
        self.atacar_entry_c.get()

        # Label para el tiempo
        self.tiempo_label = Label(self.game_window, text=str(f'{hora}:{minuto}:{segundo}'), bg="#EE3E1E", width=10)
        self.tiempo_ventana = self.game_canvas.create_window(650, 50, anchor="nw", window=self.tiempo_label)

        #Botón para ubicar al Barco
        self.btn_ubi = Button(self.game_window,text="Ubicar", bg="#EE3E1E",font=("Arial", 15), borderwidth=0,command=self.imagen_seleccionar)
        self.btn_ubi.place(x=810, y=590)

        # Botón para atacar al Barco
        self.btn_ata = Button(self.game_window, text="Atacar", bg="#EE3E1E", font=("Arial", 15), borderwidth=0, command=self.imagen_atacar)
        self.btn_ata.place(x=810, y=650)

        # Botón para empezar el juego
        self.btn_emp = Button(self.game_window, text="Empezar", bg="#EE3E1E", font=("Arial", 15), borderwidth=0,command=self.comenzar_juego)
        self.btn_emp.place(x=645, y=450)

        # Boton para reiniciar el juego
        self.btn_rei = Button(self.game_window, text="Reiniciar", bg="#EE3E1E", font=("Arial", 15), borderwidth=0, command= self.reiniciar)
        self.btn_rei.place(x=645, y=310)

        # Boton para guardar la partida
        self.btn_guardar = Button(self.game_window, text="Guardar Partida", bg="#EE3E1E", font=("Arial", 15), borderwidth=0, command= self.guardar_juego)
        self.btn_guardar.place(x=610, y=200)

        # Imagen para marcar ubicación de un barco
        self.marcar = Image.open("imagenes\Cuadro_Seleccion.png")
        self.marcar = self.marcar.resize((44, 42), Image.ANTIALIAS)
        self.img_marcar = ImageTk.PhotoImage(self.marcar)

        # Imagen para acertar un ataque
        self.acertar = Image.open("Media\Equis.png")
        self.acertar = self.acertar.resize((44, 42), Image.ANTIALIAS)
        self.img_acertar = ImageTk.PhotoImage(self.acertar)

        # Imagen para fallar un ataque
        self.fallar = Image.open("Media\Equis_blanca.png")
        self.fallar = self.fallar.resize((44, 42), Image.ANTIALIAS)
        self.img_fallar = ImageTk.PhotoImage(self.fallar)


        self.game_window.mainloop()

    """ 
    self.guardar_juego:Método que guarda la partida
    E:Llamada por parte de self.btn_guardar
    R: la variable global barcos_selecc_m tiene que ser igual a 7
    S:Las variables globales se guardan en un archivo de texto
    """
    def guardar_juego(self):
        global barcos_seleccm
        if barcos_selecc_m == 7:
            global matriz1
            global matriz2
            global matriz_pos
            global matriz_pos_rival
            global hora
            global minuto
            global segundo
            global turnos
            global turno
            global barco_jug
            global barco_riv
            guardar = open("Archivos_txt\Guardar.txt", "r+")
            guardar.truncate(0)
            guardar.write(str(matriz1) + "\n")
            guardar.write(str(matriz2) + "\n")
            guardar.write(str(matriz_pos) + "\n")
            guardar.write(str(matriz_pos_rival) + "\n")
            guardar.write(str(hora) + "\n")
            guardar.write(str(minuto) + "\n")
            guardar.write(str(segundo) + "\n")
            guardar.write(str(turnos) + "\n")
            guardar.write(str(turno) + "\n")
            guardar.write(str(barco_jug) + "\n")
            guardar.write(str(barco_riv) + "\n")
            guardar.close()
            print("Partida guardada")
        else:
            print("No se puede guardar, primero empieza el juego")


    """
    self.reiniciar:Método para reiniar el juego
    E:Llamada por parte del self.btn_rei
    R:-
    S:las variables globales vuelven a adquirir su valor original
    """
    def reiniciar(self):
        global nuf
        nuf = None
        global nuc
        nuc = None
        global barcos_selecc
        barcos_selecc = 1
        global barcos_selecc_m
        barcos_selecc_m = 1
        global cuadroc
        cuadroc = 0
        global cuadrof
        cuadrof = 0
        global turno
        turno = True
        global barco_jug
        barco_jug = 6
        global corre_tiempo
        corre_tiempo = None
        global matriz1
        global matriz2
        global matriz_pos
        global matriz_pos_rival
        matriz1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        matriz2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        matriz_pos = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        matriz_pos_rival = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.game_window.destroy()
        Game()

    """
    self.tiemp=Método que sirve como cronómetro para el juego
    E:llamada por parte de corredor tiempo
    R:-
    S:El cronómetro comienza a correr
    """
    #Créditos para https://www.youtube.com/watch?v=Bt6NnUi70Vo#
    def tiempo(self):
        global corre_tiempo
        while corre_tiempo == True:
            global hora
            global minuto
            global segundo
            for hora in range(24):
                for minuto in range(60):
                    for segundo in range(60):
                        os.system('cls')
                        self.tiempo_label.config( text = str(f'{hora}:{minuto}:{segundo}'))
                        time.sleep(1)
    """
    self.correr_tiempo: Método de hilos que permite correr la funcion del tiempo
    E: Llamada por parte de la clase Game
    S: Correr el método de self.tiempo
    R: --
    """
    def correr_tiempo(self):
        self.tiempo_thread = Thread(target=self.tiempo)
        self.tiempo_thread.start()


    """
    self.valor_entry_uby:Método que obtiene el valor de entrada para la ubicacion de fila del barco 
    E: Número indicado en la entrada
    S: Obtener el valor de la entrada de fila para ubicar barco
    R: --
    """
    def valor_entry_ubi_f(self):
        global nuf
        try:
            int(self.barcos_entry_f.get())
            nuf = int(self.barcos_entry_f.get())
        except ValueError:
            return None


    """
    self.valor_entry_ubi_c:Método que obtiene el valor de entrada para la ubicacion de la columna del barco 
    E: Número indicado en la entrada
    S: Obtener el valor de la entrada de la columna para ubicar barco
    R: --
    """
    def valor_entry_ubi_c(self):
        global nuc
        try:
            int(self.barcos_entry_c.get())
            nuc = int(self.barcos_entry_c.get())
        except ValueError:
            return None


    """
    self.valor_entry_ata_f:Función que obtiene el valor de entrada para la ubicacion de fila para atacar al rival
    E: Número indicado en la entrada
    S: Obtener el valor de la entrada de fila para atacar rival
    R: --
    """
    def valor_entry_ata_f(self):
        global nuf
        try:
            int(self.atacar_entry_f.get())
            nuf = int(self.atacar_entry_f.get())
        except ValueError:
            return None

    """
    self.valor_entry_ata_c:Método que obtiene el valor de entrada para la ubicacion de la columna para atacar al rival
    E: Número indicado en la entrada
    S: Obtener el valor de la entrada de la columna para atacar rival
    R: --
    """
    def valor_entry_ata_c(self):
        global nuc
        try:
            int(self.atacar_entry_c.get())
            nuc = int(self.atacar_entry_c.get())
        except ValueError:
            return None

    """
    self.crear_label_2: Método que crea el label para indicar que se tiene que ubicar el segundo barco
    E: Funcion llamada a partir de haber generado el primer barco
    S: Label que da la instruccion de ubicar el segundo barco
    R: haber ubicado el primer barco
    """
    def crear_label_2(self):
        self.posicionar_label.destroy()
        self.posicionar_label_2 = Label(self.game_canvas, text="Selecciona el segundo Barco", font=("Arial", 15),bg="#1ED8EE")
        self.posicionar_label_2.place(x=555, y=400)

    """
    self.crear_label_3: Método que crea el label para indicar que se tiene que ubicar el tercer barco
    E: Funcion llamada a partir de haber generado el segundo barco
    S: Label que da la instruccion de ubicar el tercer barco
    R: Haber ubicado el segundo barco
    """
    def crear_label_3(self):
        self.posicionar_label_2.destroy()
        self.posicionar_label_3 = Label(self.game_canvas, text="Selecciona el tercer Barco", font=("Arial", 15),bg="#1ED8EE")
        self.posicionar_label_3.place(x=565, y=400)

    """
    self.crear_jugar_label: Método que crea el label para indicar que es momento de empezar a jugar
    E: Funcion llamada a partir de haber generado el tercer barco
    S: Label que da la instruccion de iniciar la partida
    R: Haber ubicado el tercer barco
    """
    def crear_jugar_label(self):
        self.posicionar_label_3.destroy()
        self.jugar_label = Label(self.game_canvas, text="A Jugar!", font=("Arial", 15),bg="#1ED8EE")
        self.jugar_label.place(x=645, y=400)

    """
    self.imagen_seleccionar:Método que ubica la posición de los barcos en la matriz interna y los muestra visualmente en la interfaz
    E: Número definido en las entradas de ubicacion de fila y columna
    S: Ubica el barco en la matriz tanto visualmente como internamente
    R: Los numeros de fila y columna tienen que ser entre 0 y 9
    """
    def imagen_seleccionar(self):
        global barcos_selecc

        if barcos_selecc <= 6:
            global cuadroc
            global cuadrof
            global nuf
            global nuc
            global nuft
            global nuct
            global matriz1
            global matriz_pos

            self.valor_entry_ubi_f()
            self.valor_entry_ubi_c()

            # Caso para colocar el primer barco
            if 0<=nuc<=9 and 0<=nuf<=9 and barcos_selecc==1 and isinstance(nuc,int) and isinstance(nuf,int):

                self.game_canvas.create_image(91+nuc*47, 120+nuf*46, image=self.img_marcar, anchor="nw")
                barcos_selecc+=1
                self.crear_label_2()
                matriz1[nuf][nuc]=1
                matriz_pos[nuf][nuc] = 1

            # Caso para colocar el segundo barco
            elif 0<=nuc<=9 and 0<=nuf<=9 and 1<barcos_selecc<=3 and matriz1[nuf][nuc]==0 :
                if barcos_selecc==2: # Primer cuadrito del segundo barco

                    self.game_canvas.create_image(91 + nuc * 47, 120+ nuf * 46, image=self.img_marcar, anchor="nw")
                    nuft = nuf
                    nuct = nuc
                    barcos_selecc += 1
                    matriz1[nuf][nuc]=1
                    matriz_pos[nuf][nuc]=1

                elif barcos_selecc==3: # Segundo cuadrito del segundo barco
                    if (nuf== nuft+1 and nuc==nuct):

                        self.game_canvas.create_image(91 + nuc * 47, 120 + nuf * 46, image=self.img_marcar, anchor="nw")
                        nuft = 0
                        nuct = 0
                        barcos_selecc += 1
                        self.crear_label_3()
                        matriz1[nuf][nuc] = 1
                        matriz_pos[nuf][nuc] = 1

                    elif (nuf==nuft-1 and nuc==nuct):

                        self.game_canvas.create_image(91 + nuc * 47, 120 + nuf * 46, image=self.img_marcar, anchor="nw")
                        nuft = 0
                        nuct = 0
                        barcos_selecc += 1
                        matriz1[nuf][nuc] = 1
                        matriz_pos[nuf][nuc] = 1
                        self.crear_label_3()

                    elif (nuf==nuft and nuc==nuct+1):

                        self.game_canvas.create_image(91 + nuc * 47, 120 + nuf * 46, image=self.img_marcar, anchor="nw")
                        nuft = 0
                        nuct = 0
                        barcos_selecc += 1
                        matriz1[nuf][nuc] = 1
                        matriz_pos[nuf][nuc] = 1
                        self.crear_label_3()

                    elif (nuf==nuft and nuc==nuct-1):

                        self.game_canvas.create_image(91 + nuc * 47, 120 + nuf * 46, image=self.img_marcar, anchor="nw")
                        nuft = 0
                        nuct = 0
                        barcos_selecc += 1

                        self.crear_label_3()
                        matriz1[nuf][nuc] = 1
                        matriz_pos[nuf][nuc] = 1

            # Caso para el tercer barco
            elif 0<=nuc<=9 and 0<=nuf<=9 and 3<barcos_selecc<=6:
                if barcos_selecc == 4: # Primer cuadrito del tercer barco
                    self.game_canvas.create_image(91 + nuc * 47, 120 + nuf * 46, image=self.img_marcar, anchor="nw")
                    nuft = nuf
                    nuct = nuc
                    matriz1[nuf][nuc] = 1
                    matriz_pos[nuf][nuc]=1
                    barcos_selecc += 1

                elif barcos_selecc==5: # Segundo cuadrito del tercer barco
                    if (nuf== nuft+1 and nuc==nuct):
                        self.game_canvas.create_image(91 + nuc * 47, 120 + nuf * 46, image=self.img_marcar, anchor="nw")
                        cuadrof = nuf
                        cuadroc = nuc
                        matriz1[nuf][nuc] = 1
                        matriz_pos[nuf][nuc] = 1
                        barcos_selecc += 1


                    elif (nuf==nuft-1 and nuc==nuct):
                        self.game_canvas.create_image(91 + nuc * 47, 120 + nuf * 46, image=self.img_marcar, anchor="nw")
                        cuadrof = nuf
                        cuadroc = nuc
                        matriz1[nuf][nuc] = 1
                        matriz_pos[nuf][nuc] = 1
                        barcos_selecc += 1


                    elif (nuf==nuft and nuc==nuct+1):
                        self.game_canvas.create_image(91 + nuc * 47, 120 + nuf * 46, image=self.img_marcar, anchor="nw")
                        cuadrof = nuf
                        cuadroc = nuc
                        matriz1[nuf][nuc] = 1
                        matriz_pos[nuf][nuc] = 1
                        barcos_selecc += 1

                    elif (nuf==nuft and nuc==nuct-1):
                        self.game_canvas.create_image(91 + nuc * 47, 120 + nuf * 46, image=self.img_marcar, anchor="nw")
                        cuadrof = nuf
                        cuadroc = nuc
                        matriz1[nuf][nuc] = 1
                        matriz_pos[nuf][nuc] = 1
                        barcos_selecc += 1


                elif barcos_selecc==6: #Tercer cuadrito del tercer barco
                    if (nuf== nuft+2 and nuc==nuct and nuf == cuadrof+1 and nuc == cuadroc):
                        self.game_canvas.create_image(91 + nuc * 47, 120 + nuf * 46, image=self.img_marcar, anchor="nw")
                        nuft = 0
                        nuct = 0
                        barcos_selecc += 1
                        matriz1[nuf][nuc] = 1
                        matriz_pos[nuf][nuc] = 1
                        self.crear_jugar_label()

                    elif (nuf==nuft-2 and nuc==nuct and nuf == cuadrof-1 and nuc == cuadroc):
                        self.game_canvas.create_image(91 + nuc * 47, 120 + nuf * 46, image=self.img_marcar, anchor="nw")
                        nuft = 0
                        nuct = 0
                        barcos_selecc += 1
                        matriz1[nuf][nuc] = 1
                        matriz_pos[nuf][nuc] = 1
                        self.crear_jugar_label()


                    elif (nuf==nuft and nuc==nuct+2 and nuf == cuadrof and nuc == cuadroc+1):
                        self.game_canvas.create_image(91 + nuc * 47, 120 + nuf * 46, image=self.img_marcar, anchor="nw")
                        nuft = 0
                        nuct = 0
                        barcos_selecc += 1
                        matriz1[nuf][nuc] = 1
                        matriz_pos[nuf][nuc] = 1
                        self.crear_jugar_label()


                    elif (nuf==nuft and nuc==nuct-2 and nuf == cuadrof and nuc == cuadroc-1):
                        self.game_canvas.create_image(91 + nuc * 47, 120 + nuf * 46, image=self.img_marcar, anchor="nw")
                        nuft = 0
                        nuct = 0
                        barcos_selecc += 1
                        matriz1[nuf][nuc] = 1
                        matriz_pos[nuf][nuc] = 1
                        self.crear_jugar_label()

                    elif (nuf == nuft and nuc == nuct - 1 and nuf == cuadrof and nuc == cuadroc - 2):
                        self.game_canvas.create_image(91 + nuc * 47, 120 + nuf * 46, image=self.img_marcar, anchor="nw")
                        nuft = 0
                        nuct = 0
                        barcos_selecc += 1
                        matriz1[nuf][nuc] = 1
                        matriz_pos[nuf][nuc] = 1
                        self.crear_jugar_label()

                    elif (nuf == nuft and nuc == nuct + 1 and nuf == cuadrof and nuc == cuadroc + 2):
                        self.game_canvas.create_image(91 + nuc * 47, 120 + nuf * 46, image=self.img_marcar, anchor="nw")
                        nuft = 0
                        nuct = 0
                        barcos_selecc += 1
                        matriz1[nuf][nuc] = 1
                        matriz_pos[nuf][nuc] = 1
                        self.crear_jugar_label()

                    elif (nuf == nuft + 1 and nuc == nuct and nuf == cuadrof + 2 and nuc == cuadroc):
                        self.game_canvas.create_image(91 + nuc * 47, 120 + nuf * 46, image=self.img_marcar, anchor="nw")
                        nuft = 0
                        nuct = 0
                        barcos_selecc += 1
                        matriz1[nuf][nuc] = 1
                        matriz_pos[nuf][nuc] = 1
                        self.crear_jugar_label()

                    elif (nuf == nuft - 1 and nuc == nuct and nuf == cuadrof - 2 and nuc == cuadroc):
                        self.game_canvas.create_image(91 + nuc * 47, 120 + nuf * 46, image=self.img_marcar, anchor="nw")
                        nuft = 0
                        nuct = 0
                        barcos_selecc += 1
                        matriz1[nuf][nuc] = 1
                        matriz_pos[nuf][nuc] = 1
                        self.crear_jugar_label()


    """
    self.sonido_salpi:Método que ejecuta un sonido de salpicadura cuando se realiza un ataque fallido
    E: Coordenada de ataque fallido
    S: Sonido que indica que falló el ataque
    R: --
    """
    def sonido_salpi(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Sonidos\Salpicadura.mp3")
        pygame.mixer.music.play(loops=0)


    """
    self.sonido_explo: Método que ejecuta un sonido de explosion cuando se realiza un impacto a un barco rival
    E: Coordenada de ataque exitoso
    S: Sonido que indica que acertó el ataque
    R: --
    """
    def sonido_explo(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Sonidos\Sonido_explo.mp3")
        pygame.mixer.music.play(loops=0)

    """
    self.sonido_victoria: Método que ejecuta un sonido de victoria cuando el jugador gana el juego
    E: Numero de barcos del rival
    S: Sonido de victoria 
    R: El numero de barcos del rival debe ser 1 para saber que ya todos fueron destruidos
    """
    def sonido_victoria(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Sonidos/Sonido_Victoria.mp3")
        pygame.mixer.music.play(loops=0)

    """
    self.sonido_derrota:Método que ejecuta un sonido de derrota cuando el jugador pierde el juego
    E: Numero de barcos del jugador
    S: Sonido de derrota 
    R: El numero de barcos del jugador debe ser 1 para saber que ya todos fueron destruidos
    """
    def sonido_derrota(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Sonidos\Derrota.mp3")
        pygame.mixer.music.play(loops=0)

    """
    self.comenzar_juego: Método que da inicio a la partida, genera aleatoriamente los barcos del rival e inicia la funcion de hilos del tiempo
    E: Número de barcos seleccionados por el jugador
    S: Genera los barcos del rival de manera aleatoria e inicia el tiempo para empezar a jugar
    R: El número de barcos seleccionados debe ser 7 para indicar que el jugador ya ubicó los barcos y la función es llamada por su respectivo botón
    """
    def comenzar_juego(self):
        global corre_tiempo
        corre_tiempo = True
        if barcos_selecc == 7: # Restriccion, que indica cuando los barcos del jugador ya han sido colocados
            self.correr_tiempo()
            global matriz2
            global barcos_selecc_m
            f=None
            c=None
            global aleatoria
            matrizt=None
            global matriz_pos_rival
            while barcos_selecc_m!=7:

                # Primer barco rival
                if barcos_selecc_m==1:
                    f=random.randint(0,9)
                    c=random.randint(0,9)
                    matriz2[f][c]=1
                    matriz_pos_rival[f][c]=1
                    barcos_selecc_m+=1
                    f = random.randint(0, 9)
                    c = random.randint(0, 9)
                    matrizt = matriz2[f][c]

                # Segundo barco rival
                elif barcos_selecc_m<=3 and matrizt==0:
                    if barcos_selecc_m==2:
                        matriz2[f][c] = 1
                        matriz_pos_rival[f][c] = 1
                        barcos_selecc_m+=1
                        aleatoria= random.randint(1,4)
                    while barcos_selecc_m==3:
                        if aleatoria==1:
                            f+=1
                            if f<9 and matriz2[f][c]==0:
                                matriz2[f][c]=1
                                matriz_pos_rival[f][c] = 1
                                f = random.randint(0, 9)
                                c = random.randint(0, 9)
                                matrizt = matriz2[f][c]
                                barcos_selecc_m += 1
                            else:
                                aleatoria=random.randint(1,4)
                                f=0
                        elif aleatoria==2 :
                            f-=1
                            if  f>0 and matriz2[f][c] == 0:
                                matriz2[f][c] = 1
                                matriz_pos_rival[f][c] = 1
                                f = random.randint(0, 9)
                                c = random.randint(0, 9)
                                matrizt = matriz2[f][c]
                                barcos_selecc_m += 1
                            else:
                                aleatoria=random.randint(1,4)
                                f=0
                        elif aleatoria==3:
                            c+=1
                            if c<9 and matriz2[f][c] == 0 :
                                matriz2[f][c] = 1
                                matriz_pos_rival[f][c] = 1
                                f = random.randint(0, 9)
                                c = random.randint(0, 9)
                                matrizt = matriz2[f][c]
                                barcos_selecc_m += 1
                            else:
                                aleatoria=random.randint(1,4)
                                c=0
                        else:
                            c-=1
                            if c>0 and matriz2[f][c] == 0 :
                                matriz2[f][c] = 1
                                matriz_pos_rival[f][c] = 1
                                f = random.randint(0, 9)
                                c = random.randint(0, 9)
                                matrizt = matriz2[f][c]
                                barcos_selecc_m += 1
                            else:
                                aleatoria=random.randint(1,4)
                                c=0

                #Caso para el tercer barco rival
                elif barcos_selecc_m <= 6 and matrizt == 0:
                    if barcos_selecc_m == 4:
                        matriz2[f][c] = 1
                        matriz_pos_rival[f][c] = 1
                        barcos_selecc_m+=1
                        aleatoria= random.randint(1,4)
                    while barcos_selecc_m <=6:
                        if aleatoria == 1:
                            f +=1
                            if matriz2[f][c]==0 and matriz2[f+1][c] == 0 and f<9:
                                matriz2[f][c]=1
                                matriz2[f+1][c]=1
                                matriz_pos_rival[f][c] = 1
                                matriz_pos_rival[f+1][c] = 1
                                barcos_selecc_m +=2
                            else:
                                aleatoria = random.randint(1, 4)
                                f = 0
                        elif aleatoria==2 and f>0:
                            f -=1
                            if matriz2[f][c]==0 and matriz2[f-1][c] == 0:
                                matriz2[f][c]=1
                                matriz2[f-1][c]=1
                                matriz_pos_rival[f][c] = 1
                                matriz_pos_rival[f-1][c] = 1
                                barcos_selecc_m +=2
                            else:
                                aleatoria = random.randint(1, 4)
                                f = 0
                        elif aleatoria==3:
                            c +=1
                            if matriz2[f][c]==0 and matriz2[f][c+1] == 0 and c<9:
                                matriz2[f][c]=1
                                matriz2[f][c+1]=1
                                matriz_pos_rival[f][c] = 1
                                matriz_pos_rival[f][c+1] = 1
                                barcos_selecc_m +=2
                            else:
                                aleatoria = random.randint(1, 4)
                                c = 0
                        else:
                            c-=1
                            if matriz2[f][c] == 0 and matriz2[f][c-1] == 0 and c>0:
                                matriz2[f][c]=1
                                matriz2[f][c-1]=1
                                matriz_pos_rival[f][c] = 1
                                matriz_pos_rival[f][c-1] = 1
                                barcos_selecc_m +=2
                            else:
                                aleatoria = random.randint(1, 4)
                                c = 0
                else:
                    f = random.randint(0, 9)
                    c = random.randint(0, 9)

        print(matriz2)


    """
    self.imagen_atacar: Método que genera una imagen de ataque exitoso (Equis roja) o fallido (Equis blanca) según corresponda por parte del jugador
    E: Número definido en las entradas de ubicacion de fila y columna de atacar
    S: Genera una imagen de ataque exitoso o fallido segun los numeros de entrada
    R: Los numeros de fila y columna tienen que ser entre 0 y 9 y aparte, tiene que ser el turno del jugador
    """
    def imagen_atacar(self):
        global barcos_selecc_m
        if barcos_selecc_m == 7: # Evita que se ataque sin antes de haber presionado el boton empezar
            global turno
            global nuf
            global nuc
            global matriz2
            global barco_riv
            global turnos
            self.valor_entry_ata_f()
            self.valor_entry_ata_c()

            if 0<=nuc<=9 and 0<=nuf<=9 and barco_riv!=0 and matriz2[nuf][nuc] != 2 and turno == True and isinstance(nuc,int) and isinstance(nuf,int): # matriz2[nuf][nuc] != 2 permite evitar atacar 2 veces en un mismo lugar, si detecta que la matriz2[nuf][nuc] == 2 es porque ya se ha atacado esa coordenada
                if matriz2[nuf][nuc] == 1: # Si el jugador acierta un ataque
                    self.game_canvas.create_image(835 + nuc * 47, 118 + nuf * 46, image=self.img_acertar, anchor="nw")
                    barco_riv -= 1
                    self.sonido_explo()
                    self.victoria()
                else:
                    self.game_canvas.create_image(835 + nuc * 47, 118 + nuf * 46, image=self.img_fallar, anchor="nw")
                    self.sonido_salpi()
                turnos += 1
                self.turno_label.config(text="Turnos: " + str(turnos))
                matriz2[nuf][nuc] = 2
                turno = False
                self.game_window.after(2000,self.atacar_rival)


    """
    self.atacar_rival=Método en el cual se crean imágenes sobre la cuadrícula del rival y se modifica su matriz
    E: Llamada de self.btn_ata
    R: la global turno debe ser igual a False
    S: Ataque hacia el rival
    """
    def atacar_rival(self):
        global turno
        nuf_riv= None
        nuc_riv=None
        global matriz1
        global barco_jug
        global turnos
        global barco_riv
        if turno == False: # Cuando el no es el turno del jugador, es decir, le toca al rival jugar
            nuf_riv = random.randint(0, 9)
            nuc_riv = random.randint(0, 9)
            if matriz1[nuf_riv][nuc_riv] != 2 and barco_jug !=0 and barco_riv !=0: # Verificar si el rival está atacando una casilla nueva
                if matriz1[nuf_riv][nuc_riv] == 1: # Cuando el rival acierta
                    self.game_canvas.create_image(91 + nuc_riv * 47, 120 + nuf_riv * 46, image=self.img_acertar, anchor="nw")
                    barco_jug -= 1
                    self.sonido_explo()
                    self.derrota()
                else:
                    self.game_canvas.create_image(91 + nuc_riv * 47, 120 + nuf_riv * 46, image=self.img_fallar, anchor="nw")
                    self.sonido_salpi()
                matriz1[nuf_riv][nuc_riv] = 2 # Marca la casilla como ya atacada
                turno = True
            else:
                nuf_riv = random.randint(0, 9)
                nuc_riv = random.randint(0, 9)
                return self.atacar_rival()

    """
    self.victoria:Método que reproduce un sonido de victoria al ganar y llama a la ventana de victoria
    E: Llamada del atributo self.imagen_atacar
    R: La global barco_riv debe ser igual a 0
    S: Destrucción de la ventana del juego, reproducción del sonido victoria y llamada a la clase Ven_victoria
    """
    def victoria(self):
        global barco_riv
        global corre_tiempo
        corre_tiempo = False
        if barco_riv==0:
            self.sonido_victoria()
            self.game_window.after(3000, Ven_victoria)
            self.game_window.after(3000,self.game_window.destroy)
    """
    self.derrota: Método que reproduce un sonido de derrota al perder y llama a la ventana de derrota
    E: Llamada por parte del método self.atacar_rival
    R: La variable global barco_jug debe ser igual a 0
    S: Destrucción de la ventana del juego, reproducción del sonido derrota y llamada a la clase Ven_derrota
    """
    def derrota(self):
        global barco_jug
        global corre_tiempo
        corre_tiempo = False
        if barco_jug==0:
            self.sonido_derrota()
            self.game_window.after(3000, Ven_derrota)
            self.game_window.after(3000, self.game_window.destroy)

class Ven_victoria:
    def __init__(self):
        #Parámetros para ventana
        self.ventana_v = Tk()
        self.ventana_v.title("Battle Ship")
        self.ventana_v.geometry("1000x700")
        self.ventana_v.resizable(False, False)
        #creación del canvas
        self.canvas_v = Canvas(self.ventana_v, width=1000, height=700, bg="#EE4D1E")
        self.canvas_v.pack()
        #Label de felicitación
        self.ganaste = Label(self.ventana_v, text="¡Ganaste!", font=("Helvetica", 50),bg="#EE4D1E")
        self.ganaste.place(x= 350, y= 10)
        #Label donde aparece el tiempo empleado por el jugador
        self.tiempo_label = Label(self.ventana_v, text="Tiempo: "+str(f'{hora}:{minuto}:{segundo}'), font=("Helvetica", 40),bg="#EE4D1E")
        self.tiempo_label.place(x= 330, y= 130)
        #Label donde aparece la cantidad de turnos requeridos por el jugador
        self.turno_label = Label(self.ventana_v, text="Turnos: "+str(turnos), font=("Helvetica", 40),bg="#EE4D1E")
        self.turno_label.place(x= 330, y= 220)
        #Label de instrucción
        self.nombre_label = Label(self.ventana_v, text="Ingresa tu nombre:", font=("Helvetica", 30),bg="#EE4D1E")
        self.nombre_label.place(x= 250, y= 400)
        # Entrada para guardar el nombre del jugador
        self.entrada_nombre = tk.Entry(self.canvas_v)
        self.entrada_nombre.place(x=600, y=418)
        self.btn = Button(self.ventana_v, text='Guardar',  bg="#F35757",font=("Arial", 25), command=self.guardar_puntaje)
        self.btn.place(x=420, y=550)
        self.ventana_v.mainloop()

    """
    self.guardar_puntaje: Método que se encarga de escribir la suma de los segundos empleados, 
    el nombre del jugador y el tiempo en un archivo de texto.
    E:Llamada del self.btn
    R:-
    S: escritura de los datos en el archivo de texto
    """
    #Créditos para https://www.youtube.com/watch?v=W0fPZQBFpVE#
    def guardar_puntaje(self):
        global hora
        global minuto
        global segundo
        puntajef = open("Archivos_txt/Salon.txt", "a")
        puntajef.write(str((hora*3600)+(minuto*60)+segundo-3) + "\n")
        puntajef.write(str(self.entrada_nombre.get()) + "\n")
        puntajef.write(str(f'{hora}:{minuto}:{segundo}')+ "\n")
        puntajef.close()
        hora = 0
        minuto= 0
        segundo= 0
        self.ventana_v.destroy()
        menu()

# Clase de la partida cargada
class Partida_cargada:
    def __init__(self):
        #Parámetros para la ventana
        self.game_window = Tk()
        self.game_window.title("Battle Ship")
        self.game_window.geometry("1350x700")
        self.game_window.resizable(False,False)
        #creación del canvas
        self.game_canvas = Canvas(self.game_window, width=1350, height=700)
        self.game_canvas.pack()
        #creación de la imagen de fondo
        self.fondo = Image.open("Media\Fondo_juego.png")
        self.fondo = self.fondo.resize((1350, 700), Image.ANTIALIAS)
        self.img_fondo = ImageTk.PhotoImage(self.fondo)
        self.game_canvas.create_image(0, 0, image=self.img_fondo, anchor="nw")

        self.nombre_label = Label(self.game_canvas, text= "Jugador",font= ("Arial", 25), bg = "#EE3E1E")
        self.nombre_label.place(x= 240, y= 20)

        self.rival_label = Label(self.game_canvas, text= "Rival",font= ("Arial", 25), bg = "#EE3E1E")
        self.rival_label.place(x= 1050, y= 20)

        # Label que muestra la cantidad turnos jugados
        self.turno_label = Label(self.game_canvas, text= "Turnos: "+ str(turnos),font= ("Arial", 25), bg = "#EE3E1E")
        self.turno_label.place(x= 10, y= 650)

        # Label que muestra la cantidad de barcos del jugador
        self.barcos_jugador_label = Label(self.game_canvas, text= "Barcos: 3",font= ("Arial", 25), bg = "#EE3E1E")
        self.barcos_jugador_label.place(x= 10, y= 590)

        # Label que muestra la cantidad de barcos del rival
        self.barcos_rival_label = Label(self.game_canvas, text= "Barcos: 3",font= ("Arial", 25), bg = "#EE3E1E")
        self.barcos_rival_label.place(x= 1150, y= 590)

        # Canvas para la matriz del jugador
        self.img_matriz = Image.open("Media\Cuadricula.png")
        self.matriz_res = self.img_matriz.resize((500,500), Image.ANTIALIAS)
        self.matriz = ImageTk.PhotoImage(self.matriz_res)
        self.game_canvas.create_image(62,78,image=self.matriz,anchor= "nw")

        # Canvas para la matriz del rival
        self.img_matriz_rival = Image.open("Media\Cuadricula.png")
        self.matriz_res_rival = self.img_matriz.resize((500, 500), Image.ANTIALIAS)
        self.matriz_rival_img = ImageTk.PhotoImage(self.matriz_res)
        self.game_canvas.create_image(805,75,image=self.matriz_rival_img,anchor="nw")

        # Texto para la entrada de posicion de barcos Fila
        self.posicionar_label = Label(self.game_canvas, text= "Posición del barco Fila             ",font= ("Arial", 15), bg = "#47EE1E")
        self.posicionar_label.place(x= 170, y= 590)

        # Texto para la entrada de posicion de barcos Columna
        self.posicionar_label = Label(self.game_canvas, text="Posición del barco Columna             ", font=("Arial", 15),bg="#47EE1E")
        self.posicionar_label.place(x=470, y=590)

        # Texto para la entrada de atacar Fila
        self.posicionar_label = Label(self.game_canvas, text= "Atacar Fila             ",font= ("Arial", 15), bg = "#47EE1E")
        self.posicionar_label.place(x= 170, y= 650)

        # Texto para la entrada de atacar Fila
        self.posicionar_label = Label(self.game_canvas, text="Atacar Columna             ", font=("Arial", 15),bg="#47EE1E")
        self.posicionar_label.place(x=380, y=650)

        # Entrada para colocar barcos filas
        self.barcos_entry_f = Entry(width=10)
        self.barcos_entry_f.place(x= 380, y= 595)
        self.barcos_entry_f.get()

        # Entrada para colocar barcos columnas
        self.barcos_entry_c = Entry(width=10)
        self.barcos_entry_c.place(x=720, y=595)
        self.barcos_entry_c.get()

        # Entrada para atacar fila
        self.atacar_entry_f = Entry(width=10)
        self.atacar_entry_f.place(x= 275, y= 655)
        self.atacar_entry_f.get()

        # Entrada para atacar columna
        self.atacar_entry_c = Entry(width=10)
        self.atacar_entry_c.place(x=530, y=655)
        self.atacar_entry_c.get()

        # Label para el tiempo
        self.tiempo_label = Label(self.game_window, text=str(f'{hora}:{minuto}:{segundo}'), bg="#EE3E1E", width=10)
        self.tiempo_ventana = self.game_canvas.create_window(650, 50, anchor="nw", window=self.tiempo_label)

        #Botón para ubicar al Barco
        self.btn_ubi = Button(self.game_window,text="Ubicar", bg="#EE3E1E",font=("Arial", 15), borderwidth=0)
        self.btn_ubi.place(x=810, y=590)

        # Botón para atacar al Barco
        self.btn_ata = Button(self.game_window, text="Atacar", bg="#EE3E1E", font=("Arial", 15), borderwidth=0, command=self.imagen_atacar)
        self.btn_ata.place(x=810, y=650)

        # Boton para reiniciar el juego
        self.btn_rei = Button(self.game_window, text="Reiniciar", bg="#EE3E1E", font=("Arial", 15), borderwidth=0, command= self.reiniciar)
        self.btn_rei.place(x=645, y=310)

        # Boton para guardar la partida
        self.btn_guardar = Button(self.game_window, text="Guardar Partida", bg="#EE3E1E", font=("Arial", 15), borderwidth=0, command= self.guardar_juego)
        self.btn_guardar.place(x=610, y=200)

        # Imagen para marcar ubicación de un barco
        self.marcar = Image.open("imagenes\Cuadro_Seleccion.png")
        self.marcar = self.marcar.resize((44, 42), Image.ANTIALIAS)
        self.img_marcar = ImageTk.PhotoImage(self.marcar)

        # Imagen para acertar un ataque-
        self.acertar = Image.open("Media\Equis.png")
        self.acertar = self.acertar.resize((44, 42), Image.ANTIALIAS)
        self.img_acertar = ImageTk.PhotoImage(self.acertar)

        # Imagen para fallar un ataque
        self.fallar = Image.open("Media\Equis_blanca.png")
        self.fallar = self.fallar.resize((44, 42), Image.ANTIALIAS)
        self.img_fallar = ImageTk.PhotoImage(self.fallar)

        self.asignar_glob()
        self.obtener_matriz1()
        self.obtener_matriz2()
        self.obtener_matriz_jug()
        self.obtener_matriz_riv()

        self.imagenes_barco()
        self.imagenes_ataques_rival()
        self.imagenes_ataques_jug()
        self.cargar_turnos()
        self.correr_tiempo()

        self.game_window.mainloop()

    # Leer las lineas del archivo de texto para las globales en forma de string
    file = open('Archivos_txt/Guardar.txt', 'r')
    f = file.readlines()
    for line in f:
        if line[-1] == '\n': # Cuando llega al final de una linea
            lista_glob.append(line[:-1])
        else:
            lista_glob.append(line)

    """ 
    self.guardar_juego:Método que guarda la partida
    E:Llamada por parte de self.btn_guardar
    R: la variable global barcos_selecc_m tiene que ser igual a 7
    S:Las variables globales se guardan en un archivo de texto
    """
    def guardar_juego(self):
        global matriz1
        global matriz2
        global matriz_pos
        global matriz_pos_rival
        global hora
        global minuto
        global segundo
        global turnos
        global turno
        global barco_jug
        global barco_riv
        guardar = open("Archivos_txt/Guardar.txt", "r+")
        guardar.truncate(0)
        guardar.write(str(matriz1) + "\n")
        guardar.write(str(matriz2) + "\n")
        guardar.write(str(matriz_pos) + "\n")
        guardar.write(str(matriz_pos_rival) + "\n")
        guardar.write(str(hora) + "\n")
        guardar.write(str(minuto) + "\n")
        guardar.write(str(segundo) + "\n")
        guardar.write(str(turnos) + "\n")
        guardar.write(str(turno) + "\n")
        guardar.write(str(barco_jug) + "\n")
        guardar.write(str(barco_riv) + "\n")
        guardar.close()

    """
    self.reiniciar:Método para reiniar el juego
    E:Llamada por parte del self.btn_rei
    R:-
    S:las variables globales vuelven a adquirir su valor original
    """
    def reiniciar(self):
        global nuf
        nuf = None
        global nuc
        nuc = None
        global barcos_selecc
        barcos_selecc = 1
        global barcos_selecc_m
        barcos_selecc_m = 1
        global cuadroc
        cuadroc = 0
        global cuadrof
        cuadrof = 0
        global corredor
        corredor = True
        global f
        f = None
        global c
        c = None
        global aleatoria
        aleatoria = None
        global turno
        turno = True
        global barco_jug
        barco_jug = 6
        global corre_tiempo
        corre_tiempo = None
        global matriz1
        global matriz2
        global matriz_pos
        global matriz_pos_rival
        matriz1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        matriz2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        matriz_pos = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        matriz_pos_rival = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.game_window.destroy()
        Game()

    """
    self.tiemp=Método que sirve como cronómetro para el juego
    E:llamada por parte de corredor tiempo
    R:-
    S:El cronómetro comienza a correr
    """
    def tiempo(self):
        global corre_tiempo
        self.asignar_glob()
        while corre_tiempo == True:
            global hora
            global minuto
            global segundo
            if hora != 24:
                if minuto != 60:
                    if segundo != 60:
                        os.system('cls')
                        self.tiempo_label.config( text = str(f'{hora}:{minuto}:{segundo}'))
                        segundo += 1
                        time.sleep(1)
                    else:
                        segundo = 0
                        minuto += 1
                else:
                    minuto = 0
                    hora += 1
            else:
                hora = 0

    """
    self.correr_tiempo: Método de hilos que permite correr la funcion del tiempo
    E: Llamada por parte de la clase Game
    S: Correr la funcion de self.tiempo
    R: --
    """
    def correr_tiempo(self):
        global corre_tiempo
        corre_tiempo = True
        self.tiempo_thread = Thread(target=self.tiempo)
        self.tiempo_thread.start()

    """
    self.valor_entry_ata_f:Función que obtiene el valor de entrada para la ubicacion de fila para atacar al rival
    E: Número indicado en la entrada
    S: Obtener el valor de la entrada de fila para atacar rival
    R: --
    """
    def valor_entry_ata_f(self):
        global nuf
        try:
            int(self.atacar_entry_f.get())
            nuf = int(self.atacar_entry_f.get())
        except ValueError:
            return None

    """
        self.valor_entry_ata_c:Método que obtiene el valor de entrada para la ubicacion de la columna para atacar al rival
        E: Número indicado en la entrada
        S: Obtener el valor de la entrada de la columna para atacar rival
        R: --
        """
    def valor_entry_ata_c(self):
        global nuc
        try:
            int(self.atacar_entry_c.get())
            nuc = int(self.atacar_entry_c.get())
        except ValueError:
            return None
    """
        self.sonido_salpi:Método que ejecuta un sonido de salpicadura cuando se realiza un ataque fallido
        E: Coordenada de ataque fallido
        S: Sonido que indica que falló el ataque
        R: --
        """
    def sonido_salpi(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Sonidos/Salpicadura.mp3")
        pygame.mixer.music.play(loops=0)

    """
    self.sonido_explo: Método que ejecuta un sonido de explosion cuando se realiza un impacto a un barco rival
    E: Coordenada de ataque exitoso
    S: Sonido que indica que acertó el ataque
    R: --
    """
    def sonido_explo(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Sonidos/Sonido_explo.mp3")
        pygame.mixer.music.play(loops=0)

    """
    self.sonido_victoria: Método que ejecuta un sonido de victoria cuando el jugador gana el juego
    E: Numero de barcos del rival
    S: Sonido de victoria 
    R: El numero de barcos del rival debe ser 1 para saber que ya todos fueron destruidos
    """
    def sonido_victoria(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Sonidos\Sonido_Victoria.mp3")
        pygame.mixer.music.play(loops=0)
    """
    self.sonido_derrota:Método que ejecuta un sonido de derrota cuando el jugador pierde el juego
    E: Numero de barcos del jugador
    S: Sonido de derrota 
    R: El numero de barcos del jugador debe ser 1 para saber que ya todos fueron destruidos
    """
    def sonido_derrota(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Sonido_Derrota.mp3")
        pygame.mixer.music.play(loops=0)
    """
    self.imagen_atacar: Método que genera una imagen de ataque exitoso (Equis roja) o fallido (Equis blanca) según corresponda por parte del jugador
    E: Número definido en las entradas de ubicacion de fila y columna de atacar
    S: Genera una imagen de ataque exitoso o fallido segun los numeros de entrada
    R: Los numeros de fila y columna tienen que ser entre 0 y 9 y aparte, tiene que ser el turno del jugador
    """
    def imagen_atacar(self):
        global turno
        global nuf
        global nuc
        global matriz2
        global barco_riv
        global turnos
        self.valor_entry_ata_f()
        self.valor_entry_ata_c()

        if 0<=nuc<=9 and 0<=nuf<=9 and barco_riv!=0 and matriz2[nuf][nuc] != 2: # matriz2[nuf][nuc] != 2 permite evitar atacar 2 veces en un mismo lugar, si detecta que la matriz2[nuf][nuc] == 2 es porque ya se ha atacado esa coordenada
            if matriz2[nuf][nuc] == 1: # Si el jugador acierta un ataque
                self.game_canvas.create_image(835 + nuc * 47, 118 + nuf * 46, image=self.img_acertar, anchor="nw")
                barco_riv -= 1
                self.sonido_explo()
                self.victoria()
            else:
                self.game_canvas.create_image(835 + nuc * 47, 118 + nuf * 46, image=self.img_fallar, anchor="nw")
                self.sonido_salpi()
            turnos += 1
            self.turno_label.config(text="Turnos: " + str(turnos))
            matriz2[nuf][nuc] = 2
            turno = False
            self.game_window.after(2000,self.atacar_rival)
    """
    self.atacar_rival=Método en el cual se crean imágenes sobre la cuadrícula del rival y se modifica su matriz
    E: Llamada de self.btn_ata
    R: la global turno debe ser igual a False
    S: Ataque hacia el rival
    """
    def atacar_rival(self):
        global turno
        nuf_riv=None
        nuc_riv=None
        global matriz1
        global barco_jug
        global turnos
        global barco_riv
        if turno == False: # Cuando el no es el turno del jugador, es decir, le toca al rival jugar
            nuf_riv = random.randint(0, 9)
            nuc_riv = random.randint(0, 9)
            if matriz1[nuf_riv][nuc_riv] != 2 and barco_jug !=0 and barco_riv !=0: # Verificar si el rival está atacando una casilla nueva
                if matriz1[nuf_riv][nuc_riv] == 1: # Cuando el rival acierta
                    self.game_canvas.create_image(91 + nuc_riv * 47, 120 + nuf_riv * 46, image=self.img_acertar, anchor="nw")
                    barco_jug -= 1
                    self.sonido_explo()
                else:
                    self.game_canvas.create_image(91 + nuc_riv * 47, 120 + nuf_riv * 46, image=self.img_fallar, anchor="nw")
                    self.sonido_salpi()
                matriz1[nuf_riv][nuc_riv] = 2 # Marca la casilla como ya atacada
                turno = True
            else:
                nuf_riv = random.randint(0, 9)
                nuc_riv = random.randint(0, 9)
                return self.atacar_rival()
    """
    self.victoria:Método que reproduce un sonido de victoria al ganar y llama a la ventana de victoria
    E: Llamada del atributo self.imagen_atacar
    R: La global barco_riv debe ser igual a 0
    S: Destrucción de la ventana del juego, reproducción del sonido victoria y llamada a la clase Ven_victoria
    """
    def victoria(self):
        global barco_riv
        global corre_tiempo
        corre_tiempo = False
        if barco_riv==0:
            self.sonido_victoria()
            self.game_window.after(3000, Ven_victoria)
            self.game_window.after(3000,self.game_window.destroy)

    """
    self.derrota: Método que reproduce un sonido de derrota al perder y llama a la ventana de derrota
    E: Llamada por parte del método self.atacar_rival
    R: La variable global barco_jug debe ser igual a 0
    S: Destrucción de la ventana del juego, reproducción del sonido derrota y llamada a la clase Ven_derrota
    """
    def derrota(self):
        global barco_jug
        if barco_jug==0:
            self.sonido_derrota()
            self.game_window.after(4000, self.game_window.destroy)



    """
    self.imagenes_barco:Método que ubica los barcos de la partida guardada
    E:Llamada por parte del init
    R:-
    S:Ubicación de cada uno de los barcos guardados en la parida anterior
    """
    def imagenes_barco(self):
        global matriz_pos
        n = len(matriz_pos)
        m = len(matriz_pos[0])
        for i in range(n):
            for j in range(m):
                if matriz_pos[i][j] == 1:
                    self.game_canvas.create_image(91 + j * 47, 120 + i * 46, image=self.img_marcar, anchor="nw")

    """
    self.imagenes_ataques_rival:Método que carga los ataques realizados por el rival en la partida anterior
    E:Llamada por parte del init
    R:-
    S:Ubicación de cada uno de los ataques del rival en la parida anterior
    """
    def imagenes_ataques_rival(self):
        global matriz_pos
        global matriz1
        n = len(matriz_pos)
        m = len(matriz_pos[0])
        for i in range(n):
            for j in range(m):
                if matriz_pos[i][j] == 1 and matriz1[i][j] == 2:
                    self.game_canvas.create_image(91 + j * 47, 120 + i * 46, image=self.img_acertar, anchor="nw")
                elif matriz_pos[i][j] == 0 and matriz1[i][j] == 2:
                    self.game_canvas.create_image(91 + j * 47, 120 + i * 46, image=self.img_fallar, anchor="nw")

    """
    self.imagenes_ataques_jugador:Método que carga los ataques realizados por el juagador en la partida anterior
    E:Llamada por parte del init
    R:-
    S:Ubicación de cada uno de los ataques del jugador en la parida anterior
    """
    def imagenes_ataques_jug(self):
        global matriz_pos_rival
        global matriz2
        n = len(matriz_pos_rival)
        m = len(matriz_pos_rival[0])
        for i in range(n):
            for j in range(m):
                if matriz_pos_rival[i][j] == 1 and matriz2[i][j] == 2:
                    self.game_canvas.create_image(835 + j * 47, 118 + i * 46, image=self.img_acertar, anchor="nw")
                elif matriz_pos_rival[i][j] == 0 and matriz2[i][j] == 2:
                    self.game_canvas.create_image(835 + j * 47, 118 + i * 46, image=self.img_fallar, anchor="nw")




    """
    self.asignar_glob:Método que asigna a las variables globales los valores que tenian previamente en la 
    partida anterior
    E: Llamada por parte del init
    S:Asignación de los valores previos a las variables globales
    R:-
    """
    def asignar_glob(self):
        global lista_glob
        global hora
        global minuto
        global segundo
        global turnos
        global barco_jug
        global barco_riv
        hora = int(lista_glob[4])
        minuto = int(lista_glob[5])
        segundo = int(lista_glob[6])
        turnos = int(lista_glob[7])
        barco_jug = int(lista_glob[9])
        barco_riv = int(lista_glob[10])
    """
    self.obtener_matriz1:Método para obtener la matriz de la partida guardada del jugador
    E:Llamada del init
    R:-
    S:Obtención de la matriz del jugador cargada previamente
    """
    def obtener_matriz1(self):
        global matriz1
        matriz1 = list(lista_glob[0])
        matrizre=[]
        matrizt=[]
        i=0
        j=0
        z=0
        while j !=10:
            if i==10:
                matrizre+=[matrizt]
                matrizt=[]
                j+=1
                i=0
            else:
                if matriz1[z]==' ' or matriz1[z]==',' or matriz1[z]=='[' or matriz1[z]==']':
                    z+=1
                else:
                    matrizt+=[int(matriz1[z])]
                    i+=1
                    z+=1
        matriz1= matrizre
    """
    self.obtener_matriz2:Método para obtener la matriz de la partida guardada del rival
    E:Llamada del init
    R:-
    S:Obtención de la matriz del rival cargada previamente
    """
    def obtener_matriz2(self):
        global matriz2
        matriz2 = list(lista_glob[1])
        matrizre=[]
        matrizt=[]
        i=0
        j=0
        z=0
        while j !=10:
            if i==10:
                matrizre+=[matrizt]
                matrizt=[]
                j+=1
                i=0
            else:
                if matriz2[z]==' ' or matriz2[z]==',' or matriz2[z]=='[' or matriz2[z]==']':
                    z+=1
                else:
                    matrizt+=[int(matriz2[z])]
                    i+=1
                    z+=1
        matriz2= matrizre

    def obtener_matriz_jug(self):
        global matriz_pos
        matriz_pos = list(lista_glob[2])
        matrizre=[]
        matrizt=[]
        i=0
        j=0
        z=0
        while j !=10:
            if i==10:
                matrizre+=[matrizt]
                matrizt=[]
                j+=1
                i=0
            else:
                if matriz_pos[z]==' ' or matriz_pos[z]==',' or matriz_pos[z]=='[' or matriz_pos[z]==']':
                    z+=1
                else:
                    matrizt+=[int(matriz_pos[z])]
                    i+=1
                    z+=1
        matriz_pos= matrizre

    def obtener_matriz_riv(self):
        global matriz_pos_rival
        matriz_pos_rival = list(lista_glob[3])
        matrizre=[]
        matrizt=[]
        i=0
        j=0
        z=0
        while j !=10:
            if i==10:
                matrizre+=[matrizt]
                matrizt=[]
                j+=1
                i=0
            else:
                if matriz_pos_rival[z]==' ' or matriz_pos_rival[z]==',' or matriz_pos_rival[z]=='[' or matriz_pos_rival[z]==']':
                    z+=1
                else:
                    matrizt+=[int(matriz_pos_rival[z])]
                    i+=1
                    z+=1
        matriz_pos_rival= matrizre

    """ 
    self.cargar_turnos:Método que reconoce la cantidad de turnos cargados del archivo de texto
    E:Llamada del init
    S:Actualización de la cantidad de turnos acumulados
    R:-
    """
    def cargar_turnos(self):
        global turnos
        self.turno_label.config(text="Turnos: " + str(turnos))

class Ven_derrota:
    def __init__(self):
        #Parámetros de la ventana
        self.ventana_d = Tk()
        self.ventana_d.title("Battle Ship")
        self.ventana_d.geometry("800x700")
        self.ventana_d.resizable(False, False)
        #Creación del canvas
        self.canvas_d = Canvas(self.ventana_d, width=800, height=700, bg="#EE4D1E")
        self.canvas_d.pack()
        #Label de felicitación
        self.perdiste = Label(self.ventana_d, text="Game Over", font=("Helvetica", 50),bg="#EE4D1E")
        self.perdiste.place(x= 210, y= 60)
        #Label donde aparece la cantidad de tiempo empleado por el jugador
        self.tiempo_label = Label(self.ventana_d, text="Tiempo: "+str(f'{hora}:{minuto}:{segundo}'), font=("Helvetica", 40),bg="#EE4D1E")
        self.tiempo_label.place(x= 220, y= 180)
        #Label donde aparece la cantidad de turnos requeridos por el jugador
        self.turno_label = Label(self.ventana_d, text="Turnos: "+str(turnos), font=("Helvetica", 40),bg="#EE4D1E")
        self.turno_label.place(x= 220, y= 270)
        #Botón para volver al menú
        self.btn_menu = Button(self.ventana_d, text='Volver al menú',  bg="#E5C379",font=("Arial", 25), command= self.volver_menu)
        self.btn_menu.place(x=150, y=510)
        #Botón para reintentar
        self.btn_rei = Button(self.ventana_d, text='Reintentar',  bg="#E97E49",font=("Arial", 25), command= self.reintentar)
        self.btn_rei.place(x=450, y=510)

        self.ventana_d.mainloop()
    """
    self.volver_menu:Método para regresar a la ventana de menú
    E: Llamada por parte del self.btn_menu
    S: Devolverse a la ventana de menu
    R:-
    """
    def volver_menu(self):
        self.ventana_d.destroy()
        menu()

    """
    self.volver_menu:Método para regresar a la ventana de juego
    E: Llamada por parte del self.btn_rei
    S: Devolverse a la ventana de juego
    R:-
    """
    def reintentar(self):
        self.ventana_d.destroy()
        Game()
class Ven_ayuda1:
    def __init__(self):
        # Parámetros de la ventana
        self.ventana_a1 = Tk()
        self.ventana_a1.title("Battle Ship")
        self.ventana_a1.geometry("800x700")
        self.ventana_a1.resizable(False, False)
        # Creación del canvas
        self.canvas_a1 = Canvas(self.ventana_a1, width=800, height=700, bg="#FFFFFF")
        self.canvas_a1.pack()
        #creación de la imagen de fondo
        self.fondo = Image.open("imagenes\Ayuda1.png")
        self.fondo = self.fondo.resize((800, 700), Image.ANTIALIAS)
        self.img_fondo = ImageTk.PhotoImage(self.fondo)
        self.canvas_a1.create_image(0, 0, image=self.img_fondo, anchor="nw")
        # Botón para ver más
        self.btn_vm = Button(self.ventana_a1, text="Ver más", font=("Arial", 15), borderwidth=2,command=self.ver_mas)
        self.btn_vm.place(x=320, y=650)
        # Botón para volver al menú
        self.btn_menu = Button(self.ventana_a1, text="Menú", font=("Arial", 15), borderwidth=2, command=self.menu)
        self.btn_menu.place(x=430, y=650)


        self.ventana_a1.mainloop()
    """
    self.ver_mas:Método que destruye la ventana de ayuda 1 y llama a la siguiente ventana de ayuda
    E:Llamada por parte del self.btn_vm
    R:-
    S:Destrucción de la vetana_a1 y llamada a la clase Ven_ayuda2
    """
    def ver_mas(self):
        self.ventana_a1.destroy()
        Ven_ayuda2()
    """
    self.menu:Método que destruye la ventana de ayuda 1 y llama a la ventana de Menu
    E:Llamada por parte del self.btn_menu
    R:-
    S:Destrucción de la vetana_a1 y llamada a la clase menu
    """
    def menu(self):
        self.ventana_a1.destroy()
        menu()

class Ven_ayuda2:
    def __init__(self):
        # Parámetros de la ventana
        self.ventana_a2 = Tk()
        self.ventana_a2.title("Battle Ship")
        self.ventana_a2.geometry("800x700")
        self.ventana_a2.resizable(False, False)
        # Creación del canvas
        self.canvas_a2 = Canvas(self.ventana_a2, width=800, height=700, bg="#FFFFFF")
        self.canvas_a2.pack()
        #creación de la imagen de fondo
        self.fondo = Image.open("imagenes\Ayuda2.png")
        self.fondo = self.fondo.resize((800, 700), Image.ANTIALIAS)
        self.img_fondo = ImageTk.PhotoImage(self.fondo)
        self.canvas_a2.create_image(0, 0, image=self.img_fondo, anchor="nw")
        # Botón para ver más
        self.btn_vm = Button(self.ventana_a2, text="Regresar", font=("Arial", 15), borderwidth=2,command=self.regresar)
        self.btn_vm.place(x=120, y=650)
        # Botón para volver al menú
        self.btn_menu = Button(self.ventana_a2, text="Menú", font=("Arial", 15), borderwidth=2, command=self.menu)
        self.btn_menu.place(x=230, y=650)


        self.ventana_a2.mainloop()
    """
    self.regresar:Método que destruye la ventana de ayuda 2 y llama a la anterior ventana de ayuda
    E:Llamada por parte del self.btn_vm
    R:-
    S:Destrucción de la vetana_a1 y llamada a la clase Ven_ayuda1
    """
    def regresar(self):
        self.ventana_a2.destroy()
        Ven_ayuda1()
    """
    self.menu:Método que destruye la ventana de ayuda 2 y llama a la ventana de Menu
    E:Llamada por parte del self.btn_menu
    R:-
    S:Destrucción de la vetana_a2 y llamada a la clase menu
    """
    def menu(self):
        self.ventana_a2.destroy()
        menu()
splash()
