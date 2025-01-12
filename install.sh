#!/bin/bash

echo "Installation de la Fortune Machine..."

# Vérifier si on est sur Raspberry Pi
if [ ! -f /etc/rpi-issue ]; then
    echo "ATTENTION: Ce script doit être exécuté sur une Raspberry Pi"
    echo "Voulez-vous continuer quand même ? (o/N)"
    read reponse
    if [ "$reponse" != "o" ]; then
        exit 1
    fi
fi

# Vérifier si on est en root
if [ "$EUID" -ne 0 ]; then
    echo "Ce script doit être exécuté en tant que root"
    echo "Veuillez utiliser: sudo $0"
    exit 1
fi

echo "1. Installation des dépendances système..."
apt-get update
apt-get install -y python3-pip python3-venv xprintidle python3-tk xserver-xorg

echo "2. Création de l'environnement virtuel..."
python3 -m venv venv
source venv/bin/activate

echo "3. Installation des dépendances Python..."
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo "4. Configuration des permissions..."
usermod -a -G dialout pi
chmod +x main.py

echo "5. Installation du service systemd..."
cp fortune-machine.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable fortune-machine

echo "6. Configuration des ports série..."
# Activer le port série sur la Raspberry Pi
if ! grep -q "enable_uart=1" /boot/config.txt; then
    echo "enable_uart=1" >> /boot/config.txt
fi

# Désactiver la console série si elle est activée
sed -i 's/console=serial0,115200 //' /boot/cmdline.txt

echo "7. Configuration de l'affichage..."
# S'assurer que l'écran ne se met pas en veille automatiquement
mkdir -p /etc/X11/xorg.conf.d
cat > /etc/X11/xorg.conf.d/10-monitor.conf << EOF
Section "ServerFlags"
    Option "BlankTime" "0"
    Option "StandbyTime" "0"
    Option "SuspendTime" "0"
    Option "OffTime" "0"
EndSection
EOF

echo "Installation terminée !"
echo "Pour démarrer le service : sudo systemctl start fortune-machine"
echo "Pour voir le statut : sudo systemctl status fortune-machine"
echo "Pour voir les logs : sudo journalctl -u fortune-machine -f"
echo ""
echo "IMPORTANT : Un redémarrage est recommandé pour appliquer tous les changements."
echo "Voulez-vous redémarrer maintenant ? (o/N)"
read reponse
if [ "$reponse" = "o" ]; then
    reboot
fi 