#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

def add_favicon_links(filepath):
    """
    Добавляет ссылки на favicon в <head> HTML-файла.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Проверяем, нет ли уже ссылок на favicon
        if '<link rel="icon"' in content:
            print(f"✓ Пропуск {filepath.name}: ссылка на favicon уже существует.")
            return False

        # Ссылки на иконки для разных устройств
        favicon_html = """
    <link rel="icon" href="/favicon.ico" type="image/x-icon">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">"""

        # Вставляем ссылки перед закрывающим тегом </head>
        new_content = content.replace("</head>", favicon_html + "\n</head>", 1)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Добавлены ссылки на favicon в файл: {filepath.name}")
            return True
        else:
            print(f"✗ Не удалось добавить ссылки в {filepath.name}")
            return False

    except Exception as e:
        print(f"✗ Ошибка при обработке {filepath.name}: {e}")
        return False

if __name__ == "__main__":
    directory = Path("/home/henry/www/genmih.github.io/")
    
    # Находим все HTML-файлы в директории
    html_files = list(directory.glob('*.html'))
    
    if not html_files:
        print("HTML-файлы не найдены в указанной директории.")
    else:
        print(f"Начинаю добавление ссылок на favicon в {len(html_files)} файлов...\n")
        
        updated_count = 0
        for file in sorted(html_files):
            if add_favicon_links(file):
                updated_count += 1
        
        print(f"\n✅ Готово. Обновлено {updated_count} файлов.")

