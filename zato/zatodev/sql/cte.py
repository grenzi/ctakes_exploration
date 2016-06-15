# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Corpus(Base):
    __tablename__ = 'Corpus'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))


class CorpusMetadata(Base):
    __tablename__ = 'CorpusMetadata'

    id = Column(Integer, primary_key=True, nullable=False)
    corpusid = Column(ForeignKey(u'Corpus.id'), primary_key=True, nullable=False, index=True)
    keyname = Column(String(45), nullable=False)
    keyvalue = Column(String(255))

    Corpus = relationship(u'Corpus')


class CorpusText(Base):
    __tablename__ = 'CorpusText'

    id = Column(Integer, primary_key=True, nullable=False)
    corpusid = Column(ForeignKey(u'Corpus.id'), primary_key=True, nullable=False, index=True)
    content = Column(String, nullable=False)

    Corpus = relationship(u'Corpus')
