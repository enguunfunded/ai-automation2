# test_main.py
import os

def test_links_exists():
    assert os.path.exists("input/links.txt")

def test_output_dir_exists():
    assert os.path.isdir("output")

def test_main_runs():
    result = os.system("python main.py")
    assert result == 0
