#!/usr/bin/python
#from mininet.link import TCLink
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.topo import Topo
def myNet():


    #OpenDayLight controller
    #ODL_CONTROLLER_IP='10.0.0.4'

    #Floodlight controller
    #FL_CONTROLLER_IP='127.0.0.1'

    net = Mininet( topo=None, build=False)

    JPIPServer = net.addHost( 'JS', ip='10.0.0.2/24' )
   # JPIPClient = net.addHost( 'JC' )
    iPerfServer = net.addHost( 'IS', ip='10.0.0.3/24' )
    iPerfClient = net.addHost( 'IC', ip='10.0.0.4/24' )
    leftSwitch = net.addSwitch( 'S1' )
    rightSwitch = net.addSwitch( 'S2' )
    

    print "*** Creating links"
    net.addLink( JPIPServer, leftSwitch)#, bw=10 )
    net.addLink(iPerfClient, leftSwitch)#, bw=10)
    net.addLink( leftSwitch, rightSwitch)#, bw=10, delay='50ms' )
    #net.addLink( rightSwitch, JPIPClient)#, bw=10 )
    net.addLink(rightSwitch, iPerfServer)#, bw=10)
    
    # Add Controllers
    #fl_ctrl = net.addController( 'c1', controller=RemoteController, ip=FL_CONTROLLER_IP, port=6642)
    #net.addLink(rightSwitch, fl_ctrl)
	
    net.build()
    net.start()
    CLI( net )
    net.stop()

if __name__ == '__main__':
	myNet()
