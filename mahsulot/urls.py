from mahsulot.views import MahsulotListView, MenyuListView

from django.urls import path

urlpatterns = [
    path('', MahsulotListView.as_view(), name = 'mahsulot'),
    path('menyu_list', MenyuListView.as_view(), name = 'menyu_list'),
    
]