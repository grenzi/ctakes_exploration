#!/usr/bin/env bash
echo 'Running deploy script'
vagrant ssh -c 'cd /vagrant/zatodev; . ./go.sh; . ./deploy.sh; cd samples; . ./run-samples.sh'
