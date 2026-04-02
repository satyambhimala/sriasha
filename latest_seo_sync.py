import os
import re

base_dir = r"c:\Desktop\sriasha-main1\sriasha-main"

# --- 1. Inject JSON-LD to index.html ---
index_path = os.path.join(base_dir, "index.html")

new_schemas = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Sri Asha Forgings",
  "url": "https://www.ashaforging.com",
  "employee": [
    {
      "@type": "Person",
      "name": "Sai Rohit Chowdary",
      "jobTitle": "Director",
      "worksFor": {
        "@type": "Organization",
        "name": "Sri Asha Forgings"
      },
      "url": "https://www.ashaforging.com"
    }
  ],
  "founder": {
    "@type": "Person",
    "name": "Sai Rohit Chowdary",
    "jobTitle": "Director & Founder"
  }
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Sri Asha Forgings",
  "url": "https://www.ashaforging.com",
  "creator": {
    "@type": "Person",
    "name": "Bhimala Satyam",
    "jobTitle": "Web Designer & Developer",
    "worksFor": {
      "@type": "Organization",
      "name": "Sri Asha Forgings"
    }
  }
}
</script>
"""

with open(index_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

if "founder" not in idx_content and "Bhimala Satyam" in new_schemas:
    idx_content = idx_content.replace("</head>", new_schemas + "\n</head>")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(idx_content)
    print("Injected new JSON-LD schemas into index.html")

# --- 2. Sync Nav Bar to Faqs.html and Terms.html ---
# Extract brandName and brandTag from index.html
brand_name_pattern = re.compile(r'(<div id="brandName"[^>]*>.*?</div>)', re.DOTALL)
brand_tag_pattern = re.compile(r'(<div id="brandTag"[^>]*>.*?</div>)', re.DOTALL)

bn_match = brand_name_pattern.search(idx_content)
bt_match = brand_tag_pattern.search(idx_content)

if bn_match and bt_match:
    brand_name_html = bn_match.group(1)
    brand_tag_html = bt_match.group(1)

    for doc in ["Faqs.html", "Terms.html"]:
        path = os.path.join(base_dir, doc)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Replace brandName
            content = brand_name_pattern.sub(brand_name_html, content)
            # Replace brandTag
            content = brand_tag_pattern.sub(brand_tag_html, content)

            # Scrub fitTagline function completely
            content = re.sub(r'function fitTagline\(\)\s*\{.*?\n.*?\}', '', content, flags=re.DOTALL)
            content = re.sub(r'window\.addEventListener\([\'"]resize[\'"], fitTagline\);', '', content)
            content = re.sub(r'window\.addEventListener\([\'"]load[\'"], fitTagline\);', '', content)
            content = re.sub(r'if\(document\.fonts && document\.fonts\.ready\).*?ready\.then\(fitTagline\);.*?\}', '', content, flags=re.IGNORECASE)
            
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Synced Nav Bar and scrubbed JS in {doc}")
