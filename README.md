# CMPE210_Project
This repository is for the project titled "Implementation of Firewall and Load Balancer in POX SDN Controller".
Copy the fw210.py and fwrules.csv into the misc folder and rrlb210.py into the forwarding folder.
Update the firewall policies csv file (fwrule.csv) with the MAC address of the host you want to block.
Execute the firewall application (fw210.py) and ping the blocked host from H1 host to verify that it doesn't reach to it.
Execute the Load balancing application (rrlb210.py) and verify through wireshark that data is being divided between hots H1, H2 and H3 using round robin method.
