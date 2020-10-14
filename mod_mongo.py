#Exercice 1
import datetime
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
bd = client.db.posts_db

posts = {"auteur":"Flouflou",
         "texte":"Mon premier post du mois",
         "tags":["python","mongodb"],
         "date":datetime.datetime.utcnow()}

#Insertion d'un seul post
post_id = bd.insert_one(posts).inserted_id
print(post_id)
#exercice 2
#Obtenir un document
import pprint as p
p.pprint(bd.find_one())
print("=" * 50)
#recherche par un critere
p.pprint(bd.find_one({"auteur":"Flouflou"}))
#recherche par un critere
print("=" * 50)
p.pprint(bd.find_one({"auteur":"Mike"}))

#Exercice 3
liste_posts= [
{"auteur":"FlouClair",
         "texte":"Le renard saute la barriere",
         "tags":["renard","barriere"],
         "date":datetime.datetime.utcnow()},
{"auteur":"ClairClair",
         "texte":"les moutons n'ont aucune chance",
         "tags":["mouton","chance"],
         "date":datetime.datetime.utcnow()}
]
#Insertion et recupÃ©ration des ID
resultats = bd.insert_many(liste_posts)
print("=" * 50)
print(resultats.inserted_ids)
#RecupÃ©rer les posts qui sont dans la collection
for post in bd.find():
    p.pprint(post)
    print("="*40)

#Afficher un count de tous les documents
print("="*60)
print(bd.count_documents({}))