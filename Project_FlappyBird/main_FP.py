#pip install pygame
import pygame
import random

# Tela
LARGURA, ALTURA = 400, 600

#Cores RGB
AZUL = (135, 206, 250)
VERDE =  (0, 200, 0)
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)

#Game
GRAVIDADE = 0.5
TAMANHO_PASSARO = 20
ESPACO_CANO = 200
LARGURA_CANO = 60
VELOCIDADE_CANO = 5
ALTURA_PULO = -10

#inicio
pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Flappy Bird")
fonte = pygame.font.SysFont("Arial", 30)
relogio = pygame.time.Clock()

PASSARO_X = 50
passaro_y = ALTURA//2
velocidade = 0

cano_x = LARGURA
cano_altura = random.randint(150, 450)

pontuacao = 0
ja_pontuou = False

rodando = True

#Definindo se está ou não rodando
while rodando:
    relogio.tick(60)
    tela.fill(AZUL)

    #Captura os comandos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            velocidade = ALTURA_PULO

    velocidade += GRAVIDADE
    passaro_y += velocidade

    pygame.draw.circle(tela, AMARELO, (PASSARO_X, int(passaro_y)), TAMANHO_PASSARO)

    cano_x -=   VELOCIDADE_CANO

    #Reiniciando o Cano
    if cano_x + LARGURA_CANO < 0:
        cano_x = LARGURA
        #Reseta o teste de pontuação assim que surge um novo cano
        ja_pontuou = False
        cano_altura = random.randint(150, 450)

    #Desenhando os canos
    pygame.draw.rect(tela, VERDE, (cano_x, 0, LARGURA_CANO, cano_altura))
    pygame.draw.rect(tela, VERDE,(cano_x, cano_altura + ESPACO_CANO, LARGURA_CANO, ALTURA))

    #Teste de colisão horizontal
    colidiu_horizontal = (
        PASSARO_X + TAMANHO_PASSARO > cano_x and
        PASSARO_X - TAMANHO_PASSARO < cano_x + LARGURA_CANO
    )

    #Teste de colisão vertical
    colidiu_vertical = (
        passaro_y - TAMANHO_PASSARO < cano_altura or
        passaro_y + TAMANHO_PASSARO > cano_altura + ESPACO_CANO
    )

    #Testa se houve colisão vertical ou horizontal
    colidiu_cano = colidiu_horizontal and colidiu_vertical

    #Testa se o passaro saiu da tela
    fora_da_tela = passaro_y > ALTURA or passaro_y < 0

    #Se colidiu ou saiu da tela o jogo finaliza
    if colidiu_cano or fora_da_tela:
        rodando = False


    #Contagem de pontos
    if cano_x + LARGURA_CANO < PASSARO_X and not ja_pontuou:
        pontuacao += 1
        ja_pontuou = True

    #Placar de contagem de pontos
    texto = fonte.render(f"Pontos : {pontuacao}", True, PRETO)
    tela.blit(texto, (10, 10))

    #Sempre atualiza a tela enquanto o jogo estiver rodando
    pygame.display.update()

pygame.quit()
