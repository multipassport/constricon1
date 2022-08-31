from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db.database import Base


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    # image = ImageField
    packs = relationship('Pack', secondary='pack_items', back_populates='items')
    tags = relationship('Tag', secondary='pack_tags', back_populates='items')
    item_parts = relationship('ItemPart', back_populates='item')


class Pack(Base):
    __tablename__ = 'packs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    colour = Column(String(5))
    least_permitted_league = Column(String(20))
    width = Column(Integer)
    heigth = Column(Integer)

    items = relationship('Item', secondary='pack_items', back_populates='packs')
    tags = relationship('Tag', secondary='pack_tags', back_populates='packs')
    parts = relationship('Part', back_populates='pack')
    chosen_users = relationship(
        'User',
        secondary='favourite_pack_users',
        back_populates='favourite_packs',
    )


class PackItem(Base):
    __tablename__ = 'pack_items'

    id = Column(Integer, primary_key=True, index=True)

    item_id = Column(Integer, ForeignKey('items.id'))
    pack_id = Column(Integer, ForeignKey('packs.id'))


class Template(Base):
    __tablename__ = 'templates'

    id = Column(Integer, primary_key=True, index=True)
    # preview = ImageField

    parts = relationship('Part', back_populates='template')
    icons = relationship('Icon', back_populates='template')


class Part(Base):
    __tablename__ = 'parts'

    id = Column(Integer, primary_key=True, index=True)
    leftmost_coordinate = Column(Integer)
    rightmost_coordinate = Column(Integer)
    uppermost_coordinate = Column(Integer)
    lowermost_coordinate = Column(Integer)

    template_id = Column(Integer, ForeignKey('templates.id'))
    template = relationship('Template', back_populates='parts')
    pack_id = Column(Integer, ForeignKey('packs.id'))
    pack = relationship('Pack', back_populates='parts')
    item_parts = relationship('ItemPart', back_populates='part')


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(20), unique=True)

    items = relationship('Item', secondary='item_tags', back_populates='tags')
    packs = relationship('Pack', secondary='pack_tags', back_populates='tags')


class ItemTag(Base):
    __tablename__ = 'item_tags'

    id = Column(Integer, primary_key=True, index=True)

    item_id = Column(Integer, ForeignKey('items.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))


class PackTag(Base):
    __tablename__ = 'pack_tags'

    id = Column(Integer, primary_key=True, index=True)

    pack_id = Column(Integer, ForeignKey('packs.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))


class FavouritePackUser(Base):
    __tablename__ = 'favourite_pack_users'

    id = Column(Integer, primary_key=True, index=True)

    pack_id = Column(Integer, ForeignKey('packs.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
