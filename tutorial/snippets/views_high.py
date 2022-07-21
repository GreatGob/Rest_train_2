from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers, generics
from .models import Snippet
from .serializers import SnippetSerializer

from rest_framework import permissions
from .permission import IsOwnerReadOnly
from .serializers import UserSerializer
from django.contrib.auth.models import User




class SnippetHighlight(generics.GenericAPIView):
    queryset= Snippet.objects.all()
    renderer_classes= [renderers.StaticHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        snippet= self.get_object()
        return Response(snippet.highlighted)
    
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    def perform_create(self, serializer):
        serializer.save(owner= self.request.user)
    permission_classes= [permissions.IsAuthenticatedOrReadOnly]

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes= [permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly]
    
class UserList(generics.ListAPIView):
    queryset= User.objects.all()
    serializer_class= UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset= User.objects.all()
    serializer_class= UserSerializer