
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),

  path('accounts/', include('django.contrib.auth.urls')),

  path('', include('apps.GUIAS.urls')),

  path('restrito/', include('apps.RESTRITO.urls')),

  path('cadastro/', include('apps.CADASTRO.urls')),

]


