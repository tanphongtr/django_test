import binascii
import os

from django.db import models
from django.utils.translation import ugettext_lazy as _
# from my_project.companies.models import Company


class Token(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(_("Key"), max_length=40, primary_key=True)

    # company = models.OneToOneField(
    #     Company, related_name='auth_token',
    #     on_delete=models.CASCADE, verbose_name="Company"
    # )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key