import os


def group_files_into_subfolders():
    directory = input('Enter your files directory ')
    if os.path.exists(directory):
        file_list = [name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))]

        # Move each file to its common sub-folder name
        for filename in file_list:
            sub_folder_title = filename.split('-')[0]

            # Create a sub-folder for each file
            craete_sub_folder = os.path.join(directory, sub_folder_title)
            os.makedirs(craete_sub_folder, exist_ok=True)

            if filename.endswith('.txt') and filename.startswith(sub_folder_title):
                source_file = os.path.join(directory, filename)
                destination_file = os.path.join(craete_sub_folder, filename)
                os.rename(source_file, destination_file)
    else: print('Directory does not exists')


group_files_into_subfolders()

