from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Assignment
from .serializers import AssignmentSerializer, UserSerializer, ChangePasswordSerializer
from .permissions import IsSuperUserOrReadOnly

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class AssignmentViewSet(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated, IsSuperUserOrReadOnly]

    # Add filtering, searching, and pagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'assignee']
    search_fields = ['name', 'description']
    ordering_fields = ['created_at', 'updated_at']

    def get_queryset(self):
        
        if self.request.user.is_superuser:
            return Assignment.objects.all()
        return Assignment.objects.filter(assignee=self.request.user)
    





class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]  

    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"message": "Password updated successfully."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    