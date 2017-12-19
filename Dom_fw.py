from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
import csv

log = core.getLogger()
policyFile = "%s/pox/pox/misc/fwrules.csv" % os.environ[ 'HOME' ]

class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("firewall activation")
        self.drop = []
        with open(policyFile, 'rb') as fwrule:
            rules = csv.DictReader(fwrule)
            for row in rules:
                self.drop.append((EthAddr(row['mac_0']), EthAddr(row['mac_1'])))
                self.drop.append((EthAddr(row['mac_1']), EthAddr(row['mac_0'])))

    def ConnectionUp (self, event):
        for (src, dst) in self.drop:
            match = of.ofp_match()
            match.dl_src = src
            match.dl_dst = dst
            msg = of.ofp_flow_mod()
            msg.match = match
            event.connection.send(msg)
        log.debug("Firewall running)

def launch ():

    core.registerNew(Firewall)
