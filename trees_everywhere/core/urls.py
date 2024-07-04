
from django.urls import path
from .views import *
from .viewsets import *

urlpatterns = [
    # User
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('users_list/', users_list, name='users_list'),
    path('delete_user/<int:id>/', delete_user, name='delete_user'),
    # account
    path('create_account/', create_account, name='create_account'),
    path('account_list/', account_list, name='account_list'),
    path('account_detail/<int:id>/', account_detail, name='account_detail'),
    path('account_delete/<int:id>/', account_delete, name='account_delete'),
    path('edit_account/<int:id>/', edit_account, name='edit_account'),
    path('update_status/<int:id>/', update_status, name='update_status'),
    path('ajax_change_account/', change_account, name='change_account'),
    # Profile
    
    path('profile/', profile, name='profile'),
    path('edit_profile/<int:id>/', edit_profile, name='edit_profile'),

    # Tree
    path('home/', home , name='home'),
    path('trees/', user_trees, name='user_trees'),
    path('edit_tree/<int:id>/', edit_tree, name='edit_tree'),
    path('tree_detail/<int:pk>/', tree_detail, name='tree_detail'),
    path('add_plant/', add_plant, name='add_plant'),
    path('add_tree/', add_tree, name='add_tree'),
    path('delete_tree/<int:id>/', delete_tree, name='delete_tree'),

    # API METHODS
    path('api/v1/trees/', UserPlantedTreesList.as_view(), name='user_planted_trees_api'),
]
