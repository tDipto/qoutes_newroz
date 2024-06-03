from django.urls import path
from .views import ExtractQuotesView, QuoteDetailView,QuoteSingleDetailView,AuthorQuotesView

urlpatterns = [
    path('extract_quotes/', ExtractQuotesView.as_view(), name='extract-quotes'),
    path('quotes/', QuoteDetailView.as_view(), name='quote-detail'),
    path('quotes/<int:pk>', QuoteSingleDetailView.as_view(), name='quote-detail'),

    path('quotes/<str:author>/', AuthorQuotesView.as_view(), name='author-quotes'),


]
