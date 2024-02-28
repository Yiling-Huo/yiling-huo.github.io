#!/bin/bash

# This is used alongside the update_config.yaml in .github/workflows to auto update skin by season

# Get current season
current_season=$1

# just advance a season
case $current_season in
    "winter")
        echo "spring"
        ;;
    "spring")
        echo "summer"
        ;;
    "summer")
        echo "autumn"
        ;;
    "autumn")
        echo "winter"
        ;;
    *)
        echo "default"
        ;;
esac