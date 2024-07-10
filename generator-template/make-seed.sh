#!/bin/bash

# Check if a name is provided
if [ -z "$1" ]; then
  echo "No language name provided. Usage: ./generate_yaml.sh <language_name>"
  exit 1
fi

LANGUAGE_NAME="$1"

# Define the YAML content
YAML_CONTENT="irVersion: v50
docker: fernapi/fern-${LANGUAGE_NAME}-model:latest
dockerCommand: yarn workspace @fern-api/fern-${LANGUAGE_NAME}-model dockerTagLatest
language: ${LANGUAGE_NAME}
generatorType: model
defaultOutputMode: github
fixtures: []
scripts: []
local:
  workingDirectory: generators/${LANGUAGE_NAME}
  buildCommand:
    - yarn workspace @fern-api/fern-${LANGUAGE_NAME}-model dist:cli
  runCommand: node model/dist/bundle.cjs
"

# Directory to save the YAML file
DIRECTORY="seed/${LANGUAGE_NAME}-model"

# Create directory if it doesn't exist
mkdir -p "$DIRECTORY"

# Save YAML content to file
echo "$YAML_CONTENT" > "$DIRECTORY/seed.yml"

echo "YAML file generated successfully at: $DIRECTORY/seed.yml"