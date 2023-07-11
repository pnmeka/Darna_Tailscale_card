#Set Up Tailscale card

import variables
import subprocess
import os
import webbrowser

#importing variables from variables.py
HS_path = variables.HS_path
ip_address = variables.ip_address


image = "tailscale/tailscale:v1.40.1@sha256:08dd1f465d6e96192b36c10f4366b3988bc6ad29f7b264bd020c1762ee325305"


command1 = ["sudo", "docker", "pull", image]

command2 = f"sudo docker run --network=host -p 8240:8240 -v {HS_path}:/var/lib {image} sh -c 'tailscale web --listen 0.0.0.0:8240 & exec tailscaled --tun=userspace-networking'"

url =f"http://{ip_address}:8240"
# Run the command using os.system
subprocess.run(command1, check=True)
os.system(command2)
webbrowser.open(url)

