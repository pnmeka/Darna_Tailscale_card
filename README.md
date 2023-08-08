# Darna_Tailscale_card
Installs Tailscale card for Darna_local instance: https://github.com/seapoe1809/Darna_local

Once you set up Darna_local instance at https://github.com/seapoe1809/Darna_local, installing repo this will allow you to add Tailscale to it. Tailscale allows you to access your Darna.HI server remotely outside your wifi network.

The steps are as follows:
1. git clone this repo into Health_server that is already set up:
   
         cd Health_server
Git clone the repo:

         git clone https://github.com/pnmeka/Darna_Tailscale_card


3. Copy variables.py from Health_server that is set up to the repo. This allows tailscale_setup.py to import ip_address and directory addresses:

         cp variables.py /Darna_Tailscale_card

4. Run tailscale_setup.py
   
         cd Darna_Tailscale_card
   Launch the tailscale_setup
   
         python3 tailscale_setup.py

6. If the browser doesnt open up, then open < ip_address >:8240 and complete setup. The opened browser window will guide yout through the setup process.

7. Access the Darna server remotely from outside using IP address provided by Tailscale. Eg IP_Tailscale:3001 and Grafana dashboards from IP_Tailscale:3000 where IP_Tailscale is the IP_address provided by Tailscale.

8. Final step is to edit the variables.py file in the Health_server directory. Replace ip_address with the new IP_Tailscale address.

   Eg. in variables.py, replace ip_address="192.168.99.99" with ip_address="100.18.12.14" where the 100.18.12.14 is the IP_Tailscale address.


Note:
Please note this program only sets up a free linux account in Tailscale. The writer of this program isnt affiliated in anyway with Tailscale.

<img src="hhttps://github.com/seapoe1809/assets/blob/main/darna_local_assets/IMG_5790.jpeg" width =200, height=400>
<img src="https://github.com/pnmeka/pnmeka/blob/main/IMG_5808.jpeg" width =200, height=400>

