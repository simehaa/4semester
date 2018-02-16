if [ "$1" = "S" ]; then
  for i in "${@:2}"; do
    sum=$(($sum + $i))
  done; echo $sum
elif [ "$1" = "P" ]; then
  prod=1
  for i in "${@:2}"; do
    prod=$(($prod * $i))
  done; echo $prod
elif [ "$1" = "m" ]; then
  min=9999
  for i in "${@:2}";
  do
    if [[ "$i" < $min ]]; then min=$i; fi
  done; echo $min
max=-9999
elif [ "$1" = "M" ]; then
  for i in "${@:2}";
  do
    if [[ "$i" > $max ]]; then max=$i; fi
  done; echo $max
else
  echo "Error"
fi
