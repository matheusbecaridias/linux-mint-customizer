#!/bin/bash
sudo apt update && \
sudo apt upgrade -y && \
sudo apt dist-upgrade -y && \
sudo apt autoremove -y && \
sudo apt autoclean && \
sudo apt clean && \
sudo journalctl --vacuum-time=30d && \
sudo rm -rf /tmp/* && \
sudo rm -rf /var/tmp/* && \
rm -rf ~/.cache/*  && \
sudo apt --fix-broken install -y
echo "✅ Manutenção concluída! Reinicie o sistema *sudo reboot*"."
