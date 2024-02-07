import os
import os
import shutil
import ctypes

def delete_files():
    choice = get_user_choice()
    execute_choice(choice)

def execute_choice(choice):
    if choice == "temp":
        delete_temporary_files()
    elif choice == "recycle":
        empty_recycle_bin()
    else:
        delete_temporary_files()
        empty_recycle_bin()

def get_user_choice():
    while True:
        choice = input("Do you want to delete temporary files, recycle bin, or both? (temp/recycle/both): ").lower()
        if choice in ("temp", "recycle", "both"):
            return choice
        print("Invalid choice. Please choose 'temp', 'recycle', or 'both'.")

def delete_items_in_directory(path):
    deleted_count = 0
    error_count = 0
    
    for item_name in os.listdir(path):
        item_path = os.path.join(path, item_name)
        try:
            if os.path.isfile(item_path):
                delete_file(item_path)
            elif os.path.isdir(item_path):
                delete_directory(item_path)
            deleted_count += 1
        except Exception:
            error_count += 1
            
    return deleted_count, error_count
    
def delete_temporary_files():
    temp_path = os.environ.get('TEMP')
    deleted_items, errors = delete_items_in_directory(temp_path)
    show_result_message(deleted_items, errors)
    
def show_result_message(deleted_items, errors):
    print(f"Deleted {deleted_items} items, but failed to delete {errors} items.")
    
def delete_directory(directory_path):
    if os.path.isdir(directory_path):
        shutil.rmtree(directory_path)
        
def delete_file(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)

def empty_recycle_bin():
    SHEmptyRecycleBin = ctypes.windll.shell32.SHEmptyRecycleBinW
    SHEmptyRecycleBin(None, None, 0)

if __name__ == "__main__":
    delete_files()