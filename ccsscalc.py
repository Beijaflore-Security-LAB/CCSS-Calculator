#!/usr/bin/python3
from colorama import Fore
from colorama import Style
print(Fore.YELLOW +"This program is a simple calculator for Common Configuration Scoring System (CCSS)"+Style.RESET_ALL)
print(Fore.YELLOW +"CCSS is a scale to rate de misconfiguration of parameter and is used on configuration audit to qualify misconfiguration according to their criticity"+Style.RESET_ALL)
print("")
print("")
ccss_score = 0
AVSE = 0
# Access Vector Scoring Evaluation

print(Fore.BLUE+ "Access Vector Scoring Evaluation (AV)"+Style.RESET_ALL)
AVSE = 0
while AVSE != 1:
	AV =  input ("Local"+Fore.YELLOW+"(L)"+Style.RESET_ALL+" or Adjacent Network"+Fore.YELLOW+" (A)"+Style.RESET_ALL+" or Network"+Fore.YELLOW+" (N)"+Style.RESET_ALL+" or def: ")
	if AV == "def":
		print("")
		print(Fore.GREEN+"Local (L): Active Exploitation: A vulnerability actively exploitable with only local access requires the exploiter to have either physical access to the vulnerable system or a local (shell) account. Examples of locally exploitable configuration issues are excess privileges assigned to locally accessible user or service accounts, directories, files, and registry keys; prohibited local services enabled; weak password policies for local accounts; lack of required password protection for screen savers; and lack of required peripheral usage restrictions, such as permissions for the use of USB flash drives or CDs.")
		print("Passive Exploitation: A vulnerability passively preventing actions from occurring with local access affects only local users, processes, services, etc. Examples of these configuration issues are insufficient privileges assigned to locally accessible user or service accounts, directories, files, and registry keys; necessary local services disabled; and overly restrictive peripheral configurations, such as preventing the use of USB flash drives or CDs when an organization’s policy permits such use.")
		print("")
		print("Adjacent Network (A): Active Exploitation: A vulnerability actively exploitable with adjacent network access requires the exploiter to have access to either the broadcast or collision domain of the vulnerable software. Examples of local networks include local IP subnet, Bluetooth, IEEE 802.11, and local Ethernet segment. An example of an adjacent network configuration issue is configuring a wireless LAN network interface card to connect to any available wireless LAN automatically.")
		print("Passive Exploitation: A vulnerability passively preventing actions from occurring with adjacent network access affects users or other systems on the broadcast or collision domain of the software. An example of such a configuration issue is a system that is intended to share its Internet access with other systems on the same subnet, but is configured so that it cannot provide Internet access to them.")
		print("")
		print("Network (N): Active Exploitation: A vulnerability actively exploitable with network access means that the exploiter does not require local network access or local access. The software with the vulnerability is bound to the network stack; this is also termed “remotely exploitable.” An example is a configuration setting for a network service such as FTP, HTTP, or SMTP (e.g., excess privileges, weak password policy). Another example is a prohibited network service being enabled.")
		print("Passive Exploitation: A vulnerability passively preventing actions from occurring with network access affects users or systems outside the broadcast or collision domain. An example is a system that is intended to provide a network service to all other systems, but the service has inadvertently been disabled. Another example is a system that interacts with remote systems, but has all of its logging and auditing capabilities disabled; the system will fail to record events involving the remote systems, so this could permit malicious activity by those remote systems to go unnoticed."+Style.RESET_ALL)
		print("")
	elif AV == "L":
		AVSE = 1
		AccessVector = 0.395 
	elif AV == "A":
		AVSE = 1
		AccessVector = 0.646
	elif AV == "N":
		AVSE = 1
		AccessVector = 1.0
	else: 
		print("Wrong value");

# Authentication Scoring Evaluation
ASE = 0
print(Fore.BLUE+"Authentication Scoring Evaluation (Au)"+Style.RESET_ALL)
while ASE != 1:
	Au =  input ("Multiple "+Fore.YELLOW+"(M)"+Style.RESET_ALL+" or Single "+Fore.YELLOW+"(S)"+Style.RESET_ALL+" or None "+Fore.YELLOW+"(N)"+Style.RESET_ALL+" or def: ")
	if Au == "def":
		print("")
		print(Fore.GREEN+"Multiple (M): Exploiting the vulnerability requires that the exploiter authenticate two or more times, even if the same credentials are used each time. An example is an exploiter authenticating to an operating system in addition to providing credentials to access an application hosted on that system")
		print("")
		print("Single (S): One instance of authentication is required to access and exploit the vulnerability")
		print("")
		print("None (N): Authentication is not required to access and exploit the vulnerability"+Style.RESET_ALL)
		print("")
	elif Au == "M":
		ASE = 1
		Authentication = 0.45
	elif Au == "S":
		ASE = 1
		Authentication = 0.56 
	elif Au == "N":
		ASE = 1
		Authentication = 0.704 
	else: 
		print("Wrong value");

# Access Complexity (AC) 
ACE = 0
print(Fore.BLUE+"Access Complexity (AC) "+Style.RESET_ALL)
while ACE != 1:
	AC =  input ("High "+Fore.YELLOW+"(H)"+Style.RESET_ALL+" or Medium "+Fore.YELLOW+"(M)"+Style.RESET_ALL+" or Low "+Fore.YELLOW+"(L)"+Style.RESET_ALL+" or def: ")
	if AC == "def":
		print("")
		print(Fore.GREEN+"High (H): Active Exploitation: Specialized access conditions exist for active exploitation. For example:")
		print("	• The vulnerability makes it only slightly easier for an attack to succeed. For example, a weak password length requirement would improve an attacker’s chances of guessing or cracking a password, but since each vulnerability needs to be considered on its own (i.e., we can’t assume that the attacker has unlimited opportunities to guess), this particular vulnerability would not significantly reduce the complexity of attack.")
		print("	• The exploiter must already have elevated privileges (for example, a vulnerability that only administrators could take advantage of).")
		print("	• The vulnerability is seen very rarely in practice, so parties that could potentially exploit it are very unlikely to be looking for it.")
		print("Passive Exploitation: Not applicable to this value")
		print("")
		print("Medium (M): Active Exploitation: The access conditions for active exploitation are somewhat specialized; the following are examples: ")
		print("	• The attacking party is limited to a group of systems or users at some level of authorization, possibly untrusted.")
		print("	• Some information must be gathered before a successful attack can be launched.")
		print("	• The vulnerability is non-default, and is not commonly encountered.")
		print("	• Successful exploitation requires the victim to perform some action such as visiting a hostile web site or opening an email attachment.")
		print("Passive Exploitation: Not applicable to this value")
		print("")
		print("Low (L): Active Exploitation: Specialized access conditions for active exploitation or extenuating circumstances do not exist. The following are examples: ")
		print("• The affected product typically provides access to a wide range of systems and users, possibly anonymous and untrusted (e.g., Internet-facing web or mail server).")
		print("• The vulnerability is default or ubiquitous.")
		print("• The attack can be performed manually and requires little skill or additional information gathering.")
		print("Passive Exploitation: Vulnerabilities that passively prevent actions from occurring or otherwise do not require any actions to be performed are scored as Low. Examples are an audit service that is configured such that it fails to record security events, and an update service that is configured such that it fails to download security updates"+Style.RESET_ALL)
		print("")
	elif AC == "H":
		ACE = 1
		AccessComplexity = 0.35
	elif AC == "M":
		ACE = 1
		AccessComplexity = 0.61 
	elif AC == "L":
		ACE = 1
		AccessComplexity = 0.71
	else: 
		print("Wrong value");

# Confidentiality Impact (C)
CI = 0
print(Fore.BLUE+"Confidentiality Impact (C) "+Style.RESET_ALL)
while CI != 1:
	C =  input ("None "+Fore.YELLOW+"(N)"+Style.RESET_ALL+" or Partial "+Fore.YELLOW+"(P)"+Style.RESET_ALL+" or Complete "+Fore.YELLOW+"(C)"+Style.RESET_ALL+" or def: ")
	if C == "def":
		print("")
		print(Fore.GREEN+"None (N) : There is no impact to the confidentiality of the system")
		print("")
		print("Partial (P): There is considerable information disclosure. Access to some system files is possible, but the exploiter does not have control over what is obtained, or the scope of the loss is constrained. An example is a vulnerability that divulges only certain tables in a database. Another form of partial confidentiality impact is the use of weak password policies, which make it easier to guess or crack passwords.")
		print("AND/OR")
		print("There is considerable unauthorized access to the system. Examples include an authorized user gaining access to certain prohibited system functions, an unauthorized user gaining access to a network service offered by the system, and an unauthorized user gaining user or application-level privileges on the system (such as a database administration account). ")
		print("")
		print("Complete (C): There is total information disclosure, resulting in all system files being revealed. The exploiter is able to read all of the system's data (memory, files, etc.) An example is someone who is not authorized to act as a system administrator gaining full administrator privileges to the system"+Style.RESET_ALL)
		print("")
	elif C == "N":
		CI = 1
		ConfImpact = 0
	elif C == "P":
		CI = 1
		ConfImpact = 0.275
	elif C == "C":
		CI = 1
		ConfImpact = 0.660 
	else: 
		print("Wrong value");

# Integrity Impact (I) 
II = 0
print(Fore.BLUE+"Integrity Impact (I)  "+Style.RESET_ALL)
while II != 1:
	I =  input ("None "+Fore.YELLOW+"(N)"+Style.RESET_ALL+" or Partial "+Fore.YELLOW+"(P)"+Style.RESET_ALL+" or Complete "+Fore.YELLOW+"(C)"+Style.RESET_ALL+" or def: ")
	if I == "def":
		print("")
		print(Fore.GREEN+"None (N) : There is no impact to the integrity of the system.")
		print("")
		print("Partial (P): Modification of some system files or information is possible, but the exploiter does not have control over what can be modified, or the scope of what the exploiter can affect is limited. For example, OS or application files may be overwritten or modified, but either the exploiter has no control over which files are affected or the exploiter can modify files within only a limited context or scope, such as for a particular user or application account. Another example is poorly configured auditing or logging, which reduces the number of events that are logged or causes the records to be retained for a shorter period of time than needed.")
		print("AND/OR")
		print("The system’s security configuration can be altered. An example is a configuration setting that would allow an unauthorized file (such as one containing malware) to be stored on the system or allow an unauthorized program to be installed on the system.")
		print("")
		print("Complete (C): There is a total compromise of system integrity. There is a complete loss of system protection, resulting in the entire system being compromised. The exploiter is able to modify any files on the target system. An example is someone who is not authorized to act as a system administrator gaining full administrator privileges to the system."+Style.RESET_ALL)
		print("")
	elif I == "N":
		II = 1
		IntegImpact = 0
	elif I == "P":
		II = 1
		IntegImpact = 0.275
	elif I == "C":
		II = 1
		IntegImpact = 0.660 
	else: 
		print("Wrong value");

# Availability Impact (A)
AI = 0
print(Fore.BLUE+"Availability Impact (A)  "+Style.RESET_ALL)
while AI != 1:
	A =  input ("None "+Fore.YELLOW+"(N)"+Style.RESET_ALL+" or Partial "+Fore.YELLOW+"(P)"+Style.RESET_ALL+" or Complete "+Fore.YELLOW+"(C)"+Style.RESET_ALL+" or def: ")
	if A == "def":
		print("")
		print(Fore.GREEN+"None (N) : There is no impact to the availability of the system.")
		print("")
		print("Partial (P): There is reduced performance or interruptions in resource availability. Examples are a network stack setting that is disabled, which if enabled would reduce the impact of denial of service attacks; and excess privileges that permit a user to stop services. Another example is the unavailability of a single necessary service, such as logging or auditing services. ")
		print("")
		print("Complete (C): There is a total shutdown of the affected resource. The exploiter can render the resource completely unavailable. An example is excess privileges that permit a user to shut down a system or delete critical system files that the system cannot operate without. Another example is disabling a service that is needed to boot the system."+Style.RESET_ALL)
		print("")
	elif A == "N":
		AI = 1
		AvailImpact = 0
	elif A == "P":
		AI = 1
		AvailImpact = 0.275
	elif A == "C":
		AI = 1
		AvailImpact = 0.660
	else: 
		print("Wrong value");

# Privilege Level (PL)
PLS = 0
print(Fore.BLUE+"Privilege Level (PL)"+Style.RESET_ALL)
while PLS != 1:
	PL =  input ("Root Level "+Fore.YELLOW+"(R)"+Style.RESET_ALL+" or User Level "+Fore.YELLOW+"(U)"+Style.RESET_ALL+" or Application Level "+Fore.YELLOW+"(A)"+Style.RESET_ALL+" or Not Defined "+Fore.YELLOW+"(ND)"+Style.RESET_ALL+" or def: ")
	if PL == "def":
		print(Fore.GREEN+"Note: Privilege Level does not have an impact on how the CCSS score is calculated (Yea IDK why I must implement that)")
		print("")
		print("Root Level (R): root account is needed to exploit this misconfiguration")
		print("")
		print("User Level (U): a standard account is needed to exploit this misconfiguration")
		print("")
		print("Application Level (A): a application account is needed to exploit this misconfiguration")
		print("")
		print("Not Defined (ND): no account is needed to exploit this misconfiguration"+Style.RESET_ALL)
		print("")
	elif PL == "R":
		PLS = 1
	elif PL == "U":
		PLS = 1
	elif PL == "A":
		PLS = 1
	elif PL == "ND":
		PLS = 1
	else: 
		print("Wrong value");

# Explotiation Method (EM)
EMS = 0
print(Fore.BLUE+"Exploitation Method (EM)"+Style.RESET_ALL)
while EMS != 1:
	EM =  input ("Active "+Fore.YELLOW+"(A)"+Style.RESET_ALL+" or Passive "+Fore.YELLOW+"(P)"+Style.RESET_ALL+" or def: ")
	if EM == "def":
		print(Fore.GREEN+"Note: Exploitation Method does not have an impact on how the CCSS score is calculated (Yea IDK why I must implement that)")
		print("")
		print("Active (A): Some vulnerabilities can be actively exploited, such as an attacker gaining access to a sensitive file because the targeted system is incorrectly configured to permit any user to read the file.")
		print("")
		print("Passive (P): Other vulnerabilities passively prevent authorized actions from occurring, such as not permitting a system service or daemon to run or not generating audit log records for security events"+Style.RESET_ALL)
		print("")
	elif EM == "A":
		EMS = 1
	elif EM == "P":
		EMS = 1
	else: 
		print("Wrong value");

# Equation calculation
Impact = 10.41 * (1 - (1 - ConfImpact) * (1 - IntegImpact) * (1 - AvailImpact))
Exploitability = 20 * AccessVector * Authentication * AccessComplexity
if Impact == 0:
	fImpact = 0
else:
	fImpact = 1.176

BaseScore = round(((0.6 * Impact) + (0.4 * Exploitability) - 1.5) * fImpact,1) 

print("")
print(Fore.YELLOW+"This misconfiguration has a BaseScore of: " + str(BaseScore))
print("AV:"+ AV +"/AC:"+ AC +"/Au:"+ Au +"/C:"+ C +"/I:"+ I +"/A:"+ A +"/PL:"+ PL +"/EM:"+ EM+Style.RESET_ALL)
