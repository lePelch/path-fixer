from pathlib import Path
from tqdm import tqdm
import typer
import shutil

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

    destination_directory.mkdir(parents=True, exist_ok=True)

    files_iter = (p for p in base_directory_to_unpack.rglob("*") if p.is_file())

    for src in tqdm(files_iter, desc="Fixing paths", unit="file"):
        rel = src.relative_to(base_directory_to_unpack)
        fixed = Path(str(rel).replace("\\", "/"))
        dst = destination_directory / fixed

        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

if __name__ == "__main__":
    app()
