import random
CARDS=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
class Game:
    player:list=[]
    dealer:list=[]
    deck:list=[]
    used_deck:list=[]
    def copy(self):
        game=Game()
        game.player=self.player.copy()
        game.dealer=self.dealer.copy()
        game.deck=self.deck.copy()
        game.used_deck=self.used_deck.copy()
        return game
    def get_simulation_copy(self):
        game=Game()
        game.player=self.player.copy()
        game.dealer=self.dealer.copy()
        game.deck=self.get_unused_cards()
        game.used_deck=self.used_deck.copy()
        return game
    def clear_game(self):
        self.player.clear()
        self.dealer.clear()
        return
    def init_game(self):
        self.init_player(self.player)
        self.init_player(self.dealer)
        pass
    def init_player(self,who):
        who.clear()
        last_card=self.pop_deck()
        who.append(last_card)
        self.used_deck.append(last_card)
        last_card=self.pop_deck()
        who.append(last_card)
        self.used_deck.append(last_card)
        pass
    def init_deck(self):
        if len(self.deck)>0:
            return
        self.deck=[]
        for n in CARDS:
            self.deck.append(n)
            self.deck.append(n)
            self.deck.append(n)
            self.deck.append(n)
        for n in CARDS:
            self.deck.append(n)
            self.deck.append(n)
            self.deck.append(n)
            self.deck.append(n)
        random.shuffle(self.deck)
        self.used_deck=[]
        return
    def map_cards_2_values(self,card,value):
        if card=="J":
            return 10
        if card=="Q":
            return 10
        if card=="K":
            return 10
        if card=="A":
            if value+11<=21:
                return 11
            else:
                return 1
        return int(card)
    def get_unused_cards(self):
        unused_cards=self.deck.copy()
        random.shuffle(unused_cards)
        return unused_cards
    def pop_deck(self):
        if len(self.deck)<=0:
            self.init_deck()
        return self.deck.pop()

    def get_score(self,who):
        value=0
        for card in who:
            value+=self.map_cards_2_values(card,value)
            pass
        return value
    def hit(self,who):
        last_card=self.pop_deck()
        who.append(last_card)
        self.used_deck.append(last_card)
        pass
    def run(self):
        while self.get_score(self.player)<=21 or self.get_score(self.dealer)<17:
            if self.get_score(self.player)<=21:
                if self.player_take():
                    self.hit(self.player)
                    pass
                elif self.get_score(self.dealer)>=17:
                    break
                pass
            if self.get_score(self.dealer)<17:
                self.hit(self.dealer)
                pass
            pass
        return
    def is_player_win(self):
        if self.get_score(self.player)>=17 and self.get_score(self.player)<=21:
            return True
        return False
    def is_draw(self):
        if self.get_score(self.player)>21 and self.get_score(self.dealer)>21 or \
            (self.get_score(self.player) == self.get_score(self.dealer)):
            return True
        return False
    def is_deal_win(self):
        if self.get_score(self.dealer)<=21 and self.get_score(self.player)<self.get_score(self.dealer)\
            or (self.get_score(self.player) == self.get_score(self.dealer) and self.get_score(self.dealer)==21):
            return True
        return False
    
    def player_take(self):
        return self.get_score(self.player)<18
        safe_rate=self.player_safe_probability()
        return safe_rate>0.5
    def player_safe_probability(self):
        SIMULATION_COUNT=100
        safe_count=0
        for i in range(SIMULATION_COUNT):
            game = self.get_simulation_copy()
            game.hit(game.player)
            if game.get_score(game.player)<=21:
                safe_count+=1
            pass
        return safe_count/100
    pass