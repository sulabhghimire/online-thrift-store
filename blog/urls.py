from django.urls import path
from . import views
from .views import (
    SellAdvertiseDetailView,
    AskAdvertiseDetailView, 
    SellingList,
    BuyingList, 
    PostItem, 
    SellItem, 
    PostItemUpdate,
    SellItemUpdate,
    PostItemDelete,
    SellItemDelete,
    YourAsking,
    YourSelling,
    CategoryPage,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('search_title/', views.SearchTitle, name='search'),
    path('category_search/<int:pk>/', CategoryPage.as_view(), name='catego-search'),
    path('onsale_detail/<int:pk>/', SellAdvertiseDetailView.as_view(), name='sell_detail'),
    path('onask_detail/<int:pk>/', AskAdvertiseDetailView.as_view(), name='buy_detail'),
    path('onsale_list/', SellingList.as_view(), name='sell_list'),
    path('onask_list/', BuyingList.as_view(), name='ask_list'),
    path('listitem/', PostItem.as_view(), name='list_item'),
    path('askitem/', SellItem.as_view(), name='ask_item'),
    path('onsale_detail/<int:pk>/update', PostItemUpdate.as_view(), name='list-update'),
    path('onask_detail/<int:pk>/update', SellItemUpdate.as_view(), name='ask-update'),
    path('onsale_detail/<int:pk>/delete', PostItemDelete.as_view(), name='list-delete'),
    path('onask_detail/<int:pk>/delete', SellItemDelete.as_view(), name='ask-delete'),
    path('profile/myasking', YourAsking.as_view(), name='asking'),
    path('profile/myselling', YourSelling.as_view(), name='selling'),
]