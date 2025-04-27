from textnode import TextType
from textnode import TextNode
from markdown_to_html import markdown_to_html
from gencontent import generate_pages_recursive
import os
import shutil
import sys

def create_public_dir(static_path, public_path):
    curr_path = os.listdir(static_path)
    if not os.path.exists(public_path):
        print("create dir => ", public_path)
        os.mkdir(public_path)

    for path in curr_path:
        check_path = os.path.join(static_path, path)
        copy_path = os.path.join(public_path, path)
        if os.path.isfile(check_path):
            shutil.copy(check_path, copy_path)
            print(path, " is copy to public")
            continue
        create_public_dir(check_path, copy_path)

def del_public_dir():
    if os.path.exists("public"):
        print("delete public")
        shutil.rmtree("public")

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    del_public_dir()
    create_public_dir(dir_path_static, dir_path_public)

    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)

if __name__ == "__main__":
    main()
