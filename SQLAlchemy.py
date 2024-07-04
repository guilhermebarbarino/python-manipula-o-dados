# 1. Importações e Configurações Iniciais
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Numeric, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Configuração do Base para a criação das classes
Base = declarative_base()

# 2. Definição das Classes (Modelos)
class Cliente(Base):
    __tablename__ = 'cliente'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    Nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))
    contas = relationship('Conta', back_populates='cliente')

class Conta(Base):
    __tablename__ = 'conta'
    
    id = Column(LargeBinary, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))
    saldo = Column(Numeric)
    cliente = relationship('Cliente', back_populates='contas')

# 3. Criação do Banco de Dados e das Tabelas em Memória
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# 4. Sessão e Inserção de Dados
Session = sessionmaker(bind=engine)
session = Session()

# Inserção de dados
cliente1 = Cliente(Nome='João Silva', cpf='123456789', endereco='Rua A, 123')
cliente2 = Cliente(Nome='Maria Oliveira', cpf='109876543', endereco='Rua B, 456')

conta1 = Conta(id=b'1', tipo='corrente', agencia='5678', num=1234, id_cliente=1, saldo=1000.00)
conta2 = Conta(id=b'2', tipo='poupança', agencia='6789', num=2345, id_cliente=1, saldo=2000.00)
conta3 = Conta(id=b'3', tipo='corrente', agencia='7890', num=3456, id_cliente=2, saldo=3000.00)

session.add_all([cliente1, cliente2, conta1, conta2, conta3])
session.commit()

# 5. Recuperação de Dados
# Recuperar todos os clientes
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(f'Cliente: {cliente.Nome}, CPF: {cliente.cpf}, Endereço: {cliente.endereco}')
    for conta in cliente.contas:
        print(f'   Conta: {conta.num}, Agência: {conta.agencia}, Tipo: {conta.tipo}, Saldo: {conta.saldo:.2f}')
