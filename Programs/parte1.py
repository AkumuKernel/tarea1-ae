from mininet.topo import Topo
from mininet.link import TCLink

class MyTopo(Topo):
	def build(self):
	# Add Hosts and Switches
		s1 = self.addSwitch('s1')
		s2 = self.addSwitch('s2')
		s3 = self.addSwitch('s3')
		s4 = self.addSwitch('s4')
	
		h1 = self.addHost('h1')
		h2 = self.addHost('h2')
		h3 = self.addHost('h3')
		h4 = self.addHost('h4')
	
	# Links Switch 1 to Host 1 and 2
		self.addLink(s1,h1)
		self.addLink(s1,h2)
	
	# Link Switch 2 to Host 3
		self.addLink(s3,h3)
	
	# Link Switch 3 to Host 4
		self.addLink(s4,h4)

	# Link Switch 3 to host 4
		self.addLink(s3,s4,cls=TCLink, bw=10, delay='30ms', loss=10)
	
	# Link Switch 2 to Switch 1 and 3
		self.addLink(s2,s1)
		self.addLink(s2,s3,cls=TCLink, bw=10, delay='15ms')

topos= {'mytopo': (lambda : MyTopo())}
