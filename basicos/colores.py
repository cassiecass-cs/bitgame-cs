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

# Clase para modelar un color mediante un nombre descriptivo y su tupla RGB asociada
class Color:
    
    def __init__(self, nombre: str, valor):
        self.nombre = nombre
        self.valor = valor

class GestorColores:
    def __init__(self):
        self.colores = {}
        
    def manejarColor(self, color: Color):
        self.colores[color.nombre] = color  # Guardamos el objeto, no la tupla
        
    def obtenerColor(self, nombre: str) -> Color:
        return self.colores.get(nombre, Color("NEGRO", (0, 0, 0)))