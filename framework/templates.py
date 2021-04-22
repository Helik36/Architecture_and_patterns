from jinja2 import Template
import os
from jinja2 import Template, FileSystemLoader
from jinja2.environment import Environment


def render(template_name, folder='templates', **kwargs):
    """
    Минимальный пример работы с шаблонизатором
    :param template_name: имя шаблона
    :param kwargs: параметры для передачи в шаблон
    :return:
    """

    env = Environment()
    env.loader = FileSystemLoader(folder)
    template = env.get_template(template_name)
    return template.render(**kwargs)






# folder = 'templates - указываем, в какой папке искать шаблон
# def render(template_name, folder='templates', **kwargs):
#     """
#     :param template_name: имя шаблона
#     :param folder: папка в которой ищем шаблон
#     :param kwargs: параметры
#     :return:
#     """
#     # Открываем шаблон по имени
#     path_name = os.path.join(folder, template_name)
#     with open(path_name, encoding='utf-8') as f:
#         # Читаем
#         template = Template(f.read())
#     # рендерим шаблон с параметрами
#     return template.render(**kwargs)