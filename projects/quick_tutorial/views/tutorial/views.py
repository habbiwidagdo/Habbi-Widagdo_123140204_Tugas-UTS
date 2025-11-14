from pyramid.response import Response
from pyramid.view import view_config

# View pertama (home page)
@view_config(route_name='home')
def home(request):
    return Response('<body>Visit <a href="/howdy">hello</a></body>')

# View kedua (/howdy)
@view_config(route_name='hello')
def hello(request):
    return Response('<body>Go back <a href="/">home</a></body>')
