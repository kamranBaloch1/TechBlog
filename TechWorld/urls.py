
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("postComment",views.postComment,name="postComment"),
    path('',views.homePage,name="homePage"),
    path('Blogs/<int:id>',views.BlogPage,name="blogPage"),
    path('search',views.search,name="search"),
    path("login",views.loginUser,name="login"),
    path("signup",views.signup,name="signup"),
    path("logout",views.logoutUser,name="logout"),
    path("category/<str:category>",views.category,name="category"),
    path("contact",views.contactUs,name="contact"),
    
    
]
 