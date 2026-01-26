import urllib.request
import re
import datetime
import html
import sys
import os

def get_meta_property(content, prop):
    # Regex to find <meta property="prop" content="..."> or <meta content="..." property="prop">
    # This is a basic parser; for production, BeautifulSoup is better but this avoids dependencies.
    pattern = rb'<meta\s+(?:property=["\']' + prop.encode('utf-8') + rb'["\']\s+content=["\'](.*?)["\']|content=["\'](.*?)["\']\s+property=["\']' + prop.encode('utf-8') + rb'["\'])'
    match = re.search(pattern, content, re.IGNORECASE)
    if match:
        return (match.group(1) or match.group(2)).decode('utf-8')
    return None

def main():
    print("--- LinkedIn Post Importer ---")
    url = input("Enter LinkedIn Post URL: ").strip()
    
    if not url:
        print("No URL provided.")
        return

    print("Fetching metadata... (this might take a moment)")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }

    title = "New Thought"
    description = ""
    image_url = ""
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            content = response.read()
            
            title = get_meta_property(content, "og:title") or title
            description = get_meta_property(content, "og:description") or ""
            image_url = get_meta_property(content, "og:image") or ""
            
            print(f"\nFound Metadata:")
            print(f"Title: {title}")
            print(f"Image: {image_url}")
            print(f"Desc:  {description[:100]}...")

    except Exception as e:
        print(f"Could not fetch URL: {e}")
        print("Falling back to manual entry.")

    # Confirm/Edit details
    print("\n--- Confirm Details ---")
    new_title = input(f"Title [{title}]: ").strip()
    link_title = new_title if new_title else title
    
    # Image handling
    use_image = True
    if image_url:
        print(f"Image found: {image_url}")
        if "static.licdn.com" in image_url: # Warning for potential default/placeholder images
            print("Warning: This looks like a generic LinkedIn placeholder image.")
        
        confirm_img = input("Include this image? [Y/n]: ").strip().lower()
        if confirm_img == 'n':
            use_image = False
            image_url = ""
    else:
        use_image = False

    
    print(f"\nFetched Description: {description[:100]}..." if description else "\nNo description fetched.")
    print("Enter Content (heading/text). Paste your text below. Press Enter twice to finish:")
    
    lines = []
    # If we have a fetched description, add it to lines initially, but allow user to clear/overwrite? 
    # Better to just ask user.
    if description:
        print(f"(Current fetched text will be used if you just press Enter twice. Type 'clear' and Enter to clear it.)")
    
    while True:
        line = input()
        if not line and len(lines) > 0 and not lines[-1]:
            break
        lines.append(line)
    
    user_input = "\n".join(lines).strip()
    
    if user_input.lower() == 'clear':
        final_desc = ""
    elif user_input:
        final_desc = user_input
    else:
        final_desc = description
    
    # Process description into paragraphs
    paragraphs = [p.strip() for p in final_desc.split('\n') if p.strip()]
    description_html = "\n        ".join([f"<p>{p}</p>" for p in paragraphs])

    date_str = datetime.datetime.now().strftime('%b %Y')

    # Template
    image_html = ""
    if use_image and image_url:
        image_html = f"""
    <div class="thought-image-container">
      <img src="{image_url}" alt="{html.escape(link_title)}" class="thought-image" onerror="this.style.display='none'">
    </div>"""


    new_card = f"""
  <!-- Article: {link_title} -->
  <div class="thought-card">{image_html}
    <div class="thought-body">
      <div class="thought-header">
        <span class="thought-date">{date_str}</span>
        <h3 class="thought-title">{link_title}</h3>
      </div>
      <div class="thought-content">
        {description_html}
      </div>
      <a href="{url}" target="_blank" class="thought-cta">View on LinkedIn</a>
    </div>
  </div>
"""

    # Insert into file
    file_path = "_publications/Thoughts.md"
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    try:
        with open(file_path, "r") as f:
            content = f.read()
        
        marker = '<div class="thoughts-container">'
        if marker in content:
            parts = content.split(marker)
            new_content = parts[0] + marker + "\n" + new_card + parts[1]
            
            with open(file_path, "w") as f:
                f.write(new_content)
            print("\nSuccess! Card added to Thoughts page.")
        else:
            print("Error: Could not find 'thoughts-container' in file.")

    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()
