import random

# Have fun!

class blackjack():
    cards = ['1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', '11c', '12c', '13c', '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', '11d', '12d', '13d', '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', '11s', '12s', '13s', '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', '11h', '12h', '13h',]
    house_cards = []
    player_cards = []
    player_score = 0
    house_score = []
    key = 1
    def __init__(self):
        self.self = self
    
    def shuf(self):
        random.shuffle(self.cards)
        
    def first_deal(self):
        self.house_cards.append(self.cards.pop())
        self.house_cards.append(self.cards.pop())
        self.player_cards.append(self.cards.pop())
        self.player_cards.append(self.cards.pop())   
        print(f'\nThe house has drawn {self.house_cards[0]}')
        self.total()
        if self.player_score == 21:
            print(f'\nBlackjack! You win! \n Your cards: {self.player_cards}')
            self.key = 0
        if self.player_score > 21:
            self.you_lose()
    
    def hit(self):
        self.player_cards.append(self.cards.pop())
        
    def total(self):
        self.player_score = 0
        for i in self.player_cards:
            num = i[:-1]
            play_num = int(num)
            self.player_score += play_num
        if self.player_score > 21:
            self.you_lose()
        else:
            self.show()
    
    def show(self):
        print(f'\nYour cards are:')
        for i in self.player_cards:
            print(i)
            
    def stand(self):
        self.player_score = 0
        for i in self.player_cards:
            num = i[:-1]
            play_num = int(num)
            self.player_score += play_num
        self.house_score = 0
        for i in self.house_cards:
            num = i[:-1]
            play_num = int(num)
            self.house_score += play_num
        if self.house_score > 21:
            self.you_win()
        elif self.house_score <= 21:
            if self.player_score > self.house_score:
                self.you_win()
            elif self.player_score < self.house_score:
                self.you_lose_show()
            elif self.player_score == self.house_score:
                print(f'\nNo winners: \n{self.house_cards} \n{self.player_cards}') 
            else:
                self.you_lose_show() 
        
    def you_win(self):
        print(f'\nYou win! \n House cards: {self.house_cards} \n Your cards: {self.player_cards}')
                
    def you_lose(self):
        print(f'\nYou lose! \nYour cards: {self.player_cards}')
    
    def you_lose_show(self):
        print(f'\nYou lose! \n House cards: {self.house_cards} \n Your cards: {self.player_cards}')
        
        
        
game = blackjack()

def run():
        initiate = input("Press enter to start a game of Blackjack.\n c = clubs, h = hearts, s = spades and d = diamonds\n")
        game.shuf()
        game.first_deal()
        to_be_or = "not s"
        while to_be_or != "s" and game.key == 1:
            if game.player_score <= 21:
                to_be_or = input("hit or stand? (h/s) ")
                if to_be_or == 'h':
                    game.hit()
                    game.total()
                else:
                    game.stand()
        
            
        
run() 