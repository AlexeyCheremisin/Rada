# Домашнее задание по теме "Форматирование строк"


if __name__ == "__main__":
    team1_num = 5
    team2_num = 6
    print("В команде Мастера кода участников: %d !" % team1_num)
    print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

    score_2 = 42
    team2_time = 18015.2
    print("Команда Волшебники данных решила задач: {} !".format(score_2))
    print("Волшебники данных решили задачи за {} с !".format(team2_time))

    score_1 = 40
    challenge_result = "победа команды Мастера кода!"
    print(f"Команды решили {score_1} и {score_2} задач.")
    print(f"Результат битвы: {challenge_result}")

    tasks_total = score_1 + score_2
    time_avg = 350.4
    print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")
