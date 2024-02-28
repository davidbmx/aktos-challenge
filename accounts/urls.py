from rest_framework.routers import DefaultRouter

from accounts.views import AccountsView

router = DefaultRouter()

router.register(r'accounts', AccountsView, basename='accounts')

urlpatterns = router.urls
