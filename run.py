from app.views import *
from wsgiref.simple_server import make_server
from pyramid.config import Configurator


if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_jinja2')               #"""Include 'pyramid_jinja2' for jinja2 template"""
    config.add_route('home', '/')                  #"""Home directory route"""
    config.add_view(home_page, route_name='home')  #"""Home page"""
    config.add_route('new', '/new')                #"""New page directory route"""
    config.add_view(new_page, route_name='new')    #"""New page"""
    app    = config.make_wsgi_app()                #"""Server config"""
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
