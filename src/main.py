from textnode import TextType
from textnode import TextNode
from markdown_to_html import markdown_to_html
import os
import shutil

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

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    f_markdown = open(from_path)
    f_template = open(template_path)

    content_markdown = f_markdown.read()
    content_template = f_template.read()

    f_markdown.close()
    f_template.close()

    html_node = markdown_to_html(content_markdown)
    html_content = html_node.to_html()

    page_title = extract_title(content_markdown)

    content_template_with_title = content_template.replace("{{ Title }}", page_title)
    new_html = content_template_with_title.replace("{{ Content }}", html_content)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(new_html)

def main():
    del_public_dir()
    create_public_dir("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")
    generate_page("content/blog/glorfindel/index.md", "template.html", "public/blog/glorfindel/index.html")
    generate_page("content/blog/tom/index.md", "template.html", "public/blog/tom/index.html")
    generate_page("content/blog/majesty/index.md", "template.html", "public/blog/majesty/index.html")
    generate_page("content/contact/index.md", "template.html", "public/contact/index.html")

if __name__ == "__main__":
    main()
