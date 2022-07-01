from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("articles.urls")),
    path('auth/', include("auth.urls")),
    path('api/', include("api.urls"))
]
