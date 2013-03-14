#!/bin/bash
echo $1 > thunderdome_logging/VERSION && git tag -a v$1 && git push --tags && python setup.py sdist upload
