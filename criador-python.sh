#! /usr/bin/bash
#bash para automatizar a criaçã de arquivos python

cont=78 # o script começará a criar a partir do valor da variável $cont
# ex: como a variável está em 51 ele criará do arquivo 51 em diante

for x in {1..5} # coloque no range a quantidade de arquivos a ser criado
do
	touch ex0$cont.py
	echo "#! /usr/bin/env python3" > ex0$cont.py
	let "cont++"
done	
