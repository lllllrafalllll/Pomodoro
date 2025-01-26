from dataclasses import dataclass
from schema import UserLoginSchema
from repository import UserRepository
from exception import UserNotFoundException, UserNotCorrectPasswordException
from models import UserProfile


@dataclass
class AuthService:
    user_repository: UserRepository

    def login(self, username: str, password: str) -> UserLoginSchema:
        user = self.user_repository.get_user_by_username(username)
        self._validate_auth_user(user, password)
        print(user.id, user.access_token)
        return UserLoginSchema(user_id=user.id, access_token=user.access_token)
    
    
    @staticmethod
    def _validate_auth_user(user: UserProfile, password: str):
        if not user:
            raise UserNotFoundException
        if user.password != password:
            raise UserNotCorrectPasswordException

