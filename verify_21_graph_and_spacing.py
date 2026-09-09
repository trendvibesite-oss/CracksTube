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

incoming_counts = {f: 0 for f in articles}
slug_to_file = {}

for f in articles:
    slug = f.replace('.html', '')
    slug_to_file[slug] = f

errors = []

for f in articles:
    if not os.path.exists(f):
        errors.append(f"Missing file: {f}")
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()

    # Find internal blog links in article body
    article_text = "".join(lines)
    m_art = re.search(r'<article[^>]*>', article_text, re.IGNORECASE)
    if not m_art:
        errors.append(f"No <article> in {f}")
        continue
    art_start = m_art.end()
    art_end = article_text.find('</article>', art_start)
    art_content = article_text[art_start:art_end]

    # Find links to crackstube.blog articles
    # Excluding the home callout link https://crackstube.blog/ or crackstube.blog home links
    link_matches = []
    for line_idx, line in enumerate(lines, 1):
        for m in re.finditer(r'href="https://crackstube\.blog/([^"#\s]+)"', line):
            target_slug = m.group(1).rstrip('/')
            if target_slug in slug_to_file and slug_to_file[target_slug] != f:
                link_matches.append((line_idx, target_slug, m.group(0)))
                incoming_counts[slug_to_file[target_slug]] += 1

    print(f"\n=== {f} (Total Lines: {len(lines)}) ===")
    print(f"Outgoing links count: {len(link_matches)}")
    for line_idx, target_slug, raw_href in link_matches:
        print(f"  Line {line_idx}: -> /{target_slug}")

    if len(link_matches) != 3:
        errors.append(f"{f} has {len(link_matches)} outgoing internal links (expected 3)!")

    # Verify spacing between outgoing links
    if len(link_matches) == 3:
        l1, l2, l3 = link_matches[0][0], link_matches[1][0], link_matches[2][0]
        gap1 = l2 - l1
        gap2 = l3 - l2
        print(f"  Line Gaps: L2-L1 = {gap1} lines, L3-L2 = {gap2} lines")
        if gap1 < 10 or gap2 < 10:
            errors.append(f"{f} links are too close! Gaps: {gap1}, {gap2}")

print("\n=== INCOMING LINK SUMMARY ===")
for f in articles:
    cnt = incoming_counts[f]
    print(f"{f}: {cnt} incoming links")
    if cnt != 3:
        errors.append(f"{f} has {cnt} incoming links (expected 3)!")

print("\n" + "="*50)
if errors:
    print("VERIFICATION FAILED WITH ERRORS:")
    for err in errors:
        print(f" - {err}")
else:
    print("ALL VERIFICATIONS PASSED! Perfect 3-regular graph with wide line spacing across all 21 articles!")
print("="*50)
