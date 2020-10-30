STK è l'interfaccia grafica di un programma usato per preparare chiavette STK mediante interfacccia GUI (Graphic User Interface).
Non ci è data l'interfaccia a caratteri CLI (Command Line Interface) per eseguire programmaticamente le operazioni, cha andrebbero quindi eseguite a mano con mouse e tastiera.

STKautoGUI.py è un programma che automatizza la prima parte delle operazioni con la GUI, simulando le operazioni di mouse e tastiera
e riconoscimento di immagini (pixel a pixel, eventualmente con percentuale di errore)

Basato su librerie python pyautoguy e Keyboard

La funzione per il calcolo della password è stata ovviamente alterata

Il programma pyMousePos.py è un tool diagnostico per visualizzare le coordinate della posizione del mouse
