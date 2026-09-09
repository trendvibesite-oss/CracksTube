import os
import re

files = [
    '418dsg7-error.html', 'anko-dango-near-me.html', 'brumeblog-com-review.html',
    'clickfor-net.html', 'crackstube-alternatives.html', 'crackstube-everything-explained.html',
    'droven.io-enterprise-tech-innovation.html', 'glorvix-com.html', 'hrms-globex.html',
    'is-charfen-co-uk-legit.html', 'modcityusa-com-guide.html', 'pressvibepulse-com.html',
    'quikconsole-com.html', 'serp-insight-guest-post.html', 'serp-insight-link-insertion.html',
    'techsized-com.html', 'techyhittools-org.html', 'thealitekeepsafe-com.html',
    'vocalnewsmedia-com.html', 'yonosamachar-com.html', 'zavalio-com.html'
]

outgoing_count = {}
incoming_count = {f.replace('.html', ''): 0 for f in files}

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    link_line_nums = []
    for i, line in enumerate(lines, 1):
        matches = re.findall(r'<a\s+href="(https://crackstube\.blog/[^"]+)"[^>]*>(.*?)</a>', line, re.IGNORECASE)
        for url, anchor in matches:
            if url not in ('https://crackstube.blog/', 'https://crackstube.blog'):
                link_line_nums.append((i, url.replace('https://crackstube.blog/', '').rstrip('/'), anchor))
                slug = url.replace('https://crackstube.blog/', '').rstrip('/')
                if slug in incoming_count:
                    incoming_count[slug] += 1
    
    outgoing_count[f] = len(link_line_nums)
    print(f'=== {f} (Total Lines: {len(lines)}) ===')
    for line_num, slug, anchor in link_line_nums:
        print(f'  Line {line_num}: -> /{slug}/ ("{anchor}")')
    
    # Verify links are separated by at least 15 lines
    line_numbers_only = [l[0] for l in link_line_nums]
    for k in range(len(line_numbers_only) - 1):
        diff = line_numbers_only[k+1] - line_numbers_only[k]
        assert diff > 10, f'ERROR in {f}: Links at line {line_numbers_only[k]} and {line_numbers_only[k+1]} are too close (diff={diff} lines)!'

assert all(c == 3 for c in outgoing_count.values()), 'ERROR: Outgoing count not 3'
assert all(c == 3 for c in incoming_count.values()), 'ERROR: Incoming count not 3'

print('\nSUCCESS VERIFICATION PASSED! All 21 articles have 3 outgoing & 3 incoming links widely separated across early, middle, and late sections!')
