from rest_framework.pagination import PageNumberPagination


class MarketPaginator(PageNumberPagination):
    page_size = 10
