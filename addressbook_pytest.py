# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture # так помечается метод, создающий фикстуру
def app(request):
    # функция для инициализации и разрушения фикстуры
    # Для разрушения фикстуры в функцию инициализации передается специальный параметр request,
    # у которого есть особый метод addfinalizer, которому нужно передать функцию, к-ю фреймворк в нужный
    # момент вызовет для разрушения фикстуры
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app): # в тестовые методы в качестве параметра передается фикстура
    app.login(username="admin", password="secret")
    app.create_group(Group(name="group 2", header="qwerty", footer="asdf"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="group 22", header="qwerty22", footer="asdf22"))
    app.logout()
