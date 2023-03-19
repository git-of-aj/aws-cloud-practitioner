#!/bin/bash

# download the required utils
# https://docs.aws.amazon.com/efs/latest/ug/installing-amazon-efs-utils.html

sudo apt-get update -y
sudo apt-get -y install git binutils
git clone https://github.com/aws/efs-utils

cd efs-utils
./build-deb.sh

sudo apt-get -y install ./build/amazon-efs-utils*deb
