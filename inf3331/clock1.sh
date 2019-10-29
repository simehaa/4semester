if [ "$1" == "us" ]; then
  TZ=UTC-6 date -R
elif [ "$1" == "sk" ]; then
  TZ=UTC+7 date -R
elif [ "$1" == "no" ]; then
  TZ=UTC date -R
fi
while true; do
    now=$(date +%T); echo $now ;
    sleep 1; printf "\033c"
done
