# 📡 Wi-Fi Deauther 🚫
<br>


## 📃 Descrição do Projeto

Este projeto demonstra, de forma simples e didática, como funciona um ataque de **desautenticação Wi-Fi** (Deauth), utilizando Python e a biblioteca `Scapy`.
<br>  

O script escaneia redes sem fio ao redor e permite que você envie pacotes de deautenticação a todos os dispositivos conectados a uma rede alvo, forçando a desconexão desses dispositivos.
<br>  

O objetivo deste projeto é **educacional**, permitindo que você entenda melhor como funciona o processo de desautenticação em redes Wi-Fi e como ferramentas conhecidas realizam esse tipo de ataque.
<br>


## ⚙️ Funcionamento

1. O script ativa a placa de rede no modo **monitor** (o usuário deve configurar isso manualmente);
2. Escaneia as redes Wi-Fi disponíveis nas proximidades;
3. Permite a escolha de uma rede alvo;
4. Identifica os dispositivos conectados à rede escolhida;
5. Envia pacotes **deauth** para desconectar os dispositivos da rede.


## 🖥️ Tecnologia Utilizada

* Python


## ▶️ Como Usar

1. Coloque sua placa de rede em modo monitor:

   ```bash
   sudo ifconfig wlan0 down
   sudo iwconfig wlan0 mode monitor
   sudo ifconfig wlan0 up
   ```

2. Execute o script com permissões de superusuário:

   ```bash
   sudo python3 wifi_deauther.py
   ```

3. Siga as instruções no terminal para selecionar a rede e executar o ataque.

> 🔧 *Certifique-se de alterar no código o nome da sua interface de rede (ex: `wlan0mon`).*


## ⚠️ Aviso Legal

Este projeto é destinado **exclusivamente para fins educacionais** e de **pesquisa autorizada em segurança ofensiva**.

**⚠️ Nunca utilize esta ferramenta em redes que você não tem autorização explícita para testar.**
O uso indevido pode violar leis locais e internacionais de crimes cibernéticos.


## 📚 Fonte de Inspiração

Conteúdo didático da **XPSec Security**:https://www.instagram.com/p/Cu5V4jCgIYh/?utm_source=ig_web_copy_link&igsh=MXRzaHVkaHZxeThucw==
