

import os
from django.core.asgi import get_asgi_application
#下からの内容を追加
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from websocket.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangowebsocket.settings')

application = ProtocolTypeRouter({
     "http": get_asgi_application(),
     "websocket": AuthMiddlewareStack(
         URLRouter(
             websocket_urlpatterns
         )
     )
 }

 )

