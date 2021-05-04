#!/bin/bash
read -p "Saisir le chemin de la video à convertir : "  input
read -p "Saisir le nom du nouveau fichier : "  output
ffmpeg -i $input /Users/VPV/Desktop/$output.mp4
echo "Conversion terminée !"