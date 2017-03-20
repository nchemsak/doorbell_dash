from django.conf.urls import url, include
from rest_framework import routers
from doorbell_dash_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'photos', views.PhotoViewSet)
router.register(r'cachedImage', views.CachedImageViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^$', views.index, name='index'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
