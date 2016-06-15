#!/bin/bash
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
NC='\033[0m'

printf "\n${YELLOW}GET ${BLUE}/corpus${NC}\n"
curl -sS localhost:11223/corpus | underscore print --outfmt pretty

#curl -vX POST http://localhost:11223/corpora -d @corpora-upsert-new.json --header "Content-Type: application/json" | underscore print --outfmt pretty
