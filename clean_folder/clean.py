import sys
from pathlib import Path

CATEGORIES = {
    'image': ['.jpg', '.png', '.bmp', '.ai', '.psd', '.ico', '.jpeg', '.ps', '.svg', '.tif',
              '.tiff'],

    'video': ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.3gp', '.3g2', '.mpg', '.mpeg', '.m4v',
              '.h264', '.flv', '.rm', '.swf', '.vob', '.gif'],

    'audio': ['.mp3', '.wav', '.ogg', '.flac', '.aif', '.mid', '.midi', '.mpa', '.wma', '.wpl',
              '.cda'],

    'archive': ['.zip', '.rar', '.7z', '.z', '.gz', '.rpm', '.arj', '.pkg', '.deb'],

    'documents': ['.pdf', '.txt', '.doc', '.docx', '.rtf', '.tex', '.wpd', '.odt', '.xlsx', '.xls', '.xlsm',
                  '.ods', '.pptx', '.ppt', '.pps', '.key', '.odp'],

}


def move_files(file: Path, root_dir: Path, category: str):
    target_dir = root_dir / category
    if not target_dir.exists():
        target_dir.mkdir()
    return file.replace(target_dir / file.name)


def get_categories(file: Path):
    extention = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if extention in exts:
            return cat
    return 'unknow'


def sort_dir(root_dir: Path, current_dir: Path):

    for item in [f for f in current_dir.glob('*') if f.name not in CATEGORIES.keys()]:
        if not item.is_dir():
            category = get_categories(item)
            new_path = move_files(item, root_dir, category)
            print(new_path)
        else:
            sort_dir(root_dir, item)
            item.rmdir()


def main():
    try:
        path = Path(sys.argv[1])

    except IndexError:
        return f'No path to folder. Take as parametr'

    if not path.exists():
        return "Sorry folder not exist"

    sort_dir(path, path)

    return "All ok"


if __name__ == "main":
    print(main())
