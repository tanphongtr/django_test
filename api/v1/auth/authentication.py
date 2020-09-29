from rest_framework.authentication import TokenAuthentication
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from datetime import datetime, timedelta


class _TokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        # now = datetime.now()
        # exp = now - token.created

        # print(now)
        # print(datetime.datetime(token.created))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (token.user, token)

    pass