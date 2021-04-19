from wsgiref.simple_server import make_server
from main import Application, routes



application = Application(routes)

if __name__ == '__main__':
    with make_server('', 8000, application) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()