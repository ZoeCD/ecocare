"""
Esta aplicación fue realizada por el equipo de ECOCARE del curso de Cambio Climático y Uso de Energía en Agosto - Diciembre 2018.
Integrantes:
Zoe Caballero Domínguez
Alberto Contreras Torres
Diego Herrero Vázquez
Francisco Ariel Arenas Enciso

Esta aplicación tiene como objetivo ayudar al usuario a encontrar lugares dónde pueda llevar los materiales a reciclar y así disminuir los
desperdicios.
Dejamos el código para que futuras generaciones puedan mejorarlo e implementarlo en la comunidad.

El programa funciona desplegando imágenes con la información con ayuda de la librería de pygame

"""

#Librerias
import pygame

#Dimensiones de la pantalla
ANCHO = 400
ALTO = 711

#Colores
BLANCO = (225,225,225)

#Estados
MENU = 1
MATERIALES = 2
PAPEL = 3
CARTON = 4
VIDRIO = 5
PLASTICO = 6
CONOCENOS = 7


#Funciones que dibujan cada ventana
def dibujarMenu(ventana, imgMenu):
    ventana.blit (imgMenu, (0,0))

def dibujarMateriales(ventana, imgMateriales):
    ventana.blit(imgMateriales,(0,0))

def dibujarPapel(ventana, imgPapel):
    ventana.blit(imgPapel,(0,0))

def dibujarCarton(ventana, imgCarton):
    ventana.blit(imgCarton,(0,0))

def dibujarVidrio(ventana, imgVidrio):
    ventana.blit(imgVidrio,(0,0))

def dibujarPlastico(ventana, imgPlastico):
    ventana.blit(imgPlastico,(0,0))

def dibujarConocenos(ventana, imgConocenos):
    ventana.blit(imgConocenos,(0,0))


#Inicia pygame y contiene las intrucciones para los cambios de ventanas
def dibujar():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    #fondos
    imgMenu = pygame.image.load("1.png")
    imgMateriales = pygame.image.load ("2.png")
    imgPapel = pygame.image.load("3.png")
    imgCarton = pygame.image.load("5.png")
    imgVidrio = pygame.image.load("4.png")
    imgPlastico = pygame.image.load("6.png")
    imgConocenos = pygame.image.load("7.png")

    #INICIO
    estado = MENU

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            elif evento.type == pygame.MOUSEBUTTONUP: #Posiciones de los botones
                xm, ym = pygame.mouse.get_pos()
                if xm>86 and xm<313 and ym>316 and ym<392 and estado==MENU:
                    estado = MATERIALES
                elif xm>86 and xm<313 and ym>425 and ym<501 and estado==MENU:
                    estado = CONOCENOS
                elif xm>21 and xm<377 and ym>143 and ym<213 and estado == MATERIALES:
                    estado = PAPEL
                elif xm>21 and xm<377 and ym>272 and ym<343 and estado == MATERIALES:
                    estado = CARTON
                elif xm>21 and xm<377 and ym>405 and ym<472 and estado == MATERIALES:
                    estado = VIDRIO
                elif xm>21 and xm<377 and ym>530 and ym<602 and estado == MATERIALES:
                    estado = PLASTICO
                elif (xm > 23 and xm < 57 and ym >22 and ym < 45) and (estado == MATERIALES or estado == CONOCENOS):
                    estado = MENU
                elif (xm > 23 and xm < 57 and ym >22 and ym < 45) and (estado == PAPEL or estado == CARTON or estado == VIDRIO or estado == PLASTICO):
                    estado = MATERIALES


        ventana.fill (BLANCO)

        #Dibujan cierta ventana de acuerdo al click que se realizó

        if estado == MATERIALES:
            dibujarMateriales(ventana, imgMateriales)
        elif estado == PAPEL:
            dibujarPapel(ventana, imgPapel)
        elif estado == CARTON:
            dibujarCarton(ventana, imgCarton)
        elif estado == VIDRIO:
            dibujarVidrio(ventana, imgVidrio)
        elif estado == PLASTICO:
            dibujarPlastico(ventana, imgPlastico)
        elif estado == CONOCENOS:
            dibujarConocenos(ventana, imgConocenos)
        elif estado == MENU:
            dibujarMenu(ventana, imgMenu)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def main():
    dibujar()

main()