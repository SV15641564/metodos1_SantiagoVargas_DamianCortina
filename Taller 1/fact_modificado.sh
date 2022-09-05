#!/bin/bash

function seguidilla_de_factoriales(){

	for j in $(seq 0 1 $1)
		
	do
		echo El factorial de $j es $(bash factorial.sh $j)
	done
}

seguidilla_de_factoriales 20
