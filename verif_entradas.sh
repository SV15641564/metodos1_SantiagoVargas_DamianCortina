
pass=0

function checkvalue(){
	if [ $1 -eq 1 ] || [ $1 -eq 0 ]; then

		pass=1	
	else
		echo -e "Intente de nuevo, por favor.\n"
	fi
}

while [ $pass -eq 0 ]
do
	echo -e "\nDigite la variable: "
	read variable	
	checkvalue $variable
done
