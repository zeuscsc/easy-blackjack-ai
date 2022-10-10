from Game import Game
from KellyCriterion import kelly_criterion
import random

def get_win_probability(main_game:Game):
    win_count=0
    SIMULATION_COUNT=100
    for i in range(SIMULATION_COUNT):
        game = main_game.get_simulation_copy()
        game.init_game()
        game.run()
        if game.is_deal_win():
            pass 
        elif game.is_draw():
            pass
        elif game.is_player_win():
            win_count+=1
            pass
        # print(game.player,game.dealer,game.is_player_win())
        pass
    # print(win_count,SIMULATION_COUNT)
    # exit()
    return win_count/SIMULATION_COUNT
def gamble_amount(money,game,turn):
    win_rate=get_win_probability(game)
    amount = money*kelly_criterion(win_rate,1)
    if amount<1:
        amount = 1
    if amount>100:
        amount = 100
    if turn%1==0:
        print("money",money,"amount",amount,"win_rate",win_rate,"turn",turn)
    # exit()
    return amount
money=1000
trial=0
average_money=0
while trial<1:
    money=1000
    turn=0
    game=Game()
    game.init_deck()
    while turn<10000:
        game.clear_game()
        gamble=gamble_amount(money,game,turn)
        game.init_game()
        money-=gamble
        game.run()
        if game.is_deal_win():
            pass 
        elif game.is_draw():
            money+=gamble
            pass
        elif game.is_player_win():
            money+=gamble*2
            pass
        if money<=0:
            break
        turn+=1
        pass
    average_money+=money
    trial+=1
    pass
print(f"Player average money left:{average_money/trial},trial {trial}")