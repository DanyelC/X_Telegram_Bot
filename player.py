class Player:
    def __init__(self,id,animal,personality):
        self.id = id
        self.score = 0
        self.animal = animal
        self.personality = personality
        self.hp = 100
        self.attack = 10
        self.defense = 0
        self.gear = ["Nothing", 0]
        self.magic = ["Nothing", 0]
        self.gold = 5000



    def send_all_list(self):
        lista = []
        for attribute, value in self.__dict__.items():
            x =  str(attribute) + ' = ' +str(value)
            lista.append(x)
        return lista


#======================= QUIZ =======================

# 1 - "Voce prefere a manhã, tarde ou noite? manha, tarde, noite" 
# 2 - "Voce acredita em Deus? sim nao"
# 3 - "Se voce fosse um Deus, qual seria? Deus da Guerra, Deus da Natureza, Deus da Sabedoria"
# 4 - "Se pudesse dominar um elemento, qual seria? agua, fogo, vento, terra"
# 5 - "Vocẽ é feliz? sim, nao"
# 6 - "Com que frequencia voce mente? nenhuma, baixa, media, alta"
# 7 - "Voce é uma pessoa estressada? sim , não"
# 8 - "Voce é uma pessoa ambiciosa? sim , não"
# 9 - "Trapacear só é um problema se vocẽ for pego? verdade, mentira"
# 10 - "Poder, felicidade ou paz? dinheiro, felicidade, paz"

#======================= QUIZ =======================
