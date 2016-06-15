#!/usr/bin/env bash
echo 'Running deploy script'
vagrant ssh -c 'cd /vagrant/zatodev/samples; . ./run-samples.sh'
