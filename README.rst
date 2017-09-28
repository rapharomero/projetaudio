Reconnaissance vocale avec Google cloud
=======================================


Principe
--------

- Requête : On envoie une requête aux services cloud de Google en spécifiant l’emplacement du fichier, et des paramètres de config (taux échantillonnage, encodage, langue du décodeur)
-	Réponse : On reçoit une réponse constituée texte décodé et d’autre part d’un taux de confiance associé au décodage.

3 types de requêtes : Synchrones, Asynchrones et Streaming
----------------------------------------------------------
-	Synchrone : utile pour les fichiers de moins d’1 minute stockés en local. (possible d’utiliser ça si on trouve comment découper les fichiers vocaux et rassembler les mots obtenus)

- Asynchrone :  Ce que j’utilise pour le moment : On envoie le fichier sur le cloud, on donne accès au fichier à l’application pour qu’il fasse la reconnaissance et on récupère soit la réponse finale soit une réponse temporaire avec le texte qui a été décodé pour l’instant en attendant la fin du traitement.

-	Streaming : On envoie les fichiers en continu, ils sont stockés temporairement dans une mémoire- tampon avant d’être traités et on récupère la réponse au fur et à mesure. (peut être possible d’utiliser ça mais je ne vois pas encore comment)

Méthode Utilisée:
-----------------
On utilise un requête asynchrone en spécifiant l’adresse du fichier stocké sur le cloud (format URI), ça met à peu près 2-3 mn à renvoyer un résultat.
Il faut au préalable:
-Avoir stocké le fichier audio sur l'API Cloud Storage
-Avoir converti les fichiers en format flac
-Avoir obtenu une clé d'authentification de la Google API (Platforme -> Créer un projet -> Comptes de service -> créer compte de service -> créer clé au format JSON -> entrer la clé à la place de "myproject1")

Utilisation :

python async_sr.py <uri du fichier sur le cloud> <fichier de sauvegarde du texte>

Problèmes rencontrés:
---------------------

-Autoriser juste notre application à accéder au fichier stocké sur le Stockage Cloud, dans le cas contraire la solution serait de rendre public les fichiers audio

-Problème d’encodage de la réponse.

-Cette méthode implique de devoir envoyer chaque fichier sur le stockage cloud de google ce que n'est pas applicable à toute une base de données.


Documentation
-------------
- Google Cloud Speech Recognition: https://cloud.google.com/speech/docs/
- Comptes de service Google Cloud : https://cloud.google.com/compute/docs/access/service-accounts
- Google Cloud Storage : https://cloud.google.com/storage/docs/?hl=fr
