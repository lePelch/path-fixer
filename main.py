from pathlib import Path
from tqdm import tqdm

def main():
    print("Starting unpacking")
    source_directory_name = "exemple_data"
    destination_directory_name = "processed_directory"

    base_directory_to_unpack = Path(source_directory_name)
    destination_directory = Path(destination_directory_name)

    destination_directory.parent.mkdir(parents=True, exist_ok=True)
    
    all_element = list(base_directory_to_unpack.glob("**"))
    all_file = []
    for element in all_element:

        if not element.is_dir():
            all_file.append(element)

    for file in tqdm(all_file):
        new_file_name = file.name.replace("\\", "/")
        destination_path = destination_directory / new_file_name
        
        with file.open( "r") as files:
            file_content = files.read()
        
        print(destination_path)

        destination_path.parent.mkdir(parents=True, exist_ok=True)
        with destination_path.open("w") as files:
            files.write(file_content)

if __name__ == "__main__":
    main()
