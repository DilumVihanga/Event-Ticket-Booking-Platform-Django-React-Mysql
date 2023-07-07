from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from events.views import EventViewSet
from events.views import AdminViewSet
from events.views import OrganizerViewSet
from events.views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('events', EventViewSet, basename='event')
router.register('admin', AdminViewSet, basename='admin')
router.register('organizer', OrganizerViewSet, basename='organizer')
router.register('user', UserViewSet, basename='user')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]+static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
