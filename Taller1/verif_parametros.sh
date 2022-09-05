function help(){
	echo Debe incluir exactamente 3 parámetros: posición inicial, velocidad inicial y tiempo total, respectivamente.
}

if ! [ $# -eq 3 ]; then
	help
	exit 1
fi

if [ $# -eq 3 ]; then
	echo Muy bien, son tres parámetros, corriendo programa...
	
fi
