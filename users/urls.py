from django.urls import path

from users.views import KakaoSocialLoginView

urlpatterns = [
    path('/login', KakaoSocialLoginView.as_view()),
]