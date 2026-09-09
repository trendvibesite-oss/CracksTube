import re

with open('droven.io-enterprise-tech-innovation.html', 'r', encoding='utf-8') as fp:
    content = fp.read()

m_art = re.search(r'<article[^>]*>', content, re.IGNORECASE)
art_start = m_art.end()
art_end = content.find('</article>', art_start)

head_part = content[:art_start]
art_content = content[art_start:art_end]
tail_part = content[art_end:]

# Remove any internal links to crackstube.blog articles (except home callout link)
# Matches <p>...<a href="https://crackstube.blog/[^"]+">...</a>...</p>
def clean_inserted_p(match):
    text = match.group(0)
    if 'href="https://crackstube.blog/"' in text or 'href="https://crackstube.blog"' in text:
        return text  # keep home callout link
    return ''

clean_art_content = re.sub(r'<p>[^<]*<a href="https://crackstube\.blog/[^"]+"[^>]*>[^<]*</a>[^<]*</p>\s*', clean_inserted_p, art_content)

full_clean = head_part + clean_art_content + tail_part

with open('droven.io-enterprise-tech-innovation.html', 'w', encoding='utf-8') as fp:
    fp.write(full_clean)

print("Cleaned droven.io-enterprise-tech-innovation.html!")
