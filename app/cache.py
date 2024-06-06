import time

class TokenCache:
    def __init__(self):
        self.token = None
        self.expiry_time = None

    def set_token(self, token, expires_in):
        self.token = token
        self.expiry_time = time.time() + expires_in

    def get_token(self):
        if self.token and self.expiry_time > time.time():
            return self.token
        return None

token_cache = TokenCache()
