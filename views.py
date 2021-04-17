from framework import render


# page controller
def index_view(request):
    print(request)
    index = 'Главная страница'
    return '200 OK', render('index.html', object_list = [index])


def about_view(request):
    print(request)
    about = 'О нас '
    return '200 OK', render('about.html', object_list = [about] )


def not_found_404_view(request):
    print(request)
    not_f_404 = "404 PAGE Not Found"
    return '404 WHAT', render('404.html', object_list = [not_f_404])
