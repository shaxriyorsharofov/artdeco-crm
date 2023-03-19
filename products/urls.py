from django.urls import path
from .views import ProductsView, NewsView, Product_detail, new_comment, delete_comment

app_name = 'product'
urlpatterns = [
    path('', ProductsView, name='products'),
    path('new/', NewsView, name='news'),
    path('<int:product_id>/detail/', Product_detail, name='detail'),
    path("<int:product_id>/comment/new", new_comment, name='comment_new'),
    path("<int:product_id>/comment/<int:comment_id>/delete", delete_comment, name='comment_delete'),

]
