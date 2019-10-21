to_repeat = 'Да'
correct_answers = 0
while to_repeat == 'Да':
    if input('В каком году родился Николай Иванович Лобачевский? ') == '1792':
        correct_answers += 1
    if input('В каком году родился Николай Иванович Пирогов? ') == '1810':
        correct_answers += 1
    if input('В каком году родился Иван Федорович Крузенштерн? ') == '1770':
        correct_answers += 1
    if input('В каком году родился Михаил илларионович Кутузов? ') == '1745':
        correct_answers += 1
    if input('В каком году родился Наполеон I Бонапарт? ') == '1769':
        correct_answers += 1
    print('Количество верных ответов - ', correct_answers)
    print('Количество неверных ответов - ', 5-correct_answers)
    print('Процент верных ответов - ', correct_answers * 100 / 5)
    print('Процент неверных ответов - ', (5-correct_answers) * 100 / 5)
    to_repeat = input('Хотите начать викторину с начала? Да/Нет :')


