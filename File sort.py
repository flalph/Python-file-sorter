import os
import shutil

# Define the file categories for sorting
file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar'],
    'Apps': ['.apkg', '.exe', '.apk'],
    'Programs': ['.py', '.js', '.html'],


}

# Define where the sorted files go to
directory = input("Enter the directory to sort files: ").strip()

def organise_files():
    # Check if the directory exists
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    # Loop through the files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()

            # Find the matching category
            for category, extensions in file_categories.items():
                if file_ext in extensions:
                    category_folder = os.path.join(directory, category)

                    # Create category folder if it doesn't exist
                    if not os.path.exists(category_folder):
                        os.makedirs(category_folder)

                    # Move the file
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    print(f"Moved: {filename} → {category}")

    print("Files sorted")

if __name__ == "__main__":
    organise_files()