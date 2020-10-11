from django.urls import path     
from . import views
urlpatterns = [
    path('', views.all_shows),
    path('new',views.new_show),	   
    path('<int:show_id>', views.show_details),
    path('add_new', views.add_new),
    path('<int:edit_id>/edit', views.edit_page),
    path('<int:show_id_to_update>/update_show', views.update_show),
    path('<int:delete_show_id>/delete',views.destroy)
]