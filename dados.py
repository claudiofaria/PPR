#!/usr/bin/python
#-*- coding: utf8 -*-
import re, os

def nome():
        NOM = raw_input("Digite o nome: ")
        if re.match("^[a-zA-ZáéíóúâêîôûÁÉÍÓÚÃÕÎÂÊÎÔÛ ]+$", NOM):
                return "nomee"

while (True):
        result = nome()
        if result == "nomee":
                print ("Obrigado pela Colaboração!")
                os.system("sleep 1")
                break
        else:
                print ("Formato invalido!")
                os.system("sleep 1")

def data():
        DAT = raw_input ("Data do nascimento (dd/mm/aaaa): ")
        if re.match("^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/(19[0-9]{2}|200[0-9]|201[0-8])$", DAT):
                return "data"

while (True):
        result = data()
        if result == "data":
                print ("Obrigado pela Colaboração!")
                os.system("sleep 1")
                break
        else:
                print ("Formato invalido!")
                os.system("sleep 1")
def mail():
        MAIL = raw_input ("Digite seu e-mail: ")
        if re.match("^[A-Za-z0-9._-]*\@[A-Za-z]*\.(com|br|com.br)$", MAIL):
                return "mailc"
while (True):
        result = mail()
        if result == "mailc":
                print ("Obrigado pela Colaboração!")
                os.system("sleep 1")
                break
        else:
                print ("Formato invalido!")
                os.system("sleep 1")
def tel():
        TEL = raw_input ("Digite o número de telefone: ")
        if re.match("^([0-9]{5}|[0-9]{4})-?([0-9]{4})$", TEL):
                return "tele"
while (True):
        result = tel()
        if result == "tele":
                print ("Obrigado pela Colaboração!")
                os.system("sleep 1")
                break
        else:
                print ("Formato invalido!")
                os.system("sleep 1")

def cpfc():
        CPF = raw_input ("Digite o CPF a ser validado: ")
        if re.match ("^[0-9]{3}(\.?[0-9]{3}){2}-?[0-9]{2}$", CPF):
                return "1"
while (True):
        result = cpfc()
        if result == "1":
                print ("Obrigado pela Colaboração!")
                os.system("sleep 1")
                break
        else:
                print ("Formato invalido!")
                os.system("sleep 1")
                os.system("sleep 1")
def rgg():
        CLA = raw_input ("Digite o RG a ser validado: ")
        if re.match ("^[0-9]{2}(\.?[0-9]{3}){2}-?[0-9a-zA-Z]$", CLA):
                return "3"
while (True):
        result = rgg()
        if result == "3":
                print ("Obrigado pela Colaboração!")
                os.system("sleep 1")
                break
        else:
                print ("Formato invalido!")
                os.system("sleep 1")
def inpe():
        INPE = raw_input ("Digite o endereço IP a ser validado: ")
        if re.match ("^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$", INPE):
                return "4"
while (True):
        result = inpe()
        if result == "4":
                print ("Obrigado pela Colaboração!")
                os.system("sleep 1")
                break
        else:
                print ("Formato invalido!")
                os.system("sleep 1")

def masc():
        MAS = raw_input ("Digite a máscara a ser validada: ")
        if re.match ("^(254|252|248|240|224|192|128)(.0){3}$|^255(.255|.254|.252|.248|.240|.224|.192|.128|.0){3}$", MAS):
                return "5"
while (True):
        result = masc()
        if result == "5":
                print ("Obrigado pela Colaboração!")
                os.system("sleep 1")
                break
        else:
                print ("Formato invalido!")

