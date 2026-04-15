import os
import json
import re

# Target directory
base_dir = r"c:\Desktop\sriasha\sriasha-main"

# HTML files to update
html_files = [
    "index.html", "about.html", "gallery.html", "metallurgy.html", 
    "Faqs.html", "Terms.html", "privacypolicy.html", "404.html"
]

# New director profile data for schema
new_directors_schema = [
    {
        "@type": "Person",
        "name": "M. Asha",
        "jobTitle": "Director",
        "worksFor": { "@id": "https://www.ashaforging.com/#organization" },
        "description": "M. Asha is a Director of Sri Asha Forgings Pvt. Ltd., contributing to the strategic oversight, leadership, and operational excellence of the company's aluminium forging business in Hyderabad."
    },
    {
        "@type": "Person",
        "name": "Shivaji Koneru",
        "jobTitle": "Director",
        "worksFor": { "@id": "https://www.ashaforging.com/#organization" },
        "description": "Shivaji Koneru is a Director of Sri Asha Forgings Pvt. Ltd. with extensive experience in industrial management and manufacturing operations, supporting the growth of precision forging in India."
    }
]

# Meta tags to add
new_meta_tags = """<meta name="director" content="M. Asha — Director, Sri Asha Forgings Pvt. Ltd.">
<meta name="director" content="Shivaji Koneru — Director, Sri Asha Forgings Pvt. Ltd.">"""

# Bio text to add to hidden footer
new_bio_text = """
            M. Asha is a Director of Sri Asha Forgings Pvt. Ltd., bringing strategic leadership and governance to the board. Her expertise supports the company's commitment to high-quality aluminium alloy forging production for critical sectors.
            Shivaji Koneru is a Director of Sri Asha Forgings Pvt. Ltd. with a strong background in industrial manufacturing and management. He plays a key role in steering the company's manufacturing excellence and operational growth in the precision forging industry.
"""

def update_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update JSON-LD Schema
    schema_pattern = re.compile(r'<script\s+type="application/ld\+json">(.*?)</script>', re.DOTALL)
    
    def schema_replacer(match):
        schema_text = match.group(1)
        try:
            schema_data = json.loads(schema_text)
            if "@graph" in schema_data:
                graph = schema_data["@graph"]
                existing_names = [item.get("name") for item in graph if item.get("@type") == "Person"]
                
                added = False
                for director in new_directors_schema:
                    if director["name"] not in existing_names:
                        insert_idx = -1
                        for i, item in enumerate(graph):
                            if item.get("name") == "Sai Rohit Chowdary":
                                insert_idx = i + 1
                                break
                        
                        if insert_idx != -1:
                            graph.insert(insert_idx, director)
                        else:
                            graph.append(director)
                        added = True
                
                if added:
                    if "\n" in schema_text:
                        return f'<script type="application/ld+json">\n{json.dumps(schema_data, indent=2)}\n</script>'
                    else:
                        return f'<script type="application/ld+json">{json.dumps(schema_data, separators=(",", ":"))}</script>'
            return match.group(0)
        except Exception as e:
            return match.group(0)

    content = schema_pattern.sub(schema_replacer, content)

    # 2. Update Meta Tags
    if 'name="director" content="Shivaji Koneru' not in content:
        content = content.replace(
            '<meta name="director" content="Sai Rohit Chowdary — Director, Sri Asha Forgings Pvt. Ltd.">',
            '<meta name="director" content="Sai Rohit Chowdary — Director, Sri Asha Forgings Pvt. Ltd.">\n' + new_meta_tags
        )

    # 3. Update Hidden Footer Bio
    bio_pattern = re.compile(r'(<div style="display:none;" aria-hidden="true">)(.*?)(</div>)', re.DOTALL)
    
    def bio_replacer(match):
        prefix = match.group(1)
        inner_text = match.group(2)
        suffix = match.group(3)
        
        if 'Shivaji Koneru' not in inner_text:
            if 'Satyam Bhimala' in inner_text:
                parts = inner_text.split('Satyam Bhimala')
                new_inner = parts[0] + new_bio_text.strip() + "\n            Satyam Bhimala" + "Satyam Bhimala".join(parts[1:])
                return prefix + new_inner + suffix
            else:
                return prefix + inner_text + new_bio_text + suffix
        return match.group(0)
                
    content = bio_pattern.sub(bio_replacer, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file_path}")

for f_name in html_files:
    path = os.path.join(base_dir, f_name)
    if os.path.exists(path):
        update_file(path)
