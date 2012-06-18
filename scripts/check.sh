#!/bin/bash
JEKINS_HOME="~/"
JOBS=("zhihu-search-master" "https://github.com/ZhihuDev/search" "zhihu-search-shenchen" "https://github.com/scv119/search" "zhihu-search-sunan" "https://github.com/sunanpo/search")
BUILD_URL="http://debian2.zhq:8080/job/"

function check {

pre_resp=("" "")
while [ 0 -lt 1 ];do
counter=0
while [ $counter -lt 5 ];do
let uidx=counter+1
let pidx=uidx/2
url="http://shenchen.me:8999/fetch?url="${JOBS[$uidx]}
echo $url
response=$(curl $url) >> /dev/null
if [ "${pre_resp[$pidx]}" != "$response" ]; then
echo "========"
echo "github changed, begin to build"
echo ${JOBS[$counter]}  "changed:${pre_resp[$pidx]}" "$response"
echo "========"
curl $BUILD_URL${JOBS[$counter]}"/build"
pre_resp[$pidx]=$response
fi
let counter=counter+2
done
sleep 30
done
}

check
