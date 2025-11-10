# ue19-lab-05 
Ce projet a été réalisé dans le cadre du **labo 5, cours gestion opérationnelle de la sécurité; ue19**
L'objectif est de créer une petite application programmée en python qui interroge une API publique à l'aide de la librairie Requests
Projet qui permet de récupérer une blague avec API 
L’application choisie ici interroge l’API de blagues :  
(`https://official-joke-api.appspot.com/random_joke`)

Chaque execution du programme interroge l'API et fait donc des blagues.

#Fonctionnalité
-> Interroge une API publique via le protocole HTTP - get -> ok = 200 conditions en fonction de la réponse. 
-> Affiche une blague différente à chaque execution
-> On peut mettre le programme dans un docker

#Installation
Clonez ce dépôt :
```bash
git clone https://github.com/<username>/ue19-lab-05.git
cd ue19-lab-05
