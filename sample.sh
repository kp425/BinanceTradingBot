

echo "$1"
echo $2
echo $3
echo $4

echo symbol=BNBUSDT&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=20&recWindow=20000&timestamp=1620597003781 | openssl dgst -sha256 -hmac $3

curl -H "X-MBX-APIKEY: $2" -X POST $4