from django.contrib.auth import get_user_model
from rest_framework.serializers import (ModelSerializer,
                                        ValidationError,
                                        EmailField,
                                        CharField)

from django.db.models import Q

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
    username = CharField(required=False, allow_blank =True)
    email = EmailField(label = 'Email', required=False, allow_blank =True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
            ]
        extra_kwargs ={'password':{'write_only':True}
        }
    def validate(self, data):
        user_obj = None
        email = data.get('email')
        username = data.get('username')
        password = data['password']
        if not username and not email:
            raise ValidationError('Wrong Email or username')

        user = User.objects.filter(
        Q(email = email) |
        Q(username=username)
        # Q allow us using OR or AND to get info from database. src info: https://stackoverflow.com/questions/6567831/how-to-perform-or-condition-in-django-queryset
        ).distinct() # In case if there is a doublicate just allows us to use one of them
        user = user.exclude(email__isnull=True).exclude(email__iexact=True) #allow to exclude emails if user doesnt have
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError('The Username or mail is Not Valid')

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('InCorrect password! try again.')
        data['token'] = "Random Token"
        return data
