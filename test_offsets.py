import os
import re

files = [
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

print(f"Total files: {len(files)}")

for f in files:
    if not os.path.exists(f):
        print(f"MISSING: {f}")
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    m_art = re.search(r'<article[^>]*>', content, re.IGNORECASE)
    if not m_art:
        print(f"No <article> in {f}")
        continue
    art_start = m_art.end()
    art_end = content.find('</article>', art_start)
    art_content = content[art_start:art_end]

    h2_matches = list(re.finditer(r'<h2[^>]*>', art_content, re.IGNORECASE))
    p_ends = [m.end() for m in re.finditer(r'</p>', art_content, re.IGNORECASE)]

    print(f"\n--- {f} ---")
    print(f"Article len: {len(art_content)} chars | H2 count: {len(h2_matches)} | P count: {len(p_ends)}")

    # Test H2-based offset finding
    if len(h2_matches) >= 3:
        h2_1 = h2_matches[0].end()
        h2_mid = h2_matches[len(h2_matches) // 2].end()
        h2_last = h2_matches[-1].end()

        # find first </p> after each h2
        p_1 = next((p for p in p_ends if p > h2_1), p_ends[1] if len(p_ends) > 1 else p_ends[0])
        p_mid = next((p for p in p_ends if p > h2_mid), p_ends[len(p_ends)//2])
        p_last = next((p for p in p_ends if p > h2_last), p_ends[-1])

        print(f"Positions: early={p_1}, mid={p_mid}, late={p_last}")
        print(f"Gaps: mid-early={p_mid - p_1} chars, late-mid={p_last - p_mid} chars")
    else:
        p_1 = p_ends[1] if len(p_ends) > 1 else p_ends[0]
        p_mid = p_ends[len(p_ends)//2]
        p_last = p_ends[-2] if len(p_ends) > 2 else p_ends[-1]
        print(f"Positions (P-fallback): early={p_1}, mid={p_mid}, late={p_last}")
        print(f"Gaps: mid-early={p_mid - p_1} chars, late-mid={p_last - p_mid} chars")
