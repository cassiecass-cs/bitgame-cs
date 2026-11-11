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

CÓMO FUNCIONA EL JUEGO:
1. ARQUITECTURA MODULAR (POO): El juego está estructurado mediante clases que separan 
   responsabilidades: gestión de colores, formas geométricas, entidades (jugador y bloques), 
   control del tiempo (temporizadores), efectos físicos (gravedad) y el motor principal (Juego).
2. BUCLE PRINCIPAL (GAME LOOP): Se ejecuta a 60 FPS estables controlados por un objeto reloj. 
   En cada fotograma se procesan tres fases: eventos, física/lógica y renderizado.
3. FÍSICA Y COLISIONES: 
   - El jugador cae aplicando gravedad acumulativa de forma constante hasta colisionar con el suelo.
   - Se puede saltar con las teclas W o Flecha Arriba (siempre y cuando se esté apoyado en el suelo).
   - Los bloques rojos aparecen periódicamente en la parte superior y caen hacia el suelo, eliminándose 
     al tocarlo o terminando el juego si colisionan con el jugador.
4. SISTEMA DE PUNTUACIÓN: Un temporizador incrementa el puntaje en +1 cada segundo que el jugador 
   logre sobrevivir esquivando los bloques.
"""""
from basicos.colores import Color,GestorColores
from basicos.musica import Musica,GestorMusica
from motor.arranque import Juego

def main():
    
    negro = Color("NEGRO",(0, 0, 0))
    gris = Color("GRIS",(100, 100, 100))
    blanco = Color("BLANCO",(255, 255, 255))
    rojo = Color("ROJO",(255, 0, 0))
    
    gestorColores = GestorColores()
    gestorColores.manejarColor(negro)
    gestorColores.manejarColor(gris)
    gestorColores.manejarColor(blanco)
    gestorColores.manejarColor(rojo)
    
    # Instancias tu pista apuntando al archivo que descargaste en la carpeta 'musica'
    pista_cyberpunk = Musica("CYBER_THEME", "musica/Techno_5.mp3")
    
    gestorMusica = GestorMusica()
    gestorMusica.manejarMusica(pista_cyberpunk)
    
    juego = Juego(1280,720,"Bit Corrupción - Cassie Cass",60)
    juego.administradorColores(gestorColores)
    juego.administradorMusica(gestorMusica)
    juego.play()
    
main()