# Heater_Mining

Transformation d'un Mineur S9 Antminer en chauffage de l'habitat autonome au travers d'un thermostat connecté.

## Mes motivations

J'ai souhaité développer un système de chauffage par l'intermédiaire d'un mineur de crypto-monnaie piloté 
en température au travers d'un thermostat connecté. Le concept est exposé dans le
[Wiki](https://github.com/bastoon577-lang/Heater_Mining/wiki#principe-de-fonctionnement).

<div align="center"><img width="800" height="300" alt="Schéma_global" src="https://github.com/user-attachments/assets/9c0f9ee7-0cf2-4009-9c8e-e94505eed17c" /></div>

## Matériel nécessaire

Vous trouverez la liste du matériel nécessaire dans le 
[Wiki](https://github.com/bastoon577-lang/Heater_Mining/wiki#choix-du-mat%C3%A9riel).

## Tansformer le Mineur en chauffage

J'expose 2 voies pour permettre l'intégration du mécanisme dans le Mineur Antminer S9.
 1. [Utilisation de l'image pre-compilée](#reuse) (Mode débutant)
 2. [Re-construction d'une image custom](#diy) (Mode expert)
 
> ⚠️ **ATTENTION** néanmoins au boot du S9 sur carte SD.
>
> Il est nécessaire de persuader le mineur de booter sur la carte SD en suivant cette [procédure](https://academy.braiins.com/en/braiins-os/installation/install/#install-braiins-os-on-s9-s9i-s9j)
> en prenant soin d'intégrer une image de ce repo.

<div id='reuse'/> 

### Utilisation de l'image pre-compilée

Je met à disposition une [image pre-compilée](https://github.com/bastoon577-lang/Heater_Mining) que vous pouvez immédiatement charger avec Rufus en suivant 
ce [tuto de flashage](https://rufus.ie/fr/) sur une [carte SD](https://github.com/bastoon577-lang/Heater_Mining/wiki#une-carte-microsd-avec-adaptateur).

Cette image embarque tout le nécessaire à l'exploitation du mineur sur le réseau. Il ne reste qu'à positionner la 
configuration du thermostat au travers de l'interface WEB du Mineur en suivant ce [tuto de configurations thermostat](https://github.com/bastoon577-lang/Heater_Mining/wiki/Interractions-avec-le-script-de-monitoring#param%C3%A9trage-du-monitoring)
avec les paramètres Tuya pouvant être extrait en suivant ce [tuto d'extraction de paramètres](https://github.com/bastoon577-lang/Heater_Mining/wiki/Obtenir-les-informations-du-thermostat).

<div id='diy'/>

### Re-construction d'une image custom

La re-construction consiste à générer l'image custom pas à pas à partir d'une image 
officielle en vue de créer l'image par vous même en suivante les étapes suivantes:
 1. Télécharger une image [BraiinOS](https://feeds.braiins-os.com/)
 2. Etendre l'image pour lever les [contraintes mémoire](https://github.com/bastoon577-lang/Heater_Mining/wiki/Contraintes-m%C3%A9moire#cons%C3%A9quences-sur-la-m%C3%A9moire-et-le-stockage) 
  en suivant cette [procédure](https://github.com/bastoon577-lang/Heater_Mining/wiki/Contraintes-m%C3%A9moire#g%C3%A9n%C3%A9ration-par-extension-de-braiinos-custom)
 3. Flasher la carte SD de l'image custom avec [Rufus](https://rufus.ie/fr/)
 4. Ouvrir le service SSH sur le Mineur
 5. Se connecter en SSH
 6. 

###### Auteur : *Sébastien DALIGAULT*. 
