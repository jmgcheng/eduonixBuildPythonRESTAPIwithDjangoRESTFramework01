from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


# check 07. Creating View Function for the API
#   using ArticleSerializer of 06 lesson
#   open in the browser to check result
# postman
#   GET
#       http://127.0.0.1:8000/
#       http://127.0.0.1:8000/articles/
#   POST
#       http://127.0.0.1:8000/
#       body - raw - JSON
#       {
#           "title": "test my postman",
#           "description": "This is the description in postman"
#       }
#       forbidden CSRF cookie not set
#           add decorator @csrf_exempt
@csrf_exempt
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)

        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# check 07. Creating View Function for the API
#   using ArticleSerializer of 06 lesson
#   open in the browser to check result
# postman
#   GET
#       http://127.0.0.1:8000/articles/this-is-title/
#   PUT
#       http://127.0.0.1:8000/articles/test-my-postman/
#       body - raw - JSON
#       {
#           "title": "test my postman updated",
#           "description": "This is the description in postman. This is also udpated"
#       }
#   DELETE
#       http://127.0.0.1:8000/articles/test-my-postman/
@csrf_exempt
def article_details(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == "DELETE":
        article.delete()
        return HttpResponse(status=204)

    