from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bbs/', include('bbs.urls')),#urlにbbsがついていた場合、bbs.urlsを使用する
    path('', RedirectView.as_view(url='/bbs/')),#urlに何もついていないとき、bbsにリダイレクトする
]
