from models.bag import Bag
from models.card import Card
from models.player import create_player


def is_continue_game(players):
    for item in players:
        if not (item.is_winner is None):
            return False
    return True


bag = Bag(90)
players_count = int(input('Введите количество игроков: '))

players = []
for i in range(players_count):
    name = input(f'Введите имя игрока {i+1}')
    player_type = input(f'Введите тип игрока бот - 1, человек - 0: ')
    card = Card(bag.get_random_numbers(15))
    player = create_player(name, player_type, card)
    players.append(player)

while is_continue_game(players):
    number = bag.get_next_number()
    print(f'Номер бочонка: {number}')
    for player in players:
        print(f'билет игрока {player.name}')
        # player.card.show_number()
        print(player.card)

        player.turn(number)

has_winner = False
has_loser = False

for player in players:
    if player.is_winner is None:
        pass
    else:
        if player.is_winner:

            has_winner = True
        else:
            has_loser = True

if has_winner:
    for player in players:
        if player.is_winner:
            print(player.name, 'WIN!')
        else:
            print(player.name, 'LOOSE!')
elif has_loser:
    for player in players:
        if player.is_winner is None:
            print(player.name, 'WIN!')
        else:
            print(player.name, 'LOOSE!')
else:
    print('что-то не так')
