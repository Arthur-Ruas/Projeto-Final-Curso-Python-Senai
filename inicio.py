# Importe da biblioteca Pygame
import pygame 

# Inicialização do Pygame
pygame.init()

# Tamanho da tela do jogo
screenSize = pygame.display.set_mode([700, 500])

# Looping para manter o jogo rodando até o jogador sair
running = True
while running:

    # Testando se o jogador fechou a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenche o fundo da tela
    screenSize.fill((255, 255, 255))

    # Desenha um círculo de cor azul no centro da tela
    pygame.draw.circle(screenSize, (0, 110, 230), (350, 250), 75) # Cor, posição, tamanho

    # Atualiza o display
    pygame.display.flip()

# Saindo do app
pygame.quit() 