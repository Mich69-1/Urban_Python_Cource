# Домашнее задание по теме "Форматирование строк".

# %
team_num1, team_num2 = 15, 17
print('В команде Мастера кода участников: %s !' % team_num1)
print('Итого сегодня в командах участников: %s и %s !' % (team_num1, team_num2))

# format()
score2, team2_time = 42, 13456.07
print('Команда Волшебники данных решила задач: {} !'.format(score2))
print('Команда Волшебники данных решили {score} задачи за {time} !'.format(score=score2, time=team2_time))

# f
score1, team1_time = 43, 13445.02
challenge_result = 'победа команды Мастер кода!'
print(f'Команды решили {score1} и {score2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {score1 + score2} задач, в среднем по '
      f'{(team1_time + team2_time)/(score1 + score2)} секунды на задачу!')
