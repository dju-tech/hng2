from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics



class PersonViewList(generics.ListCreateAPIView):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer

class PersonViewDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer
  lookup_field = 'pk_or_name'

  def get_object(self):
    pk_or_name = self.kwargs.get('pk_or_name')

    if pk_or_name.isdigit():
        lookup_field = 'pk'
    else:
        lookup_field = 'name'

    queryset = self.get_queryset()
    obj = get_object_or_404(queryset, **{lookup_field: pk_or_name})
    self.check_object_permissions(self.request, obj)
    return obj









