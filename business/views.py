from rest_framework import generics,viewsets
from business.models import Business
from business.serializers import BusinessSerializer


class BusinessCreateListView(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    
class BusinessRetrivieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    
# Para usar apenas um método que faça todo o crud
    
# class BusinessViewSet(viewsets.ModelViewSet):
#     queryset = Business.objects.all()
#     serializer_class = BusinessSerializer