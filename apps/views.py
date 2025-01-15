from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from apps.models import CustomUsers, Post
from apps.serializers import UserSerializer, PostSerializer


class HelleWorldAPIView(APIView):

    def get(self,request):
        return JsonResponse({"message":"Hello World!"})

class HelloNameAPIView(APIView):
    def get(self,request):
        name  = request.GET.get('name')
        return JsonResponse({'message':f'Hello {name}!'})

class HelloLanguageAPIView(APIView):

    def get(self,request):
        language = request.GET.get('language')
        name = request.GET.get('name')
        response = {
            'uz': f'Salom {name}!',
            'en': f'Hello {name}!',
            'es': f'Hola {name}!',
        }
        return JsonResponse({"message": response.get(language,"error")})




################################ Homework ===============================

#### user API
@api_view(['GET', 'POST', 'PUT', 'DELETE','PATCH'])
def user_combo_view(request,pk=None):
    if request.method == 'GET':
        instances = CustomUsers.objects.all()
        response = UserSerializer(instances, many=True).data
        return JsonResponse({'response':response},status=HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data
        s = UserSerializer(data=data)
        response = {"message": "error"}
        if s.is_valid():
            obj = s.save()
            response = UserSerializer(instance=obj).data
        return JsonResponse(response)
    elif request.method == 'PUT':
        user = CustomUsers.objects.filter(pk=pk).first()
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return JsonResponse({"message": "error"})
    elif request.method == 'DELETE':
        user,_ = CustomUsers.objects.filter(pk=pk).delete()
        if user:
            return JsonResponse({'message': 'user deleted'},status=HTTP_204_NO_CONTENT)
        return JsonResponse({'message': 'Topilmadi'})
    elif request.method == 'PATCH':
        user = CustomUsers.objects.filter(pk=pk).first()
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_200_OK)
        return JsonResponse({"message": "error"})



#### blog post API
@api_view(['GET', 'POST', 'PUT', 'DELETE','PATCH'])
def user_post_combo_view(request,pk=None):
    if request.method == 'GET':
        instances = Post.objects.all()
        user = request.GET.get('user',default=None)
        if user is not None:
            instances = Post.objects.filter(user=user)
        response = PostSerializer(instances, many=True).data
        return JsonResponse({'response':response},status=HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data
        s = PostSerializer(data=data)
        response = {"message": "error"}
        if s.is_valid():
            obj = s.save()
            response = PostSerializer(instance=obj).data
        return JsonResponse(response)
    elif request.method == 'PUT':
        user = request.GET.get('user',default=None)
        if user is not None:
              post = Post.objects.filter(pk=pk,user=user).first()
              serializer = PostSerializer(post, data=request.data)
              if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=HTTP_200_OK)
        return JsonResponse({"message": "error"})
    elif request.method == 'DELETE':
        post , _ = Post.objects.filter(pk=pk).delete()
        if post:
            return JsonResponse({'message': 'post deleted'},status=HTTP_200_OK)
        return JsonResponse({"message": "error"})
    elif request.method == 'PATCH':
        user = request.GET.get('user', default=None)
        if user is not None:
            post = Post.objects.filter(pk=pk).first()
            serializer = PostSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=HTTP_200_OK)
        return JsonResponse({"message": "error"})




