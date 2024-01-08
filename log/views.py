from rest_framework.response import Response
from rest_framework import viewsets
from .models import SuperMc
from django.contrib.auth.hashers import make_password, check_password
from .serializers import SuperMcSerializer,SuperMcVerifyUserSerializer

class SuperMcRegister(viewsets.ModelViewSet):
    queryset = SuperMc.objects.all()
    serializer_class = SuperMcSerializer

    def create(self, request, *args, **kwargs):
        customer = SuperMc()
        customer.username = request.data['username']
        customer.phone = request.data['phone']
        customer.key = make_password(request.data['key'])
        customer.login_email = f"{request.data['phone']}@gmail.com"
        customer.login_password = request.data['key']
        customer.save()
        return Response({'status': '200', 'message': 'SuperMc instance created successfully'})
    
class SuperMcVerifyUser(viewsets.ModelViewSet):
    queryset = SuperMc.objects.all()
    serializer_class = SuperMcVerifyUserSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        customer = SuperMc.objects.get(phone=request.data['phone'])
        key = 'null'
        status = 'null'
        if check_password(request.data['key'],customer.key):
            key = customer.key
            status = 200
        else:
            key = 'fail'
            status = 400
        return Response({'status': f'{status}', 'email': f'{customer.login_password}', 'password' : f'{customer.login_email}'})