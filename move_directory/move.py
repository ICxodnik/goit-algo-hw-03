from pathlib import Path
import shutil

def move_tree(path: Path, path_final: Path ) -> None:
    if not path.exists():
        raise FileNotFoundError("Initial path not exist.")

    if path.is_dir():
        for child in path.iterdir():
            move_tree(child, path_final)
    elif path.is_file():
        ext_folder = path.suffix.lstrip('.') or "no_extension"
        dest_path = path_final / ext_folder
        dest_path.mkdir(parents=True, exist_ok=True)
        shutil.move(path.as_posix(), (dest_path / path.name).as_posix())

if __name__ == "__main__":
    path_initial = input("\nEnter an initial path: ").strip()
    path_final = input("\nEnter a final path: ").strip()
    try:
        root_initial = Path(path_initial).resolve()
        root_final = Path(path_final).resolve() 
    
        move_tree(root_initial, root_final)
    except Exception as e:
        print(f"Incorrect path or display error {e}")
    
