list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
count_of_players = len(list_players)
half_of_count = count_of_players // 2
team_1 = list_players[:half_of_count]
team_2 = list_players[half_of_count::]
# TODO Разделите участников на две команды
print(team_1, team_2, sep='\n')