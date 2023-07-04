class Player(object):
    all_players = []

    def __init__(self, name):
        self.name = name
        self.all_players.append(self)

    def remove(self):
        self.all_players.remove(self)

    def change_name(self, name):
        self.name = name

def find_player(name):
    for player in Player.all_players:
        if player.name == name:
            break
    else:
        return None
    return player

def add_player(name):
    if find_player(name) is None:
        new_player = Player(name)
        print('Successfully add new player')
    else:
        print('Player with this name exist.\nFail to add new player')

def remove_player(name):
    if find_player(name) is None:
        print('Player with this name does not exist.')
    else:
        player = find_player(name)
        player.remove()
        print('Successfully remove player')

def show_players():
    for i, player in enumerate(Player.all_players):
        print(player.name)

def modify_player(old_name, new_name):
    if find_player(old_name) is None:
        print('Player with this name does not exist.')
    elif (find_player(new_name) is not None):
        print('Player with this new name exist.')
    else:
        player = find_player(old_name)
        player.change_name(new_name)
        print('Successfully player name changed')

def handle_players():
    while True:
        command = input("Please enter a valid command: ")
        match command:
            case 'add new player' | '1':
                add_player(input('Please enter player name: '))
            case 'show players' | '2':
                show_players()
            case 'change player name' | '3':
                old_name = input('Please enter player name: ')
                new_name = input('Please enter new name: ')
                modify_player(old_name, new_name)
            case 'remove player' | '4':
                remove_player(input('Please enter player name: '))
            case 'help':
                print('1: add new player')
                print('2: show players')
                print('3: change player name')
                print('4: remove player')
                print('0: quit')
            case 'quit' | '0':
                break
            case _:
                print("Invalid command.")


handle_players()