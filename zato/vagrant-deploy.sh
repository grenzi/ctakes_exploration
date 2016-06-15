#!/usr/bin/env bash
echo 'Running deploy script'
vagrant ssh -c 'cd /vagrant/zatodev; . ./deploy.sh; cd samples; . ./run-samples.sh'
