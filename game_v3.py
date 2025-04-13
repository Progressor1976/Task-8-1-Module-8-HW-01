""" Игра угадай число. Компьютер сам загадывает и угадывает число"""

import numpy as np 

def random_predict(number: int = 1) -> int:
    
    """Угадываем число с помощью метода деления пополам"""
    
    count = 0
    min_num, max_num = 1, 100  # Задаём начальные границы диапазона

    while True:
        count += 1
        predict_number = (min_num + max_num) // 2  # Берем середину диапазона
        
        if predict_number == number:
            break  # Число угадано!
        elif predict_number > number:
            max_num = predict_number - 1  # Сужаем диапазон вниз.
        else:
            min_num = predict_number + 1  # Сужаем диапазон вверх.

    return count

def score_game(predict_function) -> int:
    
    """Определяем среднее количество попыток угадывания числа"""
    
    count_ls = [] # Создаём список, где элементами явл-я кол-ва попыток
    np.random.seed(1)  # Фиксируем seed для воспроизводимости
    random_numbers = np.random.randint(1, 101, size=1000)  # создаём список из 1000 случайных чисел
    
    for number in random_numbers:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))  # Среднее количество попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

if __name__ == '__main__':
    score_game(random_predict)