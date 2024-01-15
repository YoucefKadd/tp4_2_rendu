# Utilisez l'image Python officielle
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copie tous les fichiers du répertoire local dans le conteneur
COPY . .

# Installe les dépendances spécifiées dans le fichier requirements.txt
RUN pip install -r requirements.txt

# Commande pour démarrer l'application lorsque le conteneur est lancé
CMD ["python", "app.py"]