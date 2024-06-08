# Importe da biblioteca Pygame
import pygame 

# Importe random para números aleatorios
import random

# Importe do pygame.locals para fácil acesso as coordenadas chaves
# Atualização para atender os padrões flake8 e black
from pygame.locals import ( RLEACCEL, K_UP, K_RIGHT, K_DOWN, K_LEFT, K_ESCAPE, KEYDOWN, QUIT ) # Teclas

# Definição de constantes para altura e largura da tela
screenSizeHeight = 600
screenSizeWidth = 800

# Definindo o objeto 'jogador' extendendo a classe pygame.sprite.sprite
# A surface desenhada na tela será um atributo de 'jogador'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surface = pygame.image.load("./images/jet.png").convert()
        self.surface.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surface.get_rect()

    # Movendo o sprite com base nas teclas pressionadas
    def update(self, pressedKeys):
        if pressedKeys[K_UP]:
            self.rect.move_ip(0, -8)
            moveUpSound.play()
        if pressedKeys[K_DOWN]:
            self.rect.move_ip(0, 8)
            moveDownSound.play()
        if pressedKeys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressedKeys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Mantendo o jogador dentro da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screenSizeWidth:
            self.rect.right = screenSizeWidth
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screenSizeHeight:
            self.rect.bottom = screenSizeHeight

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surface = pygame.image.load("./images/missile.png").convert()
        self.surface.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surface.get_rect(
            center=(
                random.randint(screenSizeWidth + 20, screenSizeWidth + 100),
                random.randint(0, screenSizeHeight),
            )
        )
        self.speed = random.randint(5, 20) # Velocidade do inimigo

    # Movendo o sprite com base na velocidade
    # Removendo o sprite quando atinge o lado esquerdo da tela
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

# Definindo as nuvens
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surface = pygame.image.load("./images/cloud.png").convert()
        self.surface.set_colorkey((0, 0, 0), RLEACCEL)
        # Posicionando de maneira aleatoria
        self.rect = self.surface.get_rect(
            center=(
                random.randint(screenSizeWidth + 20, screenSizeWidth + 100),
                random.randint(0, screenSizeHeight),
            )
        )

    # Movendo a nuvem baseando-se na velocidade
    # Removendo a nuvem quando passar do lado esquerdo
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
            
# Inicialização do mixer de som            
pygame.mixer.init()

# Inicialização do Pygame
pygame.init()

# Configuração do som
pygame.mixer.init()

# Ajustando para ter uma taxa de frames
clock = pygame.time.Clock()

# Criação do objeto da tela com as constantes
screen = pygame.display.set_mode((screenSizeWidth, screenSizeHeight))

# Looping principal para mantes o jogo rodando
running = True

# Criando um evento para adicionar os inimigos
addEnemy = pygame.USEREVENT + 1
pygame.time.set_timer(addEnemy, 250)

# Criando um evento para adicionar as nuvens
addClound = pygame.USEREVENT + 2
pygame.time.set_timer(addClound, 1000)

# Instanciando o jogador
player = Player()

# Criando um grupo para manter os sprites
# - enemies é usado para detectar colisão e atualizar a posição
# - clouds é usada para atualizar a posição
# - allSprites é usado para renderização
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
allSprites = pygame.sprite.Group()
allSprites.add(player)

while running:
    
    # Carrega e toca a música de fundo
    # Sound source: http://ccmixter.org/files/Apoxode/59262
    # License: https://creativecommons.org/licenses/by/3.0/
    pygame.mixer.music.load("./sounds/Apoxode_-_Electric_1.mp3")
    pygame.mixer.music.play(loops=-1)

    # Carrega todos os arquivos de som
    # Sound sources: Jon Fincher
    moveUpSound = pygame.mixer.Sound("./sounds/Rising_putter.ogg")
    moveDownSound = pygame.mixer.Sound("./sounds/Falling_putter.ogg")
    collisionSound = pygame.mixer.Sound("./sounds/Collision.ogg")

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

        # Adicionando um inimigo
        elif event.type == addEnemy:
            # Criando um novo inimigo e o adicionando no grupo de enemies
            newEnemy = Enemy()
            enemies.add(newEnemy)
            allSprites.add(newEnemy)

        # Adicionando uma nuvem
        elif event.type == addClound:
            # Criando uma nova nuvem e a adicionando no grupo de nuvens
            newCloud = Cloud()
            clouds.add(newCloud)
            allSprites.add(newCloud)

    # Usando o conjunto de teclas pressionadas e verificando a entrada do usuário
    pressedKeys = pygame.key.get_pressed()

    # Atualizando a posição dos inimigos
    enemies.update()

    # Atualizando a posição das nuvens
    clouds.update()

    # Atuaizando o sprite com base nas teclas pressionadas
    player.update(pressedKeys)
            
    # Preenchendo a tela com a cor do céu
    screen.fill((135, 206, 250))

    # Desenhando o 'jogador' sobre 'screen'
    screen.blit(player.surface, player.rect)

    # Draw all sprites
    for entity in allSprites:
        screen.blit(entity.surface, entity.rect)

    # Checando se o inimigo colidiu com o jogador
    if pygame.sprite.spritecollideany(player, enemies):
        # Se colidiu, irá remover o player e parar o programa
        player.kill()
        running = False

        # Para a música e roda o som de colisão
        moveUpSound.stop()
        moveDownSound.stop()
        collisionSound.play()

    # Atualiza o display para exibir o conteúdo
    pygame.display.flip()

    # Garantindo que o programa tenha uma taxa de frames de 30
    clock.tick(30)

pygame.mixer.music.stop()
pygame.mixer.quit() 