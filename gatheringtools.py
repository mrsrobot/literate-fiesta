1) Add Kali repositories & Update 
2) View Categories
3) Install classicmenu indicator
4) Install Kali menu
5) Help
			''')

				opcion0 = raw_input("\033[1;36mkat > \033[1;m")
			
				while opcion0 == "1":
					print ('''
1) Add kali linux repositories
2) Update
3) Remove all kali linux repositories
4) View the contents of sources.list file
					''')
					repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
					if repo == "1":
						cmd1 = os.system("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6")
						cmd2 = os.system("echo '# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
					elif repo == "2":
						cmd3 = os.system("apt-get update -m")
					elif repo == "3":
						infile = "/etc/apt/sources.list"
						outfile = "/etc/apt/sources.list"

						delete_list = ["# Kali linux repositories | Added by Katoolin\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free\n"]
						fin = open(infile)
						os.remove("/etc/apt/sources.list")
						fout = open(outfile, "w+")
						for line in fin:
						    for word in delete_list:
						        line = line.replace(word, "")
						    fout.write(line)
						fin.close()
						fout.close()
						print ("\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m")
					elif repo == "back":
						inicio1()
					elif repo == "gohome":
						inicio1()
					elif repo == "4":
						file = open('/etc/apt/sources.list', 'r')

						print (file.read())

					else:
						print ("\033[1;31mSorry, that was an invalid command!\033[1;m") 					
						

				if opcion0 == "3":
					print (''' 
ClassicMenu Indicator is a notification area applet (application indicator) for the top panel of Ubuntu's Unity desktop environment.
It provides a simple way to get a classic GNOME-style application menu for those who prefer this over the Unity dash menu.
Like the classic GNOME menu, it includes Wine games and applications if you have those installed.
For more information , please visit : http://www.florian-diesch.de/software/classicmenu-indicator/
''')
					repo = raw_input("\033[1;32mDo you want to install classicmenu indicator ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("add-apt-repository ppa:diesch/testing && apt-get update")
						cmd = os.system("sudo apt-get install classicmenu-indicator")

				elif opcion0 == "4"	:
					repo = raw_input("\033[1;32mDo you want to install Kali menu ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("apt-get install kali-menu")
				elif opcion0 == "5":
					print (''' 
****************** +Commands+ ******************
\033[1;32mback\033[1;m 	\033[1;33mGo back\033[1;m
\033[1;32mgohome\033[1;m	\033[1;33mGo to the main menu\033[1;m
		''')


				def inicio():
					while opcion0 == "2":
						print ('''
\033[1;36m**************************** All Categories *****************************\033[1;m
1) Information Gathering			8) Exploitation Tools
2) Vulnerability Analysis			9) Forensics Tools
3) Wireless Attacks				10) Stress Testing
4) Web Applications				11) Password Attacks
5) Sniffing & Spoofing				12) Reverse Engineering
6) Maintaining Access				13) Hardware Hacking
7) Reporting Tools 				14) Extra
									
0) All
			 ''')
						print ("\033[1;32mSelect a category or press (0) to install all Kali linux tools .\n\033[1;m")

						opcion1 = raw_input("\033[1;36mkat > \033[1;m")
						if opcion1 == "back":
							inicio1()
						elif opcion1 == "gohome":
							inicio1()
						elif opcion1 == "0":
							cmd = os.system("apt-get -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")	
						while opcion1 == "1":
							print ('''
\033[1;36m=+[ Information Gathering\033[1;m
 1) acccheck					30) lbd
 2) ace-voip					31) Maltego Teeth
 3) Amap					32) masscan
 4) Automater					33) Metagoofil
 5) bing-ip2hosts				34) Miranda
 6) braa					35) Nmap
 7) CaseFile					36) ntop
 8) CDPSnarf					37) p0f
 9) cisco-torch					38) Parsero
10) Cookie Cadger				39) Recon-ng
11) copy-router-config				40) SET
12) DMitry					41) smtp-user-enum
13) dnmap					42) snmpcheck
14) dnsenum					43) sslcaudit
15) dnsmap					44) SSLsplit
16) DNSRecon					45) sslstrip
17) dnstracer					46) SSLyze
18) dnswalk					47) THC-IPV6
19) DotDotPwn					48) theHarvester
20) enum4linux					49) TLSSLed
21) enumIAX					50) twofi
22) exploitdb					51) URLCrazy
23) Fierce					52) Wireshark
24) Firewalk					53) WOL-E
25) fragroute					54) Xplico
26) fragrouter					55) iSMTP
27) Ghost Phisher				56) InTrace
28) GoLismero					57) hping3
29) goofile
0) Install all Information Gathering tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install acccheck")

							elif opcion2 == "2":
								cmd = os.system("apt-get install ace-voip")

							elif opcion2 == "3":
								cmd = os.system("apt-get install amap")
							elif opcion2 == "4":
								cmd = os.system("apt-get install automater")
							elif opcion2 == "5":
								cmd = os.system("wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
							elif opcion2 == "6":
								cmd = os.system("apt-get install braa")
							elif opcion2 == "7":
								cmd = os.system("apt-get install casefile")
							elif opcion2 == "8":
								cmd = os.system("apt-get install cdpsnarf")
							elif opcion2 == "9":
								cmd = os.system("apt-get install cisco-torch")
							elif opcion2 == "10":
								cmd = os.system("apt-get install cookie-cadger")
							elif opcion2 == "11":
								cmd = os.system("apt-get install copy-router-config")
							elif opcion2 == "12":
								cmd = os.system("apt-get install dmitry")
							elif opcion2 == "13":
								cmd = os.system("apt-get install dnmap")
							elif opcion2 == "14":
								cmd = os.system("apt-get install dnsenum")
							elif opcion2 == "15":
								cmd = os.system("apt-get install dnsmap")
							elif opcion2 == "16":
								cmd = os.system("apt-get install dnsrecon")
							elif opcion2 == "17":
								cmd = os.system("apt-get install dnstracer")
							elif opcion2 == "18":
								cmd = os.system("apt-get install dnswalk")
							elif opcion2 == "19":
								cmd = os.system("apt-get install dotdotpwn")
							elif opcion2 == "20":
								cmd = os.system("apt-get install enum4linux")
							elif opcion2 == "21":
								cmd = os.system("apt-get install enumiax")
							elif opcion2 == "22":
								cmd = os.system("apt-get install exploitdb")
							elif opcion2 == "23":
								cmd = os.system("apt-get install fierce")
							elif opcion2 == "24":
								cmd = os.system("apt-get install firewalk")
							elif opcion2 == "25":
								cmd = os.system("apt-get install fragroute")
							elif opcion2 == "26":
								cmd = os.system("apt-get install fragrouter")
							elif opcion2 == "27":
								cmd = os.system("apt-get install ghost-phisher")
							elif opcion2 == "28":
								cmd = os.system("apt-get install golismero")
							elif opcion2 == "29":
								cmd = os.system("apt-get install goofile")
							elif opcion2 == "30":
								cmd = os.system("apt-get install lbd")
							elif opcion2 == "31":
								cmd = os.system("apt-get install maltego-teeth")
							elif opcion2 == "32":
								cmd = os.system("apt-get install masscan")
							elif opcion2 == "33":
								cmd = os.system("apt-get install metagoofil")
							elif opcion2 == "34":
								cmd = os.system("apt-get install miranda")
							elif opcion2 == "35":
								cmd = os.system("apt-get install nmap")
							elif opcion2 == "36":
								print ('ntop is unavailable')
							elif opcion2 == "37":
								cmd = os.system("apt-get install p0f")
							elif opcion2 == "38":
								cmd = os.system("apt-get install parsero")
							elif opcion2 == "39":
								cmd = os.system("apt-get install recon-ng")
							elif opcion2 == "40":
								cmd = os.system("apt-get install set")
							elif opcion2 == "41":
								cmd = os.system("apt-get install smtp-user-enum")
							elif opcion2 == "42":
								cmd = os.system("apt-get install snmpcheck")
							elif opcion2 == "43":
								cmd = os.system("apt-get install sslcaudit")
							elif opcion2 == "44":
								cmd = os.system("apt-get install sslsplit")
							elif opcion2 == "45":
								cmd = os.system("apt-get install sslstrip")
							elif opcion2 == "46":
								cmd = os.system("apt-get install sslyze")
							elif opcion2 == "47":
								cmd = os.system("apt-get install thc-ipv6")
							elif opcion2 == "48":
								cmd = os.system("apt-get install theharvester")
							elif opcion2 == "49":
								cmd = os.system("apt-get install tlssled")
							elif opcion2 == "50":
								cmd = os.system("apt-get install twofi")
							elif opcion2 == "51":
								cmd = os.system("apt-get install urlcrazy")
							elif opcion2 == "52":
								cmd = os.system("apt-get install wireshark")
							elif opcion2 == "53":
								cmd = os.system("apt-get install wol-e")
							elif opcion2 == "54":
								cmd = os.system("apt-get install xplico")
							elif opcion2 == "55":
								cmd = os.system("apt-get install ismtp")
							elif opcion2 == "56":
								cmd = os.system("apt-get install intrace")
							elif opcion2 == "57":
								cmd = os.system("apt-get install hping3")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()		
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")				
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

