import os
import re
from build_site_with_droven import link_tuples

for fname, info in link_tuples.items():
    if not os.path.exists(fname):
        print(f'Error: {fname} missing')
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match article body specifically between <article ...> and </article>
    m_art_start = re.search(r'<article[^>]*>', content, re.IGNORECASE)
    art_start = m_art_start.end()
    art_end = content.find('</article>', art_start)

    head_part = content[:art_start]
    art_content = content[art_start:art_end]
    tail_part = content[art_end:]

    # Find closing </p> tags inside art_content
    p_ends = [m.end() for m in re.finditer(r'</p>', art_content, re.IGNORECASE)]
    total_p = len(p_ends)

    early_p_text = f'\n\n        <p>{info["early"][2]}</p>'
    middle_p_text = f'\n\n        <p>{info["middle"][2]}</p>'
    late_p_text = f'\n\n        <p>{info["late"][2]}</p>'

    idx_early = 2 if total_p >= 3 else 0
    idx_middle = total_p // 2
    idx_late = max(total_p - 4, idx_middle + 2)

    pos_early = p_ends[idx_early]
    pos_middle = p_ends[idx_middle]
    pos_late = p_ends[idx_late]

    new_art_content = (art_content[:pos_late] + late_p_text +
                       art_content[pos_late:pos_middle] + middle_p_text +
                       art_content[pos_middle:pos_early] + early_p_text +
                       art_content[pos_early:])

    full_new = head_part + new_art_content + tail_part
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(full_new)
    print(f'Successfully applied distributed links in {fname}!')

# Update subfolder variant Is-charfen-co-uk-Legit/index.html
if os.path.exists('Is-charfen-co-uk-Legit/index.html'):
    with open('is-charfen-co-uk-legit.html', 'r', encoding='utf-8') as f:
        root_html = f.read()
    sub_html = root_html.replace('href="css/style.css"', 'href="/css/style.css"') \
                        .replace('src="images/', 'src="/images/') \
                        .replace('href="favicon', 'href="/favicon"') \
                        .replace('src="js/main.js"', 'src="/js/main.js"')
    with open('Is-charfen-co-uk-Legit/index.html', 'w', encoding='utf-8') as f:
        f.write(sub_html)
    print('Updated Is-charfen-co-uk-Legit/index.html!')

# Update subfolder variant droven.io-enterprise-tech-innovation/index.html
if os.path.exists('droven.io-enterprise-tech-innovation/index.html'):
    with open('droven.io-enterprise-tech-innovation.html', 'r', encoding='utf-8') as f:
        root_html = f.read()
    sub_html = root_html.replace('href="css/style.css"', 'href="/css/style.css"') \
                        .replace('src="images/', 'src="/images/') \
                        .replace('href="favicon', 'href="/favicon"') \
                        .replace('src="js/main.js"', 'src="/js/main.js"')
    with open('droven.io-enterprise-tech-innovation/index.html', 'w', encoding='utf-8') as f:
        f.write(sub_html)
    print('Updated droven.io-enterprise-tech-innovation/index.html!')
