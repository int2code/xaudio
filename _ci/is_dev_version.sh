#!/bin/bash

IS_DEV_VERSION=$(grep -P '[0-9]+\.[0-9]+\.[0-9]+\.dev[0-9]+' version.txt)

if [ "$IS_DEV_VERSION" != "" ]; then
  echo "Valid dev version."
  exit 0
else
  echo "Invalid dev version! Add .dev[xx] suffix in version.txt."
  exit 1
fi