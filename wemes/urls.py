"""wemes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework_nested import routers as n_routers

from wemes import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'transactions', views.TransactionViewSet, basename='transactions')
router.register(r'items', views.ItemViewSet, basename='items')
router.register(r'colors', views.ColorViewSet, basename='colors')
router.register(r'categories', views.CategoryViewSet, basename='categories')
# router.register(r'qrcodes', views.QRCodeViewSet, basename='qrcodes')

# generates:
# /<model>/
# /<model>/{pk}/

user_router = n_routers.NestedSimpleRouter(router, r'users', lookup='customer')
user_router.register(r'transactions', views.TransactionViewSet, basename='transactions')
## generates:
# /users/{user_pk}/transactions/
# /users/{user_pk}/transactions/{pk}/

transactions_router = n_routers.NestedSimpleRouter(user_router, r'transactions', lookup='transactions')
transactions_router.register(r'items', views.ItemViewSet, basename='items')
## generates:
# /users/{user_pk}/transactions/{maildrop_pk}/items/
# /users/{user_pk}/transactions/{maildrop_pk}/items/{pk}/

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path(r'', include(router.urls)),
    path(r'', include(user_router.urls)),
    path(r'', include(transactions_router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)