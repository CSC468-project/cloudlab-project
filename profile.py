import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()

# Create node requests
nodes = [request.XenVM("node")]

# List of packages to install on each node.
updstr = "sudo apt install -y apache2 htop tmux git docker.io curl"

# Create the nodes and handle updates and initial setup
for node in nodes:
  node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD"
  node.routable_control_ip = "true"
  node.addService(rspec.Execute(shell="/bin/sh", command="apt update && sudo apt upgrade -y"))
  node.addService(rspec.Execute(shell="/bin/sh", command=updstr))
  node.addService(rspec.Execute(shell="bash", command="sudo tmux new-session -d -s kubernetes 'sudo bash /local/repository/setup;bash -i'"))

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
