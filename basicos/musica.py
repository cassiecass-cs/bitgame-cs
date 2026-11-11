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
Módulo de gestión de audio para el motor del juego.
Permite encapsular las pistas musicales y controlarlas de forma centralizada 
mediante un gestor desacoplado, siguiendo la misma filosofía del gestor de colores.
"""

import pygame

class Musica:
    """
    Representa una entidad de audio individual (pista musical).
    Almacena los metadatos básicos de la pista (su identificador único y la ruta al archivo).
    """
    
    def __init__(self, nombre: str, ruta: str):
        """
        Inicializa una nueva pista de música.

        Args:
            nombre (str): Identificador único o clave de la pista (ej. "CYBER_THEME").
            ruta (str): Ruta relativa o absoluta hacia el archivo de audio (ej. "musica/pista.ogg").
        """
        self.nombre = nombre
        self.ruta = ruta

    def obtenerNombre(self) -> str:
        """Retorna el nombre o identificador único de la pista."""
        return self.nombre

    def obtenerRuta(self) -> str:
        """Retorna la ruta del archivo de audio asociado a la pista."""
        return self.ruta
    

class GestorMusica:
    """
    Administrador centralizado de audio.
    Se encarga de registrar, almacenar y controlar la reproducción de las diferentes 
    pistas musicales del juego utilizando un diccionario de acceso por clave.
    """
    
    def __init__(self):
        """Inicializa el mezclador de Pygame y el diccionario de almacenamiento de pistas."""
        pygame.mixer.init()
        self.pistas = {}

    def manejarMusica(self, musica: Musica):
        """
        Registra o almacena una pista musical en el gestor utilizando su nombre como clave.

        Args:
            musica (Musica): Instancia de la clase Musica que se desea registrar.
        """
        self.pistas[musica.obtenerNombre()] = musica.obtenerRuta()

    def reproducir(self, nombre: str, volumen: float = 0.4,loop=-1):
        """
        Busca una pista registrada por su nombre y comienza su reproducción en bucle infinito.

        Args:
            nombre (str): Clave de la pista a reproducir.
            volumen (float, opcional): Nivel de volumen entre 0.0 y 1.0. Por defecto es 0.4.
        """
        if nombre in self.pistas:
            ruta = self.pistas[nombre]
            try:
                pygame.mixer.music.load(ruta)
                pygame.mixer.music.set_volume(volumen)
                pygame.mixer.music.play(loop)  # -1 configura la reproducción en bucle infinito
            except pygame.error as e:
                print(f"Error al reproducir la música '{nombre}': {e}")
        else:
            print(f"La pista '{nombre}' no está registrada en el gestor.")

    def detener(self):
        """Detiene de forma inmediata la reproducción de la música actual."""
        pygame.mixer.music.stop()