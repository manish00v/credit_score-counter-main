# credit_bureau/urls.py

from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('question_view')  # Redirect to questions if logged in
    else:
        return redirect('login')  # Redirect to login if not logged in

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_redirect, name='home_redirect'),  # Root URL redirect
    path('questions/', include('credit.urls')),  # Include credit app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication URLs
]
