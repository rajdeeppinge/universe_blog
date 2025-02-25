import html2text
import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime

# Load the Blogspot XML file
BLOGGER_XML_FILE = "blog-02-24-2025.xml"  # Change this to your actual XML filename

# Output directory for Jekyll posts
OUTPUT_DIR = "_posts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Parse the XML file
tree = ET.parse(BLOGGER_XML_FILE)
root = tree.getroot()
namespace = {'ns': 'http://www.w3.org/2005/Atom'}

# HTML converter setup
html_converter = html2text.HTML2Text()
html_converter.ignore_links = False  # Keeps links as Markdown
html_converter.ignore_images = False  # Keeps image markdown
html_converter.body_width = 0  # Prevents word wrapping issues

# Function to clean text for Markdown
def clean_text(text):
    if not text:
        return ""
    text = text.replace("&nbsp;", " ")  # Fix spaces
    text = re.sub(r'\s+', ' ', text).strip()  # Remove excessive spaces
    return text


# Function to parse date properly
def parse_date(date_str):
    # Remove timezone offset if present (e.g., "+05:30")
    date_str = re.sub(r"([+-]\d{2}:\d{2})$", "", date_str)
    
    # Try parsing the date without the timezone
    return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")


# Extract and convert posts
for entry in root.findall("ns:entry", namespace):
    # Extract post details
    title = entry.find("ns:title", namespace).text or "Untitled"
    content_html = entry.find("ns:content", namespace).text or ""
    content_markdown = html_converter.handle(content_html)
    published_date = entry.find("ns:published", namespace)

    # Check for draft status using <app:draft>
    draft_element = entry.find("app:control/app:draft", {'app': 'http://purl.org/atom/app#'})
    is_draft = draft_element is not None and draft_element.text == "yes"

    if published_date is None or is_draft:
        print(f"⏩ Skipping draft post: {title}")
        continue  # Skip to the next post

    published_date = published_date.text  # Convert element to string

    # Convert Blogspot date to Jekyll format YYYY-MM-DD
    date_obj = parse_date(published_date)
    formatted_date = date_obj.strftime("%Y-%m-%d")

    # Create a filename for the post
    safe_title = re.sub(r"[^\w\s-]", "", title).strip().replace(" ", "-")
    filename = f"{OUTPUT_DIR}/{formatted_date}-{safe_title}.md"

    # Prepare Markdown content
    markdown_content = f"""---
layout: post
title: "{title}"
date: {formatted_date}
---

{content_markdown}
"""

    # Save as Markdown file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"Converted: {filename}")

print("✅ All posts converted to Markdown!")

