from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="KeyDevsTest API",
        default_version='v1',
        description="API documentation",
        contact=openapi.Contact(email="imanalievaliser@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('ratings.urls')),
    path('api/', include('posts.urls')),
    path('api/', include('comments.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0))
]
