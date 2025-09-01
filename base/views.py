from rest_framework import generics
from .models import*
from .serializers import UserRegistrationSerializer,BlogSerializer,UserprofileUpdateSerializer
from rest_framework import permissions
from rest_framework .response import  Response
from rest_framework import status
from rest_framework . exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend


class UserRegistration(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class CreateBlog(generics.CreateAPIView):
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)
      

class BlogList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]

class UpdateBlog(generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_update(self, serializer):
        blog = self.get_object()
        if blog.owner != self.request.user:
            raise PermissionDenied("Você não é o autor deste blog.")
        serializer.save()
class DeleteBlog(generics.RetrieveDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("Nao tem permissao para executar esta acao")
        instance.delete()


class UserProfile(generics.RetrieveUpdateAPIView):
    queryset = User
    serializer_class = UserprofileUpdateSerializer
    permission_classes  = [permissions.IsAuthenticated]
    def perform_update(self, serializer):
        blog = self.get_object()
        if blog.owner != self.request.user:
            raise PermissionDenied("voce nao tem autorizacao de mudar esse perfil")
        serializer.save()        


      

