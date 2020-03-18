from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination


from scheduler.serializers import ArtistSerializer, SessionSerializer
from scheduler.models import Artist, Session


class ArtistList(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    #filter_fields = ('name',)


class SessionList(ListAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = '__all__'
#    filter_fields = ('status', 'appointment_date',)
    #pagination_class = ProductsPagination
