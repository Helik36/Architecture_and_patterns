from jinja2 import Template
import os

# folder = 'templates - указываем, в какой папке искать шаблон
def render(template_name, folder='templates', **kwargs):
    """
    :param template_name: имя шаблона
    :param folder: папка в которой ищем шаблон
    :param kwargs: параметры
    :return:
    """
    # Открываем шаблон по имени
    path_name = os.path.join(folder, template_name)
    with open(path_name, encoding='utf-8') as f:
        # Читаем
        template = Template(f.read())
    # рендерим шаблон с параметрами
    return template.render(**kwargs)