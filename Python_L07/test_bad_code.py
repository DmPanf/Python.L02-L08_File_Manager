import os
from pathlib import Path
from tempfile import TemporaryDirectory

from file_tools import file_copy


def test_file_copy_copy_file():
    with TemporaryDirectory() as tmp_dir:
        src_file = os.path.join(tmp_dir, "test.txt")
        with open(src_file, "w") as f:
            f.write("test")
        dest_file = os.path.join(tmp_dir, "test_copy.txt")
        file_copy(src_file, dest_file)
        assert os.path.exists(dest_file)
        assert Path(dest_file).stat().st_size == 4


def test_file_copy_copy_folder():
    with TemporaryDirectory() as tmp_dir:
        src_folder = os.path.join(tmp_dir, "test_folder")
        os.mkdir(src_folder)
        file1 = os.path.join(src_folder, "file1.txt")
        with open(file1, "w") as f:
            f.write("test")
        file2 = os.path.join(src_folder, "file2.txt")
        with open(file2, "w") as f:
            f.write("test")
        dest_folder = os.path.join(tmp_dir, "test_folder_copy")
        file_copy(src_folder, dest_folder)
        assert os.path.exists(dest_folder)
        assert os.path.exists(os.path.join(dest_folder, "file1.txt"))
        assert os.path.exists(os.path.join(dest_folder, "file2.txt"))
        assert Path(os.path.join(dest_folder, "file1.txt")).stat().st_size == 4
        assert Path(os.path.join(dest_folder, "file2.txt")).stat().st_size == 4
