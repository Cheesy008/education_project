from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'age',
            'role',
        )


class MyRegisterSerializer(RegisterSerializer):
    username = None
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    role = serializers.ChoiceField(choices=get_user_model().ROLE_CHOICES, write_only=True, required=True)

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.role = self.validated_data.get('role', '')
        username = f"{user.first_name} {user.last_name}"
        user.username = username
        user.save(update_fields=['username', 'first_name', 'last_name', 'role'])
