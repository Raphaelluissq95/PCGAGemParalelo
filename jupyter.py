from random import randint
import numpy as np
import statistics
import matplotlib.pyplot as plt

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
        self.dp_vector = []
        # gera os individuos da população

    def _gerar_populacao(self):
        """
            Gera uma população de um determinado tamanho com individuos que possuem um número
            expecífico de bits
        """
        # Ground
        self.ground_population_vector = []
        self.elementIndividual = ElementIndividual(1, 9, 8, 3, 5, 10, 5, 5, 15, 3, 132)
        for _ in range(0, self.tam_populacao):
            self.ground_population_vector.append(self.elementIndividual._groundIndividual())
        
        print("Tamanho da população:\n", len(self.ground_population_vector))
        print("Populacao Inicial:\n", self.ground_population_vector)

    def avaliarPopulacao(self):
        """
            Avalia as souluções produzidas, associando uma nota/avalição a cada elemento da população
        """
        print("\nGround:")
        self.ground_population_dp_vector = []
        for individuo in self.ground_population_vector:
            print("Individuo:\n", individuo)
            varia = np.std(individuo)
            soma = 0
            inicio = individuo[0]
            for i in range(1, len(individuo)):
                if inicio != individuo[i]:
                    soma += 1
            print("Desvio Padrão*:\n", (soma/self.elementIndividual.chromossomeSize)*varia)
            self.ground_population_dp_vector.append((soma/self.elementIndividual.chromossomeSize)*varia)
            
        self.dp_vector.append(self.ground_population_dp_vector[self.ground_population_dp_vector.index(min(self.ground_population_dp_vector))])

    def _selecionarPais(self):
        """
            Realiza a seleção do individuo mais apto por torneio, considerando N = 2
        """
        pai = []
        mae = []
        # agrupa os individuos com suas avaliações para gerar os participantes do torneio
        participantes_torneio_ground = self.ground_population_vector
        
        ground_index = self.ground_population_dp_vector.index(min(self.ground_population_dp_vector))
        pai.append(participantes_torneio_ground[ground_index])
        pai_dp = self.ground_population_dp_vector[ground_index]
        participantes_torneio_ground.remove(participantes_torneio_ground[ground_index])
        self.ground_population_dp_vector.remove(self.ground_population_dp_vector[ground_index])
        
        ground_index = self.ground_population_dp_vector.index(min(self.ground_population_dp_vector))
        mae.append(participantes_torneio_ground[ground_index])
        mae_dp = self.ground_population_dp_vector[ground_index]
        participantes_torneio_ground.remove(participantes_torneio_ground[ground_index])
        self.ground_population_dp_vector.remove(self.ground_population_dp_vector[ground_index])
        
        return pai, mae, pai_dp, mae_dp
        
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
            ponto_de_corte1 = randint(1, int(self.tam_mapa)/2)
            ponto_de_corte2 = randint(int(self.tam_mapa)/2, int(self.tam_mapa))
            filho_1.append(pai_ground[:ponto_de_corte1] + mae_ground[ponto_de_corte1:ponto_de_corte2] + pai_ground[ponto_de_corte2:])
            filho_2.append(mae_ground[:ponto_de_corte1] + pai_ground[ponto_de_corte1:ponto_de_corte2] + mae_ground[ponto_de_corte2:])
        else:
            # caso contrário os filhos são cópias exatas dos pais
            filho_1.append(pai_ground[:])
            filho_2.append(mae_ground[:])
            
        return filho_1, filho_2
        
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
                valor = individuo[0][i] + randint(-4, 4)
                if valor < 0:
                    individuo[0][i] = 0
                elif valor > 8:
                    individuo[0][i] = 8
                else:
                    individuo[0][i] = valor
                
        return individuo
    
    def avaliarNovaPopulacao(self, nova_populacao):
        """
            Avalia as souluções produzidas, associando uma nota/avalição a cada elemento da população
        """
        print("Nova População: ", nova_populacao)
        for individuo in nova_populacao:
            print("Individuo:\n", individuo)
            varia = np.std(individuo)
            soma = 0
            inicio = individuo[0]
            for i in range(1, len(individuo)):
                if inicio != individuo[i]:
                    soma += 1
            print("Desvio Padrão*:\n", (soma/self.elementIndividual.chromossomeSize)*varia)
            
    def avaliarFilho(self, filho_1, filho_2):
        """
            Avalia as souluções produzidas, associando uma nota/avalição a cada elemento da população
        """
        for individuo in filho_1:
            print("Filho1:\n", individuo)
            varia = np.std(individuo)
            soma = 0
            inicio = individuo[0]
            for i in range(1, len(individuo)):
                if inicio != individuo[i]:
                    soma += 1
            filho_1_dp = (soma/self.elementIndividual.chromossomeSize)*varia
            print("Desvio Padrão*:\n", filho_1_dp)
        
        for individuo in filho_2:
            print("Filho2:\n", individuo)
            varia = np.std(individuo)
            soma = 0
            inicio = individuo[0]
            for i in range(1, len(individuo)):
                if inicio != individuo[i]:
                    soma += 1
            filho_2_dp = (soma/self.elementIndividual.chromossomeSize)*varia
            print("Desvio Padrão*:\n", filho_2_dp)
            
        return filho_1_dp, filho_2_dp

# x_min, x_max, tam_populacao, taxa_mutacao, taxa_crossover, num_geracoes
algoritmo_genetico = AlgoritmoGenetico(1, 50, 2, 1, 75, 200)
algoritmo_genetico._gerar_populacao()
algoritmo_genetico.avaliarPopulacao()

for i in range(algoritmo_genetico.num_geracoes):
    algoritmo_genetico.avaliarPopulacao()
    nova_populacao = []
    print("Geração ", i)
    while len(nova_populacao) < algoritmo_genetico.tam_populacao:
            # seleciona os pais
            pai, mae, pai_dp, mae_dp = algoritmo_genetico._selecionarPais()
            # realiza o one point crossover dos pais para gerar os filhos
            filho_1, filho_2 = algoritmo_genetico.onePointCrossover(pai, mae)
            # realiza a mutação dos filhos e os adiciona à nova população
            filho_1 = algoritmo_genetico.mutation(filho_1)
            filho_2 = algoritmo_genetico.mutation(filho_2)
            
            filho_1_dp, filho_2_dp = algoritmo_genetico.avaliarFilho(filho_1, filho_2)

            if filho_1_dp <= pai_dp:
                nova_populacao.append(filho_1[0])
            else:
                nova_populacao.append(pai[0])
            if filho_1_dp <= mae_dp:
                nova_populacao.append(filho_1[0])
            else:
                nova_populacao.append(mae[0])
            if filho_2_dp <= pai_dp:
                nova_populacao.append(filho_2[0])
            else:
                nova_populacao.append(pai[0])
            if filho_2_dp <= mae_dp:
                nova_populacao.append(filho_2[0])
            else:
                nova_populacao.append(mae[0])

    algoritmo_genetico.ground_population_vector = nova_populacao