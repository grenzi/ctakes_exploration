#!/bin/bash
../zatoenv/zato-qs-stop.sh
find ../zatoenv | grep pid | xargs rm
../zatoenv/zato-qs-start.sh