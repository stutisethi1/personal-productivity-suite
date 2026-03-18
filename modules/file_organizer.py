import os
import shutil


def organize_files():

    folder_path = input("Enter folder path to organize: ")

    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    file_types = {
        "Images": [".jpg", ".png", ".jpeg", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mkv"],
        "Music": [".mp3"],
        "Others": []
    }

    for filename in os.listdir(folder_path):

        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):

            moved = False

            for folder, extensions in file_types.items():

                if any(filename.lower().endswith(ext) for ext in extensions):

                    target_folder = os.path.join(folder_path, folder)

                    os.makedirs(target_folder, exist_ok=True)

                    shutil.move(file_path, os.path.join(target_folder, filename))

                    moved = True
                    break

            if not moved:

                target_folder = os.path.join(folder_path, "Others")
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))

    print("Files organized successfully!")

def file_organizer_menu():

    while True:

        print("\n------ File Organizer ------")
        print("1. Organize Files")
        print("2. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            organize_files()

        elif choice == "2":
            break

        else:
            print("Invalid choice.")
