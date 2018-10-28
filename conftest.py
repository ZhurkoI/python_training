# conftest.py - специальный файл в PyTest в котором прописывается общая фикстура для всех тестов
import pytest
from fixture.application import Application


@pytest.fixture  # так помечается метод, создающий фикстуру
# параметр (scope = "session") позволяет не закрывать браузер полностью мосле окончания каждого отдельного теста
# @pytest.fixture(scope = "session")
def app(request):
    # функция для инициализации и разрушения фикстуры
    # Для разрушения фикстуры в функцию инициализации передается специальный параметр request,
    # у которого есть особый метод addfinalizer, которому нужно передать функцию, к-ю фреймворк в нужный
    # момент вызывает для разрушения фикстуры
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

