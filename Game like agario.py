import pygame
import sys
import random
import math

ancho = 1250
largo = 700

pygame.init()

pantalla = pygame.display.set_mode((ancho, largo))
pygame.display.set_caption("prueba_agario")
pantalla.fill((255,255,255))
colorDep = (255, 0, 0)
colorPre = (0, 255, 0)
fuente_titulo = pygame.font.Font(None, 40)
fuente_boton = pygame.font.Font(None, 30)
fuente = pygame.font.Font(None, 20)
fuente2 = pygame.font.Font(None, 21)
ctd_pre = ""
ctd_dep = ""
ctd_com = ""
vel_pre = ""
vel_dep = ""
tasa_comida = ""
vida_pre = ""
vida_dep = ""
reap_pre = ""
reap_dep = ""
vel_sim = ""

velocidadSim = pygame.time.Clock()

comida = []
depredadores = []
presas = []

def crear_comida(cantidad):
    for i in range(cantidad):
        x = random.randint(20,930)
        y = random.randint(20,680)
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        
        comida.append((x, y, 5, color))

def crear_jugadores(cantidad, tipo_jugador):
    for i in range(cantidad):
        x = random.randint(30,920)
        y = random.randint(30,660)
        prox_comida = []
        prox_dep = []
        prox_presa = []
        tiempo_caza = []
        tiempo_actual = 0
        max_tiempo_comer = 0
        tiempo_actual_comer = 0

        if tipo_jugador == 0:
            presas.append([x, y, 10, colorPre, prox_comida, prox_dep])
        else:
            depredadores.append([x, y, 20, colorDep, prox_presa, tiempo_caza, tiempo_actual, max_tiempo_comer, tiempo_actual_comer])

def pintar(lista):
    for x in lista:
        pygame.draw.circle(pantalla, (x[3]), (x[0], x[1]), x[2])

def comer(jugador):

    distancia = math.sqrt((math.pow(jugador[0] - jugador[4][0], 2) + math.pow(jugador[1] - jugador[4][1], 2)))
    if distancia < jugador[2]:
        return True

def comer_jugador(depredador):

    distancia = math.sqrt((math.pow(depredador[0] - depredador[4][0], 2) + math.pow(depredador[1] - depredador[4][1], 2)))
    if distancia < depredador[2] - 5:
        return True

def detectar_depredador(jugador, objetivo):

    nearest = []
    mas_cercano = []

    for obj in objetivo:
        distancia = math.sqrt((math.pow(jugador[0] - obj[0], 2) + math.pow(jugador[1] - obj[1], 2)))

        nearest.append([distancia, obj])
    
    mas_cercano = sorted(nearest, key=lambda x: x[0])

    return mas_cercano[0][1]

def animacion_boton(ventana, boton, palabra):
    if boton.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(ventana, (237,128,19), boton, 0)
    else:
        pygame.draw.rect(ventana, (255,0,0), boton, 0)
        
    texto = fuente_titulo.render(palabra, True, (255,255,255))
    pantalla.blit(texto, (boton.x + (190-texto.get_width())/2, boton.y + (30-texto.get_height())/2))

def asignar_pre(pos):
    for i in range(len(presas) - pos):
        posibles = comida
        presas[i + pos][4] = random.choice(posibles)
        presas[i + pos][5] = detectar_depredador(presas[i], depredadores)
        posibles.remove(presas[i][4])
        comida.append(presas[i][4])

def asignar_dep(pos):
    for i in range(len(depredadores) - pos):
        depredadores[i + pos][4] = random.choice(presas)
        depredadores[i + pos][5] = random.randint(100, 600)
        depredadores[i + pos][7] = random.randint(500, 1200)
        
iteraciones = 0
cont_tiempo_pre = 0
cont_tiempo_dep = 0
running = True
bandera = 0

while running:

    velocidadSim.tick(60)

    if bandera < 2:
        pantalla.fill((255,255,255))

    pygame.draw.rect(pantalla, (0,0,0), (950, 0, 300, 700))
    pygame.draw.rect(pantalla, (255,255,255), (980, 10, 240, 35))

    pygame.draw.rect(pantalla, (255,255,255), (970, 80, 230, 25))
    pre_in = pygame.draw.rect(pantalla, (255,255,255), (1205, 80, 40, 25), 2)
    pygame.draw.rect(pantalla, (255,255,255), (970, 115, 230, 25))
    dep_in = pygame.draw.rect(pantalla, (255,255,255), (1205, 115, 40, 25), 2)
    pygame.draw.rect(pantalla, (255,255,255), (970, 150, 230, 25))
    com_in = pygame.draw.rect(pantalla, (255,255,255), (1205, 150, 40, 25), 2)

    pygame.draw.rect(pantalla, (255,255,255), (970, 205, 230, 25))
    t1 = pygame.draw.rect(pantalla, (255,255,255), (1205, 205, 40, 25), 2)
    pygame.draw.rect(pantalla, (255,255,255), (970, 240, 230, 25))
    t2 = pygame.draw.rect(pantalla, (255,255,255), (1205, 240, 40, 25), 2)
    pygame.draw.rect(pantalla, (255,255,255), (970, 275, 230, 25))
    t3 = pygame.draw.rect(pantalla, (255,255,255), (1205, 275, 40, 25), 2)
    pygame.draw.rect(pantalla, (255,255,255), (970, 310, 230, 25))
    t4 = pygame.draw.rect(pantalla, (255,255,255), (1205, 310, 40, 25), 2)
    pygame.draw.rect(pantalla, (255,255,255), (970, 345, 230, 25))
    t5 = pygame.draw.rect(pantalla, (255,255,255), (1205, 345, 40, 25), 2)
    pygame.draw.rect(pantalla, (255,255,255), (970, 380, 230, 25))
    t6 = pygame.draw.rect(pantalla, (255,255,255), (1205, 380, 40, 25), 2)
    pygame.draw.rect(pantalla, (255,255,255), (970, 415, 230, 25))
    t7 = pygame.draw.rect(pantalla, (255,255,255), (1205, 415, 40, 25), 2)
    pygame.draw.rect(pantalla, (255,255,255), (970, 450, 230, 25))
    t8 = pygame.draw.rect(pantalla, (255,255,255), (1210, 450, 30, 25), 2)
    boton = pygame.draw.rect(pantalla, (255,0,0), (1010, 620, 190, 30))
    boton2 = pygame.draw.rect(pantalla, (255,0,0), (1010, 660, 190, 30))

    pygame.draw.rect(pantalla, (255,255,255), (970, 505, 170, 25))
    pygame.draw.rect(pantalla, (255,255,255), (1150, 505, 40, 25), 2)
    pygame.draw.rect(pantalla, (255,255,255), (970, 540, 170, 25))
    pygame.draw.rect(pantalla, (255,255,255), (1150, 540, 40, 25), 2)
    pygame.draw.rect(pantalla, (255,255,255), (970, 575, 170, 25))
    pygame.draw.rect(pantalla, (255,255,255), (1150, 575, 80, 25), 2)

    titulo = fuente_titulo.render("Variables", True, (0,0,0))
    pre1 = fuente.render("Cantidad de presas inicial", True, (0,0,0))
    pre1_1 = fuente2.render(ctd_pre, True, (255,255,255))
    dep1 = fuente.render("Cantidad de depredadores inicial", True, (0,0,0))
    dep1_1 = fuente2.render(ctd_dep, True, (255,255,255))
    com1 = fuente.render("Cantidad de comida inicial", True, (0,0,0))
    com1_1 = fuente2.render(ctd_com, True, (255,255,255))
    texto1 = fuente.render("Velocidad presas", True, (0,0,0))
    texto1_1 = fuente2.render(vel_pre, True, (255,255,255))
    texto2 = fuente.render("Velocidad depredadores", True, (0,0,0))
    texto2_1 = fuente2.render(vel_dep, True, (255,255,255))
    texto3 = fuente.render("Tasa aparición comida", True, (0,0,0))
    texto3_1 = fuente2.render(tasa_comida, True, (255,255,255))
    texto4 = fuente.render("Tiempo de vida presas", True, (0,0,0))
    texto4_1 = fuente2.render(vida_pre, True, (255,255,255))
    texto5 = fuente.render("Tiempo de vida depredadores", True, (0,0,0))
    texto5_1 = fuente2.render(vida_dep, True, (255,255,255))
    texto6 = fuente.render("Tasa de reaparición presas", True, (0,0,0))
    texto6_1 = fuente2.render(reap_pre, True, (255,255,255))
    texto7 = fuente.render("Tasa de reaparición depredadores", True, (0,0,0))
    texto7_1 = fuente2.render(reap_dep, True, (255,255,255))
    texto8 = fuente.render("Velocidad de simulación", True, (0,0,0))
    texto8_1 = fuente2.render(vel_sim, True, (255,255,255))
    comenzar = fuente_titulo.render("Comenzar", True, (255,255,255))
    finalizar = fuente_boton.render("Finalizar", True, (255,255,255))

    campo_num_pre = fuente.render("Numero de presas", True, (0,0,0))
    num_pre = fuente2.render(str(len(presas)), True, (255,255,255))
    campo_num_dep = fuente.render("Numero de depredadores", True, (0,0,0))
    num_dep = fuente2.render(str(len(depredadores)), True, (255,255,255))
    campo_num_it = fuente.render("Numero de iteraciones", True, (0,0,0))
    num_it = fuente2.render(str(iteraciones), True, (255,255,255))

    pantalla.blit(titulo, (980 + (240-titulo.get_width())/2, 10 + (35-titulo.get_height())/2))
    pantalla.blit(pre1, (970 + (230-pre1.get_width())/2, 80 + (25-pre1.get_height())/2))
    pantalla.blit(pre1_1, (1212, 80 + (25-pre1_1.get_height())/2))
    pantalla.blit(dep1, (970 + (230-dep1.get_width())/2, 115 + (25-dep1.get_height())/2))
    pantalla.blit(dep1_1, (1212, 115 + (25-dep1_1.get_height())/2))
    pantalla.blit(com1, (970 + (230-com1.get_width())/2, 150 + (25-com1.get_height())/2))
    pantalla.blit(com1_1, (1208, 150 + (25-com1_1.get_height())/2))
    pantalla.blit(texto1, (970 + (230-texto1.get_width())/2, 205 + (25-texto1.get_height())/2))
    pantalla.blit(texto1_1, (1216, 205 + (25-texto1_1.get_height())/2))
    pantalla.blit(texto2, (970 + (230-texto2.get_width())/2, 240 + (25-texto2.get_height())/2))
    pantalla.blit(texto2_1, (1216, 240 + (25-texto2_1.get_height())/2))
    pantalla.blit(texto3, (970 + (230-texto3.get_width())/2, 275 + (25-texto3.get_height())/2))
    pantalla.blit(texto3_1, (1208, 275 + (25-texto3_1.get_height())/2))
    pantalla.blit(texto4, (970 + (230-texto4.get_width())/2, 310 + (25-texto4.get_height())/2))
    pantalla.blit(texto4_1, (1208, 310 + (25-texto4_1.get_height())/2))
    pantalla.blit(texto5, (970 + (230-texto5.get_width())/2, 345 + (25-texto5.get_height())/2))
    pantalla.blit(texto5_1, (1208, 345 + (25-texto5_1.get_height())/2))
    pantalla.blit(texto6, (970 + (230-texto6.get_width())/2, 380 + (25-texto6.get_height())/2))
    pantalla.blit(texto6_1, (1208, 380 + (25-texto6_1.get_height())/2))
    pantalla.blit(texto7, (970 + (230-texto7.get_width())/2, 415 + (25-texto7.get_height())/2))
    pantalla.blit(texto7_1, (1208, 415 + (25-texto7_1.get_height())/2))
    pantalla.blit(texto8, (970 + (230-texto8.get_width())/2, 450 + (25-texto8.get_height())/2))
    pantalla.blit(texto8_1, (1220, 450 + (25-texto8_1.get_height())/2))
    pantalla.blit(comenzar, (1010 + (190-comenzar.get_width())/2, 620 + (30-comenzar.get_height())/2))
    pantalla.blit(finalizar, (1010 + (190-finalizar.get_width())/2, 660 + (30-finalizar.get_height())/2))

    pantalla.blit(campo_num_pre, (970 + (170-campo_num_pre.get_width())/2, 505 + (25-campo_num_pre.get_height())/2))
    pantalla.blit(num_pre, (1155, 505 + (25-num_pre.get_height())/2))
    pantalla.blit(campo_num_dep, (970 + (170-campo_num_dep.get_width())/2, 540 + (25-campo_num_dep.get_height())/2))
    pantalla.blit(num_dep, (1155, 540 + (25-num_dep.get_height())/2))
    pantalla.blit(campo_num_it, (970 + (170-campo_num_it.get_width())/2, 575 + (25-campo_num_it.get_height())/2))
    pantalla.blit(num_it, (1155, 575 + (25-num_it.get_height())/2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pre_in.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 
                    or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5
                    or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 
                    or event.key == pygame.K_9 or event.key == pygame.K_BACKSPACE):
                    if len(ctd_pre) < 3:
                        ctd_pre += event.unicode
                        if event.key == pygame.K_BACKSPACE:
                            ctd_pre = ctd_pre[:-1]
                    if event.key == pygame.K_BACKSPACE:
                            ctd_pre = ctd_pre[:-1]

        if dep_in.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 
                    or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5
                    or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 
                    or event.key == pygame.K_9 or event.key == pygame.K_BACKSPACE):
                    if len(ctd_dep) < 3:
                        ctd_dep += event.unicode
                        if event.key == pygame.K_BACKSPACE:
                            ctd_dep = ctd_dep[:-1]
                    if event.key == pygame.K_BACKSPACE:
                            ctd_dep = ctd_dep[:-1]

        if com_in.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 
                    or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5
                    or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 
                    or event.key == pygame.K_9 or event.key == pygame.K_BACKSPACE):
                    if len(ctd_com) < 4:
                        ctd_com += event.unicode
                        if event.key == pygame.K_BACKSPACE:
                            ctd_com = ctd_com[:-1]
                    if event.key == pygame.K_BACKSPACE:
                            ctd_com = ctd_com[:-1]

        if t1.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 
                    or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5
                    or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 
                    or event.key == pygame.K_9 or event.key == pygame.K_BACKSPACE):
                    if len(vel_pre) < 2:
                        vel_pre += event.unicode
                        if event.key == pygame.K_BACKSPACE:
                            vel_pre = vel_pre[:-1]
                    if event.key == pygame.K_BACKSPACE:
                            vel_pre = vel_pre[:-1]

        if t2.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 
                    or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5
                    or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 
                    or event.key == pygame.K_9 or event.key == pygame.K_BACKSPACE):
                    if len(vel_dep) < 2:
                        vel_dep += event.unicode
                        if event.key == pygame.K_BACKSPACE:
                            vel_dep = vel_dep[:-1]
                    if event.key == pygame.K_BACKSPACE:
                                vel_dep = vel_dep[:-1]

        if t3.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 
                    or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5
                    or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 
                    or event.key == pygame.K_9 or event.key == pygame.K_BACKSPACE):
                    if len(tasa_comida) < 4:
                        tasa_comida += event.unicode
                        if event.key == pygame.K_BACKSPACE:
                            tasa_comida = tasa_comida[:-1]
                    if event.key == pygame.K_BACKSPACE:
                        tasa_comida = tasa_comida[:-1]

        if t4.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 
                    or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5
                    or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 
                    or event.key == pygame.K_9 or event.key == pygame.K_BACKSPACE):
                    if len(vida_pre) < 4:
                        vida_pre += event.unicode
                        if event.key == pygame.K_BACKSPACE:
                            vida_pre = vida_pre[:-1]
                    if event.key == pygame.K_BACKSPACE:
                            vida_pre = vida_pre[:-1]

        if t5.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 
                    or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5
                    or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 
                    or event.key == pygame.K_9 or event.key == pygame.K_BACKSPACE):
                    if len(vida_dep) < 4:
                        vida_dep += event.unicode
                        if event.key == pygame.K_BACKSPACE:
                            vida_dep = vida_dep[:-1]
                    if event.key == pygame.K_BACKSPACE:
                            vida_dep = vida_dep[:-1]

        if t6.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 
                    or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5
                    or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 
                    or event.key == pygame.K_9 or event.key == pygame.K_BACKSPACE):
                    if len(reap_pre) < 4:
                        reap_pre += event.unicode
                        if event.key == pygame.K_BACKSPACE:
                            reap_pre = reap_pre[:-1]
                    if event.key == pygame.K_BACKSPACE:
                            reap_pre = reap_pre[:-1]

        if t7.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 
                    or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5
                    or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 
                    or event.key == pygame.K_9 or event.key == pygame.K_BACKSPACE):
                    if len(reap_dep) < 4:
                        reap_dep += event.unicode
                        if event.key == pygame.K_BACKSPACE:
                            reap_dep = reap_dep[:-1]
                    if event.key == pygame.K_BACKSPACE:
                            reap_dep = reap_dep[:-1]

        if t8.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 
                    or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5
                    or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 
                    or event.key == pygame.K_9):
                    if len(vel_sim) < 1:
                        vel_sim += event.unicode
                    if len(vel_sim) == 1:
                        vel_sim = event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if boton.collidepoint(pygame.mouse.get_pos()):
                if ctd_pre != "" and ctd_dep != "" and ctd_com != "" and vel_pre != "" and vel_dep != "" and tasa_comida != "" and vida_pre != "" and vida_dep != "" and reap_pre != "" and reap_dep != "" and vel_sim != "":
                    crear_comida(int(ctd_com))
                    crear_jugadores(int(ctd_pre), 0)
                    crear_jugadores(int(ctd_dep), 1)
                    asignar_pre(0)
                    asignar_dep(0)
                    limite_comida = len(comida)/2
                    limite_presas = len(presas)/2
                    limite_depredadores = len(depredadores)/2
                    bandera = 1
            if boton2.collidepoint(pygame.mouse.get_pos()):
                ctd_pre = ""
                ctd_dep = ""
                ctd_com = ""
                vel_pre = ""
                vel_dep = ""
                tasa_comida = ""
                vida_pre = ""
                vida_dep = ""
                reap_pre = ""
                reap_dep = ""
                vel_sim = ""
                presas = []
                depredadores = []
                comida = []
                iteraciones = 0
                cont_tiempo_pre = 0
                cont_tiempo_dep = 0
                bandera = 0

    animacion_boton(pantalla, boton, "Comenzar")
    animacion_boton(pantalla, boton2, "Finalizar")

    if bandera == 1:

        if len(comida) <= limite_comida:
            crear_comida(int(tasa_comida))
            limite_comida = len(comida)/2
            
        if cont_tiempo_pre >= int(vida_pre):
            cont_tiempo_pre = 0
            for i in range(random.randint(1, len(presas))):
                presas.remove(random.choice(presas))

        if cont_tiempo_dep >= int(vida_dep):
            cont_tiempo_dep = 0
            for i in range(random.randint(1, len(depredadores))):
                depredadores.remove(random.choice(depredadores))
        
        if len(presas) > 0 and len(depredadores) > 0:
            
            lista_muerte = []

            for i in range(len(depredadores)):
                if depredadores[i][7] <= depredadores[i][8]:
                    lista_muerte.append(depredadores[i])
            
            for dep in lista_muerte:
                depredadores.remove(dep)

            if len(presas) > 0 and len(depredadores) > 0:

                if len(presas) <= limite_presas:
                    num = len(presas)
                    crear_jugadores(int(reap_pre), 0)
                    limite_presas = len(presas)/2
                    asignar_pre(num)
                    
                if len(depredadores) <= limite_depredadores:
                    num2 = len(depredadores)
                    crear_jugadores(int(reap_dep), 1)
                    limite_depredadores = len(depredadores)/2
                    asignar_dep(num2)

                pintar(comida)
                pintar(presas)
                pintar(depredadores)

                for i in range(len(presas)):
                    
                    dx = presas[i][0] - presas[i][5][0]
                    dy = presas[i][1] - presas[i][5][1]
                    dxy = abs(dx) + abs(dy)

                    if dxy >= 20 and dxy <= 80:

                        if dx < 0:
                            presas[i][0] -= int(vel_pre) * int(vel_sim)
                        if dx > 0:
                            presas[i][0] += int(vel_pre) * int(vel_sim)
                        if dy < 0:
                            presas[i][1] -= int(vel_pre) * int(vel_sim)
                        if dy > 0:
                            presas[i][1] += int(vel_pre) * int(vel_sim)

                        presas[i][4] = random.choice(comida)

                    else:

                        if presas[i][4] in comida:

                            cx = presas[i][0] - presas[i][4][0]
                            cy = presas[i][1] - presas[i][4][1]

                            if cx < 0:
                                presas[i][0] += int(vel_pre) * int(vel_sim)
                            if cx > 0:
                                presas[i][0] -= int(vel_pre) * int(vel_sim)
                            if cy < 0:
                                presas[i][1] += int(vel_pre) * int(vel_sim)
                            if cy > 0:
                                presas[i][1] -= int(vel_pre) * int(vel_sim)
                                        
                            alimentar = comer(presas[i])
                            if alimentar:
                                comida.remove(presas[i][4])
                                presas[i][4] = random.choice(comida)
                                
                        else:
                            presas[i][4] = random.choice(comida)

                        presas[i][5] = detectar_depredador(presas[i], depredadores)


                for i in range(len(presas)):
                    if presas[i][0] < presas[i][2]:
                        presas[i][0] = presas[i][2]
                    if presas[i][1] < presas[i][2]:
                        presas[i][1] = presas[i][2]
                    if presas[i][0] > 950 - presas[i][2]:
                        presas[i][0] = 950 - presas[i][2]
                    if presas[i][1] > largo - presas[i][2]:
                        presas[i][1] = largo - presas[i][2]

                for i in range(len(depredadores)):
                    if depredadores[i][0] < depredadores[i][2]:
                        depredadores[i][0] = depredadores[i][2]
                    if depredadores[i][1] < depredadores[i][2]:
                        depredadores[i][1] = depredadores[i][2]
                    if depredadores[i][0] > 950 - depredadores[i][2]:
                        depredadores[i][0] = 950 - depredadores[i][2]
                    if depredadores[i][1] > largo - depredadores[i][2]:
                        depredadores[i][1] = largo - depredadores[i][2]

                for i in range(len(depredadores)):

                    if depredadores[i][6] <= depredadores[i][5]:

                        if depredadores[i][4] in presas:
                            
                            px = depredadores[i][0] - depredadores[i][4][0]
                            py = depredadores[i][1] - depredadores[i][4][1]

                            if px < 0:
                                depredadores[i][0] += int(vel_dep) * int(vel_sim)
                            if px > 0:
                                depredadores[i][0] -= int(vel_dep) * int(vel_sim)
                            if py < 0:
                                depredadores[i][1] += int(vel_dep) * int(vel_sim)
                            if py > 0:
                                depredadores[i][1] -= int(vel_dep) * int(vel_sim)

                            cazar = comer_jugador(depredadores[i])
                            if cazar:
                                presas.remove(depredadores[i][4])

                                if len(presas) > 0:
                                    depredadores[i][4] = random.choice(presas)
                                    depredadores[i][5] = random.randint(100, 600)
                                    depredadores[i][7] = random.randint(500, 1200)
                                    depredadores[i][8] = 0
                                else:
                                    bandera = 2
                                    pantalla.fill((255,255,255))
                                    pintar(comida)
                                    pintar(depredadores)
                                    pygame.draw.rect(pantalla, (255,255,255), (0, 0, 950, 40))
                                    mensaje = fuente_titulo.render("La simulación ha finalizado", True, (0,0,0))
                                    pantalla.blit(mensaje, (0 + (950-mensaje.get_width())/2, 0 + (40-mensaje.get_height())/2))
                                    pygame.draw.rect(pantalla, (255,255,255), (0, 40, 950, 40))
                                    mensaje2 = fuente_titulo.render("porque se cazaron todas las presas", True, (0,0,0))
                                    pantalla.blit(mensaje2, (0 + (950-mensaje2.get_width())/2, 40 + (40-mensaje2.get_height())/2))

                        else:
                            if len(presas) > 0:
                                depredadores[i][4] = random.choice(presas)
                                depredadores[i][5] = random.randint(100, 600)
                            else:
                                bandera = 2
                                pantalla.fill((255,255,255))
                                pintar(comida)
                                pintar(depredadores)
                                pygame.draw.rect(pantalla, (255,255,255), (0, 0, 950, 40))
                                mensaje = fuente_titulo.render("La simulación ha finalizado", True, (0,0,0))
                                pantalla.blit(mensaje, (0 + (950-mensaje.get_width())/2, 0 + (40-mensaje.get_height())/2))
                                pygame.draw.rect(pantalla, (255,255,255), (0, 40, 950, 40))
                                mensaje2 = fuente_titulo.render("porque las presas se extinguieron", True, (0,0,0))
                                pantalla.blit(mensaje2, (0 + (950-mensaje2.get_width())/2, 40 + (40-mensaje2.get_height())/2))

                    else:
                        if len(presas) > 0:
                            depredadores[i][6] = 0
                            depredadores[i][4] = random.choice(presas)
                            depredadores[i][5] = random.randint(100, 600)
                        else:
                            bandera = 2
                            pantalla.fill((255,255,255))
                            pintar(comida)
                            pintar(depredadores)
                            pygame.draw.rect(pantalla, (255,255,255), (0, 0, 950, 40))
                            mensaje = fuente_titulo.render("La simulación ha finalizado", True, (0,0,0))
                            pantalla.blit(mensaje, (0 + (950-mensaje.get_width())/2, 0 + (40-mensaje.get_height())/2))
                            pygame.draw.rect(pantalla, (255,255,255), (0, 40, 950, 40))
                            mensaje2 = fuente_titulo.render("porque las presas se extinguieron", True, (0,0,0))
                            pantalla.blit(mensaje2, (0 + (950-mensaje2.get_width())/2, 40 + (40-mensaje2.get_height())/2))
                            

                    depredadores[i][6] += 1
                    depredadores[i][8] += 1

            else:
                bandera = 2
                pantalla.fill((255,255,255))
                pintar(comida)
                pintar(presas)
                pygame.draw.rect(pantalla, (255,255,255), (0, 0, 950, 40))
                mensaje = fuente_titulo.render("La simulación ha finalizado", True, (0,0,0))
                pantalla.blit(mensaje, (0 + (950-mensaje.get_width())/2, 0 + (40-mensaje.get_height())/2))
                pygame.draw.rect(pantalla, (255,255,255), (0, 40, 950, 40))
                mensaje2 = fuente_titulo.render("porque los depredadores se extinguieron", True, (0,0,0))
                pantalla.blit(mensaje2, (0 + (950-mensaje2.get_width())/2, 40 + (40-mensaje2.get_height())/2))

        else:
            bandera = 2

            if len(presas) == 0:
                pintar(comida)
                pintar(depredadores)
                pygame.draw.rect(pantalla, (255,255,255), (0, 0, 950, 40))
                mensaje = fuente_titulo.render("La simulación ha finalizado", True, (0,0,0))
                pantalla.blit(mensaje, (0 + (950-mensaje.get_width())/2, 0 + (40-mensaje.get_height())/2))
                pygame.draw.rect(pantalla, (255,255,255), (0, 40, 950, 40))
                mensaje2 = fuente_titulo.render("porque las presas se extinguieron", True, (0,0,0))
                pantalla.blit(mensaje2, (0 + (950-mensaje2.get_width())/2, 40 + (40-mensaje2.get_height())/2))
                
            if len(depredadores) == 0:
                pintar(comida)
                pintar(presas)
                pygame.draw.rect(pantalla, (255,255,255), (0, 0, 950, 40))
                mensaje = fuente_titulo.render("La simulación ha finalizado", True, (0,0,0))
                pantalla.blit(mensaje, (0 + (950-mensaje.get_width())/2, 0 + (40-mensaje.get_height())/2))
                pygame.draw.rect(pantalla, (255,255,255), (0, 40, 950, 40))
                mensaje2 = fuente_titulo.render("porque los depredadores se extinguieron", True, (0,0,0))
                pantalla.blit(mensaje2, (0 + (950-mensaje2.get_width())/2, 40 + (40-mensaje2.get_height())/2))

            if len(presas) == 0 and len(depredadores) == 0:
                pintar(comida)
                pygame.draw.rect(pantalla, (255,255,255), (0, 0, 950, 40))
                mensaje = fuente_titulo.render("La simulación ha finalizado", True, (0,0,0))
                pantalla.blit(mensaje, (0 + (950-mensaje.get_width())/2, 0 + (40-mensaje.get_height())/2))
                pygame.draw.rect(pantalla, (255,255,255), (0, 40, 950, 40))
                mensaje2 = fuente_titulo.render("porque las dos poblaciones se extinguieron", True, (0,0,0))
                pantalla.blit(mensaje2, (0 + (950-mensaje2.get_width())/2, 40 + (40-mensaje2.get_height())/2))
                

        if (int(vel_sim) == 0):
            iteraciones+=1
        else:
            iteraciones+=int(vel_sim)

        cont_tiempo_pre+=1
        cont_tiempo_dep+=1

    pygame.display.update()