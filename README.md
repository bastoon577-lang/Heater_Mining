# Heater_Mining

Transformation d'un Mineur S9 Antminer en chauffage de l'habitat autonome au travers d'un thermostat connecté.

<div align="center"><img width="800" height="300" alt="Schéma_global" src="https://github.com/user-attachments/assets/9c0f9ee7-0cf2-4009-9c8e-e94505eed17c" /></div>

## Mes motivations

J'ai souhaité développer un système de chauffage par l'intermédiaire d'un mineur de crypto-monnaie piloté 
en température au travers d'un thermostat connecté dont le principe de fonctionnement est décrit [ici](https://github.com/bastoon577-lang/Heater_Mining/wiki#principe-de-fonctionnement).

## Concept

Les mineurs de cryptomonaies utilisent des cartes de hashage permettant la validation des transactions au sein de la blockchain. Gourmant en énergie, 
ces équippements dissipent de la chaleur par leurs activitées de minage. L'objectif de ce projet est de permettre de chauffer l'habitat par une boucle d'asservissement
en utilisant un thermostat connecté au sein du réseau Local Area Network (LAN).

## Matériel nécessaire

La liste détaillée du matériel est décrite [ici](https://github.com/bastoon577-lang/Heater_Mining/wiki#choix-du-mat%C3%A9riel):
 * Un mineur S9,
 * Un thermostat connecté
 * Une carte MicroSD

## Tansformer le Mineur

> ⚠️ **ATTENTION** au boot du S9 sur carte SD.
>
> Il est nécessaire de persuader le mineur de booter sur la carte SD en suivant cette [procédure](https://academy.braiins.com/en/braiins-os/installation/install/#install-braiins-os-on-s9-s9i-s9j) tout en prenant soin d'intégrer une image spéciphique de ce repo.

J'expose 2 voies pour permettre la transformation du Mineur Antminer S9.
 1. [Utilisation de l'image pre-compilée](#reuse) (Mode débutant)
 2. [Re-construction d'une image custom](#diy) (Mode expert)

<div id='reuse'/>
 
### Utilisation de l'image pre-compilée

Je met à disposition une [image pre-compilée disponible sur mon drive](https://drive.google.com/drive/folders/1-P7-u0t1UEWt9rnBm152xv2MaqvQLXVr) que vous pouvez immédiatement charger avec Rufus en suivant la [procédure de flashage](https://rufus.ie/fr/). 

Cette image embarque tout le nécessaire à l'exploitation du mineur sur le réseau et possède son service SSH fermé par sécurité, il reste néanmoins nécessaire de paramétrer le Module TIC sur le Mineur en suivant cette [procédure](#parameters).

<div id='diy'/>

### Re-construction d'une image custom

La re-construction consiste à générer l'image custom pas à pas à partir d'une image 
officielle en vue de créer l'image par vous même en suivant [cette procédure](https://github.com/bastoon577-lang/Heater_Mining/wiki/Re%E2%80%90construction-d'une-image-custom), puis d'effectuer la configuration du thermostat sur le Mineur en suivant cette [procédure](#parameters).

<div id='parameters'/>
 
## Paramétrer le Thermostat sur le Mineur

Il ne reste qu'à positionner la configuration du thermostat au travers de l'interface WEB du Mineur en suivant ce [tuto de configurations thermostat](https://github.com/bastoon577-lang/Heater_Mining/wiki/Interractions-avec-le-script-de-monitoring#param%C3%A9trage-du-monitoring)
avec les paramètres Tuya pouvant être extraient en suivant ce [tuto d'extraction de paramètres](https://github.com/bastoon577-lang/Heater_Mining/wiki/Obtenir-les-informations-du-thermostat).

## Paramétrer le Mineur (stratum)

La construction du mineur étant terminée, il est maintenant nécessaire de le configurer comme vous le feriez sans l'intégration du concept de Heater_Mining :
 * Pools (Configuration -> Pools),
 * Performances (facultatif),
 * Température & Fans (facultatif).

Un test de minage est alors possible par l'onglet **Quick Actions** :
 * START BOSminer
 * STOP BOSminer
 * ...

## Utilisation du **custom_monitor**

L'utilisation du `custom_monitor` est directement accessible dans l'interface WEB (System -> Log) au travers de [cette procédure](https://github.com/bastoon577-lang/Heater_Mining/wiki/Interractions-avec-le-script-de-monitoring).

###### Auteur : *Sébastien DALIGAULT*. 
