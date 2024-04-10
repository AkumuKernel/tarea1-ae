from mininet.topo import Topo
from mininet.link import TCLink

class MyTopo(Topo):
	def build(self):
		# Add Hosts and Switches
		s1 = self.addSwitch('s1')
		s2 = self.addSwitch('s2')
		s3 = self.addSwitch('s3')
		s4 = self.addSwitch('s4')
		hostChile = self.addHost('h1')
		hostAustralia = self.addHost('h2')
		
		# Links Switch 1 to Hosts Chile
		self.addLink(s1, hostChile)
		# Link Switch 1 to Host 2
		self.addLink(s1, s2, cls=TCLink, bw=5, delay='50ms', loss=2)
		# Link Switch 2 to Host 3
		self.addLink(s2, s3, cls=TCLink, bw=10, delay='70ms', loss=2)
		# Link Switch 3 to Host 4
		self.addLink(s3, s4, cls=TCLink, bw=5, delay='30ms', loss=2)
		
		# Links Switch 4 to Host Australia
		self.addLink(s4, hostAustralia)

topos = {'mytopo': (lambda: MyTopo())}
