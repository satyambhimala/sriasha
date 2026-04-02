import os
import json
import re

path = r"c:\Desktop\sriasha-main1\sriasha-main\index.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Extract the script tag content
pattern = re.compile(r'(<script\s+type="application/ld\+json">)(.*?)(</script>)', re.DOTALL)
match = pattern.search(content)

if match:
    prefix = match.group(1)
    json_str = match.group(2)
    suffix = match.group(3)
    
    try:
        data = json.loads(json_str)
        # Check if WebSite already exists
        has_website = any(item.get('@type') == 'WebSite' for item in data.get('@graph', []))
        if not has_website:
            website_node = {
                "@type": "WebSite",
                "@id": "https://www.ashaforging.com/#website",
                "url": "https://www.ashaforging.com/",
                "name": "Sri Asha Forgings Pvt. Ltd.",
                "potentialAction": [
                    {
                        "@type": "TradeAction",
                        "target": "https://www.ashaforging.com/#contact",
                        "name": "Request a Quote"
                    }
                ]
            }
            if "@graph" in data:
                data["@graph"].append(website_node)
            else:
                pass # structure not standard graph
                
            new_json_str = json.dumps(data, separators=(',', ':'))
            new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]
            
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("Successfully updated structured data.")
    except Exception as e:
        print("Error parsing json", e)
else:
    print("Could not find script tag in index.html")
