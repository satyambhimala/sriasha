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

# The reinforced organization block (from user's reference with enhancements)
reinforced_organization = {
    "@type": "Organization",
    "@id": "https://www.ashaforging.com/#organization",
    "name": "Sri Asha Forgings Pvt. Ltd.",
    "alternateName": ["AFPL Forgings", "Sri Asha Forgings", "Aluminium Forgings Pvt Ltd"],
    "url": "https://www.ashaforging.com",
    "logo": "https://www.ashaforging.com/images/RFd6tsd9_sri-asha-forgings-logo-removebg-preview.webp",
    "description": "Sri Asha Forgings Pvt. Ltd. is a Hyderabad-based forging company specializing in aluminium forgings, steel forgings, copper alloys, and bronze alloys for industrial applications.",
    "foundingDate": "2004",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Plot No. 161A, IDA Phase II, Cherlapalli",
        "addressLocality": "Hyderabad",
        "addressRegion": "Telangana",
        "postalCode": "500051",
        "addressCountry": "India"
    },
    "sameAs": [
        "https://www.indiamart.com/",
        "https://www.tradeindia.com/",
        "https://www.exportersindia.com/"
    ]
}

# The directors (updated with description and absolute URLs)
directors_schema = [
    {
        "@type": "Person",
        "name": "Manduru Ravi Kumar",
        "jobTitle": "Managing Director",
        "worksFor": { "@id": "https://www.ashaforging.com/#organization" },
        "description": "Founder and Managing Director of Sri Asha Forgings Pvt. Ltd. with over 20 years of expertise in metallurgical engineering and industrial forging."
    },
    {
        "@type": "Person",
        "name": "Sai Rohit Chowdary",
        "jobTitle": "Director",
        "worksFor": { "@id": "https://www.ashaforging.com/#organization" },
        "description": "Sai Rohit Chowdary is a Director of Sri Asha Forgings Pvt. Ltd. and a BITS Pilani Dubai Alumnus with expertise in industrial growth, mechanical industries, and production management.",
        "knowsAbout": [
            "Mechanical Industry", "Forging Operations", "Industrial Business Development",
            "Manufacturing Management", "Industrial Growth Strategy", "Bike Parts Manufacturing"
        ]
    },
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

# Satyam Bhimala's schema - copied from current and must remain constant
satyam_bhimala_schema = {
    "@type": "Person",
    "name": "Satyam Bhimala",
    "url": "https://www.cantford.com",
    "jobTitle": "Entrepreneur, Founder of Cantford, Business Platform Developer & Advisor",
    "affiliation": {
        "@type": "Organization",
        "name": "Sri Asha Forgings Pvt. Ltd.",
        "url": "https://www.ashaforging.com/"
    },
    "founder": {
        "@type": "Organization",
        "name": "Cantford",
        "url": "https://www.cantford.com"
    },
    "description": "Satyam Bhimala is an Entrepreneur, Founder of Cantford, and Business Advisor focused on building business platforms, brand development, and digital business growth.",
    "knowsAbout": [
        "Entrepreneurship", "Business Development", "Brand Development", "Luxury Brand Concepts",
        "Business Platforms", "Digital Business Strategy", "Business Advisory"
    ],
    "sameAs": [
        "https://www.cantford.com", "https://www.ashaforging.com", "https://www.seoultramx.com"
    ]
}

def clean_script_and_meta(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove all current application/ld+json blocks that contain Organization, ManufacturingBusiness, or Person info
    # We want to replace these with one clean consolidated block
    script_pattern = re.compile(r'<script\s+type="application/ld\+json">.*?</script>', re.DOTALL)
    
    # We'll collect all existing scripts to extract any specific info (like Product schema)
    existing_scripts = script_pattern.findall(content)
    other_schemas = []
    
    for script_tag in existing_scripts:
        try:
            # Strip tag to get JSON
            json_text = re.search(r'>(.*)<', script_tag, re.DOTALL).group(1)
            data = json.loads(json_text)
            
            # If it's a @graph, look through its elements
            if "@graph" in data:
                for item in data["@graph"]:
                    if item.get("@type") not in ["Organization", "Person", "WebSite", "ManufacturingBusiness"]:
                        other_schemas.append(item)
            else:
                # If it's a standalone object, check its type
                if data.get("@type") not in ["Organization", "Person", "WebSite", "ManufacturingBusiness"]:
                    other_schemas.append(data)
        except:
            pass # Skip if unparseable
            
    # Now remove all existing schema blocks
    content = script_pattern.sub('', content)

    # 2. Build the final reinforced @graph
    final_graph = {
        "@context": "https://schema.org",
        "@graph": [
            reinforced_organization
        ]
    }
    
    # Add WebSite object
    final_graph["@graph"].append({
        "@type": "WebSite",
        "@id": "https://www.ashaforging.com/#website",
        "url": "https://www.ashaforging.com/",
        "name": "Sri Asha Forgings Pvt. Ltd.",
        "potentialAction": [{
            "@type": "TradeAction",
            "target": "https://www.ashaforging.com/#contact",
            "name": "Request a Quote"
        }]
    })

    # Add Directors
    for dir_obj in directors_schema:
        final_graph["@graph"].append(dir_obj)
        
    # Add Satyam Bhimala
    final_graph["@graph"].append(satyam_bhimala_schema)
    
    # Add other extracted schemas (like Product)
    for other in other_schemas:
        # Avoid duplicates
        if not any(o.get("@type") == other.get("@type") and o.get("name") == other.get("name") for o in final_graph["@graph"]):
            final_graph["@graph"].append(other)

    # 3. Inject the clean script back into the head
    # We'll put it after the canonical or after the viewport
    new_script = "\n<script type=\"application/ld+json\">\n" + json.dumps(final_graph, indent=2) + "\n</script>\n"
    
    if '<link rel="canonical"' in content:
        content = content.replace('<link rel="canonical"', new_script + '<link rel="canonical"', 1)
    elif '</head>' in content:
        content = content.replace('</head>', new_script + '</head>', 1)

    # 4. Fix other metadata links (og:image, logo etc)
    # Ensure they use the absolute professional logo path
    prof_logo = "https://www.ashaforging.com/images/RFd6tsd9_sri-asha-forgings-logo-removebg-preview.webp"
    
    # og:image
    content = re.sub(r'<meta property="og:image" content="[^"]+">', f'<meta property="og:image" content="{prof_logo}">', content)
    # twitter:image
    content = re.sub(r'<meta name="twitter:image" content="[^"]+">', f'<meta name="twitter:image" content="{prof_logo}">', content)
    # author's image if any
    
    # Also clean up duplicate meta tags if any (meta director etc might have been added multiple times)
    # Actually, let's just make sure there are no duplicate director meta tags
    # These are usually single lines, we can use a set to keep track
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Consolidated and Reinforced Schema in {file_path}")

for f_name in html_files:
    path = os.path.join(base_dir, f_name)
    if os.path.exists(path):
        clean_script_and_meta(path)
