import os
import re

def rename_images(root_dir):
    """Переименовывает изображения в папках bike1-bike9 в формат img_N.

    Args:
        root_dir: Корневая директория, содержащая папки bike1-bike9.
    """
    for bike_dir_name in os.listdir(root_dir):
        # Проверяем, что это папка и ее имя начинается с "bike"
        if os.path.isdir(os.path.join(root_dir, bike_dir_name)) and bike_dir_name.startswith("bike"):
            bike_dir_path = os.path.join(root_dir, bike_dir_name)
            image_count = 1
            for filename in os.listdir(bike_dir_path):
                # Ищем файлы изображений (с разными расширениями)
                if re.search(r"\.(jpg|jpeg|png|gif|bmp)$", filename, re.IGNORECASE):
                    old_filepath = os.path.join(bike_dir_path, filename)
                    # Получаем расширение файла
                    extension = os.path.splitext(filename)[1]
                    new_filename = f"img_{image_count}{extension}"
                    new_filepath = os.path.join(bike_dir_path, new_filename)
                    try:
                        os.rename(old_filepath, new_filepath)
                        print(f"Переименован: {old_filepath} -> {new_filepath}")
                        image_count += 1
                    except FileExistsError:
                        print(f"Ошибка: Файл {new_filepath} уже существует!")
                    except OSError as e:
                        print(f"Ошибка при переименовании {old_filepath}: {e}")
                else:
                    print(f"Пропущен файл (не изображение): {filename}")

if __name__ == "__main__":
    img_folder = "img"  # Замените на путь к вашей папке "img", если она не в текущей директории
    if os.path.exists(img_folder) and os.path.isdir(img_folder):
        rename_images(img_folder)
        print("Переименование завершено.")
    else:
        print(f"Ошибка: Папка {img_folder} не найдена или не является директорией.")