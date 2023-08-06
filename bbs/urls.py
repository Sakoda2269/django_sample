from django.urls import path
from . import views


app_name = "bbs"

urlpatterns = [
    path("", views.index, name="index"),#bbs/の場合(第一引数）、viewsのindex関数を呼び出す
    path("<int:id>", views.detail, name="detail"),#bbs/id(整数)でその番号の投稿の詳細を表示
    path("create", views.create, name="create"),#記事の作成
    path("<int:id>/delete", views.delete, name="delete"),#記事の削除
    path("new", views.new, name="new"),#新規の記事の入力画面
    path("<int:id>/edit", views.edit, name="edit"),#記事の編集画面
    path("<int:id>/update",views.update, name="update"),#記事の編集
]