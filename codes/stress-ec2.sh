#!/usr/bin/bash

# for 300 sec 1 GB and 2 vpcu --> t2.micro --> get 60 % of cpu 
# make it 600 sec get --> 90% CPU

sudo apt install stress -y
stress --cpu 2 --timeout 600
