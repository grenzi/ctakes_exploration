# coding: utf-8
from sqlalchemy import BigInteger, Column, Index, Integer, Numeric, String, Table, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


t_AMBIGLUI = Table(
    'AMBIGLUI', metadata,
    Column('LUI', String(10), nullable=False, index=True),
    Column('CUI', String(8), nullable=False)
)


t_AMBIGSUI = Table(
    'AMBIGSUI', metadata,
    Column('SUI', String(10), nullable=False, index=True),
    Column('CUI', String(8), nullable=False)
)


t_DELETEDCUI = Table(
    'DELETEDCUI', metadata,
    Column('PCUI', String(8), nullable=False),
    Column('PSTR', Text, nullable=False)
)


t_DELETEDLUI = Table(
    'DELETEDLUI', metadata,
    Column('PLUI', String(10), nullable=False),
    Column('PSTR', Text, nullable=False)
)


t_DELETEDSUI = Table(
    'DELETEDSUI', metadata,
    Column('PSUI', String(10), nullable=False),
    Column('LAT', String(3), nullable=False),
    Column('PSTR', Text, nullable=False)
)


t_MERGEDCUI = Table(
    'MERGEDCUI', metadata,
    Column('PCUI', String(8), nullable=False),
    Column('CUI', String(8), nullable=False)
)


t_MERGEDLUI = Table(
    'MERGEDLUI', metadata,
    Column('PLUI', String(10)),
    Column('LUI', String(10))
)


t_MRAUI = Table(
    'MRAUI', metadata,
    Column('AUI1', String(9), nullable=False),
    Column('CUI1', String(8), nullable=False),
    Column('VER', String(10), nullable=False),
    Column('REL', String(4)),
    Column('RELA', String(100)),
    Column('MAPREASON', Text, nullable=False),
    Column('AUI2', String(9), nullable=False),
    Column('CUI2', String(8), nullable=False, index=True),
    Column('MAPIN', String(1), nullable=False)
)


t_MRCOLS = Table(
    'MRCOLS', metadata,
    Column('COL', String(40)),
    Column('DES', String(200)),
    Column('REF', String(40)),
    Column('MIN', Integer),
    Column('AV', Numeric(5, 2)),
    Column('MAX', Integer),
    Column('FIL', String(50)),
    Column('DTY', String(40))
)


class MRCONSO(Base):
    __tablename__ = 'MRCONSO'
    __table_args__ = (
        Index('X_MRCONSO_SAB_TTY', 'SAB', 'TTY'),
    )

    CUI = Column(String(8), nullable=False, index=True)
    LAT = Column(String(3), nullable=False)
    TS = Column(String(1), nullable=False)
    LUI = Column(String(10), nullable=False, index=True)
    STT = Column(String(3), nullable=False)
    SUI = Column(String(10), nullable=False, index=True)
    ISPREF = Column(String(1), nullable=False)
    AUI = Column(String(9), primary_key=True)
    SAUI = Column(String(50))
    SCUI = Column(String(100), index=True)
    SDUI = Column(String(100), index=True)
    SAB = Column(String(40), nullable=False)
    TTY = Column(String(40), nullable=False)
    CODE = Column(String(100), nullable=False, index=True)
    STR = Column(Text, nullable=False, index=True)
    SRL = Column(Integer, nullable=False)
    SUPPRESS = Column(String(1), nullable=False)
    CVF = Column(Integer)


t_MRCUI = Table(
    'MRCUI', metadata,
    Column('CUI1', String(8), nullable=False),
    Column('VER', String(10), nullable=False),
    Column('REL', String(4), nullable=False),
    Column('RELA', String(100)),
    Column('MAPREASON', Text),
    Column('CUI2', String(8), index=True),
    Column('MAPIN', String(1))
)


t_MRCXT = Table(
    'MRCXT', metadata,
    Column('CUI', String(8), index=True),
    Column('SUI', String(10)),
    Column('AUI', String(9), index=True),
    Column('SAB', String(40), index=True),
    Column('CODE', String(100)),
    Column('CXN', Integer),
    Column('CXL', String(3)),
    Column('RANK', Integer),
    Column('CXS', Text),
    Column('CUI2', String(8)),
    Column('AUI2', String(9)),
    Column('HCD', String(100)),
    Column('RELA', String(100)),
    Column('XC', String(1)),
    Column('CVF', Integer)
)


class MRDEF(Base):
    __tablename__ = 'MRDEF'

    CUI = Column(String(8), nullable=False, index=True)
    AUI = Column(String(9), nullable=False, index=True)
    ATUI = Column(String(11), primary_key=True)
    SATUI = Column(String(50))
    SAB = Column(String(40), nullable=False, index=True)
    DEF = Column(Text, nullable=False)
    SUPPRESS = Column(String(1), nullable=False)
    CVF = Column(Integer)


t_MRDOC = Table(
    'MRDOC', metadata,
    Column('DOCKEY', String(50), nullable=False),
    Column('VALUE', String(200)),
    Column('TYPE', String(50), nullable=False),
    Column('EXPL', Text)
)


t_MRFILES = Table(
    'MRFILES', metadata,
    Column('FIL', String(50)),
    Column('DES', String(200)),
    Column('FMT', Text),
    Column('CLS', Integer),
    Column('RWS', Integer),
    Column('BTS', BigInteger)
)


t_MRHIER = Table(
    'MRHIER', metadata,
    Column('CUI', String(8), nullable=False, index=True),
    Column('AUI', String(9), nullable=False, index=True),
    Column('CXN', Integer, nullable=False),
    Column('PAUI', String(10), index=True),
    Column('SAB', String(40), nullable=False, index=True),
    Column('RELA', String(100)),
    Column('PTR', Text, index=True),
    Column('HCD', String(100)),
    Column('CVF', Integer)
)


t_MRHIST = Table(
    'MRHIST', metadata,
    Column('CUI', String(8), index=True),
    Column('SOURCEUI', String(100), index=True),
    Column('SAB', String(40), index=True),
    Column('SVER', String(40)),
    Column('CHANGETYPE', Text),
    Column('CHANGEKEY', Text),
    Column('CHANGEVAL', Text),
    Column('REASON', Text),
    Column('CVF', Integer)
)


t_MRMAP = Table(
    'MRMAP', metadata,
    Column('MAPSETCUI', String(8), nullable=False, index=True),
    Column('MAPSETSAB', String(40), nullable=False),
    Column('MAPSUBSETID', String(10)),
    Column('MAPRANK', Integer),
    Column('MAPID', String(50), nullable=False),
    Column('MAPSID', String(50)),
    Column('FROMID', String(50), nullable=False),
    Column('FROMSID', String(50)),
    Column('FROMEXPR', Text, nullable=False),
    Column('FROMTYPE', String(50), nullable=False),
    Column('FROMRULE', Text),
    Column('FROMRES', Text),
    Column('REL', String(4), nullable=False),
    Column('RELA', String(100)),
    Column('TOID', String(50)),
    Column('TOSID', String(50)),
    Column('TOEXPR', Text),
    Column('TOTYPE', String(50)),
    Column('TORULE', Text),
    Column('TORES', Text),
    Column('MAPRULE', Text),
    Column('MAPRES', Text),
    Column('MAPTYPE', String(50)),
    Column('MAPATN', String(100)),
    Column('MAPATV', Text),
    Column('CVF', Integer)
)


class MRRANK(Base):
    __tablename__ = 'MRRANK'

    RANK = Column(Integer, nullable=False)
    SAB = Column(String(40), primary_key=True, nullable=False)
    TTY = Column(String(40), primary_key=True, nullable=False)
    SUPPRESS = Column(String(1), nullable=False)


class MRREL(Base):
    __tablename__ = 'MRREL'

    CUI1 = Column(String(8), nullable=False, index=True)
    AUI1 = Column(String(9), index=True)
    STYPE1 = Column(String(50), nullable=False)
    REL = Column(String(4), nullable=False)
    CUI2 = Column(String(8), nullable=False, index=True)
    AUI2 = Column(String(9), index=True)
    STYPE2 = Column(String(50), nullable=False)
    RELA = Column(String(100))
    RUI = Column(String(10), primary_key=True)
    SRUI = Column(String(50))
    SAB = Column(String(40), nullable=False, index=True)
    SL = Column(String(40), nullable=False)
    RG = Column(String(10))
    DIR = Column(String(1))
    SUPPRESS = Column(String(1), nullable=False)
    CVF = Column(Integer)


class MRSAB(Base):
    __tablename__ = 'MRSAB'

    VCUI = Column(String(8))
    RCUI = Column(String(8))
    VSAB = Column(String(40), primary_key=True)
    RSAB = Column(String(40), nullable=False, index=True)
    SON = Column(Text, nullable=False)
    SF = Column(String(40), nullable=False)
    SVER = Column(String(40))
    VSTART = Column(String(8))
    VEND = Column(String(8))
    IMETA = Column(String(10), nullable=False)
    RMETA = Column(String(10))
    SLC = Column(Text)
    SCC = Column(Text)
    SRL = Column(Integer, nullable=False)
    TFR = Column(Integer)
    CFR = Column(Integer)
    CXTY = Column(String(50))
    TTYL = Column(String(400))
    ATNL = Column(Text)
    LAT = Column(String(3))
    CENC = Column(String(40), nullable=False)
    CURVER = Column(String(1), nullable=False)
    SABIN = Column(String(1), nullable=False)
    SSN = Column(Text, nullable=False)
    SCIT = Column(Text, nullable=False)


class MRSAT(Base):
    __tablename__ = 'MRSAT'

    CUI = Column(String(8), nullable=False, index=True)
    LUI = Column(String(10))
    SUI = Column(String(10))
    METAUI = Column(String(100), index=True)
    STYPE = Column(String(50), nullable=False)
    CODE = Column(String(100))
    ATUI = Column(String(11), primary_key=True)
    SATUI = Column(String(50))
    ATN = Column(String(100), nullable=False, index=True)
    SAB = Column(String(40), nullable=False, index=True)
    ATV = Column(Text)
    SUPPRESS = Column(String(1), nullable=False)
    CVF = Column(Integer)


t_MRSMAP = Table(
    'MRSMAP', metadata,
    Column('MAPSETCUI', String(8), nullable=False),
    Column('MAPSETSAB', String(40), nullable=False),
    Column('MAPID', String(50), nullable=False),
    Column('MAPSID', String(50)),
    Column('FROMEXPR', Text, nullable=False),
    Column('FROMTYPE', String(50), nullable=False),
    Column('REL', String(4), nullable=False),
    Column('RELA', String(100)),
    Column('TOEXPR', Text),
    Column('TOTYPE', String(50)),
    Column('CVF', Integer)
)


class MRSTY(Base):
    __tablename__ = 'MRSTY'

    CUI = Column(String(8), nullable=False, index=True)
    TUI = Column(String(4), nullable=False)
    STN = Column(String(100), nullable=False)
    STY = Column(String(50), nullable=False, index=True)
    ATUI = Column(String(11), primary_key=True)
    CVF = Column(Integer)


t_MRXNS_ENG = Table(
    'MRXNS_ENG', metadata,
    Column('LAT', String(3), nullable=False),
    Column('NSTR', Text, nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXNW_ENG = Table(
    'MRXNW_ENG', metadata,
    Column('LAT', String(3), nullable=False),
    Column('NWD', String(100), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_BAQ = Table(
    'MRXW_BAQ', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_CHI = Table(
    'MRXW_CHI', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_CZE = Table(
    'MRXW_CZE', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_DAN = Table(
    'MRXW_DAN', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_DUT = Table(
    'MRXW_DUT', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_ENG = Table(
    'MRXW_ENG', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_EST = Table(
    'MRXW_EST', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_FIN = Table(
    'MRXW_FIN', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_FRE = Table(
    'MRXW_FRE', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_GER = Table(
    'MRXW_GER', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_GRE = Table(
    'MRXW_GRE', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_HEB = Table(
    'MRXW_HEB', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_HUN = Table(
    'MRXW_HUN', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_ITA = Table(
    'MRXW_ITA', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_JPN = Table(
    'MRXW_JPN', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(500), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_KOR = Table(
    'MRXW_KOR', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(500), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_LAV = Table(
    'MRXW_LAV', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_NOR = Table(
    'MRXW_NOR', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_POL = Table(
    'MRXW_POL', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_POR = Table(
    'MRXW_POR', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_RUS = Table(
    'MRXW_RUS', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_SCR = Table(
    'MRXW_SCR', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_SPA = Table(
    'MRXW_SPA', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_SWE = Table(
    'MRXW_SWE', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)


t_MRXW_TUR = Table(
    'MRXW_TUR', metadata,
    Column('LAT', String(3), nullable=False),
    Column('WD', String(200), nullable=False, index=True),
    Column('CUI', String(8), nullable=False),
    Column('LUI', String(10), nullable=False),
    Column('SUI', String(10), nullable=False)
)
