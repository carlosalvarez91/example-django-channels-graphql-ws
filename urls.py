import pathlib

import django
import django.contrib.admin
import django.contrib.auth

import channels_graphql_ws
# -------------------------------------------------------------------- URL CONFIGURATION
def graphiql(request):
    """Trivial view to serve the `graphiql.html` file."""
    del request
    graphiql_filepath = pathlib.Path(__file__).absolute().parent / "graphiql.html"
    with open(graphiql_filepath) as f:
        return django.http.response.HttpResponse(f.read())


urlpatterns = [
    django.urls.path("", graphiql),
    django.urls.path("admin", django.contrib.admin.site.urls),
]
