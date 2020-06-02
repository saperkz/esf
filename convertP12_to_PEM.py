# ***************************
# App: ConverP12
# Description: Converts all certificates in folder with name "AUTH..." and "RSA..." also shows "issued to" and expiration date
# Date: 03.04.2020
# Author: Olzhas Omarov
# Python version: 3.8
# Compatibility: Any
# Email: ooskenesary@gmail.com
# ***************************

import glob, datetime
from OpenSSL import crypto


inp_passwd = input('Input password: ')
passwd = inp_passwd.encode()

#====AUTH certificate export to PEM=============
find_orig_certname_auth=glob.glob("AUTH_*")
p12_auth=open(*find_orig_certname_auth, "rb") 
cert_auth = crypto.load_pkcs12(p12_auth.read(),passwd)
p12_auth.close()

exp_auth = open("AUTH.pem", "wb")
exp_auth.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert_auth.get_certificate()))
exp_auth.close()

#====RSA certificate export to PEM=============

find_orig_certname_rsa=glob.glob("RSA256_*")
p12_rsa=open(*find_orig_certname_rsa, "rb") 
cert_rsa = crypto.load_pkcs12(p12_rsa.read(),passwd)
p12_rsa.close()   

exp_rsa = open("RSA.pem", "wb")
exp_rsa.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert_rsa.get_certificate()))
exp_rsa.close()

#===========USERNAME-CHECK======================

exp_auth = open("AUTH.pem")
certn_auth = crypto.load_certificate(crypto.FILETYPE_PEM, exp_auth.read())
subject_auth=certn_auth.get_subject()
issued_to_auth=subject_auth.CN

valid_auth= certn_auth.get_notAfter()
string_auth=valid_auth.decode('UTF-8','ignore')
date_time_obj = string_auth[0:-1]
valid_auth_date = datetime.datetime.strptime(date_time_obj, '%Y%m%d%H%M%S')
valid_auth_until = valid_auth_date.strftime("%d.%m.%Y")


exp_rsa = open("RSA.pem")
certn_rsa = crypto.load_certificate(crypto.FILETYPE_PEM, exp_rsa.read())
subject_rsa=certn_rsa.get_subject()
issued_to_rsa=subject_rsa.CN

valid_rsa= certn_rsa.get_notAfter()
string_rsa=valid_rsa.decode('UTF-8','ignore')
date_time_obj = string_rsa[0:-1]
valid_rsa_date = datetime.datetime.strptime(date_time_obj, '%Y%m%d%H%M%S')
valid_rsa_until = valid_rsa_date.strftime("%d.%m.%Y")

print('\n')
print('Сертификат AUTH экспортирован для -',issued_to_auth)
print('Сертификат AUTH действителен до -',valid_auth_until,'\n')
print('Сертификат RSA экспортирован для -',issued_to_rsa)
print('Сертификат RSA действителен до -',valid_rsa_until)
input()
