class Player:
    def __init__(self,id,animal,personality):
        self.id = id
        self.Score = 0
        self.Animal = animal
        self.Personality = personality
        self.Hp = 100
        self.Attack = 10
        self.Defense = 0
        self.Gear = ["Nothing", 0]
        self.Magic = ["Nothing", 0]
        self.Gold = 5000
        self.Power = float(self.Score)*0.5 + float(self.Hp)*10 + float(self.Attack)*5 + float(self.Defense)*2 + float(self.Gear[1])*5+ float(self.Magic[1])*2+ float(self.Gold)*0.7
        #colocar animal na conta


    def send_all_list(self):
        lista = []
        for attribute, value in self.__dict__.items():
            #x =  str(attribute) + ' = ' +str(value)
            lista.append(str(value))
            #lista.append(x)
        return lista

    
    

#======================= QUIZ =======================

# 1 - "Do you prefer morning, afternoon or evening? Morning, afternoon, night. 1,1,2"
# 2 - "Do you believe in God? Yes, no , -1, 3"
# 3 - "If you were a God, who would you be? God of War, God of Nature, God of Wisdom. -5 , 1 , 4"
# 4 - "If you could master an element, what would it be? Water, fire, wind, earth. 1, -5, 1, 0 "
# 5 - "Are you happy? Yes, no. 1 , -3"
# 6 - "How often do you lie? None, low, medium, high. 0, -1, -2, -4"
# 7 - "Are you a stressed person? Yes, no. -2, 2"
# 8 - "Are you an ambitious person? Yes, no, -3, 2"
# 9 - "Cheating is only a problem if you get caught? Truth, lie. -4, 2"
# 10 - "Power, happiness or peace? Power, happiness, peace. -2, -1, 1"

#======================= QUIZ =======================
 #fazer aquela parada de estado?
 # The Chosen One -- power += 10000 / 0-5
 # Knight -- power += 3000 / 6-10
 # Peasant -- power += 1000 / 10-15
 # Repugnant -- power -= 1000 / 15-18
 # Human-Demon -- power += 10000 / -28 - -10
