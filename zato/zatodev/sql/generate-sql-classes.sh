#!/usr/bin/env bash
#TODO see about getting this to the zato extra paths - https://zato.io/docs/admin/guide/enabling-extra-libs.html
#TODO get db connection into zato outgoing automatically (scriptable at least)
echo "requires sqlacodegen and oursql from pip or easy_install"
sqlacodegen --noinflect mysql+oursql://root:admin@localhost/ytex > ytex.py
sqlacodegen --noinflect mysql+oursql://root:admin@localhost/umls > umls.py
sqlacodegen --noinflect mysql+oursql://root:admin@localhost/cte > cte.py

