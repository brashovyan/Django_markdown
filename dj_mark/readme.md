Markdown django

создаем обычный проект

устанавливаем pip install django-markdownx

Копируем настройки (как обычно статик, медиа, темплейтс,
в insalled_apps надо добавить 'markdownx')

в urls (которые в папке с настройками) делаем маркдовн

Дальше по примеру создаем модель (сущность) и добавляем ее в админку

P.s. картинки сами загружаются в папку media в подкаталог markdownx

в папке mainapp создаем templatetags и там blog_exstras.py

ну и смотри пример index.html и base.html





