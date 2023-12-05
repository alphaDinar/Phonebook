from rest_framework.response import Response
from rest_framework import viewsets
from .models import SuperMc
from django.contrib.auth.hashers import make_password, check_password
from .serializers import SuperMcSerializer,SuperMcCheckRegisterSerializer

class SuperMcRegister(viewsets.ModelViewSet):
    queryset = SuperMc.objects.all()
    serializer_class = SuperMcSerializer

    def create(self, request, *args, **kwargs):
        customer = SuperMc()
        customer.username = request.data['username']
        customer.phone = request.data['phone']
        customer.password = make_password(request.data['password'])
        customer.key = make_password(request.data['password'])
        customer.save()
        return Response({'status': '200', 'message': 'SuperMc instance created successfully'})
    
class SuperMcCheckRegister(viewsets.ModelViewSet):
    queryset = SuperMc.objects.all()
    serializer_class = SuperMcCheckRegisterSerializer

    def create(self, request, *args, **kwargs):
        customer = SuperMc.objects.get(phone=request.data['phone'])
        key = 'null'
        status = 'null'
        # print(check_password(request.data['password'],customer.password))
        if check_password(request.data['password'],customer.password):
            key = customer.key
            status = 200
        else:
            key = 'fail'
            status = 400
        
        return Response({'status': f'{status}', 'message': f'{key}'})