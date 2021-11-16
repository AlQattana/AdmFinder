#!/usr/bin/python
# AdmFinder is a Admin login page finder .
# Coded By alqattana - github.com/alqattana
# Author will be not responsible for any damage!
# Coded in 8/12/2015

# importer
import httplib
import socket
import sys
import urllib2
import urllib
import socket
import argparse
import sys
import os
import threading
import Queue
import re
import httplib
from lists import *

# clearer XD
if sys.platform == "linux" or sys.platform == "linux2":
    cl = "clear"
else:
    cl = "cls"
os.system(cl)


# coloring
class colors:
    def __init__(self):
        self.green = "\033[92m"
        self.blue = "\033[94m"
        self.bold = "\033[1m"
        self.yellow = "\033[93m"
        self.orange = "\033[33m"
        self.red = "\033[91m"
        self.end = "\033[0m"


clr = colors()

try:
    print clr.green+'''
   _____       .___        ___________.__            .___            
  /  _  \    __| _/_____   \_   _____/|__| ____    __| _/___________ 
 /  /_\  \  / __ |/     \   |    __)  |  |/    \  / __ |/ __ \_  __ \
/    |    \/ /_/ |  Y Y  \  |     \   |  |   |  \/ /_/ \  ___/|  | \/
\____|__  /\____ |__|_|  /  \___  /   |__|___|  /\____ |\___  >__|   
        \/      \/     \/       \/            \/      \/    \/            
    [+]- Admin Panel Finder v 1.0            
    [+]- Coded by @alqattana                  
    
    '''+clr.end
    FoundPages = 0
    ScannedPages = 0

    try:
        site = raw_input(clr.bold+" [*]- Enter the website : "+clr.end)
        if not len(site) > 0:
            print clr.bold+clr.yellow+" [?]- WTF !?, Enter a website man !"+clr.end+clr.end
            print clr.bold+clr.red+" [!]- Exiting ."+clr.end+clr.end
            exit()
        site = site.replace("http://", "")
        print(clr.yellow+" [#]- Checking if " + clr.bold +
              "[ "+site+" ]"+clr.end+clr.yellow + " online ..."+clr.end)
        conn = httplib.HTTPConnection(site)
        conn.connect()
        print clr.green+" [+]- Bam!! ,  Website is Online ."+clr.end
    except (httplib.HTTPResponse, socket.error) as Exit:
        print(
            clr.red+" [!]- Oops Error occured, Website offline or invalid URL"+clr.end)
        print clr.bold+clr.red+" [!]- Exiting ."+clr.end+clr.end
        exit()
    print clr.bold+"\n [*]- Enter site source code:"+clr.end
    print " [1]-[PHP]"
    print " [2]-[ASP]"
    print " [3]-[CFM]"
    print " [4]-[JS]"
    print " [5]-[CGI]"
    print " [6]-[BRF]"
    print clr.bold+"\n [*]- Select one and hit 'Enter' .\n"+clr.end
    try:
        code = input(clr.bold+" [*]- Your choice : "+clr.end)
    except (SyntaxError, NameError):
        print clr.bold+clr.yellow+" [?]- WTF !?, Pic a number man !"+clr.end+clr.end
        print clr.bold+clr.red+" [!]- Exiting ."+clr.end+clr.end
        exit()
    if code == 1:
        print(
            clr.green+"\n [+]- Finding PHP Admin Pages in " + site + " ...\n"+clr.end)
        for admin in php:
            admin = admin.replace("\n", "")
            admin = "/" + admin
            host = site + admin
            print(clr.yellow+" [#]- Checking " + host + " ..."+clr.end)
            connection = httplib.HTTPConnection(site)
            connection.request("GET", admin)
            response = connection.getresponse()
            ScannedPages = ScannedPages + 1
            if response.status == 200:
                FoundPages = FoundPages + 1
                print "%s %s" % (clr.bold+clr.green+" [+]- " + host, "[Bam !! ,Admin page found!]"+clr.end+clr.end)
                raw_input(
                    clr.bold+" [*]- Press enter to continue scanning ."+clr.end)
            elif response.status == 404:
                ScannedPages = ScannedPages
            elif response.status == 302:
                print "%s %s" % (clr.orange+" [?]- " + host, " [Possible admin page]"+clr.end)
            else:
                print "%s %s" % (clr.orange+" [?]- " + host, "[Not sure, check it your self XD]"+clr.end)
            connection.close()
        print(clr.bold+clr.green+"\n [/]- Completed . \n"+clr.end+clr.end)
        print clr.bold+" ["+clr.end, FoundPages, clr.bold+"]-"+clr.end + clr.bold+" Admin pages found"+clr.end
        print clr.bold+" ["+clr.end, ScannedPages, clr.bold+"]-"+clr.end + clr.bold+" total pages scanned"+clr.end
        print(clr.bold+" [/]- The Game is over, see you soon ."+clr.end)
        exit()

    if code == 2:
        print(
            clr.green+"\n [+]- Finding ASP Admin Pages in " + site + " ...\n"+clr.end)
        for admin in asp:
            admin = admin.replace("\n", "")
            admin = "/" + admin
            host = site + admin
            print(clr.yellow+" [#]- Checking " + host + " ..."+clr.end)
            connection = httplib.HTTPConnection(site)
            connection.request("GET", admin)
            response = connection.getresponse()
            ScannedPages = ScannedPages + 1
            if response.status == 200:
                FoundPages = FoundPages + 1
                print "%s %s" % (clr.bold+clr.green+" [+]- " + host, "[Bam !! ,Admin page found!]"+clr.end+clr.end)
                raw_input(
                    clr.bold+" [*]- Press enter to continue scanning ."+clr.end)
            elif response.status == 404:
                ScannedPages = ScannedPages
            elif response.status == 302:
                print "%s %s" % (clr.orange+" [?]- " + host, " [Possible admin page]"+clr.end)
            else:
                print "%s %s" % (clr.orange+" [?]- " + host, "[Not sure, check it your self XD]"+clr.end)
            connection.close()
        print(clr.bold+clr.green+"\n [/]- Completed . \n"+clr.end+clr.end)
        print clr.bold+" ["+clr.end, FoundPages, clr.bold+"]-"+clr.end + clr.bold+" Admin pages found"+clr.end
        print clr.bold+" ["+clr.end, ScannedPages, clr.bold+"]-"+clr.end + clr.bold+" total pages scanned"+clr.end
        print(clr.bold+" [/]- The Game is over, see you soon ."+clr.end)
        exit()

    if code == 3:
        print(
            clr.green+"\n [+]- Finding CFM Admin Pages in " + site + " ...\n"+clr.end)
        for admin in cfm:
            admin = admin.replace("\n", "")
            admin = "/" + admin
            host = site + admin
            print(clr.yellow+" [#]- Checking " + host + " ..."+clr.end)
            connection = httplib.HTTPConnection(site)
            connection.request("GET", admin)
            response = connection.getresponse()
            ScannedPages = ScannedPages + 1
            if response.status == 200:
                FoundPages = FoundPages + 1
                print "%s %s" % (clr.bold+clr.green+" [+]- " + host, "[Bam !! ,Admin page found!]"+clr.end+clr.end)
                raw_input(
                    clr.bold+" [*]- Press enter to continue scanning ."+clr.end)
            elif response.status == 404:
                ScannedPages = ScannedPages
            elif response.status == 302:
                print "%s %s" % (clr.orange+" [?]- " + host, " [Possible admin page]"+clr.end)
            else:
                print "%s %s" % (clr.orange+" [?]- " + host, "[Not sure, check it your self XD]"+clr.end)
            connection.close()
        print(clr.bold+clr.green+"\n [/]- Completed . \n"+clr.end+clr.end)
        print clr.bold+" ["+clr.end, FoundPages, clr.bold+"]-"+clr.end + clr.bold+" Admin pages found"+clr.end
        print clr.bold+" ["+clr.end, ScannedPages, clr.bold+"]-"+clr.end + clr.bold+" total pages scanned"+clr.end
        print(clr.bold+" [/]- The Game is over, see you soon ."+clr.end)
        exit()

    if code == 4:
        print(
            clr.green+"\n [+]- Finding JS Admin Pages in " + site + " ...\n"+clr.end)
        for admin in js:
            admin = admin.replace("\n", "")
            admin = "/" + admin
            host = site + admin
            print(clr.yellow+" [#]- Checking " + host + " ..."+clr.end)
            connection = httplib.HTTPConnection(site)
            connection.request("GET", admin)
            response = connection.getresponse()
            ScannedPages = ScannedPages + 1
            if response.status == 200:
                FoundPages = FoundPages + 1
                print "%s %s" % (clr.bold+clr.green+" [+]- " + host, "[Bam !! ,Admin page found!]"+clr.end+clr.end)
                raw_input(
                    clr.bold+" [*]- Press enter to continue scanning ."+clr.end)
            elif response.status == 404:
                ScannedPages = ScannedPages
            elif response.status == 302:
                print "%s %s" % (clr.orange+" [?]- " + host, " [Possible admin page]"+clr.end)
            else:
                print "%s %s" % (clr.orange+" [?]- " + host, "[Not sure, check it your self XD]"+clr.end)
            connection.close()
        print(clr.bold+clr.green+"\n [/]- Completed . \n"+clr.end+clr.end)
        print clr.bold+" ["+clr.end, FoundPages, clr.bold+"]-"+clr.end + clr.bold+" Admin pages found"+clr.end
        print clr.bold+" ["+clr.end, ScannedPages, clr.bold+"]-"+clr.end + clr.bold+" total pages scanned"+clr.end
        print(clr.bold+" [/]- The Game is over, see you soon ."+clr.end)
        exit()

    if code == 5:
        print(
            clr.green+"\n [+]- Finding CGI Admin Pages in " + site + " ...\n"+clr.end)
        for admin in cgi:
            admin = admin.replace("\n", "")
            admin = "/" + admin
            host = site + admin
            print(clr.yellow+" [#]- Checking " + host + " ..."+clr.end)
            connection = httplib.HTTPConnection(site)
            connection.request("GET", admin)
            response = connection.getresponse()
            ScannedPages = ScannedPages + 1
            if response.status == 200:
                FoundPages = FoundPages + 1
                print "%s %s" % (clr.bold+clr.green+" [+]- " + host, "[Bam !! ,Admin page found!]"+clr.end+clr.end)
                raw_input(
                    clr.bold+" [*]- Press enter to continue scanning ."+clr.end)
            elif response.status == 404:
                ScannedPages = ScannedPages
            elif response.status == 302:
                print "%s %s" % (clr.orange+" [?]- " + host, " [Possible admin page]"+clr.end)
            else:
                print "%s %s" % (clr.orange+" [?]- " + host, "[Not sure, check it your self XD]"+clr.end)
            connection.close()
        print(clr.bold+clr.green+"\n [/]- Completed . \n"+clr.end+clr.end)
        print clr.bold+" ["+clr.end, FoundPages, clr.bold+"]-"+clr.end + clr.bold+" Admin pages found"+clr.end
        print clr.bold+" ["+clr.end, ScannedPages, clr.bold+"]-"+clr.end + clr.bold+" total pages scanned"+clr.end
        print(clr.bold+" [/]- The Game is over, see you soon ."+clr.end)
        exit()

    if code == 6:
        print(
            clr.green+"\n [+]- Finding BRF Admin Pages in " + site + " ...\n"+clr.end)
        for admin in brf:
            admin = admin.replace("\n", "")
            admin = "/" + admin
            host = site + admin
            print(clr.yellow+" [#]- Checking " + host + " ..."+clr.end)
            connection = httplib.HTTPConnection(site)
            connection.request("GET", admin)
            response = connection.getresponse()
            ScannedPages = ScannedPages + 1
            if response.status == 200:
                FoundPages = FoundPages + 1
                print "%s %s" % (clr.bold+clr.green+" [+]- " + host, "[Bam !! ,Admin page found!]"+clr.end+clr.end)
                raw_input(
                    clr.bold+" [*]- Press enter to continue scanning ."+clr.end)
            elif response.status == 404:
                ScannedPages = ScannedPages
            elif response.status == 302:
                print "%s %s" % (clr.orange+" [?]- " + host, " [Possible admin page]"+clr.end)
            else:
                print "%s %s" % (clr.orange+" [?]- " + host, "[Not sure, check it your self XD]"+clr.end)
            connection.close()
        print(clr.bold+clr.green+"\n [/]- Completed . \n"+clr.end+clr.end)
        print clr.bold+" ["+clr.end, FoundPages, clr.bold+"]-"+clr.end + clr.bold+" Admin pages found"+clr.end
        print clr.bold+" ["+clr.end, ScannedPages, clr.bold+"]-"+clr.end + clr.bold+" total pages scanned"+clr.end
        print(clr.bold+" [/]- The Game is over, see you soon ."+clr.end)
        exit()

except TypeError:
    print clr.red+"[!]- NO target specified"+clr.end
except socket.gaierror:
    print clr.red+"[!]- NOPE WRONG URL"+clr.end
except KeyboardInterrupt:
    print clr.bold+clr.red+"\n [!]- Abort signal Detected"+clr.end+clr.end
except httplib.BadStatusLine:
    print clr.red+"[-]- Something went wrong try again or let it go"+clr.end
