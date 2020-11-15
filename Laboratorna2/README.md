# Laboratorna 2

## Хід роботи
1. За допомогою пакетного менеджера *PIP* встановив *pipenv* та створив ізольоване середовище для Python:
    ```
    pip3 install pipenv
    pipenv --python 3.8
    pipenv shell
    ```
1. Встановив бібліотеки:
    ```
    pipenv install requests
    pipenv install ntplib
    ```
1. Створив файл *app.py*, запустив, програма працює правильно.
1. Для тестування встановив бібліотеку *pytest*, запустив тести, всі тести виконались успішно:
    ```
    pipenv install pytest
    pytest tests/tests.py
    ```
1. Дописав у програмі app.py функцію, яка буде перевіряти час доби AM/PM та відповідно друкувати Доброго дня/ночі. Також у файлі (*tests.py*) написав тест який перевіряє правильність роботи функції.
1. Виконання функції та тестів перенаправив у файл *results.txt*:
    ```
    pipenv run python app.py append >> results.txt
    pipenv run pytest tests/tests.py >> results.txt
    ```
1. Написав make-файл для сховища. Додав правила налаштування середовища та встановив залежності ( make install), запустив модульні тести ( make test), запустив додаток ( make run) та розгорнув ( make deploy).

