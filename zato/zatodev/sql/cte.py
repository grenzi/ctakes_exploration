# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Corpus(Base):
    __tablename__ = 'Corpus'

    idCorpus = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))


class CorpusMetadatum(Base):
    __tablename__ = 'CorpusMetadatum'

    idCorpusMetadatum = Column(Integer, primary_key=True, nullable=False)
    idCorpus = Column(ForeignKey(u'Corpus.idCorpus'), primary_key=True, nullable=False, index=True)
    KeyName = Column(String(45), nullable=False)
    KeyValue = Column(String(255))

    Corpus = relationship(u'Corpus')


class CorpusText(Base):
    __tablename__ = 'CorpusText'

    idCorpusText = Column(Integer, primary_key=True, nullable=False)
    content = Column(String, nullable=False)
    idCorpus = Column(ForeignKey(u'Corpus.idCorpus'), primary_key=True, nullable=False, index=True)

    Corpus = relationship(u'Corpus')
