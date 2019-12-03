from .consumer import MyGraphqlWsConsumer


import channels
import channels.auth
import django
import django.contrib.auth

import channels_graphql_ws

# ------------------------------------------------------------------------- ASGI ROUTING

# NOTE: Please note `channels.auth.AuthMiddlewareStack` wrapper, for
# more details about Channels authentication read:
# https://channels.readthedocs.io/en/latest/topics/authentication.html
application = channels.routing.ProtocolTypeRouter(
    {
        "websocket": channels.auth.AuthMiddlewareStack(
            channels.routing.URLRouter(
                [django.urls.path("graphql/", MyGraphqlWsConsumer)]
            )
        )
    }
)
