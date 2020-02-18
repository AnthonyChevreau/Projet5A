# Projet5A
Projet Voiture autonome:
<p align="center">
  <img src="https://github.com/AnthonyChevreau/Projet5A/blob/master/img/car.jpg" width="350" title="Voiture autonome">
</p>  
  Documentation :
  
    + Présentation PPTX
    + Rapport
  
  Jetson Nano :
  
    + My_Model.h5 : Modèle de classification Keras
    + crop.py : programme d'identification des panneaux
    + snapshot.py : programme de prise de photo
    + car.py : programme de reconnaissance des panneaux
    + comUART.py : programme de communication entre jetson nano et openmv en uart
    
  OpenMv :
  
    + com.py : programme de reception et décodage des données de la jetson
    + suivi.py : programme de suivi de ligne
    
  Demo :
  
    + suivi_de_ligne.mp4 : video de suivi de ligne 
    + detection.mp4 : video de capture, detection, reconnaisance et envoi de donnée de panneau
