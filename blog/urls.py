from django.urls import path
from .views import home_view, about_view, contact_view, blog_view, blog_detail_view


urlpatterns = [
     path('', home_view),
     path('about/', about_view),
     path('contact/', contact_view),
     path('blog/', blog_view),
     path('blog/<int:a>', blog_detail_view),
]