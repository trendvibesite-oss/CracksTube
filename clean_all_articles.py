import os
import re

articles = [
    '418dsg7-error.html',
    'anko-dango-near-me.html',
    'brumeblog-com-review.html',
    'clickfor-net.html',
    'crackstube-alternatives.html',
    'crackstube-everything-explained.html',
    'droven.io-enterprise-tech-innovation.html',
    'glorvix-com.html',
    'hrms-globex.html',
    'is-charfen-co-uk-legit.html',
    'modcityusa-com-guide.html',
    'pressvibepulse-com.html',
    'quikconsole-com.html',
    'serp-insight-guest-post.html',
    'serp-insight-link-insertion.html',
    'techsized-com.html',
    'techyhittools-org.html',
    'thealitekeepsafe-com.html',
    'vocalnewsmedia-com.html',
    'yonosamachar-com.html',
    'zavalio-com.html'
]

def clean_inserted_p(match):
    text = match.group(0)
    # If it's a home callout link at the bottom, keep it!
    if 'href="https://crackstube.blog/"' in text or 'href="https://crackstube.blog"' in text:
        return text
    return ''

for fname in articles:
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', encoding='utf-8') as fp:
        content = fp.read()

    m_art = re.search(r'<article[^>]*>', content, re.IGNORECASE)
    if not m_art:
        continue
    art_start = m_art.end()
    art_end = content.find('</article>', art_start)

    head_part = content[:art_start]
    art_content = content[art_start:art_end]
    tail_part = content[art_end:]

    # Remove any internal links to crackstube.blog articles inside <p> tags
    clean_art_content = re.sub(r'<p>[^<]*<a href="https://crackstube\.blog/[^"]+"[^>]*>[^<]*</a>[^<]*</p>\s*', clean_inserted_p, art_content)

    full_clean = head_part + clean_art_content + tail_part

    with open(fname, 'w', encoding='utf-8') as fp:
        fp.write(full_clean)
    print(f"Cleaned {fname}")

print("ALL 21 ARTICLES CLEANED!")
