from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views

router= DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename= "snippets"),
router.register(r'users', views.UserViewSet, basename="users"),

urlpatterns = [
    path('', include(router.urls))
]

