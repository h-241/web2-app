from sqlmodel import Field, Relationship, SQLModel



# JSON payload containing access token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: int | None = None


class NewPassword(BaseModel):
    token: str
    new_password: str
