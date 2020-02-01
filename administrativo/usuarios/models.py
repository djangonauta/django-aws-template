"""Modelos da aplicação usuarios."""

import hashlib

from django.contrib.auth import models

# from auditlog.models import AuditlogHistoryField dj3
# from auditlog.registry import auditlog dj3
from model_utils.models import TimeStampedModel


class Usuario(TimeStampedModel, models.AbstractUser):
    """Usuário base do projeto."""

    class Meta:
        """Model meta."""

        verbose_name = 'Usuário'
        db_table = 'administrativo\".\"usuarios_usuario'

    # history = AuditlogHistoryField() dj3

    def gravatar_url(self):
        """Obtém a url gravatar em função do email fornecido."""
        email_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()
        return '//www.gravatar.com/avatar/{}'.format(email_hash)


# auditlog.register(Usuario) dj3
