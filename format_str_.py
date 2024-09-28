team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = "Победа команды Волшебники Данных!"
else:
    result = "Ничья!"

team1_num_str = "В команде Мастера кода участников: %s" % team1_num
summ_team_boy = "Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num)
task_score = "Команды решили {} и {} задач.".format(score_1, score_2)
time_team_2 = "Волшебники данных решили задачи за {} ".format(team2_time)
task_1_2 = f"Команды решили {score_1} и {score_2} задач."
challenge_result = f"Результат битвы: {result}!"
total = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу"

print(challenge_result)
print(team1_num_str)
print(summ_team_boy)
print(task_score)
print(time_team_2)
print(task_1_2)