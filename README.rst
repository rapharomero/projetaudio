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

J’utilise un requête asynchrone en spécifiant l’adresse du fichier stocké sur le cloud (format URI), ça met à peu près 2-3 mn à renvoyer un résultat.

Problèmes rencontrés :
---------------------

Autoriser juste notre application à accéder au fichier stocké sur le Stockage Cloud, dans le cas contraire la solution serait de rendre public les fichiers audio
Problème d’encodage de la réponse.
