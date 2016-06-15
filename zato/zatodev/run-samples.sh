#!/bin/bash
export ZATOHOST=localhost
export ZATOPORT=11223

BLUE='\033[0;34m'
YELLOW='\033[0;33m'
NC='\033[0m'

printf "\n${YELLOW}GET ${BLUE}/corpus${NC}\n"
curl -sS $ZATOHOST:$ZATOPORT/corpus | underscore print --outfmt pretty

printf "\n${YELLOW}POST ${BLUE}/corpus/add${NC}\n"
curl -sS -XPOST $ZATOHOST:$ZATOPORT/corpus/add -d '{"name":"another corpus name", "description":"the description of the corpus"}' --header "Content-Type: application/json" | underscore print --outfmt pretty


printf "\n${YELLOW}POST ${BLUE}/corpus/1/update${NC}\n"
curl -sS -XPOST $ZATOHOST:$ZATOPORT/corpus/1/update -d '{"name":"edited corpus name", "description":"the description of the corpus"}' --header "Content-Type: application/json" | underscore print --outfmt pretty


printf "\n${YELLOW}GET ${BLUE}/corpus${NC}\n"
curl -sS $ZATOHOST:$ZATOPORT/corpus | underscore print --outfmt pretty