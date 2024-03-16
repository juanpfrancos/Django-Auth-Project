from datetime import timedelta
from rest_framework_simplejwt.tokens import Token

class CustomToken(Token):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['exp'] = self.payload['exp']
        self['user_id'] = self.payload['user_id']
        self['username'] = self.payload['username']
        self['email'] = self.payload['email']
        self['is_staff'] = self.payload['is_staff']

    @classmethod
    def create(cls, user, access_token_lifetime=None):
        access_token_lifetime = timedelta(minutes=30) if access_token_lifetime is None else access_token_lifetime
        return super().create(user, access_token_lifetime)
