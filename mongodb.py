from pymongo import MongoClient
from urllib.parse import quote_plus

# 1. Conectar ao MongoDB Atlas
# Substitua 'your_password' pela sua senha real
username = "guihbs"
password = "466@@123#"
escaped_password = quote_plus(password)
connection_string = f"mongodb+srv://{username}:{escaped_password}@bank.xaaphph.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)

# 2. Criação do banco de dados e da coleção
db = client['bank_db']
collection = db['bank']

# 3. Inserir Documentos na Coleção 'bank'
clientes = [
    {
        "Nome": "João Silva",
        "cpf": "123456789",
        "endereco": "Rua A, 123",
        "contas": [
            {"num": 1234, "agencia": "5678", "tipo": "corrente", "saldo": 1000.00},
            {"num": 2345, "agencia": "6789", "tipo": "poupança", "saldo": 2000.00}
        ]
    },
    {
        "Nome": "Maria Oliveira",
        "cpf": "109876543",
        "endereco": "Rua B, 456",
        "contas": [
            {"num": 3456, "agencia": "7890", "tipo": "corrente", "saldo": 3000.00}
        ]
    }
]

# Inserir os documentos na coleção
collection.insert_many(clientes)

# 4. Recuperar Informações
# Recuperar todos os documentos
print("Recuperar todos os clientes:")
for cliente in collection.find():
    print(cliente)

# Recuperar clientes por nome
print("\nRecuperar cliente por nome 'João Silva':")
cliente_joao = collection.find_one({"Nome": "João Silva"})
print(cliente_joao)

# Recuperar todas as contas de um cliente específico
print("\nRecuperar todas as contas de 'Maria Oliveira':")
cliente_maria = collection.find_one({"Nome": "Maria Oliveira"})
if cliente_maria:
    for conta in cliente_maria['contas']:
        print(conta)

# Recuperar clientes com saldo maior que um valor específico
print("\nRecuperar clientes com saldo maior que 1500.00:")
clientes_com_saldo = collection.find({"contas.saldo": {"$gt": 1500.00}})
for cliente in clientes_com_saldo:
    print(cliente)
