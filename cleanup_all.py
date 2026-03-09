#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pathlib import Path

def cleanup_html_file(filepath):
    """
    Находит и удаляет из HTML-файла все лишние теги и фрагменты.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        
        # Паттерны для поиска и удаления различных ненужных элементов
        patterns_to_remove = [
            # 1. Пустые теги <p>, которые могут оставаться после конвертации
            re.compile(r'<p class=""\s*></p>'),
            
            # 2. Лишние якоря (cutid1, cutid1-end) и пустые теги вокруг них
            re.compile(r'<a name=["\']cutid1(-end)?["\']></a>'),
            
            # 3. Пустые div'ы с якорями внутри
            re.compile(r'<div><a name="[^"]+"></a></div>'),
            
            # 4. Лишние теги <br> в разных комбинациях
            re.compile(r'(<br\s*/?>\s*)+'),
            
            # 5. Вступительный абзац в glava1.html
            re.compile(r'<p><b>Начинаем публикацию роман.*?сохранены\.</b></p>'),
            
            # 6. Пустые div'ы
            re.compile(r'<div>\s*</div>'),
        ]

        # Последовательно применяем все паттерны для очистки
        for pattern in patterns_to_remove:
            content = pattern.sub('', content)

        # Убираем лишние пробельные строки для более чистого кода
        content = re.sub(r'\n\s*\n', '\n', content)

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content.strip())
            print(f"✓ Файл {filepath.name} успешно очищен.")
            return True
        else:
            print(f"✓ Пропуск {filepath.name}: элементы для удаления не найдены.")
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
        print(f"Начинаю очистку {len(html_files)} файлов глав...\n")
        
        cleaned_count = 0
        for file in html_files:
            if cleanup_html_file(file):
                cleaned_count += 1
        
        print(f"\n✅ Готово. Очищено {cleaned_count} файлов.")

