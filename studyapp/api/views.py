# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from studyapp.models import Room

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    return Response(routes)
    # return JsonResponse(routes,safe=False)

@api_view(['GET'])
def getRooms(request):
    rooms=Room.objects.all()
    return Response(rooms)