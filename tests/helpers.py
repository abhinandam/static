from bs4 import BeautifulSoup
import os
import subprocess

def get_files(path):
    files = os.listdir(path)
    files.sort()
    return files

def parse_html(path):
    return BeautifulSoup(open(path), 'html.parser')

def get_tag(path, selector):
    soup = parse_html(path)
    return soup.find(selector)

def get_content(path, selector):
    tag = get_tag(path, selector)
    # http://stackoverflow.com/a/18602241/358804
    contents = tag.decode_contents(formatter='html')
    return contents.strip()

def check_title(path, title):
    expected_title = get_content(path, 'title')
    assert expected_title == title

def check_body(path, expected_body):
    actual_body = get_content(path, 'body')
    assert actual_body == expected_body

def generate(source, dest):
    script = os.path.join('.', 'generate.sh')
    return subprocess.run([script, source, dest])
