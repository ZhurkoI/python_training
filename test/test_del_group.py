def test_delete_first_group(app):
    # в тестовые методы в качестве параметра передается фикстура
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()