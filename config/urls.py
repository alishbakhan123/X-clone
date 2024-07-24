"""
URL configuration for config project.

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
from django.urls import path
from x.views import xListView, xAdd, xDelete, xEditView, xLikeAdd, xLikeSubtract

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', xListView),
    path('xAdd/', xAdd),
    path('xDelete/<int:x_id>/', xDelete),
    path('xEditView/<int:x_id>/', xEditView),
    path('xLikeAdd/<int:x_id>/', xLikeAdd),
    path('xLikeSubtract/<int:x_id>/', xLikeSubtract),
]
