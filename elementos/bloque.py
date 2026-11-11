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
from basicos.figuras import Cuadrado
from basicos.gravedad import EfectoGravedad
from basicos.colores import GestorColores
import random

# Entidad Bloque autónoma (maneja su propio tamaño, peso, físicas y renderizado)
class Bloque(Cuadrado):
    def __init__(self, ancho: int, alto: int, x: int, y: int, color, factor_gravedad: float = 0.5):
        super().__init__(ancho, alto, x, y, color)    
        
        # Cada bloque gestiona su propio peso/gravedad internamente
        self.efecto_gravedad = EfectoGravedad(0, factor_gravedad)
        
        # Aquí puedes dejar listas las bases para futuros tamaños o propiedades DLC
        self.ancho_personalizado = ancho
        self.alto_personalizado = alto

    def actualizar(self):
        """El bloque calcula su propio movimiento vertical en función de su gravedad."""
        self.FORMA.y += self.efecto_gravedad.gravedad()

    def dibujar(self, ventana):
        """El bloque se renderiza a sí mismo usando su forma y color heredados."""
        pygame.draw.rect(ventana, self.obtenerColor(), self.FORMA)
        

class BloqueNormal(Bloque):
    
    def __init__(self,x,y,gestorColores):
        super().__init__(50, 50, x, y, gestorColores.obtenerColor("ROJO"), random.choice([0.3,0.4]))
        
class BloqueGrande(Bloque):
    
    def __init__(self,x,y,gestorColores):
        super().__init__(70, 70, x, y, gestorColores.obtenerColor("ROJO"), random.choice([0.5,0.6]))