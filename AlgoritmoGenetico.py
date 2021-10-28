#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
import numpy as np
#from string import maketrans

class AlgoritmoGenetico():
    """
        Algoritmo genético
    """
    tam_mapa = 132 # valor máixo do tamanho do jogo
    def __init__(self, x_min, x_max, tam_populacao, taxa_mutacao, taxa_crossover, num_geracoes):
        """
            Inicializa todos os atributos da instância
        """
        self.x_min = x_min
        self.x_max = x_max
        self.tam_populacao = tam_populacao
        self.taxa_mutacao = taxa_mutacao
        self.taxa_crossover = taxa_crossover
        self.num_geracoes = num_geracoes
        self.populacao = []
        # gera os individuos da população

    def _gerar_populacao(self):
        """
            Gera uma população de um determinado tamanho com individuos que possuem um número
            expecífico de bits
        """
        # Ground
        self.ground_population_vector = []
        self.ground_mating_vector = []
        self.elementIndividual = ElementIndividual(1, 9, 4, 3, 5, 10, 5, 5, 15, 3, 132)
        for _ in range(0, self.tam_populacao):
            self.ground_population_vector.append(self.elementIndividual._groundIndividual())

        for _ in range(0, self.tam_populacao):
            self.ground_mating_vector.append(self.elementIndividual._groundIndividual())

        # Block
        self.block_population_vector = []
        self.block_mating_vector = []
        for _ in range(0, self.tam_populacao):
            self.block_population_vector.append(self.elementIndividual._blockIndividual())

        for _ in range(0, self.tam_populacao):
            self.block_mating_vector.append(self.elementIndividual._blockIndividual())

        # Enemy
        self.enemy_population_vector = []
        self.enemy_mating_vector = []
        for _ in range(0, self.tam_populacao):
            self.enemy_population_vector.append(self.elementIndividual._enemyIndividual())

        for _ in range(0, self.tam_populacao):
            self.enemy_mating_vector.append(self.elementIndividual._enemyIndividual())

        # Coin
        self.coin_population_vector = []
        self.coin_mating_vector = []
        for _ in range(0, self.tam_populacao):
            self.coin_population_vector.append(self.elementIndividual._coinIndividual())

        for _ in range(0, self.tam_populacao):
            self.coin_mating_vector.append(self.elementIndividual._coinIndividual())

    # def _funcao_objetivo(self, individuo): # cálculo para selecionar o melhor vetor
    #     """
    #         Calcula a função objetivo utilizada para avlaiar as soluções produzidas
    #     """
    #     peso = individuo[0]*individuo[1]*(individuo[2]/individuo[1])
    #     print("Peso: ", peso)
    #     return peso

    def avaliarPopulacao(self):
        """
            Avalia as souluções produzidas, associando uma nota/avalição a cada elemento da população
        """
        print("\nGround:")
        self.ground_population_dp_vector = []
        self.ground_mating_dp_vector = []
        for individuo in self.ground_population_vector:
            print(individuo)
            print(np.std(individuo))
            self.ground_population_dp_vector.append(np.std(individuo))
        
        for individuo in self.ground_mating_vector:
            print(individuo)
            print(np.std(individuo))
            self.ground_mating_dp_vector.append(np.std(individuo))

        print("\nBlock:")
        self.block_population_dp_vector = []
        self.block_mating_dp_vector = []
        for individuo in self.ground_population_vector:
            print(individuo)
            print(np.std(individuo))
            self.block_population_dp_vector.append(np.std(individuo))
        
        for individuo in self.ground_mating_vector:
            print(individuo)
            print(np.std(individuo))
            self.block_mating_dp_vector.append(np.std(individuo))

        print("\nEnemy:")
        self.enemy_population_dp_vector = []
        self.enemy_mating_dp_vector = []
        for individuo in self.ground_population_vector:
            print(individuo)
            print(np.std(individuo))
            self.enemy_population_dp_vector.append(np.std(individuo))
        
        for individuo in self.ground_mating_vector:
            print(individuo)
            print(np.std(individuo))
            self.enemy_mating_dp_vector.append(np.std(individuo))

        print("\nCoin:")
        self.coin_population_dp_vector = []
        self.coin_mating_dp_vector = []
        for individuo in self.ground_population_vector:
            print(individuo)
            print(np.std(individuo))
            self.coin_population_dp_vector.append(np.std(individuo))
        
        for individuo in self.ground_mating_vector:
            print(individuo)
            print(np.std(individuo))
            self.coin_mating_dp_vector.append(np.std(individuo))

    def avaliarNovaPopulacao(self, nova_populacao):
        """
            Avalia as souluções produzidas, associando uma nota/avalição a cada elemento da população
        """
        print("Nova População: ", nova_populacao)
        # print(np.std(ground_new_population_vector))
        

    def avaliar(self):
        """
            Avalia as souluções produzidas, associando uma nota/avalição a cada elemento da população
        """
        individuo_escolhido = []
        desvio_padrao = 10
        ground = []
        for individuo in self.populacao:
            ground = individuo[0]
            if np.std(ground) <= desvio_padrao:
                individuo_escolhido = individuo
                desvio_padrao = np.std(ground)

        return individuo_escolhido

    def avaliar_melhor_filho(self):
        """
            Avalia as souluções produzidas, associando uma nota/avalição a cada elemento da população
        """
        print(len(self.populacao))

    def _selecionarPais(self):
        """
            Realiza a seleção do individuo mais apto por torneio, considerando N = 2
        """
        pai = []
        mae = []
        # agrupa os individuos com suas avaliações para gerar os participantes do torneio
        participantes_torneio_pai_ground = self.ground_population_vector
        participantes_torneio_mae_ground = self.ground_mating_vector
        participantes_torneio_pai_block = self.block_population_vector
        participantes_torneio_mae_block = self.block_mating_vector
        participantes_torneio_pai_enemy = self.enemy_population_vector
        participantes_torneio_mae_enemy = self.enemy_mating_vector
        participantes_torneio_pai_coin = self.coin_population_vector
        participantes_torneio_mae_coin = self.coin_mating_vector
        # escolhe os melhores indivíduos
        ground_pai_index = self.ground_population_dp_vector.index(min(self.ground_population_dp_vector))
        print("Menor Ground DP Pai: ", self.ground_population_dp_vector[ground_pai_index])
        pai.append(participantes_torneio_pai_ground[ground_pai_index])
        ground_mae_index = self.ground_mating_dp_vector.index(min(self.ground_mating_dp_vector))
        print("Menor Ground DP Mãe: ", self.ground_mating_dp_vector[ground_mae_index])
        mae.append(participantes_torneio_mae_ground[ground_mae_index])
        block_pai_index = self.block_population_dp_vector.index(min(self.block_population_dp_vector))
        pai.append(participantes_torneio_pai_block[block_pai_index])
        block_mae_index = self.block_mating_dp_vector.index(min(self.block_mating_dp_vector))
        mae.append(participantes_torneio_mae_block[block_mae_index])
        enemy_pai_index = self.enemy_population_dp_vector.index(min(self.enemy_population_dp_vector))
        pai.append(participantes_torneio_pai_enemy[enemy_pai_index])
        enemy_mae_index = self.enemy_mating_dp_vector.index(min(self.enemy_mating_dp_vector))
        mae.append(participantes_torneio_mae_enemy[enemy_mae_index])
        coin_pai_index = self.coin_population_dp_vector.index(min(self.coin_population_dp_vector))
        pai.append(participantes_torneio_pai_coin[coin_pai_index])
        coin_mae_index = self.coin_mating_dp_vector.index(min(self.coin_mating_dp_vector))
        mae.append(participantes_torneio_mae_coin[coin_mae_index])
        # retorna individuo com a maior avaliação, ou seja, o vencedor do torneio
        return pai, mae

    def onePointCrossover(self, pai, mae):
        """
            Aplica o crossover de acordo com uma dada probabilidade (taxa de crossover)
        """
        filho_1 = []
        filho_2 = []
        # ground crossover
        pai_ground = pai[0]
        mae_ground = mae[0]
        if randint(1,100) <= self.taxa_crossover:
            # caso o crossover seja aplicado os pais trocam suas caldas e com isso geram dois filhos
            ponto_de_corte = randint(1, int(self.tam_mapa))
            filho_1.append(pai_ground[:ponto_de_corte] + mae_ground[ponto_de_corte:])
            filho_2.append(mae_ground[:ponto_de_corte] + pai_ground[ponto_de_corte:])
        else:
            # caso contrário os filhos são cópias exatas dos pais
            filho_1.append(pai_ground[:])
            filho_2.append(mae_ground[:])
        # block crossover
        pai_block = pai[1]
        mae_block = mae[1]
        if randint(1,100) <= self.taxa_crossover:
            # caso o crossover seja aplicado os pais trocam suas caldas e com isso geram dois filhos
            ponto_de_corte = randint(1, int(self.tam_mapa))
            filho_1.append(pai_block[:ponto_de_corte] + mae_block[ponto_de_corte:])
            filho_2.append(mae_block[:ponto_de_corte] + pai_block[ponto_de_corte:])
        else:
            # caso contrário os filhos são cópias exatas dos pais
            filho_1.append(pai_block[:])
            filho_2.append(mae_block[:])
        # enemy crossover
        pai_enemy = pai[2]
        mae_enemy = mae[2]
        if randint(1,100) <= self.taxa_crossover:
            # caso o crossover seja aplicado os pais trocam suas caldas e com isso geram dois filhos
            ponto_de_corte = randint(1, int(self.tam_mapa))
            filho_1.append(pai_enemy[:ponto_de_corte] + mae_enemy[ponto_de_corte:])
            filho_2.append(mae_enemy[:ponto_de_corte] + pai_enemy[ponto_de_corte:])
        else:
            # caso contrário os filhos são cópias exatas dos pais
            filho_1.append(pai_enemy[:])
            filho_2.append(mae_enemy[:])
        # coin crossover
        pai_coin = pai[3]
        mae_coin = mae[3]
        if randint(1,100) <= self.taxa_crossover:
            # caso o crossover seja aplicado os pais trocam suas caldas e com isso geram dois filhos
            ponto_de_corte = randint(1, int(self.tam_mapa))
            filho_1.append(pai_coin[:ponto_de_corte] + mae_coin[ponto_de_corte:])
            filho_2.append(mae_coin[:ponto_de_corte] + pai_coin[ponto_de_corte:])
        else:
            # caso contrário os filhos são cópias exatas dos pais
            filho_1.append(pai_coin[:])
            filho_2.append(mae_coin[:])
        # retorna os filhos obtidos pelo crossover
        return (filho_1, filho_2)

    def mutation(self, individuo):
        """
            Realiza a mutação dos bits de um indiviuo conforme uma dada probabilidade
            (taxa de mutação)
        """
        # caso a taxa de mutação seja atingida, ela é realizada em um bit aleatório
        # ground
        individuo_ground = individuo[0]
        for i in range(0, len(individuo_ground) - 1):
            if randint(1,100) <= self.taxa_mutacao:
                individuo[0][i] = randint(0, 4)
        # block
        individuo_block = individuo[1]
        for i in range(0, len(individuo_block) - 1):
            if randint(1,100) <= self.taxa_mutacao:
                individuo[1][i] = randint(0, 10)
        # enemy
        individuo_enemy = individuo[2]
        for i in range(0, len(individuo_enemy) - 1):
            if randint(1,100) <= self.taxa_mutacao:
                individuo[2][i] = randint(0, 5)
        # coin
        individuo_coin = individuo[3]
        for i in range(0, len(individuo_coin) - 1):
            if randint(1,100) <= self.taxa_mutacao:
                individuo[3][i] = randint(0, 1)
            
        return individuo

    def gerar_mapa(self, nova_geracao):
        print(nova_geracao)
        ng_ground = nova_geracao[0]
        ng_ground_aux = nova_geracao[0]
        ng_block = nova_geracao[1]
        ng_enemy = nova_geracao[2]
        ng_coin = nova_geracao[3]
        ng_block_height = []
        ng_enemy_height = []
        ng_coin_height = []
        for height in ng_ground:
            ng_block_height.append(height + self.elementIndividual.min_height_block)
            ng_enemy_height.append(height + 1)
            ng_coin_height.append(height + self.elementIndividual.max_coin_height)

        lines = []
        column = ""
        end = 0
        
        for j in range(0, 16):
            for i in range(0, self.tam_mapa - 1):
                if ng_ground[i] == 1 and j == 0:
                    column = column + "X"
                    ng_ground[i] = ng_ground[i] - 1
                elif ng_ground[i] > 1:
                    column = column + "|"
                    ng_ground[i] = ng_ground[i] - 1
                elif ng_ground[i] == 1:
                    column = column + "%"
                    ng_ground[i] = ng_ground[i] - 1
                else:
                    if j + 1 == ng_enemy_height[i]:
                        column = column + self.elementIndividual.e[ng_enemy[i]]
                    elif j + 1 == ng_block_height[i]:
                        column = column + self.elementIndividual.b[ng_block[i]]
                    elif j + 1 == ng_coin_height[i]:
                        column = column + self.elementIndividual.c[ng_coin[i]]
                    else:
                        column = column + "-"
            lines.append(column)
            column = ""

        f = open("C:/Users/rapha/Desktop/algoritmo_genetico-master/niveis/level_randomized.txt", "w+")

        for j in range(0, 16):
            f.write("" + lines[15 - j] + "\n")

        f.close()

class ElementIndividual():
    def __init__(self, max_ground, max_ground_sequence, max_ground_height, min_height_block, max_block, block_type, max_enemy, enemy_type, max_coin, max_coin_height, chromossomeSize):
        self.max_coin = int(max_coin)
        self.max_coin_height = int(max_coin_height)
        self.max_enemy = int(max_enemy)
        self.enemy_type = int(enemy_type)
        self.min_height_block = int(min_height_block)
        self.max_block = int(max_block)
        self.block_type = int(block_type)
        self.max_ground = int(max_ground)
        self.max_ground_sequence = int(max_ground_sequence)
        self.max_ground_height = int(max_ground_height)
        self.chromossomeSize = int(chromossomeSize)

        self.g = ['-', 'X', '|', '%'] # ground
        self.b = ['-', '#', '?', '@', '1', '2', 'D', 'S', 'C', 'U', 'L'] # blocks
        self.e = ['-', 'y', 'E', 'g', 'k', 'r'] # enemies
        self.c = ['-', 'o'] # coins

    def _groundIndividual(self):
        # gound parts (gparts) 1 - 4
        # ground size (gsize) 1 - 132
        # ground maximum height (ghmax) 0 - 4

        g_vector = []
        sequence = 0
        max_sequence = 0
        height = 0
        while sequence < self.chromossomeSize:
            max_sequence = randint(1, int(self.max_ground_sequence))
            if sequence + max_sequence <= self.chromossomeSize:
                height = randint(0, self.max_ground_height)
                for _ in range(max_sequence):
                    g_vector.append(height)
                sequence += max_sequence

        return g_vector

    def _blockIndividual(self):
        # block maximum height (bhmax) 1 - 4
        # block maximum (bmax) 1 - 132
        # block type (btype) 1 - 11

        b_vector = []
        block = self.max_block
        for _ in range(0, int(block)):
            for _ in range(0, int((self.chromossomeSize/self.max_block) - 1)):
                b_vector.append(0)
            if block > 0:
                b_vector.append(randint(1, self.block_type))
                block -= 1
            
        if len(b_vector) < 132:
            falta = 132 - len(b_vector)
            for _ in range(0, falta):
                b_vector.append(0)

        return b_vector

    def _enemyIndividual(self):
        # enemy maximum (emax) 1 - 132
        # enemy type (etype) 1 - 9

        e_vector = []
        enemy = self.max_enemy
        for _ in range(0, int(enemy)):
            for _ in range(0, int((self.chromossomeSize/self.max_enemy) - 1)):
                e_vector.append(0)
            if enemy > 0:
                e_vector.append(randint(1, self.enemy_type))
                enemy -= 1

        if len(e_vector) < 132:
            falta = 132 - len(e_vector)
            for _ in range(0, falta):
                e_vector.append(0)
        
        return e_vector

    def _coinIndividual(self):
        # coin maximum (cmax) 1 - 132
        # coin maximum height (chmax) 1 - 4

        c_vector = []
        coin = self.max_coin
        for _ in range(0, int(coin)):
            for _ in range(0, int((self.chromossomeSize/self.max_coin) - 1)):
                c_vector.append(0)
            if coin > 0:
                c_vector.append(1)
                coin -= 1

        if len(c_vector) < 132:
            falta = 132 - len(c_vector)
            for _ in range(0, falta):
                c_vector.append(0)
        
        return c_vector

def main():
    # cria uma instância do algoritmo genético com as configurações do enunciado
    # AlgoritmoGenetico(x_min, x_max, tam_populacao, taxa_mutacao, taxa_crossover, num_geracoes)
    algoritmo_genetico = AlgoritmoGenetico(1, 5, 5, 5, 75, 10)
    algoritmo_genetico._gerar_populacao()
    algoritmo_genetico.avaliarPopulacao()

    for _ in range(algoritmo_genetico.num_geracoes):
        nova_populacao = []
        while len(nova_populacao) < algoritmo_genetico.tam_populacao:
            # seleciona os pais
            pai, mae = algoritmo_genetico._selecionarPais()
            # realiza o one point crossover dos pais para gerar os filhos
            filho_1, filho_2 = algoritmo_genetico.onePointCrossover(pai, mae)
            # realiza a mutação dos filhos e os adiciona à nova população
            filho_1 = algoritmo_genetico.mutation(filho_1)
            filho_2 = algoritmo_genetico.mutation(filho_2)

            nova_populacao.append(filho_1)
            nova_populacao.append(filho_2)

        algoritmo_genetico.populacao = nova_populacao

    algoritmo_genetico.avaliarNovaPopulacao(nova_populacao)
    
    filho = algoritmo_genetico.avaliar()
    algoritmo_genetico.gerar_mapa(filho)
    
    return 0

if __name__ == '__main__':
    main()