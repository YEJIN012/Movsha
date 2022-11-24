from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User
from movies.serializers.user import UserSerializer

class CustomRegisterSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password, email
    # 추가 설정 필드: profile_image, nickname
    profile_image = serializers.ImageField(required=False, use_url=True)
    nickname = serializers.CharField(max_length=10)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['profile_image'] = self.validated_data.get('profile_image', '')
        data['nickname'] = self.validated_data.get('nickname', '')
        
        return data

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('profile_image',)

class NicknameSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('nickname',)
