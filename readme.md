# Créer une api relier a un cluster cassandra avec docekr

dans ce brief nous avons fait une api connecter a un cluster cassandra compoé de deux container cassandra

## Contenu

* _docker-cassandra-fastapi_ : doccier contenant toute les ressources
* _app_ : dossier contenant l'api faite avec Fastapi, et le fichier requirement pour créer l'image
* docker-compose.yml_ : le docker-compose utiliser pour le brief
* _Dockerfile_ : le dockerfile pour créer l'image Fastapi

## Pour lancer l'api et cassandra

pour lancer le tout, il faut commancer par aller dans le dossier _docker-cassandra-fastapi_

````bash
cd docker-cassandra-fastapi
````

Une fois dedans, on va build l'image fastapi puis lancer tout les container

````bash
docker-compose build
````
puis 
````bash
docker-compose up -d
````

une fois le docker-compose lancé, il faudra attendre quelque minute pour que cassandra est le temps de s'initialiser

## Creer et remplire la base

Normalement ce niveau le docker-compose s'est lancé.

Mais la base est vide, nous allons la créer et la remplire.

pource faire il faut tout d'abord aller dans l'un des container cassandra

````bash
docker exec -it cassandra-c01 bash
````

une fois dans le container, il faudra lancer le CLI de cassandra

````bash
cqlsh
````

une fois fait, il faudra lancer la commande suivante pour créer et remplire la base

````bash
source 'ressources/init.cql'
````

## Utiliser l'api



puis pour utiliser l'api il sufit d'ouvrire un navigateur web et de taper dans la barre d'adresse `localhost:80`

ce qui vous redirigera vers la doc de l'api, pour faire les test
