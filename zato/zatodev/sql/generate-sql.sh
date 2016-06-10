#!/usr/bin/env bash
#TODO see about getting this to the zato extra paths - https://zato.io/docs/admin/guide/enabling-extra-libs.html
#TODO get db connection into zato outgoing automatically (scriptable at least)
echo "requires sqlacodegen and oursql from pip or easy_install"
sqlacodegen mysql+oursql://root:admin@localhost/ytex > db-ytex.py
sqlacodegen mysql+oursql://root:admin@localhost/umls > db-umls.py
sqlacodegen mysql+oursql://root:admin@localhost/cte > db-cte.py

