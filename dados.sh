#!/bin/bash

NOME(){
        read -p "Digite seu nome: " nome
        echo $nome | grep -E -i '^[a-zA-ZáéíóúâêîôûÁÉÍÓÚÃÕÎÂÊÎÔÛ ]+$'
        if [ $? == 0 ]; then
                echo "nome valido"
                CPF
        else
                echo "nome invalido"
                NOME
        fi
}

EMAIU(){
        read -p "Digite seu e-mail: " mail
        echo $mail | grep -E -i '^[A-Za-z0-9._-]*\@[A-Za-z]*\.(com|br|com.br)$'

        if [ $? == 0 ]; then
                echo "e-mail valido"
                IP
        else
                echo "e-mail invalido"
                EMAIU
        fi
}

CPF(){
        read -p "Digite seu CPF(xxx.xxx.xxx-xx): " cpf
        echo $cpf | grep -E '^[0-9]{3}(\.?[0-9]{3}){2}-?[0-9]{2}$'
        if [ $? == 0 ]; then
                echo "cpf ok!"
                RG
        else
                echo "cpf errado"
                CPF
        fi
}
RG(){
        read -p "Digite seu RG(xx.xxx.xxx-x): " rg
        echo $rg | grep -E '^[0-9]{2}(\.?[0-9]{3}){2}-?[0-9a-zA-Z]$'
        if [ $? == 0 ]; then
                echo "RG confere com o padrão!"
                TEL
        else
                echo "RG errado!"
                RG
        fi
}
TEL(){
        read -p "Digite seu telefone(xxxxx-xxxx): " tel
        echo $tel | grep -E '^([0-9]{5}|[0-9]{4})-?([0-9]{4})$'
        if [ $? == 0 ]; then
                echo "Telefone confere com o padrão!"
                NASC
        else
                echo "Formato não aceito"
                TEL
        fi
}
NASC(){
        read -p "Digite sua data de nascimento(dd/mm/aaaa) " nasc
        echo $nasc | grep -E '(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/(19[0-9]{2}|200[0-9]|201[0-8])'
        if [ $? == 0 ]; then
                echo "Data confere com o Formato!"
                EMAIU
        else
                echo "Formato inválido!"
                NASC
        fi
}
IP(){
        read -p "Digite seu IP(xxx.xxx.xxx.xxx): " ip
        echo $ip | grep -E '^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$'
        if [ $? == 0 ]; then
                echo "IP válido"
                MASK
        else
                echo "IP inválido"
                IP
        fi
}
MASK(){
        read -p "Digite sua máscara(255.255.255.255)" masc
        echo $masc | grep -E '^(254|252|248|240|224|192|128)(.0){3}$|^255(.255|.254|.252|.248|.240|.224|.192|.128|.0){3}$'
        if [ $? == 0 ]; then
                echo "Mascara válida"
        else
                echo "Mascara Invalida"
        fi
}
NOME

