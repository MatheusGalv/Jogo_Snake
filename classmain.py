import pygame
import random

class SnakeGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Jogo Snake Python")
        self.largura, self.altura = 600, 400
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.relogio = pygame.time.Clock()

        # Cores RGB
        self.preta = (0, 0, 0)
        self.branca = (255, 255, 255)
        self.vermelha = (255, 0, 0)
        self.verde = (0, 255, 0)

        # Parâmetros da cobra
        self.tamanho_quadrado = 20
        self.velocidade_jogo = 15

    def gerar_comida(self):
        comida_x = round(random.randrange(0, self.largura - self.tamanho_quadrado) / float(self.tamanho_quadrado)) * float(self.tamanho_quadrado)
        comida_y = round(random.randrange(0, self.altura - self.tamanho_quadrado) / float(self.tamanho_quadrado)) * float(self.tamanho_quadrado)
        return comida_x, comida_y

    def desenhar_comida(self, comida_x, comida_y):
        pygame.draw.rect(self.tela, self.verde, [comida_x, comida_y, self.tamanho_quadrado, self.tamanho_quadrado])

    def desenhar_cobra(self, pixels):
        for pixel in pixels:
            pygame.draw.rect(self.tela, self.branca, [pixel[0], pixel[1], self.tamanho_quadrado, self.tamanho_quadrado])

    def desenhar_pontuacao(self, pontuacao):
        fonte = pygame.font.SysFont("Helvetica", 35)
        texto = fonte.render(f"Pontos: {pontuacao}", True, self.vermelha)
        self.tela.blit(texto, [1, 1])

    def selecionar_velocidade(self, tecla):
        if tecla == pygame.K_DOWN:
            return 0, self.tamanho_quadrado
        elif tecla == pygame.K_UP:
            return 0, -self.tamanho_quadrado
        elif tecla == pygame.K_RIGHT:
            return self.tamanho_quadrado, 0
        elif tecla == pygame.K_LEFT:
            return -self.tamanho_quadrado, 0
        return 0, 0

    def rodar_jogo(self):
        fim_jogo = False

        x = self.largura / 2
        y = self.altura / 2

        velocidade_x = 0
        velocidade_y = 0

        tamanho_cobra = 1
        pixels = []

        comida_x, comida_y = self.gerar_comida()

        while not fim_jogo:
            self.tela.fill(self.preta)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_jogo = True
                elif evento.type == pygame.KEYDOWN:
                    velocidade_x, velocidade_y = self.selecionar_velocidade(evento.key)

            # Desenhar comida
            self.desenhar_comida(comida_x, comida_y)

            # Atualizar a posição da cobra
            if x < 0 or x >= self.largura or y < 0 or y >= self.altura:
                fim_jogo = True

            x += velocidade_x
            y += velocidade_y

            # Desenhar cobra
            pixels.append([x, y])
            if len(pixels) > tamanho_cobra:
                del pixels[0]

            # Se a cobra bater em seu próprio corpo
            for pixel in pixels[:-1]:
                if pixel == [x, y]:
                    fim_jogo = True

            self.desenhar_cobra(pixels)

            # Desenhar pontos
            self.desenhar_pontuacao(tamanho_cobra - 1)

            # Atualização da tela
            pygame.display.update()

            # Criar uma nova comida
            if x == comida_x and y == comida_y:
                tamanho_cobra += 1
                comida_x, comida_y = self.gerar_comida()

            self.relogio.tick(self.velocidade_jogo)

if __name__ == "__main__":
    jogo = SnakeGame()
    jogo.rodar_jogo()