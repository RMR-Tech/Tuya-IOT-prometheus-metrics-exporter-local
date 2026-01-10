#!/bin/bash

# Script to run linting and type checking with ruff and ty

set -e

echo ""
echo "=== Running Ruff Format ==="
echo ""
uv run ruff format .


echo "=== Running Ruff Linter ==="
echo ""
uv run ruff check --fix .

echo ""
echo "=== Running ty Type Checker ==="
echo ""
uvx ty check

echo ""
echo "✅ All checks completed successfully!"

