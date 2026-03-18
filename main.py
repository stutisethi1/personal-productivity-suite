from modules.calculator import calculator_menu
from modules.notes_manager import notes_menu
from modules.timer import timer_menu
from modules.file_organizer import file_organizer_menu
from modules.unit_converter import unit_converter_menu
from modules.backup_manager import BackupManager

def show_menu():
    print("\n==========================================")
    print("      PERSONAL PRODUCTIVITY SUITE")
    print("==========================================")
    print("1. Calculator")
    print("2. Notes Manager")
    print("3. Timer")
    print("4. File Organizer")
    print("5. Unit Converter")
    print("6. Create Backup")
    print("7. Exit")

def main():
    backup = BackupManager()
    while True:
        show_menu()

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            calculator_menu()
        elif choice == "2":
            notes_menu()
        elif choice == "3":
            timer_menu()
        elif choice == "4":
            file_organizer_menu()
        elif choice == "5":
            unit_converter_menu()

        elif choice == "6":
            backup.create_backup()
            input("Press Enter to continue...")

        elif choice == "7":
            print("Exiting program...")
            break


if __name__ == "__main__":
    main()