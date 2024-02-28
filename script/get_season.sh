#!/bin/bash

# This is used alongside the update_config.yaml in .github/workflows to auto update skin by season

# Get the current month
month=$(date "+%m")

# Determine the season based on the month
case $month in
    12 | 1 | 2)
        echo "winter"
        ;;
    3 | 4 | 5)
        echo "spring"
        ;;
    6 | 7 | 8)
        echo "summer"
        ;;
    9 | 10 | 11)
        echo "autumn"
        ;;
    *)
        echo "default"
        ;;
esac