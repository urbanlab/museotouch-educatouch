INSTALLATION

https://docs.google.com/document/d/16XiiIOVHsMI1e4RbTmKDsdmGEER45u2yHAsZ41uEVoA/edit

LICENSE
Museotouch, Logiciel d'exploration de collections pour interface tactile utilisant Kivy                        *
 *  Concept : Département du Rhône, Muchomedia, Trafik *  
 *  Développement : Département du Rhône, Muchomedia, Biin *  
 *  Produit par Erasme, centre d'innovation du Département du Rhône  *
 *  Copyright (c) 2008-2012                                                *
 *  Contact : museotouch-utilisateurs@googlegroups.com (usages) / museokivy@googlegroups.com (développement) *

Ce programme est un logiciel libre distribue sous licence AGPL-V3 : https://www.gnu.org/licenses/agpl-3.0.html *
Vous pouvez l'utiliser, le distribuer et le modifier selon les termes de cette license. *
Pour plus de details voir la page de présentation : http://www.erasme.org/tout-savoir-sur-Museotouch *

## Procédure de configuration de la nouvelle table
S'assurer que la version de python installée est python 2.7.12 (commande `python -V` en ligne de commande pour afficher la version de python installée)
Se rendre sur http://aka.ms/vcpython27 et télécharger VCForPython27.msi (c'est le compilateur C++ pour python 2.7)
Exécuter le fichier téléchargé (le guide d'installation s'ouvrira)
En ligne de commande depusi le dépot où se trouve l'application, installer twisted: `pip install twisted`
Installer de la même façon nfcpy: `pip install nfcpy`
Mettre à jour la dernière version de kivy: `pip install --upgrade kivy`
Lancer le "main" de l'application
Première utilisation: il faut lancer un par un tous les modules pour ques les données et médias soient téléchargés. Bien vérifier que tout a été chargé lors du lancement du module (possibilité d'erreur timeOut Excpetion). En cas d'erreur, relancer le module. Répéter.

