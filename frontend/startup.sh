#!/usr/bin/bash

set -eu pipefail

if [ "$NODE_ENV" = "Production" ]; then
  echo "Running production server"
  npm run build
else
  echo "Running developing server"
    npm run dev
fi
