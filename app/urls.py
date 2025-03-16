from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuração do Schema View
schema_view = get_schema_view(
    openapi.Info(
        title="Business register API Cliente",
        default_version='v1',
        description="A presente documentação ahu",
        terms_of_service="https://www.exemplo.com/termos/",
        contact=openapi.Contact(email="suporte@exemplo.com"),
        license=openapi.License(name="Licença MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/v1/', include('business.urls')),

    # URLs para a documentação da API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
