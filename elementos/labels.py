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

# Clase Texto encargada de gestionar y renderizar tipografías en pantalla
class Texto:
    
    def __init__(self, texto: str, antiAnalising: bool, color, fuente: str, tamano: int):
        self.TEXTO = texto
        self.ANTIANALISING = antiAnalising
        self.COLOR = color
        self.FUENTE = pygame.font.SysFont(fuente, tamano)
    
    def cambiarTexto(self, texto: str):
        """Actualiza la cadena de texto a mostrar."""
        self.TEXTO = texto
    
    def obtenerColor(self):
        """Retorna el valor crudo del color."""
        return self.COLOR.valor
    
    def cambiarColor(self, color):
        """Cambia el color del texto."""
        self.COLOR = color
    
    def dibujar(self, ventana, x: int, y: int):
        """Renderiza y dibuja el texto directamente en la ventana en las coordenadas dadas."""
        superficie_texto = self.FUENTE.render(self.TEXTO, self.ANTIANALISING, self.obtenerColor())
        ventana.blit(superficie_texto, (x, y))