# Utilisez une image de base Python
FROM python:3.8

# Créez le répertoire /app
RUN mkdir /app

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers requis dans le conteneur
COPY app.py /app/
COPY data.py /app/
COPY templates /app/templates/

# Installez les dépendances
RUN pip install --no-cache-dir Flask pymongo flask_paginate

# Exposez le port
EXPOSE 5000
    
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]