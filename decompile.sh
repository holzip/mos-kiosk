#!/bin/bash

find . -name "*.pyc" | while read -r file; do
    output_file="${file%.pyc}.py"
    echo "Декомпиляция: $file -> $output_file"
    
    "pycdc" "$file" > "$output_file" 2> /dev/null

    if [ ! -s "$output_file" ]; then
        echo "  [!] Ошибка декомпиляции $file (возможно, неподдерживаемый опкод)"
        rm "$output_file"
    fi
done

echo "Готово!"