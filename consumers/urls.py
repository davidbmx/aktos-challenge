from rest_framework.routers import DefaultRouter

from consumers.views import ConsumerViewset

router = DefaultRouter()

router.register(r'consumers', ConsumerViewset, basename='consumers')

urlpatterns = router.urls
