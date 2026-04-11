#!/bin/bash

echo "Cleaning outputs..."

# Only delete contents if folder exists
if [ -d "outputs" ]; then
    rm -rf outputs/backtests/*
    rm -rf outputs/monte_carlo/*
    rm -rf outputs/figures/*
    echo "Outputs cleaned."
else
    echo "No outputs folder found."
fi
