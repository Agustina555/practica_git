
# Evita los enemigos / pygame
print("Cambio realizado desde la web de GitHub")
import pygame
import random
# Inicializar Pygame
pygame.init()

# Configuración de la ventana
Ancho, Alto = 600, 700
pantalla = pygame.display.set_mode((Ancho, Alto))
pygame.display.set_caption("Evita los enemigos")
reloj = pygame.time.Clock()

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 200, 255)

# Jugador
jugador_ancho = 60
jugador_alto = 20

jugador_x = Ancho // 2 - jugador_ancho // 2
jugador_y = Alto - 60

velocidad_jugador = 7

jugador = pygame.Rect(
    jugador_x,
    jugador_y,
    jugador_ancho,
    jugador_alto
)
# Enemigos
enemigos = []
enemigo_ancho = 40
enemigo_alto = 40

velocidad_enemigos = 5

# Puntaje 
puntaje = 0
fuente = pygame.font.SysFont("Arial", 30)

# funcion para crear enemigos
def crear_enemigo():
    x = random.randint(0, Ancho - enemigo_ancho)

    enemigo = pygame.Rect(
        x,
        0,
        enemigo_ancho,
        enemigo_alto
    )

    enemigos.append(enemigo)

# Bucle principal (loop)
ejecutando = True
game_over = False

while ejecutando:

    reloj.tick(60)

    # Eventos
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()

    if not game_over:

        if teclas[pygame.K_LEFT] and jugador.left > 0:
            jugador.x -= velocidad_jugador

        if teclas[pygame.K_RIGHT] and jugador.right < Ancho:
            jugador.x += velocidad_jugador

        # Crear enemigos aleatoriamente
        if random.randint(1, 25) == 1:
            crear_enemigo()

        # Mover enemigos
        for enemigo in enemigos[:]:

            enemigo.y += velocidad_enemigos

            # Colisión
            if jugador.colliderect(enemigo):
                game_over = True

            # Eliminar enemigos que salen
            if enemigo.top > Alto:
                enemigos.remove(enemigo)
                puntaje += 1
                # Aumentar dificultad
                if puntaje % 5 == 0:
                    velocidad_enemigos += 0.5

    # Dibujar 
    pantalla.fill(NEGRO)

    # Jugador
    pygame.draw.rect(pantalla, AZUL, jugador)

    # Enemigos
    for enemigo in enemigos:
        pygame.draw.rect(pantalla, ROJO, enemigo)

    # Puntaje
    texto_puntaje = fuente.render(
        f"Puntaje: {puntaje}",
        True,
        BLANCO
    )

    pantalla.blit(texto_puntaje, (20, 20))

    # Game Over
    if game_over:

        texto_game_over = fuente.render(
            "GAME OVER",
            True,
            ROJO
        )

        pantalla.blit(
            texto_game_over,
            (Ancho // 2 - 100, Alto // 2)
        )

    pygame.display.update()

# Esc para salir 
pygame.quit()
