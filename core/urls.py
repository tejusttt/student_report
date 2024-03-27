"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from home.views import *
from RecipeApp.views import *
from stu.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/', home , name="home"),
    path('recipes/', recipes , name = "recipes"),
    path('delete-recipe/<id>/', delete_recipe, name = "delete_recipe"),
    path('update-recipe/<id>/', update_recipe, name = "update_recipe"),
    path('about/', about, name = "about"),
    path('contact/', contact , name = "contact"),
    path('login/', login_page , name = "login_page"),
    path('register/', register , name = "register"),
    path('logout/', logout_page , name = "logout_page"),
    path('landing-page/', landing_page, name = "landing_page"),
    path('', get_student, name="get_student"),
    path('see-marks/<student_id>/', see_marks, name="see_marks"),
    path('admin/', admin.site.urls),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()