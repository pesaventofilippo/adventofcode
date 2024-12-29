#!/bin/zsh
AOC_SESSION_FILE="$HOME/.config/adventofcode.session"
AOC_MAX_WIDTH=80

for year in {2015..2024}; do
    mkdir -p "$year"
    cd "$year"

    for day in {01..25}; do
        mkdir -p "day$day"
        cd "day$day"
        aoc -s "$AOC_SESSION_FILE" -w $AOC_MAX_WIDTH -y $year -d $day -o -i input.txt -p puzzle.md download
        cd ..
    done

    cd ..
done
