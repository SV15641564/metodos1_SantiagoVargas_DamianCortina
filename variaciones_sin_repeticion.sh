
n=20
r=3

N=$(bash factorial.sh $n)

resta=$(($n-$r))

resta_f=$(bash factorial.sh $resta)

echo "$(($N/$resta_f))"
