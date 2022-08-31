from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from ..db.database import Base


class Icon(Base):
    __tablename__ = 'icons'

    id = Column(Integer, primary_key=True, index=True)
    # preview = ImageField
    template_id = Column(Integer, ForeignKey('templates.id'))
    template = relationship('Template', back_populates='icons')
    tag_id = Column(Integer, ForeignKey('tags.id'))
    tag = relationship('Tag', back_populates='icons')
    chosen_users = relationship(
        'User',
        secondary='favourite_icon_users',
        back_populates='favourite_icons',
    )


class IconPart(Base):
    __tablename__ = 'icon_parts'

    id = Column(Integer, primary_key=True, index=True)

    icon_id = Column(Integer, ForeignKey('icons.id'))
    icon = relationship('Icon', back_populates='icon_parts')
    part_id = Column(Integer, ForeignKey('parts.id'))
    part = relationship('Part', back_populates='icon_parts')
    item_id = Column(Integer, ForeignKey('items.id'))
    item = relationship('Item', back_populates='icon_parts')


class FavouriteIconUser(Base):
    __tablename__ = 'favourite_icon_users'

    id = Column(Integer, primary_key=True, index=True)

    icon_id = Column(Integer, ForeignKey('icons.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
