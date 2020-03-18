







```shell
practice-python/StudioScheduler/projectstudio  5-js ✗ ruby-2.6.1                                             2d4h ⚑ ◒  
▶ python3 manage.py shell
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

>>> from scheduler.models import Artist

>>> artist = Artist.objects.all()[0]

>>> from scheduler.serializers import ArtistSerializer

>>> serializer = ArtistSerializer()

>>> data = serializer.to_representation(artist)
>>>
>>> from rest_framework.renderers import JSONRenderer

>>> renderer = JSONRenderer()

>>> renderer.render(data)
b'{"id":1,"name":"Coach","location":"Harlem"}'

>>> print(renderer.render(data))
b'{"id":1,"name":"Coach","location":"Harlem"}'

>>> ```




