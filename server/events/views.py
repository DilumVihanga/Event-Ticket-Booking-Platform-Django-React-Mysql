from django.shortcuts import render
from .models import Event , Admin , Organizer , User
from .serializers import EventSerializer, AdminSerializer, OrganizerSerializer, UserSerializer
from rest_framework import viewsets



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer  

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer    

from django.shortcuts import render
from django.http import JsonResponse

""" def register_view(request):
    if request.method == 'POST':
        user_name = request.POST.get('userNAME')
        user_email = request.POST.get('userEMAIL')
        user_password = request.POST.get('USERPASSWORD')
        user_phone = request.POST.get('userPHONE')
        user_nic = request.POST.get('userNIC')

        # Process registration logic
        # ...

        return JsonResponse({'message': 'Registration successful'})
    else:
        # GET method is not supported for registration
        return JsonResponse({'message': 'Method not allowed'}, status=405) """
