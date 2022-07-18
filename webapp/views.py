from django.http import HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here


class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({'flag': True, 'data': serializer.data})

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'flag': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'flag': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):

    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response({'flag': False, 'message': 'User not found'}, status=status.HTTP_200_OK)
        except:
            return Response({'flag': False, 'message': 'User not found'}, status=status.HTTP_200_OK)

    def get(self, request, id):
        article = self.get_object(id=id)
        serializer = ArticleSerializer(article)
        return Response({'flag': True, 'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, id):
        article = self.get_object(id=id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'flag': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'flag': False, 'message': serializer.errors}, status=status.HTTP_200_OK)

    def delete(self, request, id):
        article = self.get_object(id=id)
        article.delete()
        return Response({'flag': True}, status=status.HTTP_200_OK)

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response({'flag': True, 'data': serializer.data})

#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'flag': True, 'data': serializer.data}, status=status.HTTP_200_OK)
#         return Response({'flag': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#     return Response({'flag': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)

#     except Article.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response({'flag': True, 'data': serializer.data}, status=status.HTTP_200_OK)

#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'flag': True, 'data': serializer.data}, status=status.HTTP_200_OK)
#         return Response({'flag': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=status.HTTP_200_OK)
