from rest_framework.authentication import TokenAuthentication
from django_test.models import Token

class TokenAuthentication(TokenAuthentication):
    model = Token