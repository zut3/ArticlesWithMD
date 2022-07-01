from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from serializers.articles import ArticleSerializer
from serializers.auth import UserSerializer
from articles.models import Article
from services import auth
from django.db.utils import IntegrityError
from django.contrib.auth import logout


class Registration(APIView):

    def post(self, request, format=None):
        ser = UserSerializer(request.POST)
        if not ser.is_valid():
            return Response(ser.errors, status=400)

        username = ser.validated_data["username"]
        password = ser.validated_data["password"]
        try:
            user = auth.register_user(username, password)
        except IntegrityError:
            return Response({"error": "User have exist"}, status=400)
        token = Token.objects.create(user=user)
        return Response({"token": str(token[0])}, status=200)


class Login(APIView):

    def post(self, request, format=None):
        ser = UserSerializer(data=request.data)
        if not ser.is_valid():
            return Response(ser.errors, status=400)

        username = ser.validated_data["username"]
        password = ser.validated_data["password"]
        user = auth.get_user(username, password)
        if user is None:
            return Response({"error": "User doesn't exist"}, status=400)
        token = Token.objects.get_or_create(user=user)
        return Response({"token": str(token[0])})


class ArticlesView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.all()


class NewArticleView(generics.CreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.id)


