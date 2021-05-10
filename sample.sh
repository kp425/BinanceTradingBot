#!/usr/bin/env bash

timestamp=$(date +%s%N)
timestamp=${timestamp:0:13}
echo $timestamp

SECRET=$2
BASE_URL="https://testnet.binance.vision"
API_PATH="/api/v3/order"

# QUERY_STRING="symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559"
QUERY_STRING="symbol=BNBUSDT&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=20&recWindow=20000&timestamp=$timestamp"

echo $QUERY_STRING
hash=$(echo -n $QUERY_STRING | \
openssl dgst -sha256 -hmac $SECRET)

hash=$(echo $hash | sed 's/(stdin)= //g')


URL="$BASE_URL$API_PATH?$QUERY_STRING&signature=$hash"
echo $URL
echo $hash

curl -H "X-MBX-APIKEY: $1" -X POST $URL