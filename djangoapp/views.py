from django.http import HttpResponse
from django.shortcuts import render

from .database import client




def index(request):
    return HttpResponse("<h1>Testando Django e Mongodb</h1>")



#Define Db Name
dbname = client['testemongo']

#Define Collection
collection = dbname['pymongo']

jovem_1={
    "registro": "1515151-0",
    "nome": "Marcos Antonio Manfre",
    "secao": "Tropa 2",
    "data_nascimento": "11/12/1950"
}


collection.insert_one(jovem_1)

for jovem in collection.find():
    print(jovem.get('_id'))
    print(jovem.get('nome'))