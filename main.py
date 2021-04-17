from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
import views


routes = {
    '/': views.index_view,
    '/about/': views.about_view,
}

class Application:

    def __init__(self, routes):
        self.routes = routes

    def __call__(self, environ, start_response):
        setup_testing_defaults(environ)
        print('work')
        path = environ['PATH_INFO']
        # проверка наличия (отсутствия) слеша в конце адреса
        if path[-1] != '/':
            path = path + '/'
        if path in self.routes:
            view = self.routes[path]
        else:
            view = views.not_found_404_view
        request = {}
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]


application = Application(routes)

if __name__ == '__main__':
    with make_server('', 8000, application) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()