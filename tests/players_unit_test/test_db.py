from test import Player

jogador = Player()
#jogador.add_player('Samuel', 'Araujo', '@redwoodsam')
#jogador.add_player('Luiz', 'Gustavo', '@luizgustavo')

def test_existing_player_checker():
    assert jogador.check_if_player_exists('Luiz') == True

def test_admin_checker():
    assert jogador.check_admin('Luiz') == False

def test_grant_admin():
    assert jogador.grant_admin('Samuel') == True

def test_granted_admin():
    assert jogador.check_admin('Samuel') == True

def test_add_highest_score():
    assert jogador.add_highest_score('Samuel', 1) == True

def test_get_my_hiscore():
    assert jogador.get_my_hiscore() == 1

print(jogador.get_leaderboard())

