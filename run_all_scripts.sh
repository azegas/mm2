#!/bin/bash

# below runs all scripts in order, and if one fails, the next one will not run

python3 1_fetch_stock_data.py && \
python3 2_fetch_historical_data.py && \
python3 3_draw_charts.py