from turtle import up, update
import pygame
import random
import math
from pygame import mixer


pygame.init()
#establecer el modo en el que se muestra pygame
pantalla=pygame.display.set_mode((800,600))

#titulo e icono
pygame.display.set_caption('GalaxiWar')
icono = pygame.image.load('C:\\Users\\sgcov\\Desktop\\Codigos python\\__pycache__\\pruebas python\\galaxiwar\\vader.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('C:\\Users\\sgcov\\Desktop\\Codigos python\\__pycache__\\pruebas python\\galaxiwar\\stars.jpg')
#jugador
img_jugador=pygame.image.load('C:\\Users\\sgcov\\Desktop\\Codigos python\\__pycache__\\pruebas python\\galaxiwar\\obiwan.png')
jugador_x = 368#lo ubicamos en el centro que sería 400 menos la mitad de los 64 pixeles del icono.png
jugador_y = 500
jugador_x_cambio = 0

#agregar musica
mixer.music.load('C:\\Users\\sgcov\\Desktop\\Codigos python\\__pycache__\\pruebas python\\galaxiwar\\banda.mp3')
#mixer.music.set_volume(0.3) esto sirve para bajar y subir volumen
mixer.music.play(-1)
#enemigo multiple
img_enemigo=[]
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_de_enemigos = 10

for e in range(cantidad_de_enemigos):
    #enemigo
    img_enemigo.append(pygame.image.load('C:\\Users\\sgcov\\Desktop\\Codigos python\\__pycache__\\pruebas python\\galaxiwar\\overdark.png'))
    enemigo_x.append(random.randint(0,736))#lo ubicamos en el centro que sería 400 menos la mitad de los 64 pixeles del icono.png
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)



#bala
img_bala=pygame.image.load('C:\\Users\\sgcov\\Desktop\\Codigos python\\__pycache__\\pruebas python\\galaxiwar\\misil2.png')
bala_x = 0#lo ubicamos en el centro que sería 400 menos la mitad de los 64 pixeles del icono.png
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

#datos creador
fuente2 = pygame.font.Font('freesansbold.ttf', 0)
texto_a = 10
texto_b = 550


#puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

#texto final del juego
fuente_final = pygame.font.Font('freesansbold.ttf', 40)

def datos_programador(x,y):
    texto2 = fuente.render('Programador: Javier Fiestas Botella',True,(0,255,0))
    pantalla.blit(texto2, (x, y))
    


def texto_final():
    mi_fuente_final = fuente_final.render('GAME OVER', True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (220, 200))


def mostrar_puntaje(x,y):
    texto = fuente.render(f'Score: {puntaje}',True,(0,255,0))
    pantalla.blit(texto, (x, y))
#funcion para ubicar el jugador
def jugador(x,y):
    #blit=metodo que significa arrojar y ponemos la figura acompañado de una tupla con las coordenadas domde se aloja
    pantalla.blit(img_jugador, (x, y))
# funcion enemigo
def enemigo(x,y, ene):
    #blit=metodo que significa arrojar y ponemos la figura acompañado de una tupla con las coordenadas domde se aloja
    pantalla.blit(img_enemigo[ene], (x, y))

def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_1-x_2,2) + math.pow(y_2-y_1,2))
    if distancia < 27:
        return True
    else:
        return False

#para que la pantalla no se vaya solo salga al darle a la x que es =QUIT
se_ejecuta = True
while se_ejecuta:
    #color del fondo
    #pantalla.fill((205, 144 , 228))
    pantalla.blit(fondo,(0,0))
    for evento in pygame.event.get():
        #evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        #evento al presionar flecha
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3#esto es lo que da el movimiento
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("C:\\Users\\sgcov\\Desktop\\Codigos python\\__pycache__\\pruebas python\\galaxiwar\\sss.mp3")
                sonido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x,bala_y)
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
        
    #modificar ubicacion del jugador
    jugador_x += jugador_x_cambio
    
    #mantener dentro de los bordes
    if jugador_x <=0:
        jugador_x = 0
    elif jugador_x >=736:
        jugador_x = 736

    #modificar ubicacion del enemigo
    for e in range(cantidad_de_enemigos):

        #fin del juego
        if enemigo_y[e] > 480:
            for k in range(cantidad_de_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            datos_programador(texto_a,texto_b)
            break
        enemigo_x[e] += enemigo_x_cambio[e]
    
    #mantener dentro de los bordes
        if enemigo_x[e] <=0.3:
            enemigo_x_cambio[e] = 0.3
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >=736:
            enemigo_x_cambio[e] = -0.3
            enemigo_y[e] += enemigo_y_cambio[e]

        #colision
        colision = hay_colision(enemigo_x[e],enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound("C:\\Users\\sgcov\\Desktop\\Codigos python\\__pycache__\\pruebas python\\galaxiwar\\lll.mp3")
            sonido_colision.play()
            bala_y = -500 
            bala_visable = False
            puntaje += 1
            enemigo_x[e] = random.randint(0,736)#lo ubicamos en el centro que sería 400 menos la mitad de los 64 pixeles del icono.png
            enemigo_y[e] = random.randint(50,200)

        enemigo(enemigo_x[e],enemigo_y[e], e)
    
    
    #movimiento bala
    if bala_y <= -64:
        bala_y =500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio
   
    
    jugador(jugador_x,jugador_y)
    mostrar_puntaje(texto_x, texto_y)
    
    
    pygame.display.update()
