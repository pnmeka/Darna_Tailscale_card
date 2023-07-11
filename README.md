# Darna_Tailscale_card
Installs Tailscale card for Darna_local instance: https://github.com/seapoe1809/Darna_local

Once you set up Darna_local instance at https://github.com/seapoe1809/Darna_local, this will allow  you to add Tailscale to it which will enable you to access your Darna.HI server remotely.
The steps are as follows:
1. git clone this repo into Health_server that is already set up:
   
                       $cd Health_server
                       $git clone https://github.com/pnmeka/Darna_Tailscale_card


3. Copy variables.py from Health_server that is set up to the repo:

                       $cp variables.py /Darna_Tailscale_card

4. Run tailscale_setup.py
   
                       $python3 tailscale_setup.py

6. If the browser doesnt open up, then open <ip_address>:8240 and complete setup

7. Access the server remotely from outside using IP address provided by Tailscale. Eg IP_Tailscale:3000 and Grafana dashboards from IP_Tailscale:3001


Note:
Please note this program only sets up a free linux account in Tailscale. The writer of this program isnt affiliated in anyway with Tailscale.
