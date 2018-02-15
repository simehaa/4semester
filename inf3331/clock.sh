if [ "$1" == "us" ]; then
  while true; do
    now=$(date -d "-6 hours" +%T); echo $now ;
    sleep 1; printf "\033c"
done
elif [ "$1" == "sk" ]; then
  while true; do
    now=$(date -d "+7 hours" +%T); echo $now ;
    sleep 1; printf "\033c"
done
elif [ "$1" == "no" ]; then
  while true; do
    now=$(date +%T); echo $now ;
    sleep 1; printf "\033c"
done
fi
