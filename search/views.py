from django.shortcuts import render
from django.core.paginator import Paginator
from bs4 import BeautifulSoup as bs
import requests


# Create your views here.
def home(request):
    return render(request, 'search/home.html')


def search(request):
    if request.method == 'GET':
        search = request.GET['search']
        url = 'https://www.ask.com/web?q='+search
        res = requests.get(url)
        soup = bs(res.text, 'lxml')

        result_listings = soup.find_all('div', {'class': 'PartialSearchResults-item'})

        final_result = []

        for result in result_listings:
            result_title = result.find(class_='PartialSearchResults-item-title').text
            result_url = result.find('a').get('href')
            result_desc = result.find(class_='PartialSearchResults-item-abstract').text

            final_result.append((result_title, result_url, result_desc))

        context = {
            'search': search,
            'final_result': final_result,
        }

        return render(request, 'search/search.html', context)

    else:
        return render(request, 'search/search.html')
