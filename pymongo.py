from bson import ObjectId

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['nome_do_banco']

collection = db['nome_da_colecao']

# Consulta todos os documentos na coleção
documents = collection.find()

# Insere um novo documento
new_document = {'name': 'John Doe', 'email': 'john@example.com'}
collection.insert_one(new_document)

# Atualiza um documento existente
document = collection.find_one({'_id': ObjectId('document_id')})
document['name'] = 'Jane Doe'
collection.replace_one({'_id': ObjectId('document_id')}, document)

# Exclui um documento
collection.delete_one({'_id': ObjectId('document_id')})

