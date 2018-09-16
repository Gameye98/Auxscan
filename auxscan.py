## auxscan.py
# -*- coding: utf-8 -*-
##
"""
#####################################
# Auxscan Project                   #
# MyFB : www.fb.com/cgi.izo         #
#####################################
# Author: DedSecTL                  #
# BlackHole Security                #
#####################################
"""
"""
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import sys
import requests

bannerAuxscan = """
  /                        \   ####################
 ( ( __- ^ ^- , - ^ ^ - __) )  # AUXSCAN  2.0     #
 '....- - - ' ; - - - ...-..'  # Author: DedSecTL #
   <....| o       o |....>     # Date: 06-03-2018 #
        \           /          # Code: Python     #
         )         (           # BlackHoleSec     #
         : o __ o  :           ####################
          * ----- *            # Auxscan Project  #
     (C) Copyright 2018        ####################

Usage: auxscan [options] <url|dork|hostname|ip>

OPTIONS:
   -a,--apafi <url>: Admin Panel Finder
   -w,--whois <hostname>: Whois Lookup
   -p,--pscan <hostname>: Port Scanner
   -u,--upafi <url>: Upload Panel Finder
   -t,--trace <hostname>: Traceroute
   -d,--dnsup <hostname>: DNS Lookup
   -i,--ipgeo <ip>: IPGeolocation
   -h,--httphg <hostname>: HTTP Header Grabber
"""

def auxscan(opt, target):
	if opt == "-a" or opt == "--apafi":
		print("[+] Opt: Admin Panel Finder")
		print("[+] Target:",target,"\n")
		for path in open("admin").read().split("\n"):
			print(target+"/"+path)
			print("Path:","/"+path)
			print("Header:",requests.get(target+"/"+path).status_code)
	elif opt == "-w" or opt == "--whois":
		print(requests.get('http://api.hackertarget.com/whois/?q='+target).text)
	elif opt == "-p" or opt == "--pscan":
		print(requests.get('http://api.hackertarget.com/nmap/?q='+target).text)
	elif opt == "-u" or opt == "--upafi":
		print("[+] Opt: Upload Panel Finder")
		print("[+] Target:",target,"\n")
		for path in open("upload").read().split("\n"):
			print(target+"/"+path)
			print("Path:","/"+path)
			print("Header:",requests.get(target+"/"+path).status_code)
	elif opt == "-t" or opt == "--trace":
		print(requests.get('https://api.hackertarget.com/mtr/?q='+target).text)
	elif opt == "-d" or opt == "--dnsup":
		print(requests.get('http://api.hackertarget.com/dnslookup/?q='+target).text)
	elif opt == "-i" or opt == "--ipgeo":
		print(requests.get('https://tools.keycdn.com/geo.json?host='+target).text)
	elif opt == "-h" or opt == "--httphg":
		print(requests.get('http://api.hackertarget.com/httpheaders/?q='+target).text)
	else:
		print("auxscan: error:",opt,"is not an option")

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print(bannerAuxscan)
	else:
		auxscan(sys.argv[1], sys.argv[2])