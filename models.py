from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import relationship

url = URL.create(
    drivername='postgresql+psycopg2',
    username='postgres',
    password='1234',
    host='localhost',
    database='postgres',
    port=5432
)
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Operadora(Base):
    __tablename__ = 'operadora'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=True)
    cnpj = Column(String, nullable=True)


class Prestador(Base):
    __tablename__ = 'prestador'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=True)
    cnpj = Column(String, nullable=True)
    cidade = Column(String, nullable=True)
    estado = Column(String, nullable=True)


class Procedimento(Base):
    __tablename__ = 'procedimento'
    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String, nullable=True)
    valor = Column(Float, nullable=True)
    operadora_id = Column(Integer, ForeignKey('operadora.id'))
    operadora = relationship(Operadora)


class Beneficiario(Base):
    __tablename__ = 'beneficiario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=True)
    num_carteira = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    procedimento_id = Column(Integer, ForeignKey('procedimento.id'))
    prestador_id = Column(Integer, ForeignKey('procedimento.id'))
    procedimento = relationship(Procedimento)
    prestador = relationship(Prestador)



Base.metadata.create_all(engine)
