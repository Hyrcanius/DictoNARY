import math
import pygame
import sys

# --- 1. MOTOR MATEMÁTICO ---
class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector2D(self.x + otro.x, self.y + otro.y)

    def __mul__(self, escalar: float):
        return Vector2D(self.x * escalar, self.y * escalar)

    @classmethod
    def desde_polar(cls, magnitud: float, angulo_grados: float):
        angulo_radianes = math.radians(angulo_grados)
        return cls(magnitud * math.cos(angulo_radianes), magnitud * math.sin(angulo_radianes))


class Proyectil:
    def __init__(self, x_inicial: float, y_inicial: float, velocidad_vector: Vector2D):
        self.posicion = Vector2D(x_inicial, y_inicial)
        self.velocidad = velocidad_vector

    def actualizar(self, dt: float, gravedad: Vector2D):
        self.velocidad = self.velocidad + (gravedad * dt)
        self.posicion = self.posicion + (self.velocidad * dt)


# --- 2. CONFIGURACIÓN DE PYGAME ---
pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("PhysiCode 2D - Multi-Parábolas (Espacio para disparar)")

COLOR_FONDO = (20, 24, 33)
COLOR_PELOTA = (255, 87, 34)
COLOR_SUELO = (76, 175, 80)
COLOR_RASTRO = (150, 150, 150)

reloj = pygame.time.Clock()

# --- 3. INICIALIZACIÓN DE VARIABLES ---
gravedad = Vector2D(0, -9.8)
dt = 0.15
rastro_posiciones = []

# Control de ángulos para los disparos consecutivos
angulo_actual = 15
velocidad_inicial = Vector2D.desde_polar(magnitud=75, angulo_grados=angulo_actual)
pelota = Proyectil(x_inicial=50, y_inicial=50, velocidad_vector=velocidad_inicial)

# --- 4. BUCLE PRINCIPAL ---
ejecutando = True

while ejecutando:
    # CAPTURA DE EVENTOS (Teclado y Mouse)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
            
        # Si el usuario PRESIONA una tecla
        if evento.type == pygame.KEYDOWN:
            # Si esa tecla es la BARRA ESPACIADORA
            if evento.key == pygame.K_SPACE:
                # Aumentamos el ángulo para el siguiente tiro
                angulo_actual += 15
                
                # Si nos pasamos de 90 grados, reiniciamos el lienzo
                if angulo_actual > 80:
                    angulo_actual = 15
                    rastro_posiciones.clear() # Limpiamos la pantalla
                
                # Creamos una nueva pelota con el nuevo ángulo
                nueva_velocidad = Vector2D.desde_polar(magnitud=75, angulo_grados=angulo_actual)
                pelota = Proyectil(x_inicial=50, y_inicial=50, velocidad_vector=nueva_velocidad)

    # FÍSICA
    if pelota.posicion.y >= 50:
        pelota.actualizar(dt, gravedad)
        pos_x = int(pelota.posicion.x)
        pos_y = int(ALTO - pelota.posicion.y)
        rastro_posiciones.append((pos_x, pos_y))

    # RENDERIZADO
    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(pantalla, COLOR_SUELO, (0, ALTO - 50, ANCHO, 50))

    # Dibujamos TODOS los rastros acumulados
    for punto in rastro_posiciones:
        pygame.draw.circle(pantalla, COLOR_RASTRO, punto, 2)

    # Dibujamos la pelota
    if pelota.posicion.y >= 50:
        pos_actual_x = int(pelota.posicion.x)
        pos_actual_y = int(ALTO - pelota.posicion.y)
        pygame.draw.circle(pantalla, COLOR_PELOTA, (pos_actual_x, pos_actual_y), 12)
    else:
        if rastro_posiciones:
            pygame.draw.circle(pantalla, COLOR_PELOTA, rastro_posiciones[-1], 12)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()