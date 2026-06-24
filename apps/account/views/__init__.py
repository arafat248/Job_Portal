from .auth import (
    EmployeeRegistrationView,
    EmployerRegistrationView,
    UserLoginView,
    UserLogoutView,
)
from .profile import (
    EmployeeEditProfileView,
    EmployerEditProfileView,
    CandidateProfileView,
    EmployerProfileView,
)

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema

from ..models import User, EmployeeProfile, EmployerProfile
from ..models.user import UserSerializer, UserRegistrationSerializer
from ..models.profiles import EmployeeProfileSerializer, EmployerProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegistrationSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

    @swagger_auto_schema(
        operation_description="Get current user profile",
        responses={200: UserSerializer}
    )
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class EmployeeProfileViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'employee':
            return EmployeeProfile.objects.filter(user=self.request.user)
        return EmployeeProfile.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EmployerProfileViewSet(viewsets.ModelViewSet):
    serializer_class = EmployerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'employer':
            return EmployerProfile.objects.filter(user=self.request.user)
        return EmployerProfile.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

