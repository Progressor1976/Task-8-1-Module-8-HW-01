# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](README.md#описание-проекта)  
[2. Какой кейс решаем?](README.md#какой-кейс-решаем)  
[3. Краткая информация о данных](README.md#краткая-информация-о-данных)  
[4. Этапы работы над проектом](README.md#этапы-работы-над-проектом)  
[5. Алгоритм программы](README.md#алгоритм-программы)  
[6. Результаты](README.md#результаты)    
[7. Выводы](README.md#выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](README.md#оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### Краткая информация о данных
Таблица используемых данных с названием и описанием:
```
| **Перменная**     | **Тип данных**| **Описание**
| -----------       | -----------   | -----------
| number            | int           | Загаданное число (от 1 до 100)
| count             | int           | Количество попыток для угадывания числа
| min_num           | int           | Нижняя граница диапазона поиска
| max_num           | int           | Верхняя граница диапазона поиска
| predict_number    | int           | Число, которое алгоритм предполагает в данный момент
| count_ls          | list[int]     | Список количества попыток для каждого числа
| random_numbers    | numpy.ndarray | Массив из 1000 случайных чисел от 1 до 100
| score             | int           | Среднее количество попыток угадывания
```

:arrow_up:[к оглавлению](README.md#оглавление)


### Этапы работы над проектом  
Для реализации данного проекта мы выполнили следующие основные этапы:
```
1. настроили среду разработки (IDE) VS Code для написания кода в ней;
2. научились пользоваться и применили инструмент Jupyter Notebook;
3. написали программу в Python;
4. выкложили проект на GitHub для презентации.
```

:arrow_up:[к оглавлению](README.md#оглавление)


### Алгоритм программы
Краткий алгоритм пронраммы следующий:
```
1. Компьютер загадывает число (из random_array).
2. Функция random_predict пытается его угадать, перебирая случайные числа.
3. Считается, сколько попыток понадобилось.
4. Этот процесс повторяется 1000 раз.
5. Вычисляется среднее количество попыток.
```

:arrow_up:[к оглавлению](README.md#оглавление)


### Результаты:  
Программа находит число меньше чем за 20 попыток, что удовлетворяет требованиям задания.
Также мы постарались удовлетворить остальным требованиям задания. 

:arrow_up:[к оглавлению](README.md#оглавление)


### Выводы:  
В процессе поиска решения данной задачи мы выяснили, что существуют разные методики угаывания числа с разной эффективностью.

:arrow_up:[к оглавлению](README.md#оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами
