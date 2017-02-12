#!/usr/bin/python
import os
import sys
import xml.parsers.expat
from xml.parsers.expat import ParserCreate, ExpatError, errors
from xml.dom import minidom
from xml.dom.minidom import parse
import csv 


def writeToCSV(xmldoc):
    # Path of CSV file
    csvfile = open('C:/Users/Desktop/XMLParser/LTE-eNodeB.csv', 'w')
    # Defining field headers for xml file
    fieldnames = ['IP_Root_Tag', 'IP', 'PEERIP_Root_Tag', 'PEERIP',  'LOCALIP_Root_Tag',  'LOCALIP', 'DSTIP_Root_Tag',  'DSTIP', 'NEXTHOP_IP_Root_Tag',  'NEXTHOP', 'NEXTHOPIP_IP_Root_Tag', 'NEXTHOPIP',  'SIP_Root_Tag', 'SIP', 'CIP_Root_Tag', 'CIP', 'DIP_Root_Tag', 'DIP', 'SWC_Root_Tag', 'SWC']
    writer = csv.DictWriter(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n', fieldnames=fieldnames)
    writer.writeheader()
    xmldoc = minidom.parse('C:/Users/Desktop/XMLParser/LTE-eNodeB.xml')
# Get xml elements
    for attrib in xmldoc.getElementsByTagName("class"):
        
        for att in attrib.getElementsByTagName("attributes"):
            for ip in att.getElementsByTagName("IP"):
                
                
                ipValuetag = ip.parentNode.parentNode.nodeName
                ipValue = ip.childNodes[0].data
                writer.writerow({'IP_Root_Tag': ipValuetag, 'IP': ipValue})
                
            for peerip in att.getElementsByTagName("PEERIP"):

               peeripValuetag = peerip.parentNode.parentNode.nodeName
               #writer.writerow({'PEERIP_Root_Tag': peeripValuetag}) 
               peeripValue = peerip.childNodes[0].data
               #writer.writerow({'PEERIP':peeripValue})
               writer.writerow({'PEERIP_Root_Tag': peeripValuetag, 'PEERIP':peeripValue})

               
               
            for sip in att.getElementsByTagName("SIP"):

                sipValuetag = sip.parentNode.parentNode.nodeName
                sipValue = sip.childNodes[0].data
                writer.writerow({'SIP_Root_Tag': sipValuetag, 'SIP':sipValue})
                
            for cip in att.getElementsByTagName("CIP"):

                cipValuetag = cip.parentNode.parentNode.nodeName
                cipValue = cip.childNodes[0].data
                writer.writerow({'CIP_Root_Tag': cipValuetag, 'CIP':cipValue})
               

            for localip in att.getElementsByTagName("LOCALIP"):

                localipValuetag = localip.parentNode.parentNode.nodeName
                localipValue = localip.childNodes[0].data
                writer.writerow({'LOCALIP_Root_Tag': localipValuetag, 'LOCALIP':localipValue})
                #localipValue = localip.childNodes[0].data
                #writer.writerow({'LOCALIP':localipValue})

            for dstip in att.getElementsByTagName("DSTIP"):

                dstipValuetag = dstip.parentNode.parentNode.nodeName
                dstipValue = dstip.childNodes[0].data
                writer.writerow({'DSTIP_Root_Tag': dstipValuetag, 'DSTIP':dstipValue})
                #dstipValue = dstip.childNodes[0].data
                #writer.writerow({'DSTIP':dstipValue})

            for nexthopip in att.getElementsByTagName("NEXTHOP"):

                nexthopipValuetag = nexthopip.parentNode.parentNode.nodeName
                nexthopipValue = nexthopip.childNodes[0].data
                writer.writerow({'NEXTHOP_IP_Root_Tag': nexthopipValuetag, 'NEXTHOP':nexthopipValue})
                
            for NEXTHOPIP2 in att.getElementsByTagName("NEXTHOPIP"):

                nexthopip2Valuetag = NEXTHOPIP2.parentNode.parentNode.nodeName
                nexthopip2Value = NEXTHOPIP2.childNodes[0].data
                writer.writerow({'NEXTHOPIP_IP_Root_Tag': nexthopip2Valuetag, 'NEXTHOPIP':nexthopip2Value})
                #nexthopip2Value = NEXTHOPIP2.childNodes[0].data
                #writer.writerow({'NEXTHOPIP':nexthopip2Value})    

            for dip in att.getElementsByTagName("DIP"):
                dipValuetag = dip.parentNode.parentNode.nodeName
                dipValue = dip.childNodes[0].data
                writer.writerow({'DIP_Root_Tag': dipValuetag, 'DIP':dipValue})

            for swcip in att.getElementsByTagName("SWC"):
                swcipValuetag = swcip.parentNode.parentNode.nodeName
                swcipValue = swcip.childNodes[0].data
                writer.writerow({'SWC_Root_Tag': swcipValuetag, 'SWC':swcipValue})
                             
            
# Path of XML File 
xmldoc = minidom.parse('C:/Users/Desktop/XMLParser/LTE-eNodeB.xml')        

writeToCSV(xmldoc)

    




    
