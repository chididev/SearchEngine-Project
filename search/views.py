from django.shortcuts import render
import lxml
from bs4 import BeautifulSoup as bs4


# Create your views here.
def home(request):
    return render(request, 'search/home.html')

def search(request):
    if request.method == 'POST':
        search = request.POST('search')
        url = 'https://www.ask.com/web?q='+search
        res = request.get(url)
        soup = bs4(res.text, 'lxml')
        result_list = soup.find_all('div', {'class': 'PartialSearchResults-item'})
        final_results = []

        for result in result_list:
            result_title = result.find(class_='PartialSearchResults-item-title').text
            result_url = result.find('a').get('href')
            result_desc = result.find(class_='PartialSearchResults-item-abstract').text
            final_results.append((result_title, result_url, result_desc))
        context = {
                'final_results':final_results,
            }
        return render(request, 'search/search.html', context)

    else:
        return render(request, 'search/search.html')
