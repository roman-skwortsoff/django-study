from django.urls import path
from .views import shop_index, groups_list, start_page

appname = 'shopapp'
urlpatterns = [
path('', start_page, name='start'),
path('shop/', shop_index, name='index'),
path('groups/', groups_list, name='groups_list')
]