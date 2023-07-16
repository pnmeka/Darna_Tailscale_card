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

command2 = f"sudo docker run --network=host -p 8240:8240 -v {HS_path}:/var/lib {image} --restart=on-failure sh -c 'tailscale web --listen 0.0.0.0:8240 & exec tailscaled --tun=userspace-networking'"

url =f"http://{ip_address}:8240"
# Run the command using os.system
subprocess.run(command1, check=True)
os.system(command2)
webbrowser.open(url)

#write to darna.py

file_path = f'{HS_path}/darna.py' 

with open('flask1.py', 'r') as file:
    lines = file.readlines()

if len(lines) >= 3:
    del lines[-3:]

lines.append("\n@app.route('/tailscale')\n")
lines.append("def tailscale():\n")
lines.append("    if 'logged_in' in session:\n")
lines.append("        # User is logged in, redirect to the protected page\n")
lines.append("        url3 = f\"http://{ip_address}:8240\"\n")
lines.append("        return redirect(url3)\n")
lines.append("    else:\n")
lines.append("        # User is not logged in, redirect to the login page\n")
lines.append("        return redirect('/login')\n")
lines.append("\nif __name__ == '__main__':\n")
lines.append("    app.run('0.0.0.0', port=3001)\n")
lines.append("    print(\"server is running at http://localhost:3001\")\n")

with open('flask1.py', 'w') as file:
    file.writelines(lines)
