# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:47:15 2020

@author: Admin
"""
import glob
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

exp_rsa = open("RSA.pem")
certn_rsa = crypto.load_certificate(crypto.FILETYPE_PEM, exp_rsa.read())
subject_rsa=certn_rsa.get_subject()
issued_to_rsa=subject_rsa.CN

print('Сертификат AUTH экспортирован для -',issued_to_auth)
print('Сертификат RSA экспортирован для -',issued_to_rsa)

input()


