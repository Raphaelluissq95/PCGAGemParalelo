# coding: utf-8
import random
import numpy as np

symbol_references = {
    'y': 'Spiky',
    'Y': 'Winged Spiky',
    'E': 'Goomba',
    'g': 'Goomba',
    'G': 'Winged Goomba',
    'k': 'Green Koopa',
    'K': 'Winged Green Koopa',
    'r': 'Red Koopa',
    'X': 'Ground Block',
    '#': 'Pyramind Block',
    '%': 'Jump through platform',
    '|': 'Background for the jump through platform',
    '*': 'Bullet bill where the top * will be the bullet bill head',
    'B': 'Bullet bill head',
    'b': 'Bullet bill neck or body',
    '?': 'Special Questoin block',
    '@': 'Special Question block',
    'Q': 'Coin Question block',
    '!': 'Coin Question block',
    '1': 'Invisible 1 up block',
    '2': 'Invisible coin bock',
    'D': 'Used block',
    'S': 'Normal Brick Block',
    'C': 'Coing Brick Block',
    'U': 'Musrhoom Brick Block',
    'L': '1 up Block',
    'o': 'Coin',
    't': 'Empty Pipe',
    'T': 'Pipe with Piranaha Plant in it',
    '<': 'Top left of empty pipe',
    '>': 'Top right of empty pipe',
    '[': 'Left of empty pipe',
    ']': 'Right of empty pipe'
}

action_dict = {
    'run' : 0,
    'jump' : 1
}

mario = "M"
finish = "F"

symbol_list = ['y', 'Y', 'E', 'g', 'G', 'k', 'K', 'r', 'X', '#', '%', '|', '*', 'B', 'b', '?', '@', 'Q', '!', '1', '2', 'D', 'S', 'C', 'U', 'L', 'o', 't', 'T', '<', '>', '[', ']']

def generate_map_split_four_statements(g_vector, g, ghmax, b_vector, b, e_vector, e, c_vector, c, lw):
    blocks = ''
    for blck in b_vector:
        if blck == 0:
            blocks = blocks + '-'
        else:
            blocks = blocks + b[blck - 1]

    enemies = ''
    for enm in e_vector:
        if enm == 0:
            enemies = enemies + '-'
        else:
            enemies = enemies + e[enm - 1]

    coins = ''
    for cns in c_vector:
        if cns == 0:
            coins = coins + '-'
        else:
            coins = coins + c[cns - 1]

    background = '-'
    for i in range(1, lw - 1):
        background = background + '-'

    ground = 'XXX'
    for i in range(0, lw - 1):
        ground = ground + g_vector[i]

    f = open("C:/Users/Raphael/Documents/Mario-AI-Framework-master/levels/new_level/level_randomized.txt", "w+")
    for i in range(1, 15 - (ghmax + 3)):
        f.write("""-------------------------------------------------------------------------------------------------------------------------------\n""")
    
    f.write("""-----------------------------------------""" + blocks + """-----------------------------------------------------------------------------\n""")
    f.write("""-------------------------------------------------------------------------------------------------------------------------------\n""")
    f.write("""-------------------------------------------------------------------------------------------------------------------------------\n""")
    f.write("""-M----------------------------------"""+ enemies + """----------------------------""" + coins + """---------------------------------F-\n""")
    for i in range(0, ghmax):
        f.write(ground + "\n")
    
    f.close()

def generate_map_rythm_style(rythm, symbol_list=symbol_list):
    random_map = [mario]
    for r in range(1, len(rythm) - 3):
        if rythm[r] == 0:
            random_map.append('-')
        else:
            random_map.append(random.choice(symbol_list))
    random_map.append(finish+'-')

    f = open("C:/Users/Raphael/Documents/Mario-AI-Framework-master/levels/new_level/level_randomized.txt", "w+")
    f.write("""----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
""")

    line = ''
    for rm in random_map:
        line = line + rm
    
    f.write(line)
    f.write("""
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX""")
    f.close()

def generate_rythm(action_dict, game_size=131):
    rythm = []
    rythm = [0]
    for x in range(0, game_size - 1):
        rythm.append(random.choice(list(action_dict.values())))

    print("Generated rythm: ", rythm)
    print("Max jump: ", rythm.count(1))

    generate_map_rythm_style(rythm)

def generate_map_card_style(symbol_references, symbol_list):
    size = len(symbol_list)
    random_map = []
    
    for time in range(0, 5):
        #position = random.randrange(5, 125)
        i = random.randrange(0, size - 1)
        random_map.append(symbol_list[i])

    f = open("C:/Users/Raphael/Documents/Mario-AI-Framework-master/levels/new_level/level_randomized.txt", "w+")
    f.write("""----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
""")
    f.write("-M--------" + random_map[0] + "--------------------" + random_map[1] + "----------------------------" + random_map[2] + "---------------" + random_map[3] + "-------------------------" + random_map[4] + "-------------------------F-")
    f.write("""
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX""")
    f.close()

    print("""
        O mapa foi criado utilizando:
        - """ + random_map[0] + " - " + symbol_references[random_map[0]] + """
        - """ + random_map[1] + " - " + symbol_references[random_map[1]] + """
        - """ + random_map[2] + " - " + symbol_references[random_map[2]] + """
        - """ + random_map[3] + " - " + symbol_references[random_map[3]] + """
        - """ + random_map[4] + " - " + symbol_references[random_map[4]] + """
    """)

class GroundIndividual():
    def __init__(self, min_ground, min_ground_sequence, max_ground_height, desiredEntropy, chromossomeSize):
        self.min_ground = min_ground
        self.min_ground_sequence = min_ground_sequence
        self.max_ground_height = max_ground_height
        self.desiredEntropy = desiredEntropy
        self.chromossomeSize = chromossomeSize

        self._groundIndividual()

    def _groundIndividual(self):
        # ground entropy (ge) 0 - 1 (não usado ainda)
        # gound parts (gmin) 1 - 3
        # entropy parts (gparts) 1 - lw
        # ground maximum height (ghmax) 0 - 15
        g_vector = []

        for _ in range(0, (self.chromossomeSize/self.min_ground)):
            g_vector.append(random.randint(1, self.max_ground_height))

        print("G vector: ", g_vector)

def block_agent(b, lw):
    # block sparseness (bx) 0 - 1
    # blocks types (btypes) 0 - 4
    # block sparseness parts(bpart) 1 - lw
    bx = 1
    bpart = 10
    b_vector = []
    for i in range(0, bpart - 1):
        b_vector.append(random.randint(0, 4))

    return b_vector

def enemy_agent(e, lw):
    # enemies sparseness (ex) 0 - 1
    # enemies type (etype) 0 - 4
    # enemies sparseness parts (epart) -1 - lw
    ex = 0
    epart = 20
    e_vector = []
    for i in range(0, epart - 1):
        e_vector.append(random.randint(0, 4))

    return e_vector

def coin_agent(c, lw):
    # coins sparseness (cs) 0 - 1
    # coins maximum heights (chmax) 0 - 10
    # coins type (ctype) 0 - 3
    # coins sparseness parts (cpart) 0 - lw
    cs = 0.5
    cpart = 10
    chmax = 2
    c_vector = []
    for i in range(0, cpart - 1):
        c_vector.append(random.randint(0, 3))

    return c_vector

def split_four_statments():
    # split in:
    g = ['X', ' '] # ground
    b = ['#', '%', '?', '@', '1', '2', 'D', 'S', 'C', 'U', 'L'] # blocks
    e = ['y', 'E', 'g', 'k', 'r', '*', 'B', 'b', 'T'] # enemies
    c = ['Q', '!', 'o'] # coins

    # GroundIndividual(min_ground, min_ground_sequence, max_ground_height, desiredEntropy, chromossomeSize)
    ground_individual = GroundIndividual(2, 2, 4, 0.0, 200)
    # b_vector = block_agent(b, lw)
    # e_vector = enemy_agent(e, lw)
    # c_vector = coin_agent(c, lw)

    # generate_map_split_four_statements(g_vector, g, ghmax, b_vector, b, e_vector, e, c_vector, c, lw)

#generate_map_card_style(symbol_references, symbol_list)

#generate_rythm(action_dict)

#nivel = 
#| 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 |
#| 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 |
#| 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 |
#| 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 |
#| 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 |
#| 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 |
#| 0 0 0 0 0 0 0 0 0 0 e 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 |
#| 0 0 0 0 0 0 0 0 0 b b b 0 0 0 0 0 b c b 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 |
#| 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 |
#| 0 M 0 0 0 0 0 0 0 e 0 0 0 0 0 0 e 0 0 0 0 0 0 e 0 0 0 0 c 0 0 0 0 0 0 e F 0 |
#| g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g |
#| g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g g |