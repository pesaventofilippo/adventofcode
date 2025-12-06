#!/bin/bash
YEAR=$1

if test -d "$YEAR/"; then
    echo "Directory exists."
    exit 1
fi

echo -e "| [$YEAR]($YEAR/) | 0/50  | [AoC / $YEAR](https://adventofcode.com/$YEAR) |" >> README.md

mkdir -p "$YEAR"
cp ".templates/readme-year.md" "$YEAR/README.md"
sed -i '' "s/#YEAR/$YEAR/g" "$YEAR/README.md"

for day in $(seq -f "%02g" 1 12); do
    mkdir -p "$YEAR/day$day"
    cp ".templates/day.py" "$YEAR/day$day/main.py"
    touch "$YEAR/day$day/input.txt"
done
