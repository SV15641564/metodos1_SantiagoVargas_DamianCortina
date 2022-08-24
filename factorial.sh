#!/bin/bash

n=$1

factorial=1

if [ $n -eq 0 ] || [ $n -eq 1 ]; then
	echo $factorial

else
	while [ $n -gt 1 ]
	
	do
	
		let factorial=$factorial*$n
		let n=$n-1

	done
		echo $factorial
		
		
fi

