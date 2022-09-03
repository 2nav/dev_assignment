from django.contrib.auth.models import User

from django.db.migrations.serializer import BaseSerializer
from django.db.migrations.writer import MigrationWriter


class UserSerializer(BaseSerializer):
    def serialize(self):
        return repr(self.username), {'from django.contrib.auth.models import User'}


MigrationWriter.register_serializer(User, UserSerializer)
