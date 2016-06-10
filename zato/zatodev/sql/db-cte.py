# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Corpus(Base):
    __tablename__ = 'Corpora'

    idCorpus = Column(Integer, primary_key=True)
    name = Column(String(255))
    metadata = Column(String)


class Corpu(Base):
    __tablename__ = 'Corpus'

    idCorpus = Column(Integer, primary_key=True)
    name = Column(String(255))
    metadata = Column(String)


class CorpusText(Base):
    __tablename__ = 'CorpusText'

    idCorpusText = Column(Integer, primary_key=True, nullable=False)
    content = Column(String, nullable=False)
    Corpus_idCorpus = Column(ForeignKey(u'Corpus.idCorpus'), primary_key=True, nullable=False, index=True)

    Corpu = relationship(u'Corpu')
