from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bs4 import BeautifulSoup
import requests
from rest_framework import generics



from .models import Quote
from .serializers import QuoteSerializer

class ExtractQuotesView(APIView):

    def post(self, request):
        url = request.data.get('url')
        if not url:
            return Response({'error': 'URL is required'}, status=status.HTTP_400_BAD_REQUEST)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raises a HTTPError for bad responses (4xx or 5xx)
        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        soup = BeautifulSoup(response.content, 'html.parser')
        quotes = soup.select('div.quoteText')

        if not quotes:
            return Response({'error': 'No quotes found on the page'}, status=status.HTTP_400_BAD_REQUEST)

        extracted_quotes = []
        for quote in quotes:
            quote_text = quote.contents[0].strip().replace('“', '').replace('”', '')
            author_tag = quote.find('span', class_='authorOrTitle')
            if author_tag:
                author = author_tag.string.strip()
                extracted_quotes.append({'text': quote_text, 'author': author})
            else:
                return Response({'error': 'Author not found for a quote'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = QuoteSerializer(data=extracted_quotes, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class QuoteDetailView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class QuoteSingleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer





class QuoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        author = self.kwargs['author']
        return Quote.objects.filter(author=author)


from django.db.models import Q

class AuthorQuotesView(generics.ListCreateAPIView):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        author = self.kwargs['author']
        return Quote.objects.filter(Q(author__icontains=author))
