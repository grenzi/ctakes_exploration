#!/usr/bin/env bash
sphinx-apidoc  -o ./doc/source/ ./zatodev/
cd doc
make html
cd ..
open -a safari ./doc/build/html/index.html

