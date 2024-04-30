from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProductListCreateView, ProductUpdateDeleteView

urlpatterns = [
    # 상품 등록, 목록 조회
    path("", ProductListCreateView.as_view(), name="product-list-create"),

    # 상품 수정, 삭제
    path("<int:pk>/", ProductUpdateDeleteView.as_view(), name="product-update-delete"),
]
