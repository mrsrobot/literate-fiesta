0) Install all Sniffing & Spoofing tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install burpsuite")

							elif opcion2 == "2":
								cmd = os.system("apt-get install dnschef")

							elif opcion2 == "3":
								cmd = os.system("apt-get install fiked")
							elif opcion2 == "4":
								cmd = os.system("apt-get install hamster-sidejack")
							elif opcion2 == "5":
								cmd = os.system("apt-get install hexinject")
							elif opcion2 == "6":
								cmd = os.system("apt-get install iaxflood")
							elif opcion2 == "7":
								cmd = os.system("apt-get install inviteflood")
							elif opcion2 == "8":
								cmd = os.system("apt-get install ismtp")
							elif opcion2 == "9":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/isr-evilgrade.git")
							elif opcion2 == "10":
								cmd = os.system("apt-get install mitmproxy")
							elif opcion2 == "11":
cmd = os.system("apt-get install ohrwurm")
