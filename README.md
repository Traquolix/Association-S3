Application légère pour la gestion de la trésorerie d’une association :

Sommaire :
    1) Import et versions
    2) Gérer adhérents
    3) Générer facture
    4) Générer bon de commande
    5) Gérer bilan
    6) Information CSV

1) Import et versions :
    - Pillow : 8.1.0
    - pip : 20.3.3
    - reportlab : 3.5.59
    - setuptools : 51.3.3
    
2) Gérer adhérents :
/!\ ne pas suprimer tous les adhérents et quitter l'aplication car lors de la réouverture l'aplication va lire des csv vide, ce qui va créer une erreur /!\
   
    Ajouter un adhérent ou une organisation :
        - Ajout d'un adhérent appartenant à une organisation : Rentrez le nom, prénom, selectionner l'organisation (si Il y a des organisations, sinon voir ligne 24), puis cliquez sur ajouter adhérent.
        - Ajout d'un adhérent indépendant : Rentrez le nom, prénom, selectionner indépendant, puis ajoutez l'adresse et la ville de l'adhérent, puis cliquez sur ajouter adhérent.
    
    Le bouton "gérer organisation" permet d'ajouter ou de suprimer une organisation :
        -  Ajout d'une organisation : Rentrez le nom, l'adresse et la ville de l'organisation puis cliquez sur ajouter organisation.
   
    Suprimer un adhérent ou une organisation :
        Il suffit de selectionner l'adhérent ou l'organisation (dans la liste de droite) et cliquer sur le bouton suprimer adhérent ou suprimer organisation.
        Il y a aussi un boutton "tout suprimer" qui permet de suprimer tous les adhérent ou toutes les organisations (/!\ il n'y a pas de confirmation /!\).
    
3) Générer facture
   
    Rentrez le numéro de facture, le bon de commande référent, le montant total, le destinataire et le nombre de personne concernées puis cliquez sur le boutton valider.
    Selectionnez un adhérent, rentrer un type de tarif, puis ajouté le à l'aide du boutton "ajouter".
    Une fois tous les adhérents voulus ajoutés, cliquez sur "générer facture". Choisissez le chemin et le nom de la facture puis enregister.
   
4) Générer bon de commande :
   
    Rentrez le numéro de bon de commande, le destinataire, le montant total, et le nombre de personne concernées puis cliquez sur le boutton valider.
    Selectionnez un adhérent, rentrez le prix unitaire, la quantité, le montant HT, et une remarque (facultatif) puis cliquez sur le boutton ajouter.
    Une fois tous les adhérents voulus ajoutés, cliquez sur "générer bon de commande". Choisissez le chemin et le nom du bon de commande puis enregister.
   
5) Gérer bilan :

    Dans cette fenêtre plusieurs actions sur des opérations sont possibles:
    Toutes les commandes influent sur le fichier bilan_2019.csv qui se situe dans /data/Bilan_financier_2020/
    Les 2 autres fichiers dans ce dossiers sont d'autres fichiers qui pourront être utiliser plus tard pour gérer les prévisions

        Les opérations sont définis par:
            un type (dépense ou recette)
            une catégorie (que l'on peut créer)
            une date
            un montant
            une description (facultativement)

        Ajouter une opération (formulaire gauche):
            Une opération ne doit pas être identique à une opération déja inscrite

            Choisir un des deux type d'opération (dépense ou recette), cela sélectionne la liste de catégorie correspondante au type
            Entrer une date sous le format JJ/MM/AAAA, /!\ tous les mois sont paramétré pour faire 31 jours
            Enter un montant, /!\ le montant doit avoir un point comme séparateur entre la partie entières et la partie décimale et doit contenir 2 chiffres après la virgule
            Entrer une description, cette étape n'est pas obligatoire
            Choisir une catégorie parmis laquelle ajouter cette opération

        Supprimer une opération (liste recette + bouton 'supprimer recette' OU liste depense + bouton 'supprimer depense'):

            Cliquer sur une opération dans une liste et cliquer sur le bouton 'supprimer' correspondant
            /!\ Si vous cliquez sur le mauvais bouton 'supprimer' c'est l'opération en tête de l'autre liste qui sera supprimé

        Modifier une opération (liste recette + bouton 'modifier recette' OU liste depense + bouton 'modifier depense'):
            /!\ Il n'est pas possible de modifier le type et la catégorie d'une opération

            Entrer sur le formulaire a gauche la date, le montant ainsi que la description si nécessaire
            Cliquer sur l'opération a modifié dans les listes
            Cliquer sur le bouton 'modifier' correspondant au type de l'opération à modifier

   Bouton Gestion & Résumé Catégories:
            
        Ce bouton permet d'accéder à la page de gestion de catégorie

   Gestion de catégorie:
        
        Pour créer une catégorie, il suffit de choisir un type (dépense ou recette), d'entrer le nom de la catégorie voulu 
        puis d'appuyer sur le bouton 'Ajouter Catégorie'

        Pour supprimer une catégorie, il faut cliquer sur la catégorie souhaitée dans la liste puis d'appuyer sur 'supprimer catégorie'
        /!\ Supprimer une catégorie supprime toutes ses opérations

6) Information CSV :
    - adherents.csv : Contient tout les adhérent liés à une organisation
    - adherents_independants.csv : Contient tout les adhérent indépendant (ceux qui ne sont pas liés à une organisation)
    - organisations.csv : contient toutes les organisations
    - budget_2019.csv : Contient toutes les opérations ainsi que les catégories