# Car Price Prediction

### Prédiction du prix des voitures en real-time
Ce projet a pour objectif de prédire le prix des voitures Peugeot 206 en fonction des données extraites du site Avito. Le processus se déroule en plusieurs étapes :

## Étapes du Projet :

1. **Chargement du code HTML depuis Avito avec Selenium :**
   - Utilisation de la bibliothèque Selenium pour extraire le contenu HTML des pages des voitures  sur Avito.

2. **Analyse et extraction des données avec BeautifulSoup :**
   - Analyse du code HTML récupéré pour extraire les informations pertinentes telles que le prix, le modèle, le kilométrage, etc. avec BeautifulSoup.

3. **Analyse des données avec Pandas :**
   - Nettoyage et préparation des données extraites à l'aide de Pandas pour les rendre exploitables pour la modélisation.

4. **Création d'un modèle de prédiction :**
   - Développement d'un modèle de machine learning pour prédire le prix d'une Peugeot 206 en fonction des caractéristiques fournies par l'utilisateur.

5. **Intégration de Streamlit pour le Déploiement :**
   - Utilisation de Streamlit pour créer une application web qui permet aux utilisateurs de saisir des caractéristiques de la voiture et d'obtenir une prédiction du prix.
   - Utilisation de la bibliothèque **pickle** pour sauvegarder et charger le modèle de prédiction, facilitant ainsi son déploiement.

## Technologies Utilisées :

- **Selenium** : Pour l'extraction des données depuis le site web.
- **BeautifulSoup** : Pour le parsing et l'extraction des données du HTML.
- **Pandas** : Pour l'analyse et le nettoyage des données.
- **Scikit-learn/TensorFlow** : Pour la création du modèle de prédiction.
- **Streamlit** : Pour la création de l'application web et le déploiement du modèle.
- **pickle** : Pour sauvegarder et charger le modèle de machine learning.

## Comment exécuter le projet :

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances nécessaires à partir du fichier `requirement.txt`.
3. Exécutez l'application Streamlit pour interagir avec le modèle via l'interface web.

## Contributeurs :
- [Ibnchakroune Houssam] - Développeur principal

---

**Note :** Ce projet est à des fins éducatives et de démonstration. Les résultats obtenus peuvent varier en fonction de la qualité et de la quantité des données extraites.
