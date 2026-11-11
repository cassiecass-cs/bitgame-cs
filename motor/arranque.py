# Copyright (C) 2026 Cassie Cass
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
Version: 1.2
Author: Cassie Cass
License: GNU General Public License v3.0 (GPLv3)

---
"""

import pygame
import sys
import random
from basicos.colores import GestorColores
from basicos.musica import GestorMusica
from basicos.figuras import Rectangulo
from elementos.jugador import Jugador
from elementos.bloque import BloqueNormal,BloqueGrande
from elementos.temporizador import Temporizador
from elementos.labels import Texto

# Motor principal del juego que inicializa la ventana, recursos y bucle de juego
class Juego():
    
    def __init__(self, ancho: int, alto: int, titulo: str, fps: int = 60):
        pygame.init()
        self.ANCHO = ancho
        self.ALTO  = alto

        self.ventana = pygame.display.set_mode((self.ANCHO, self.ALTO))
        pygame.display.set_caption(titulo)

        self.RELOJ = pygame.time.Clock()
        self.FPS = fps
        self.dificuldad = 0

    def administradorColores(self, gestorColores: GestorColores):
        self.GESTORCOLORES = gestorColores
    
    def administradorMusica(self,gestorMusica:GestorMusica):
        self.GESTORMUSICA = gestorMusica
        
    def play(self):
        en_ejecucion = True
        
        
        while en_ejecucion:
            self.GESTORMUSICA.reproducir("CYBER_THEME", volumen=0.4)    
            # 1. INSTANCIACIÓN DE ESCENARIO Y ENTIDADES AUTÓNOMAS
            suelo = Rectangulo(1280, 100, 0, 600, self.GESTORCOLORES.obtenerColor("GRIS"))
            jugador = Jugador(50, 50, 20, 340, self.GESTORCOLORES.obtenerColor("BLANCO"))
            
            cronometro_enemigos = Temporizador(1000)
            cronometro_puntaje = Temporizador(1000)
            lista_bloques = []
            
            texto_del_puntaje = Texto("Puntaje: 0", True, self.GESTORCOLORES.obtenerColor("BLANCO"), "Arial", 20)
            visualizador_de_fps = Texto("FPS: 0", True, self.GESTORCOLORES.obtenerColor("BLANCO"), "Arial", 20)
            texto_game_over = Texto("", True, self.GESTORCOLORES.obtenerColor("ROJO"), "Arial", 40)
            
            puntaje = 0
            jugando_partida = True
            
            while jugando_partida:
                
                # --- 2. GESTIÓN DE EVENTOS ---
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        jugando_partida = False
                        en_ejecucion = False
                    elif evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_ESCAPE:
                            jugando_partida = False
                            en_ejecucion = False
                    
                    # El jugador procesa sus propios eventos de entrada (como saltar)
                    jugador.manejar_evento(evento)

                # --- 3. ACTUALIZACIÓN DE FÍSICAS Y LÓGICA DE ENTIDADES ---
                # El jugador actualiza su movimiento y colisión con el suelo internamente
                jugador.actualizar(self.ANCHO, suelo.obtenerFigura())

                self.tipos_bloques = [BloqueNormal,BloqueGrande]
                # Generación automática de bloques enemigos en intervalos controlados
                if cronometro_enemigos.es_momento():
                    
                    if puntaje <= 20:
                        self.dificultad  = 4
                    elif puntaje <= 40:
                        self.dificultad  = 8
                    elif puntaje <= 60:
                        self.dificultad  = 12
                    elif puntaje <= 100:
                        self.dificultad  = 14
                    
                    for _ in range(random.randint(1, self.dificultad)):
                        posicion_aleatoria_x = random.randint(0, self.ANCHO - 50)
                        
                        bloque_a_generar = random.choice(self.tipos_bloques)
                        
                        nuevo_bloque = bloque_a_generar(
                            posicion_aleatoria_x, 20, 
                            self.GESTORCOLORES
                        )
                        lista_bloques.append(nuevo_bloque)
                
                # Actualización y chequeo de colisiones de los bloques activos
                for i in range(len(lista_bloques) - 1, -1, -1):
                    bloque = lista_bloques[i]
                    
                    # Cada bloque gestiona y calcula su propia actualización física
                    bloque.actualizar()
                
                    # Si el bloque toca el suelo, se elimina de la lista
                    if bloque.obtenerFigura().colliderect(suelo.obtenerFigura()):
                        lista_bloques.pop(i)
                   
                    # Si el bloque toca al jugador, finaliza la partida actual
                    elif bloque.obtenerFigura().colliderect(jugador.obtenerFigura()):
                        jugando_partida = False
                        break
                
                # Incremento del puntaje basado en tiempo de supervivencia
                if cronometro_puntaje.es_momento():
                    puntaje += 1
                
                # --- 4. RENDERIZADO VISUAL ---
                color_ventana = self.GESTORCOLORES.obtenerColor("NEGRO")
                self.ventana.fill(color_ventana.valor)
                
                # Dibujar el suelo (elemento estático del escenario)
                pygame.draw.rect(self.ventana, suelo.obtenerColor(), suelo.obtenerFigura())
                
                # Cada entidad se encarga de dibujarse a sí misma en la pantalla
                jugador.dibujar(self.ventana)
                
                for bloque in lista_bloques:
                    bloque.dibujar(self.ventana)
                
                # Actualizar y dibujar los textos usando sus propios métodos encapsulados
                texto_del_puntaje.cambiarTexto(f"Puntaje: {puntaje}")
                texto_del_puntaje.dibujar(self.ventana, 10, 10)
                
                visualizador_de_fps.cambiarTexto(f"FPS: {int(self.RELOJ.get_fps())}")
                visualizador_de_fps.dibujar(self.ventana, 1060, 10)
                
                # Actualizar pantalla y mantener los FPS estables
                pygame.display.flip()
                self.RELOJ.tick(self.FPS)

            # --- PANTALLA DE GAME OVER FLUIDA (Sin congelar la ventana) ---
            if en_ejecucion:
                tiempo_inicio_espera = pygame.time.get_ticks()
                esperando = True
                
                while esperando:
                    for evento in pygame.event.get():
                        if evento.type == pygame.QUIT:
                            esperando = False
                            en_ejecucion = False
                        elif evento.type == pygame.KEYDOWN:
                            if evento.key == pygame.K_RETURN or evento.key == pygame.K_SPACE:
                                esperando = False

                    self.ventana.fill(self.GESTORCOLORES.obtenerColor("NEGRO").valor)
                    texto_game_over.cambiarTexto(f"¡GAME OVER! Puntaje final: {puntaje}")
                    texto_game_over.dibujar(self.ventana, self.ANCHO // 2 - 250, self.ALTO // 2 - 20)
                    
                    pygame.display.flip()
                    
                    # Pausa de 3 segundos sin congelar el sistema operativo
                    if pygame.time.get_ticks() - tiempo_inicio_espera > 3000:
                        esperando = False

                    self.RELOJ.tick(self.FPS)

        pygame.quit()
        sys.exit()