

# 自定义过滤规则
from rest_framework.filters import BaseFilterBackend

class MyFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # 真正的过滤规则
        # params=request.GET.get('teacher')
        # queryset.filter('''''')
        return queryset[:1]