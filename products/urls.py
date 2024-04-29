from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProductCreateView, ProductListView, ProductDetailView

urlpatterns = [
    # 상품 등록
    path("", ProductCreateView.as_view(), name="product-create"),

    # 상품 목록 조회
    path("", ProductListView.as_view(), name="product-list"),

    # 상품 상세 조회, 수정, 삭제
    path("<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
]
