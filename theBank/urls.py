from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PropertyMarket.urls')),
    path('blogs/', include('Blog.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('contact/', include('ContactUs.urls')),
    path('faqs/', include('FAQS.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
