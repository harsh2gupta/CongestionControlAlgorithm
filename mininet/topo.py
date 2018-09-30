"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.link import TCLink
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )
       
        # Add hosts and switches
        JPIPServer = self.addHost( 'JS', ip='10.0.0.2/24' )
        #JPIPClient = self.addHost( 'JC' )
	iPerfServer = self.addHost( 'IS', ip='10.0.0.3/24' )
        iPerfClient = self.addHost( 'IC', ip='10.0.0.4/24' )
        leftSwitch = self.addSwitch( 'S1' )
        rightSwitch = self.addSwitch( 'S2' )

        # Add links
        self.addLink( JPIPServer, leftSwitch)#, bw=10 )
	self.addLink(iPerfClient, leftSwitch)#, bw=10)
        self.addLink( leftSwitch, rightSwitch)#, bw=10, delay='50ms' )
        #self.addLink( rightSwitch, JPIPClient)#, bw=10 )
	self.addLink(rightSwitch, iPerfServer)#, bw=10)
	

topos = { 'mytopo': ( lambda: MyTopo() ) }
