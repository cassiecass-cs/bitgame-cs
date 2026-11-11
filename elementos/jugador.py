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
from basicos.figuras import Rectangulo
from basicos.gravedad import EfectoGravedad

# Entidad Jugador controlada por el usuario (movimiento lateral, salto y físicas propias)
class Jugador(Rectangulo):
     
    def __init__(self, ancho: int, alto: int, x: int, y: int, color):
        super().__init__(ancho, alto, x, y, color)
        
        self.movimiento = 7
        self.fueraDelSuelo = True
        self.efecto_gravedad = EfectoGravedad(0, 0.5)

    def manejar_evento(self, evento):
        """Procesa los eventos de teclado específicos del jugador (como saltar)."""
        if evento.type == pygame.KEYDOWN:
            if (evento.key == pygame.K_UP or evento.key == pygame.K_w) and not self.fueraDelSuelo:
                self.efecto_gravedad.VELOCIDAD_Y = -10
                self.fueraDelSuelo = True

    def actualizar(self, ancho_pantalla, suelo):
        """Gestiona el movimiento horizontal continuo, la gravedad y las colisiones."""
        
        # 1. Movimiento horizontal continuo (teclas mantenidas)
        teclas = pygame.key.get_pressed()
        
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.FORMA.x -= self.movimiento
            if self.FORMA.x < 0:
                self.FORMA.x = 0
                
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.FORMA.x += self.movimiento
            if self.FORMA.right >= ancho_pantalla:
                self.FORMA.right = ancho_pantalla

        # 2. Aplicación de gravedad vertical
        self.FORMA.y += self.efecto_gravedad.gravedad()
        
        # 3. Colisión con el suelo
        if self.FORMA.colliderect(suelo):
            if self.efecto_gravedad.VELOCIDAD_Y > 0:
                self.FORMA.bottom = suelo.top
                self.fueraDelSuelo = False
                self.efecto_gravedad.VELOCIDAD_Y = 0

    def dibujar(self, ventana):
        """Método para renderizarse usando los atributos heredados."""
        pygame.draw.rect(ventana, self.obtenerColor(), self.FORMA)