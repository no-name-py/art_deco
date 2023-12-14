from .models import *
from .serializer import *
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

class ImageListView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImagePortfolioSerializer
    permission_classes = [IsAuthenticated]

class ImageCreateView(CreateAPIView):
    serializer_class = ImagePortfolioSerializer
    permission_classes = [IsAdminUser]

class ImageuUpdateView(UpdateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImagePortfolioSerializer
    permission_classes = [IsAdminUser]

class ImageuDeleteView(DestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImagePortfolioSerializer
    permission_classes = [IsAdminUser]



class ProjestsListView(ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [IsAuthenticated]

class ProjestsCreateView(CreateAPIView):
    serializer_class = ProjectsSerializer
    permission_classes = [AllowAny]

class ProjectsUpdateView(UpdateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [IsAdminUser]

class ProjectsDeleteView(DestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [IsAdminUser]













