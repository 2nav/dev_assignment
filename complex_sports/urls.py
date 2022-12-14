"""complex_sports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from Users import views as user_views
from Sports import views as sport_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sport_views.home, name='home'),
    path('sport/<int:id>/', sport_views.sportsDetailView, name='sport-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('register/', user_views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('slots/', sport_views.SlotListView.as_view(), name='slot-list'),
    path('slots/<int:id>', sport_views.SlotDetailView, name='slot-detail'),
    path('bookings/', sport_views.BookingListView.as_view(), name='booking-list'),
    path('bookings/<int:id>', sport_views.BookingDetailView, name='booking-detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
