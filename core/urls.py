from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),
    path('basket/', include('basket.urls', namespace='basket')),
    path('account/', include('account.urls', namespace='account')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('sellbook/', include('sellbook.urls', namespace='sellbook')),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
