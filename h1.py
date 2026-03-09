#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pathlib import Path

def add_book_title_to_h1(filepath):
    """
    Добавляет название книги в заголовок H1 в HTML-файле главы.
    Изменяет '<h1>Глава X</h1>' на '<h1>Проще чем убить — Глава X</h1>'.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Паттерн для поиска заголовка главы, который еще не содержит название книги
        pattern = re.compile(r"<h1>(Глава\s\d+)</h1>")
        
        # Замена с добавлением названия книги
        new_content, num_replacements = pattern.subn(r"<h1>Проще чем убить — \1</h1>", content)

        if num_replacements > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Обновлен заголовок в файле: {filepath.name}")
            return True
        else:
            print(f"✓ Пропуск {filepath.name}: заголовок уже обновлен или не соответствует шаблону.")
            return False
            
    except Exception as e:
        print(f"✗ Ошибка при обработке {filepath.name}: {e}")
        return False

if __name__ == "__main__":
    # Укажите путь к директории с вашими файлами
    directory = Path("/home/henry/www/genmih.github.io/")
    
    # Находим все файлы глав
    html_files = sorted(list(directory.glob('glava*.html')))
    
    if not html_files:
        print("Файлы глав (glava*.html) не найдены в указанной директории.")
    else:
        print(f"Начинаю обработку {len(html_files)} файлов глав...\n")
        
        updated_count = 0
        for file in html_files:
            if add_book_title_to_h1(file):
                updated_count += 1
        
        print(f"\n✅ Готово. Обновлено {updated_count} файлов.")

