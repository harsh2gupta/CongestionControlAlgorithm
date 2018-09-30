#!/usr/bin/python

"""
Create a network where different switches are connected to
different controllers, by creating a custom Switch() subclass.
"""

from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller, RemoteController
from mininet.topolib import TreeTopo
from mininet.log import setLogLevel
from mininet.cli import CLI
from topo import MyTopo
setLogLevel( 'info' )

# Two local and one "external" controller (which is actually c0)
# Ignore the warning message that the remote isn't (yet) running
c2 = RemoteController( 'c2' )
mytopo = MyTopo()
net = Mininet( topo=mytopo,  build=False )
net.addController(c2)
rightSwitch = net.get('rightSwitch')
_intf = Intf( 'eth0', node=rightSwitch)

net.build()
net.start()
CLI( net )
net.stop()
