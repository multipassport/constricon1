from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from ..db.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(254), unique=True, index=True)
    hashed_password = Column(String(32))
    is_superuser = Column(Boolean, default=True)
    league = Column(String(20))
    # image = ImageField

    favourite_icons = relationship(
        'User',
        secondary='favourite_icon_users',
        back_populates='chosen_users',
    )
    favourite_packs = relationship(
        'User',
        secondary='favourite_pack_users',
        back_populates='chosen_users',
    )
