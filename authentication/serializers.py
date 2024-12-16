from django.utils.translation import gettext_lazy as _
from .models import User
from django.contrib.auth import authenticate
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'full_name', 'password', 'account_type']
        write_only_fields = ('password')
        read_only_fields = ('is_staff', 'is_superuser', 'is_active')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserAuthSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get(
                'request'), email=email, password=password)
            if not user:
                # Avoid specifying exact error for security reasons
                raise serializers.ValidationError(
                    _("Unable to log in with provided credentials."), code='authorization')
        else:
            raise serializers.ValidationError(
                _("Must include 'email' and 'password'."), code='authorization')

        # If authentication succeeds, retrieve the user object
        attrs['user'] = user
        return attrs
