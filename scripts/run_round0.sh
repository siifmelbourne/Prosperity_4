#!/bin/bash

echo "Running replay backtest..."
python backtest/run_backtest.py

echo "Running Monte Carlo..."
python backtest/run_monte_carlo.py
