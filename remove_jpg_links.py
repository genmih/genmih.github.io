#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pathlib import Path

def remove_jpg_images(filepath, pattern):
    """
    Находит и удаляет теги <img>, ссылающиеся на .jpg файлы,
    а также следующие за ними теги <br>.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Заменяем найденный паттерн на пустую строку
        new_content, num_replacements = pattern.subn('', content)

        if num_replacements > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Удалены {num_replacements} ссылки на JPG из: {filepath.name}")
            return True
        else:
            print(f"✓ Пропуск {filepath.name}: ссылки на JPG не найдены.")
            return False
            
    except Exception as e:
        print(f"✗ Ошибка при обработке {filepath.name}: {e}")
        return False

if __name__ == "__main__":
    directory = Path("/home/henry/www/genmih.github.io/")
    # Паттерн для поиска <img> с .jpg и последующих <br>
    jpg_pattern = re.compile(
        r'<img[^>]+src="[^"]+\.jpg"[^>]*>\s*(<br\s*/?>\s*)*',
        re.IGNORECASE
    )
    
    html_files = sorted(list(directory.glob('glava*.html')))
    print(f"Начинаю поиск и удаление ссылок на JPG в {len(html_files)} файлах глав...\n")
    
    for file in html_files:
        remove_jpg_images(file, jpg_pattern)
    
    print("\n✅ Готово. Очистка от ссылок на JPG завершена.")