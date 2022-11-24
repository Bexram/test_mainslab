Запуск:
pip install -r .\requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

API:
/loader/load/ - загрузка файла
/loader/bills/ - показать все счета

Фильтры:
/loader/bills?client=client1&org=OOO Client1Org1
