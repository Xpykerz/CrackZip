import zipfile
from threading import Thread

def extract_zip(zfile, password):
    try:
        zfile.extractall(pwd=password)
        print "[+] Password Found: " + password + '\n'
    except:
        print "[-] Password Not Match: " + password + '\n'

def main():
	print "   _____                _     _______       "
	print "  / ____|              | |   |___  (_)      "
	print " | |     _ __ __ _  ___| | __   / / _ _ __  "
	print " | |    | '__/ _` |/ __| |/ /  / / | | '_ \ "
	print " | |____| | | (_| | (__|   <  / /__| | |_) |"
	print "  \_____|_|  \__,_|\___|_|\_\/_____|_| .__/ "
	print "                                     | |    "
	print "                                     |_|    "
	print "			https://github.com/Xpykerz "
	print "			Ask: https://t.me/MQ_XZ    "
	print "\n"

	zname = raw_input("Enter ZipFile Name: ")
	dname = raw_input("Enter Worldlist Name: ")
	print "\n"

	zFile = zipfile.ZipFile(zname)
	passFile = open(dname)

	for line in passFile.readlines():
		password = line.strip('\n')
		t = Thread(target=extract_zip, args=(zFile, password))
		t.start()

if __name__ == '__main__':
    main()
