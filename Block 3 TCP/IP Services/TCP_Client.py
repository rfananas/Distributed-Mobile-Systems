#!/usr/bin/python3

# ------------------------------------------------------------------
# Name: TCP_Client_1.py
#
# Description: Acts as an TCP/IP socket server
#
# Autor: Walter Rothlin
#
# History:
# 26-May-2020   Walter Rothlin      Initial Version
# ------------------------------------------------------------------

import socket
# https://realpython.com/python-sockets/

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

from SocketDefinitions import *
import lxml.etree
import lxml.etree.ElementTree as elementTree

xmlStr = <

elementTree.fromString(xmlStr)
print (elementTree.tostring(root, method='xml'))

doLoop = True
while doLoop:
    xml_file = lxml.etree.parse("serviceMsg.xml")
    xml_validator = lxml.etree.XMLSchema(file="serviceMsg.xsd")
    is_valid = xml_validator.validate(xml_file)
    print("XSD Validation:", is_valid)


    sendMsg = File_getFileContent("serviceMsg.xml")
    print("Received:", callService(msg=sendMsg))
    answer = input("Beenden?")
    if answer != "":
        doLoop = False
print(f"TCP/IP Client closed on '{PORT:d}'!")