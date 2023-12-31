from djoser.serializers import UserCreateSerializer
from .models import CustomUser

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "password"]