from rest_framework.pagination import CursorPagination, PageNumberPagination


class SmallPageNumberPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'limit'


class LargePageNumberPagination(PageNumberPagination):
    page_size = 10


class MyCursorPagination(CursorPagination):
    page_size = 2
    ordering = 'difficulty'
