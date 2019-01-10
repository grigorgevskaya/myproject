from getpass import getpass
import sys

from ui import app
from myproject.model import base, User

app = creat_app()                                                                                               Й

with app.app_context():
    username = input('Введите имя:')

    if User.query.filter(User.username = username).count():
        print('Пользователь с таким именем уже существует')
        sys.exit(0)   

    password1 = getpass ('Введите пароль')
    password2 = getpass ('Повторите пароль')

    if  password1 >  password2:
        print('Пароли не одинаковые')
        sys.exit(0)
    elif password1 <  password2:
        print('Пароли не одинаковые')
        sys.exit(0)



    new_user = User (username=username, is_admin='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print('Создан пользователь с id={}', format(new_user.id))
        
