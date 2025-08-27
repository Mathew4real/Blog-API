from rest_framework import viewsets,generics
from .models import*
from .serializers import UserRegistrationSerializer,BlogSerializer
from rest_framework import permissions


class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class CreateBlog(generics.CreateAPIView):
    queryset = Blog
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)


