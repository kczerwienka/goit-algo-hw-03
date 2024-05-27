from pathlib import Path
import shutil

def copy_tree(source: Path, destination: Path = None) -> None:
    print(str(source.name))

    if not destination:
        destination = source / "dist"

    if source.is_file():
        print((source.suffix.lstrip(".")))
        new_dest = destination / f"{source.suffix.lstrip(".")}"

        if new_dest.exists():
            shutil.copy(source, new_dest)
        else:
            new_dest.mkdir(parents=True)
            shutil.copy(source, new_dest)
            print("2")

    if source.is_dir():
        for child in source.iterdir():
            copy_tree(child, destination)

if __name__ == "__main__":
    path = input("Input [source],[destination]")
    
    s = None
    d = None

    if "," in path:
        source, destination = path.split(",")
       
        s = Path(source)
        
        d = Path(destination)
        copy_tree(s, d)
    
    else:
        s = Path(path)
        copy_tree(s)

    
    