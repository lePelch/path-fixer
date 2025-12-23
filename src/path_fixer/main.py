from pathlib import Path
from tqdm import tqdm
import typer

app = typer.Typer(
    help="Tool for extracting Windows backups to Linux.\n"
         "Fixes paths and generates the directory structure."
)

@app.command()
def main(
    base_directory_to_unpack: Path = typer.Argument(
        ...,
        help="Directory containing files incorrectly formatted using Windows paths.",
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
    ),
    destination_directory: Path = typer.Argument(
        ...,
        help=(
            "Name of the directory where the files will be placed "
            "with a correct directory structure."
        ),
        exists=False,
        file_okay=False,
        dir_okay=True,
        readable=True,
    ),
):

    destination_directory.parent.mkdir(parents=True, exist_ok=True)
 
    all_element = list(base_directory_to_unpack.glob("**"))
    all_file = []
    for element in all_element:

        if not element.is_dir():
            all_file.append(element)

    for file in tqdm(all_file):
        new_file_name = file.name.replace("\\", "/")
        destination_path = destination_directory / new_file_name
 
        with file.open( "rb") as files:
            file_content = files.read()

        print(destination_path)

        destination_path.parent.mkdir(parents=True, exist_ok=True)
        with destination_path.open("wb") as files:
            files.write(file_content)

if __name__ == "__main__":
    app()
