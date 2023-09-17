from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets


# check 12. Viewsets Routers
# browsable API UI and POSTMAN same usage as before
# watch video why he only made list and create
class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






# check 12. Viewsets Routers
# browsable API UI and POSTMAN same usage as before





# check 11. Generic Class Based View
# browsable API UI and POSTMAN same usage as before
# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# check 11. Generic Class Based View
# browsable API UI and POSTMAN same usage as before
# class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
#     lookup_field = 'slug'
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer







# check 10. Mixins in Class Based View
# browsable API UI and POSTMAN same usage as before
# class ArticleList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# check 10. Mixins in Class Based View
# browsable API UI and POSTMAN same usage as before
# class ArticleDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     lookup_field = 'slug'

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)






# check 09. Class Based API View
# browsable API UI and POSTMAN same usage as before
# 
# class ArticleList(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# check 09. Class Based API View
# browsable API UI and POSTMAN same usage as before
# 
# class ArticleDetails(APIView):
#     def get_object(self, slug):
#         try:
#             return Article.objects.get(slug=slug)
#         except Article.DoesNotExist:
#             raise Http404
    
#     def get(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
    
#     def put(self, request, slug):
#         article = self.get_object(slug)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug):
#         article = self.get_object(slug)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    





# check 08. API View Decorator
# browsable UI Api can be seen now in this setup
#   http://127.0.0.1:8000/articles/
# postman
#   GET
#       http://127.0.0.1:8000/articles/
#   POST
#       http://127.0.0.1:8000/articles/
#       body - raw - JSON
#       {
#           "title": "api view decorator",
#           "description": "This is the description in postman"
#       }
# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)

#         return Response(serializer.data)
    
#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
            
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# check 08. API View Decorator
# browsable UI Api can be seen now in this setup
#   http://127.0.0.1:8000/articles/
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
# @api_view(['GET', 'PUT', 'DELETE'])
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# check 07. Creating View Function for the API
#   using ArticleSerializer of 06 lesson
#   open in the browser to check result
# postman
#   GET
#       http://127.0.0.1:8000/
#       http://127.0.0.1:8000/articles/
#   POST
#       http://127.0.0.1:8000/
#       http://127.0.0.1:8000/articles/
#       body - raw - JSON
#       {
#           "title": "test my postman",
#           "description": "This is the description in postman"
#       }
#       forbidden CSRF cookie not set
#           add decorator @csrf_exempt
# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)

#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
            
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


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
# @csrf_exempt
# def article_details(request, slug):
#     try:
#         article = Article.objects.get(slug=slug)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
    
#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)

    