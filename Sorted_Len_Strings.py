def sort_strings(strings, order=None):
    if order == 'возрастающий':
        sorted_strings = sorted(strings, key=len)
    elif order == 'убывающий':
        sorted_strings = sorted(strings, key=len, reverse=True)
    else:
        raise ValueError('Invalid order')

    return sorted_strings


strings = ['Не выходи из комнаты, не совершай ошибку...',
           'Зачем тебе Солнце, если ты куришь Шипку?',
           'Только в уборную—и сразу же возвращайся',
           'За дверью бессмысленно все, особенно — вопли.']

print(sort_strings(strings, 'возрастающий'))
print(sort_strings(strings, 'убывающий'))