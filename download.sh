#!/bin/zsh
AOC_SESSION_FILE="$HOME/.config/adventofcode.session"
AOC_MAX_WIDTH=80
YEAR=2025

mkdir -p "$YEAR"
cd "$YEAR"

for day in {01..12}; do
    mkdir -p "day$day"
    cd "day$day"
    aoc -s "$AOC_SESSION_FILE" -w $AOC_MAX_WIDTH -y $YEAR -d $day -i input.txt -p puzzle.md download
    cd ..
done

cd ..
