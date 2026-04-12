import re
import os

def get_classes_from_css(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Remove comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    # Simple regex for classes
    classes = set(re.findall(r'\.([a-zA-Z_-][a-zA-Z0-9_-]*)', content))
    return classes

def get_classes_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    classes = set()
    matches = re.findall(r'class="([^"]+)"', content)
    for match in matches:
        classes.update(match.split())
    return classes

css_file = 'css/style.css'
html_file = 'index.html'

css_classes = get_classes_from_css(css_file)
html_classes = get_classes_from_html(html_file)

print("Classes in CSS but not in HTML:")
unused_in_html = css_classes - html_classes
for c in sorted(unused_in_html):
    # Check if it's a font-awesome class or something standard we should keep
    # Or if it's used in a complex selector that we might have missed
    print(f"  .{c}")

print("\nClasses in HTML but not in CSS:")
unused_in_css = html_classes - css_classes
for c in sorted(unused_in_css):
    print(f"  .{c}")
