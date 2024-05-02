from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter


# 상품 등록, 상품 조회 (GET 요청시에만 페이지네이션 및 필터링(검색기능) 가능 / POSTMAN BODY에 JSON 형식으로 넣으면 기능 안되는게 정상)
class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    pagination_class = PageNumberPagination  # 페이지네이션 클래스 설정
    pagination_class.page_size = 3  # 페이지당 게시글 수 설정

    def get_queryset(self):
        queryset = Product.objects.all()
        title = self.request.query_params.get('title', None)
        username = self.request.query_params.get('username', None)
        content = self.request.query_params.get('content', None)
        if title:
            queryset = queryset.filter(title__icontains=title)
        if username:
            queryset = queryset.filter(username=username)
        if content:
            queryset = queryset.filter(content__icontains=content)
        return queryset

    def perform_create(self, serializer):
        serializer.save(username=self.request.user.username)


# 상품 수정 및 삭제
class ProductUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.username != request.user.username:
            raise PermissionDenied("해당 권한이 없습니다.")
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.username != request.user.username:
            raise PermissionDenied("해당 권한이 없습니다.")
        serializer = self.get_serializer(
            instance, data=request.data, partial=kwargs.get('partial', False)
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
