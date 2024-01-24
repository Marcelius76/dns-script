#  Skrtypt do podstawowej konfiguracji pliku strefy DNS  #
#  dla serwera BIND w systemach operacyjnych LINUX/UNIX  #
#      copyright (c) 2024 marcin@daz@gmail.com           #
#                Licencja GNU/GPL                        #

import os
os.system("clear")

path = ("/etc/bind")

print('--------------------------------------------------')
TTL = input("Podaj wartość TTL (domyślnie 604800): ")
_ttl = ("$" + TTL)

sciezka = "~/tmp/bind/"
DOMENA = input ("podaj nazwę domeny: ")
plik = ("db." + DOMENA)
#print(plik)
MAIL = input("Podaj e-mail administratora domeny: ")
_email = MAIL.replace("@",".")
_soa1 = ("@    IN    SOA    " + DOMENA + "    "  +_email + " (" )

serial = "1"
serial = input("parametr serial, domyślnie: " + serial + " ")
_serial = ("    " + serial + " ; Serial")

refresh = "604800"
refresh = input("wpisz paramert refresh, domyślnie: " + refresh + " ")
_refresh = ("    " + refresh + " ; Refresh")

retry = "86400"
retry = input("wpisz parametr retry, domyśnie: " + retry + " ")
_retry = ("    " + retry + " ; Retry")

expire_ = "2419200"
expire_ = input("Wpisz paranetr expire, domyślnie: " + expire_ + " ")
_expire_ = ("    " + expire_ + " ; Expire")

ncttl = "604800"
ncttl = input("wpisz negative cache TTL, domyślnie: " + ncttl + " ")
_ncttl = ("    " + ncttl + "); Negative Cache TTL")

dns1 = input("Wpisz IP podstawowego serwera DNS")
_nazwa_dns1 = ("@    IN    NS    dns1")
_ip_dns1 = ("dns1    IN    A    " + dns1)

odp = ("N")
odp = input("czy chcesz podać IP zapasowego serwera DNS? t/n")

if odp == "t":
    dns2 = input("wpisz IP zapasowego serwera DNS")
    _nazwa_dns2 = ("@    IN    NS    dns2")
    _ip_dns2 = ("dns2   IN    A    " + dns2)
    #return (_nazwa_dns2, _ip_dns2)
else:
    _nazwa_dns2 = " "
    _ip_dns2 = " "
    exit


print(_ttl)
print(_soa1)
print(_serial)
print(_refresh)
print(_retry)
print(_expire_)
print(_ncttl)
print("")
print(_nazwa_dns1)
print(_ip_dns1)

f = open(plik, "w")
f.close

f = open(plik, "a")
f.write(_ttl + "\n")
f.write("\n")
f.write(_soa1 + "\n")
f.write(_serial + "\n")
f.write(_refresh + "\n")
f.write(_retry + "\n")
f.write(_expire_ + "\n")
f.write(_ncttl + "\n")
f.write("\n")
f.write(_nazwa_dns1 + "\n")
f.write(_ip_dns1 + "\n")
if odp == "t":
    f.write(_nazwa_dns2 + "\n")
    f.write(_ip_dns2 + "\n")
else:
    exit

f.close
