import requests
import json

# URL de base de l'API JSONPlaceholder
BASE_URL = "https://jsonplaceholder.typicode.com"

# Fonction pour effectuer une requête GET
def get_request(url):
    response = requests.get(url)
    return response.json()

# Fonction pour effectuer une requête POST
def post_request(url, data):
    response = requests.post(url, json=data)
    return response.json()

# Fonction pour effectuer une requête PUT
def put_request(url, data):
    response = requests.put(url, json=data)
    return response.json()

# Fonction pour effectuer une requête DELETE
def delete_request(url):
    response = requests.delete(url)
    return response.status_code

# Fonction pour récupérer une liste de ressources
def get_resources(resource):
    url = f"{BASE_URL}/{resource}"
    response = get_request(url)
    return response

# Fonction pour créer une nouvelle ressource
def create_resource(resource, data):
    url = f"{BASE_URL}/{resource}"
    response = post_request(url, data)
    return response

# Fonction pour récupérer les détails d'une ressource
def get_resource(resource, id):
    url = f"{BASE_URL}/{resource}/{id}"
    response = get_request(url)
    return response

# Fonction pour mettre à jour une ressource
def update_resource(resource, id, data):
    url = f"{BASE_URL}/{resource}/{id}"
    response = put_request(url, data)
    return response

# Fonction pour supprimer une ressource
def delete_resource(resource, id):
    url = f"{BASE_URL}/{resource}/{id}"
    response = delete_request(url)
    return response

# Exemples d'utilisation des fonctions CRUD avec l'API JSONPlaceholder

# Récupération de la liste des utilisateurs
users = get_resources("users")
print(users)

# Création d'un nouvel article
new_post = {
    "title": "Nouvel article",
    "body": "Contenu de l'article",
    "userId": 1
}
created_post = create_resource("posts", new_post)
print(created_post)

# Récupération des détails d'un article
post = get_resource("posts", 1)
print(post)

# Mise à jour de l'article
updated_post = {
    "title": "Article mis à jour",
    "body": "Contenu mis à jour"
}
result = update_resource("posts", 1, updated_post)
print(result)

# Suppression d'un article
delete_status = delete_resource("posts", 1)
print(delete_status)
