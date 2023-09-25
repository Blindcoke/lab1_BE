# lab1_BE
## Інсталяція

Для встановлення проекту використовуйте наступні кроки:

1. Клонуйте репозиторій:

   ```bash
   git clone https://github.com/Blindcoke/lab1_BE
   
2. Перейдіть до папки проекту:
    ```bash
   cd yourproject
3. Створіть та активуйте віртуальне середовище
    ```bash
   python3 -m venv env
   source ./env/bin/activate
   source ./env/Scripts/activate
4. Встановіть Flask
    ```bash
   pip install flask
5. Запишіть всі залежності проекту в файл requirements.txt:
    ```bash
   pip freeze > requirements.txt
6. Створіть папку для вашого додатку в репозиторії і додайте файли __init__.py та views.py.
   
7. Тепер ви можете запустити застосунок командою:
    ```bash
   flask run --host 0.0.0.0 -p 5000
8. Відкрийте веб-браузер і перейдіть за адресою http://localhost:5000 для перевірки застосунку локально.
