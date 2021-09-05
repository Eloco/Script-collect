#!/bin/bash
version="1.0.3"

function installJava(){
  command -v apt >/dev/null 2>&1 && (apt-get update; apt-get install openjdk-8-jdk -y; return;)
  command -v yum >/dev/null 2>&1 && (yum install java-1.8.0-openjdk -y; return;)
}

function installUnzip(){
  command -v apt >/dev/null 2>&1 && (apt-get update; apt-get install unzip -y; return;)
  command -v yum >/dev/null 2>&1 && (yum install unzip -y; return;)
}

command -v java >/dev/null 2>&1 || installJava
export -p
java -jar ./BILIBILI-HELPER.jar $SESSDATA $DEDEUSERID $BILI_JCT $SCKEY >> message.txt 2>&1
cat message.txt
echo "执行完成"
