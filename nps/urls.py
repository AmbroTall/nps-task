from django.urls import path, include
from rest_framework import routers
from .views import SystemSettings, Response,dowell_scale_admin,dowell_scale, default_scale

app_name="nps"
router = routers.DefaultRouter()
router.register('nps-setting', viewset=SystemSettings)
router.register('nps-response', viewset=Response)
urlpatterns = [
    path('', include(router.urls)),
    path('nps-admin/', dowell_scale_admin,name='admin_page'),
    path('nps-scale/<str:tname>', dowell_scale, name='detail_page'),
    path('nps-scale/default/', default_scale, name='default_page')
]


# from .views import response_create, system_settings_create, SystemSettingsAll,setting_view_detail
# urlpatterns = [
#     path('nps-scale-settings/', system_settings_create, name="settings_page"),
#     path('nps-response/', response_create, name="response_page"),
#     path('all-nps-settings/', SystemSettingsAll.as_view(), name="settings_all"),
#     path('nps-single-setting/<int:pk>/', setting_view_detail, name='detailview'),
# ]