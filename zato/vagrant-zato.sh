#!/usr/bin/env bash
curl -O https://zato.io/download/osx/2.0/Vagrantfile
#this vagrantfile is different, but including the original source here. 
vagrant up --provider virtualbox
vagrant ssh