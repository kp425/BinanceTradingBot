#!/usr/bin/env bash

timestamp=$(date +%s%N)
timestamp=${timestamp:0:13}


SECRET=$2
BASE_URL="https://testnet.binance.vision"
API_PATH="/api/v3/order"


# QUERY_STRING="symbol=BNBUSDT&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=20&recWindow=20000&timestamp=$timestamp"

QUERY_STRING="symbol=BNBUSDT&side=BUY&type=LIMIT&quantity=1&timeInForce=GTC&price=400&timestamp=$timestamp"

hash=$(echo -n $QUERY_STRING | \
openssl dgst -sha256 -hmac $SECRET)

hash=$(echo $hash | sed 's/(stdin)= //g')

URL="$BASE_URL$API_PATH?$QUERY_STRING&signature=$hash"

echo $timestamp
echo $QUERY_STRING
echo $URL
echo $hash

curl -H "X-MBX-APIKEY: $1" -X POST $URL