from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import requests
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def home(request):
    return render(request, 'search/home.html')

@csrf_exempt
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
            'final_result': final_result
        }

        return render(request, 'search/search.html', context)

    else:
        return render(request, 'search/search.html')













# def search(request):
#     # if request.method == 'GET':
#     #     word = request.GET.get('word')
#     #     api = 'https://www.ask.com/web?q='+word
#     #     result = request.get(api)
#     #     soup = bs4(result.text, 'lxml')
#     #     result_list = soup.find_all('div', {'class':'PartialSearchResults-item'})
#     #     final_results = []
#     #     for result in result_list:
#     #         result_title = result.find(class_='PartialSearchResults-item-title').text
#     #         result_url = result.find('a').get('href')
#     #         result_desc = result.find(class_='PartialSearchResults-item-abstract').text
#     #         final_results.append((result_title, result_url, result_desc))
#     #     context = {
#     #         'final_results':final_results,
#     #     }
#         return render(request, 'search/search.html')
