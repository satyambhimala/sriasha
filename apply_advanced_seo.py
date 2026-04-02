import os
import re

base_dir = r"c:\Desktop\sriasha-main1\sriasha-main"

html_files = [
    "index.html", "Terms.html", "privacypolicy.html",
    "metallurgy.html", "Faqs.html", "about.html", "gallery.html", "404.html"
]

meta_tags_to_inject = """
  <!-- Advanced Local SEO Core -->
  <meta name="geo.placename" content="Hyderabad, Telangana, India">
  <meta name="DC.language" content="en-IN">
  <link rel="alternate" hreflang="en-in" href="https://www.ashaforging.com/">
  <link rel="alternate" hreflang="x-default" href="https://www.ashaforging.com/">
"""

faq_schema = """
<!-- FAQ Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What aluminium alloys does Sri Asha Forgings manufacture?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We manufacture AA 6061, AA 7075, AA 2024 and other aerospace-grade aluminium alloy forgings in Hyderabad, India."
      }
    },
    {
      "@type": "Question", 
      "name": "How do I request a quote for custom forgings?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Visit our Request a Quote section at https://www.ashaforging.com/#contact or call our sales team directly."
      }
    }
  ]
}
</script>
"""

product_schema = """
<!-- Product Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Aluminium AA 6061 T652 Open Die Forging",
  "manufacturer": {
    "@type": "Organization",
    "name": "Sri Asha Forgings"
  },
  "material": "Aluminium Alloy AA 6061",
  "description": "Precision open die forgings for aerospace and defence applications manufactured in Hyderabad, India since 2004."
}
</script>
"""

def update_image_tags(content):
    # Regex to find <img ... alt="something" ... > and append SEO string to alt, and add title.
    # Exclude tiny icons or empty alts
    def replacer(match):
        full_tag = match.group(0)
        alt_content = match.group(2)
        
        # Don't touch if alt is empty or it's clearly a generic icon or if it already has Hyderabad India
        banned = ["banner", "icon", "logo"]
        if not alt_content or any(b in alt_content.lower() for b in banned):
            return full_tag
        if "Hyderabad" in alt_content and "India" in alt_content:
            return full_tag # already optimized
            
        new_alt = alt_content.strip() + " open die forging Hyderabad India"
        
        # Inject title attribute
        new_title = "Sri Asha Forgings - Precision Forging"
        # We can extract a bit of material name if possible, else generic
        if "AA" in alt_content:
            new_title = f"Sri Asha Forgings - {alt_content.split('AA')[1][:5].strip()} Precision Forging"
            
        # create new tag
        if 'title=' not in full_tag.lower():
            # replace alt text
            modified_tag = full_tag.replace(f'alt="{alt_content}"', f'alt="{new_alt}" title="{new_title}"')
            return modified_tag
            
        return full_tag

    # Matches <img ... alt="some text" ... >
    return re.sub(r'(<img[^>]*?alt=")([^"]+?)("[^>]*?>)', replacer, content, flags=re.IGNORECASE)


for f_name in html_files:
    path = os.path.join(base_dir, f_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Step 2: Inject Meta tags into head
        # First remove existing generic ones to avoid duplicates
        content = re.sub(r'<meta name="geo\.placename".*?>', '', content, flags=re.IGNORECASE)
        content = re.sub(r'<meta name="DC\.language".*?>', '', content, flags=re.IGNORECASE)
        content = re.sub(r'<link rel="alternate" hreflang="en-in".*?>', '', content, flags=re.IGNORECASE)
        content = re.sub(r'<link rel="alternate" hreflang="x-default".*?>', '', content, flags=re.IGNORECASE)
        
        # Insert right before </head>
        content = content.replace("</head>", meta_tags_to_inject + "\n</head>")
        
        # Step 1: Update Image Tags
        content = update_image_tags(content)
        
        # Step 3: FAQ Schema to index.html
        if f_name == "index.html":
            if "FAQPage" not in content:
                content = content.replace("</head>", faq_schema + "\n</head>")
                
        # Step 4: Product Schema to gallery.html
        if f_name == "gallery.html":
            if '"@type": "Product"' not in content:
                content = content.replace("</head>", product_schema + "\n</head>")

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Applied Advanced SEO to {f_name}")
    else:
        print(f"File {f_name} not found")
