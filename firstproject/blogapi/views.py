from django.shortcuts import render
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from blogapi.models import posts

class PostView(APIView):
    def get(self,request,*args,**kwargs):
        if "liked_by" in request.query_params:
            id=int(request.query_params.get("liked_by"))
            data=[post for post in posts if id in post["liked_by"]]
            return Response(data=data)
        return Response(data=posts)

    def post(self,request,*args,**kwargs):
        data=request.data
        posts.append(data)
        return Response(data=data)

class PostDetailView(APIView):
    def get(self,request,*args,**kwargs):
        print(kwargs)
        pid=kwargs.get("pid")
        post=[post for post in posts if post["postId"]==pid].pop()
        return Response(data=post)

    def put(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        post=[post for post in posts if post["postId"]==pid].pop()
        post.update(request.data)
        return Response(data=post)

    def delete(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        post = [post for post in posts if post["postId"] == pid].pop()
        posts.remove(post)
        return Response(data=post)




