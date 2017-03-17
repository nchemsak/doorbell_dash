from django.conf.urls import url, include
from rest_framework import routers
from doorbell_dash_app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'photos', views.PhotoViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
