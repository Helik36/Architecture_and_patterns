from wsgiref.util import setup_testing_defaults
from framework import GetRequests, PostRequests
import views
import quopri
import datetime

routes = {
    '/': views.index_view,
    '/about/': views.about_view,
    '/contacts/': views.page_contants
}

w_time = datetime.datetime.now()

class Application:

    def __init__(self, routes):
        self.routes = routes

    def __call__(self, environ, start_response):
        setup_testing_defaults(environ)
        print('work')

        # получаем адрес, по которому выполнен переход
        path = environ['PATH_INFO']

        # проверка наличия (отсутствия) слеша в конце адреса
        if path[-1] != '/':
            path = path + '/'

        request = {}
        # Получаем все данные запроса
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = data
            # Выводим инфу в консоль
            print(f'Нам пришёл post-запрос: {Application.decode_value(data)}')
            # Записываем эту же инфу в текстовый файл
            with open('inquiries.txt', 'a', encoding='utf-8') as f:
                f.write(f'{w_time}: {Application.decode_value(data)} \n \n')

        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = request_params
            print(f'Нам пришли GET-параметры: {request_params}')

        # находим нужный контроллер
        # отработка паттерна page controller
        if path in self.routes:
            view = self.routes[path]
        else:
            view = views.not_found_404_view

        # запуск контроллера с передачей объекта request
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data

