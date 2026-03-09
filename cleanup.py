#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pathlib import Path

def cleanup_html_file(filepath, patterns_to_remove):
    """
    Находит и удаляет из файла все фрагменты, соответствующие списку паттернов.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        total_replacements = 0

        # Применяем все паттерны для удаления
        for pattern in patterns_to_remove:
            content, num_replacements = pattern.subn('', content)
            total_replacements += num_replacements

        if total_replacements > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content.strip()) # .strip() убирает лишние пробелы в начале/конце
            print(f"✓ Очищен: {filepath.name} ({total_replacements} удалений)")
            return True
        else:
            print(f"✓ Пропуск {filepath.name}: элементы для удаления не найдены.")
            return False
            
    except Exception as e:
        print(f"✗ Ошибка при обработке {filepath.name}: {e}")
        return False

if __name__ == "__main__":
    directory = Path("/home/henry/www/genmih.github.io/")
    
    # Список регулярных выражений для удаления разных элементов
    patterns = [
        # 1. Старая навигация: <div ><a href="index.html" ...>...</div>
        re.compile(r'<div >\s*<a href="index\.html".*?</div>', re.DOTALL),
        
        # 2. Подпись автора: <p ...>&mdash; <font ...><b>Скот Лесной</b>...
        # Этот паттерн более гибкий и учитывает разные вариации
        re.compile(r'<p class=""[^>]*>\s*&mdash;\s*<font[^>]*>\s*<b>Скот Лесной</b>\s*</font>\s*,\s*[\d\.\s]*</p>\s*(<a name=[^>]+></a>(<p class=""\s*></p>)?)?', re.DOTALL),
        
        # 3. Старый футер: <footer><p>«Проще чем убить» ...</p></footer>
        re.compile(r'\s*<footer>\s*<p>«Проще чем убить» — С\. Лесной</p>\s*</footer>', re.DOTALL)
    ]
    
    html_files = sorted(list(directory.glob('glava*.html')))
    print(f"Начинаю комплексную очистку {len(html_files)} файлов глав...\n")
    
    for file in html_files:
        cleanup_html_file(file, patterns)
    
    print("\n✅ Готово. Очистка завершена.")