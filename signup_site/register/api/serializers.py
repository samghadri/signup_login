from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, ValidationError, EmailField, CharField
User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label = 'Email Address')
    email2 = EmailField(label = 'Verify Email')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
            ]
        extra_kwargs ={'password':{'write_only':True}
        }
    def validate(self, data):
        email = data['email']
        user_queryset = User.objects.filter(email = email)
        if user_queryset.exists():
            raise ValidationError('This email already exists')
        return data


    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get('email2')
        email2 = value
        if email1 != email2:
            raise ValidationError('Emails must Match!')
        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get('email')
        email2 = value
        if email1 != email2:
            raise ValidationError('Emails must Match!')
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
        username = username,
        email = email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
        'username',
        'email',
        ]

class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(label='User Name..', max_lengh=30)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token',
            ]
        extra_kwargs ={'password':{'write_only':True}
        }
    def validate(self, data):
        # email = data['email']
        # user_queryset = User.objects.filter(email = email)
        # if user_queryset.exists():
            raise ValidationError('This email already exists')
