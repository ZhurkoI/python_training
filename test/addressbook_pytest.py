# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app): # в тестовые методы в качестве параметра передается фикстура
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="group 2", header="qwerty", footer="asdf"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="group 22", header="qwerty22", footer="asdf22"))
    app.session.logout()
