from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(dotenv_path=BASE_DIR)

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')), # Django JET URLS    
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path(r'', include('api.urls')),
    path(str(os.getenv('DJANGO_ADMIN_URL')), admin.site.urls),
]
