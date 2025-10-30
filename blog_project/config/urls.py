from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple home page view
def home(request):
    return HttpResponse("<h2>Welcome to My Blog API 🚀</h2>")

urlpatterns = [
    path('', home),  # 👈 Root route (fixes 404 at '/')
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),  # user auth routes
    path('api/blog/', include('blog.urls')),   # blog CRUD routes
]
