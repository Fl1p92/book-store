from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include(('apps.core.urls', "core", ), namespace='core')),
    path('', include(('apps.store.urls', "store", ), namespace='store')),
]
