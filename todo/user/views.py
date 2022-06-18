from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer


class UserView(APIView):

    def get(self, request):
        return Response({'message': 'Hello, World!'})

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            name = user_serializer.validated_data.get('name')
            return Response({'name': name})
        return Response(user_serializer.errors, status=400)

    def put(self, request, pk=None):
        return Response({'message': 'PUY'})

    def delete(self, request, pk=None):
        return Response({'message': 'DELETE'})
