from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="ALX Travel App API",
        default_version='v1',
        description="API documentation for ALX Travel App - Listings Management",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@alxtravelapp.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Listings app URLs
    path('api/', include('listings.urls')),
    
    # API Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), 
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), 
         name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), 
         name='schema-json'),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
