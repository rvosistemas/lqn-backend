from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from strawberry.django.views import GraphQLView
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from core.schema import schema
from core.views import redoc_view, PlanetViewSet, FilmViewSet, CharacterViewSet

router = DefaultRouter()
router.register(r'planets', PlanetViewSet)
router.register(r'films', FilmViewSet)
router.register(r'characters', CharacterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)