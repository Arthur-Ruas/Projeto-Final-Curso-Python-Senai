# Importe da biblioteca Pygame
import pygame 

# Importe do pygame.locals para fácil acesso as coordenadas chaves
# Atualização para atender os padrões flake8 e black
from pygame.locals import ( K_UP, K_RIGHT, K_DOWN, K_LEFT, K_ESCAPE, KEYDOWN, QUIT ) # Teclas

# Definição de constantes para altura e largura da tela
screenSizeHeight = 600
screenSizeWidth = 800

# Definindo o objeto 'jogador' extendendo a classe pygame.sprite.sprite
# A surface desenhada na tela será um atributo de 'jogador'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surface = pygame.Surface((75, 25))
        self.surface.fill((255, 255, 255))
        self.rect = self.surface.get_rect()

# Inicialização do Pygame
pygame.init()

# Criação do objeto da tela com as constantes
screen = pygame.display.set_mode((screenSizeWidth, screenSizeHeight))

# Looping principal para mantes o jogo rodando
running = True

# Instanciando o jogador
player = Player()

while running:
    
    # Verificando os eventos da fila
    for event in pygame.event.get():

        # Verificando se alguma tecla foi pressionada
        if event.type == KEYDOWN: 

            # Verifica se a tecla ESC foi pressionada
            if event.type == K_ESCAPE:
                running = False

        # Verifica se o jogador fechou a janela do aplicativo
        elif event.type == QUIT:
            running = False
            
    # Preenchendo a tela com a cor branca
    screen.fill((100, 100, 100))

    # Criando uma superfície (surface) e passe uma tupla com altura e comprimento
    #surface = pygame.Surface((50, 50))

    # Dando ao 'surface' uma dor
    #surface.fill((255, 80, 110))
    #rect = surface.get_rect()

    # Colocando a 'surface' no centro de 'screen'
    #surfaceCenter = (
    #    (screenSizeWidth - surface.get_width()) / 2,
    #    (screenSizeHeight - surface.get_height()) / 2
    #) 

    # Desenhando a surface sobre 'screen'
    #screen.blit(surface, surfaceCenter)

    # Desenhando o 'jogador' sobre 'screen'
    screen.blit(player.surface, (screenSizeWidth / 2, screenSizeHeight / 2))

    # Atualiza o display para exibir o conteúdo
    pygame.display.flip()
        