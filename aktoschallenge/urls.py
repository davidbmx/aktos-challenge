from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('consumers.urls', 'consumers'))),
    path('', include(('accounts.urls', 'accounts')))
]
