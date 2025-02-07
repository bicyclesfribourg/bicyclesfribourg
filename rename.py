import os
import re

# def rename_images(root_dir):
#     """Переименовывает изображения в папках bike1-bike9 в формат img_N.

#     Args:
#         root_dir: Корневая директория, содержащая папки bike1-bike9.
#     """
#     for bike_dir_name in os.listdir(root_dir):
#         # Проверяем, что это папка и ее имя начинается с "bike"
#         if os.path.isdir(os.path.join(root_dir, bike_dir_name)) and bike_dir_name.startswith("bike"):
#             bike_dir_path = os.path.join(root_dir, bike_dir_name)
#             image_count = 1
#             for filename in os.listdir(bike_dir_path):
#                 # Ищем файлы изображений (с разными расширениями)
#                 if re.search(r"\.(jpg|jpeg|png|gif|bmp)$", filename, re.IGNORECASE):
#                     old_filepath = os.path.join(bike_dir_path, filename)
#                     # Получаем расширение файла
#                     extension = os.path.splitext(filename)[1]
#                     new_filename = f"img_{image_count}{extension}"
#                     new_filepath = os.path.join(bike_dir_path, new_filename)
#                     try:
#                         os.rename(old_filepath, new_filepath)
#                         print(f"Переименован: {old_filepath} -> {new_filepath}")
#                         image_count += 1
#                     except FileExistsError:
#                         print(f"Ошибка: Файл {new_filepath} уже существует!")
#                     except OSError as e:
#                         print(f"Ошибка при переименовании {old_filepath}: {e}")
#                 else:
#                     print(f"Пропущен файл (не изображение): {filename}")

def rename_folders(root_dir):
    """Переименовывает папки, содержащие 'bike' в их имени, в формат bike_N.

    Args:
        root_dir: Корневая директория, содержащая папки для переименования.
    """
    bike_folders = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d)) and 'bike' in d]
    bike_folders.sort()  # Сортируем для последовательного переименования
    for i, folder_name in enumerate(bike_folders, start=1):
        old_folder_path = os.path.join(root_dir, folder_name)
        new_folder_name = f"bike{i}"
        new_folder_path = os.path.join(root_dir, new_folder_name)
        try:
            os.rename(old_folder_path, new_folder_path)
            print(f"Папка переименована: {old_folder_path} -> {new_folder_path}")
        except FileExistsError:
            print(f"Ошибка: Папка {new_folder_path} уже существует!")
        except OSError as e:
            print(f"Ошибка при переименовании {old_folder_path}: {e}")



if __name__ == "__main__":
    img_folder = "img"  # Замените на путь к вашей папке "img", если она не в текущей директории
    if os.path.exists(img_folder) and os.path.isdir(img_folder):
        rename_folders(img_folder)  # Добавляем вызов функции переименования папок
        # rename_images(img_folder)
        print("Переименование завершено.")
    else:
        print(f"Ошибка: Папка {img_folder} не найдена или не является директорией.")
# NumberPhotos = [0, 4, 5, 1, 7, 4, 2, 4, 5, 5]
# n = 1
# for i in range(1, 10):
#     for g in range(1, NumberPhotos[i]+1):
#         print(f'<link rel="preload" href="img/bike{i}/img_{g}.png" as="image">')
