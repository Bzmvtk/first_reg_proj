from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirmation = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirmation', 'image')


    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User with this email has already existed')
        return email

    def validate(self, validate_data):
        # print(validate_data)
        password = validate_data.get('password')
        password_confirmation = validate_data.get('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError("Parol' nevernyi")
        return validate_data

    def create(self, validate_data):
        email = validate_data.get('email')
        password = validate_data.get('password')
        image = validate_data.get('image')
        user = User.objects.create_user(email, password, image)
        return user