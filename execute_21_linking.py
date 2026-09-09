import os
import re

articles = [
    '418dsg7-error.html',                         # 0
    'anko-dango-near-me.html',                     # 1
    'brumeblog-com-review.html',                   # 2
    'clickfor-net.html',                           # 3
    'crackstube-alternatives.html',                # 4
    'crackstube-everything-explained.html',        # 5
    'droven.io-enterprise-tech-innovation.html',   # 6
    'glorvix-com.html',                            # 7
    'hrms-globex.html',                            # 8
    'is-charfen-co-uk-legit.html',                 # 9
    'modcityusa-com-guide.html',                   # 10
    'pressvibepulse-com.html',                     # 11
    'quikconsole-com.html',                        # 12
    'serp-insight-guest-post.html',                # 13
    'serp-insight-link-insertion.html',            # 14
    'techsized-com.html',                          # 15
    'techyhittools-org.html',                      # 16
    'thealitekeepsafe-com.html',                   # 17
    'vocalnewsmedia-com.html',                     # 18
    'yonosamachar-com.html',                       # 19
    'zavalio-com.html'                             # 20
]

# Dictionary of target article link variants (url, variant_sentences)
link_pool = {
    0: {
        'url': 'https://crackstube.blog/418dsg7-error',
        'sentences': [
            'If you encounter unexpected browser errors while reading digital blogs, consult our <a href="https://crackstube.blog/418dsg7-error" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">418dsg7 error code details</a> for troubleshooting solutions.',
            'If digital security tools flag unusual browser errors or server codes during navigation, see our <a href="https://crackstube.blog/418dsg7-error" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">418dsg7 error troubleshooting guide</a> for step-by-step resolution.',
            'For users dealing with persistent script failures across web utility portals, read our guide on <a href="https://crackstube.blog/418dsg7-error" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">418dsg7 system error fix</a>.'
        ]
    },
    1: {
        'url': 'https://crackstube.blog/anko-dango-near-me',
        'sentences': [
            'After exploring tech and business topics, take a quick break and explore our <a href="https://crackstube.blog/anko-dango-near-me" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Anko Dango Japanese food guide</a> for authentic culinary treats.',
            'For food lovers and journalists writing about Japanese cultural cuisine, check out our <a href="https://crackstube.blog/anko-dango-near-me" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Anko Dango sweet dumplings guide</a> for localized culinary reporting.',
            'If you enjoy discovering international dessert trends and regional flavors, read our feature on <a href="https://crackstube.blog/anko-dango-near-me" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Anko Dango recipe and origins</a>.'
        ]
    },
    2: {
        'url': 'https://crackstube.blog/brumeblog-com-review',
        'sentences': [
            'If you enjoy discovering independent lifestyle publications and tech reviews, read our <a href="https://crackstube.blog/brumeblog-com-review" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">BrumeBlog tech review article</a> analyzing online content channels.',
            'For an in-depth review of independent blog networks and publishing platforms, view our <a href="https://crackstube.blog/brumeblog-com-review" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">BrumeBlog digital publishing guide</a>.',
            'To explore how modern independent media blogs format tech news, check out our <a href="https://crackstube.blog/brumeblog-com-review" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">BrumeBlog portal analysis</a>.'
        ]
    },
    3: {
        'url': 'https://crackstube.blog/clickfor-net',
        'sentences': [
            'When analyzing new publishing sites, comparing domain structures is essential; review our <a href="https://crackstube.blog/clickfor-net" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Clickfor Net platform guide</a> for domain safety and publishing standards.',
            'To compare domain trust signals across different online platforms, consult our <a href="https://crackstube.blog/clickfor-net" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Clickfor Net digital review</a> for domain safety evaluation.',
            'For readers exploring utility platforms and web service verification, check out our <a href="https://crackstube.blog/clickfor-net" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Clickfor Net domain safety check</a>.'
        ]
    },
    4: {
        'url': 'https://crackstube.blog/crackstube-alternatives',
        'sentences': [
            'For users experiencing unexpected script errors across web media utilities, browse our <a href="https://crackstube.blog/crackstube-alternatives" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">CracksTube alternative platforms list</a> to compare reliable choices.',
            'Users researching online utility portals often compare web service choices; explore our <a href="https://crackstube.blog/crackstube-alternatives" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">CracksTube alternative site recommendations</a> to evaluate safe media choices.',
            'For readers interested in discovering secondary web tools and media utilities, browse our <a href="https://crackstube.blog/crackstube-alternatives" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">CracksTube alternatives guide</a>.'
        ]
    },
    5: {
        'url': 'https://crackstube.blog/crackstube-everything-explained',
        'sentences': [
            'To learn more about how online media hubs syndicate lifestyle and entertainment content, check out our <a href="https://crackstube.blog/crackstube-everything-explained" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">CracksTube platform explained guide</a>.',
            'Before selecting third-party alternatives, understand how the main platform is structured by reading our comprehensive <a href="https://crackstube.blog/crackstube-everything-explained" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">CracksTube digital streaming details</a>.',
            'To gain full transparency into how multi-category content hubs manage user data and streaming features, explore our <a href="https://crackstube.blog/crackstube-everything-explained" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">CracksTube comprehensive portal guide</a>.'
        ]
    },
    6: {
        'url': 'https://crackstube.blog/droven.io-enterprise-tech-innovation',
        'sentences': [
            'To understand how enterprise artificial intelligence, cloud architecture, and automation drive business growth, read our detailed <a href="https://crackstube.blog/droven.io-enterprise-tech-innovation" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Droven.io enterprise tech innovation guide</a>.',
            'Organizations evaluating modern cloud migration and zero-trust security frameworks should examine our <a href="https://crackstube.blog/droven.io-enterprise-tech-innovation" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Droven.io enterprise technology insights</a>.',
            'For a practical analysis of practical AI adoption, machine learning pipelines, and digital transformation strategy, check out our <a href="https://crackstube.blog/droven.io-enterprise-tech-innovation" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Droven.io AI enterprise solutions</a> breakdown.'
        ]
    },
    7: {
        'url': 'https://crackstube.blog/glorvix-com',
        'sentences': [
            'Digital content creators evaluating tech platforms can also read our <a href="https://crackstube.blog/glorvix-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Glorvix information hub overview</a> to compare modern content architecture.',
            'To see how modern media portals organize digital content feeds, read our <a href="https://crackstube.blog/glorvix-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Glorvix technology portal details</a> covering online publishing architecture.',
            'To compare modern tech news hubs with general news platforms, examine our <a href="https://crackstube.blog/glorvix-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Glorvix site trust review</a>.'
        ]
    },
    8: {
        'url': 'https://crackstube.blog/hrms-globex',
        'sentences': [
            'While general web tools focus on public content, administrative portals handle corporate access; read our <a href="https://crackstube.blog/hrms-globex" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">HRMS Globex portal information</a> for enterprise system details.',
            'While public tech portals publish general information, enterprise systems manage secure data; examine our <a href="https://crackstube.blog/hrms-globex" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">HRMS Globex portal guide</a> for organization management tools.',
            'Individuals navigating secure login portals and administrative tools should review our <a href="https://crackstube.blog/hrms-globex" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">HRMS Globex employee system breakdown</a> for workforce software analysis.'
        ]
    },
    9: {
        'url': 'https://crackstube.blog/is-charfen-co-uk-legit',
        'sentences': [
            'When visiting unfamiliar media portals, assessing security signals is critical; inspect our <a href="https://crackstube.blog/is-charfen-co-uk-legit" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Charfen.co.uk website safety assessment</a> for trust score evaluation guidelines.',
            'When accessing enterprise portals, verifying website security signals is vital; review our <a href="https://crackstube.blog/is-charfen-co-uk-legit" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Charfen.co.uk Legit Review</a> for domain trust assessment methods.',
            'When discovering new online blogs, verifying site security is essential; see our <a href="https://crackstube.blog/is-charfen-co-uk-legit" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Charfen.co.uk domain credibility check</a> for full domain background details.'
        ]
    },
    10: {
        'url': 'https://crackstube.blog/modcityusa-com-guide',
        'sentences': [
            'If this error code appears while running modified applications or custom digital tools, check out our <a href="https://crackstube.blog/modcityusa-com-guide" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">ModCityUSA community details</a> for troubleshooting user software setups.',
            'Users seeking interactive media utilities and gaming mod networks can check out our <a href="https://crackstube.blog/modcityusa-com-guide" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">ModCityUSA modding community overview</a>.',
            'When evaluating specialized web portals and user communities, compare trust factors using our <a href="https://crackstube.blog/modcityusa-com-guide" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">ModCityUSA platform analysis</a> covering online network safety.'
        ]
    },
    11: {
        'url': 'https://crackstube.blog/pressvibepulse-com',
        'sentences': [
            'Beyond local sweet shops, readers tracking food trends and digital news can explore our <a href="https://crackstube.blog/pressvibepulse-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">PressVibePulse news platform details</a> for trending media coverage.',
            'Readers interested in trending news channels and online press platforms can view our <a href="https://crackstube.blog/pressvibepulse-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">PressVibePulse news platform overview</a>.',
            'Modding enthusiasts looking for breaking tech news and media updates can read our <a href="https://crackstube.blog/pressvibepulse-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">PressVibePulse media channel review</a>.'
        ]
    },
    12: {
        'url': 'https://crackstube.blog/quikconsole-com',
        'sentences': [
            'For creators focused specifically on gaming portals and interactive media, consult our <a href="https://crackstube.blog/quikconsole-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">QuikConsole gaming insights</a> for performance strategies.',
            'For insights into system performance tuning and portal loading speeds, check out our <a href="https://crackstube.blog/quikconsole-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">QuikConsole gaming platform guide</a>.',
            'Readers tracking gaming industry headlines can also check out our <a href="https://crackstube.blog/quikconsole-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">QuikConsole hardware advice</a> for console news and performance tips.'
        ]
    },
    13: {
        'url': 'https://crackstube.blog/serp-insight-guest-post',
        'sentences': [
            'To improve search visibility and authority for new web projects, consult our <a href="https://crackstube.blog/serp-insight-guest-post" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">SERP Insight guest post publishing guide</a> for content outreach tips.',
            'Domain owners seeking to build legitimate editorial trust and search authority can consult our <a href="https://crackstube.blog/serp-insight-guest-post" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">SERP Insight guest post overview</a>.',
            'Gaming site owners looking to publish tech content and increase domain authority should explore our <a href="https://crackstube.blog/serp-insight-guest-post" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">SERP Insight content outreach guide</a>.'
        ]
    },
    14: {
        'url': 'https://crackstube.blog/serp-insight-link-insertion',
        'sentences': [
            'Website operators building media aggregation platforms can also review our <a href="https://crackstube.blog/serp-insight-link-insertion" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">SERP Insight link insertion strategy</a> for backlink optimization techniques.',
            'Web developers managing online forums or mod repositories can benefit from our <a href="https://crackstube.blog/serp-insight-link-insertion" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">SERP Insight link insertion guide</a> for search visibility.',
            'In addition to publishing full guest articles, digital marketers should review our <a href="https://crackstube.blog/serp-insight-link-insertion" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">SERP Insight backlink optimization</a> strategies.'
        ]
    },
    15: {
        'url': 'https://crackstube.blog/techsized-com',
        'sentences': [
            'When researching digital platforms, verifying domain authority is essential; explore our <a href="https://crackstube.blog/techsized-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">TechSized platform evaluation details</a> for domain trust analysis.',
            'For insights into how tech blogs structure news content and maintain editorial quality, read our <a href="https://crackstube.blog/techsized-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">TechSized website trust review</a>.',
            'When placing contextual links across technology sites, evaluating domain quality is vital; explore our <a href="https://crackstube.blog/techsized-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">TechSized publishing standards guide</a> for publisher trust criteria.'
        ]
    },
    16: {
        'url': 'https://crackstube.blog/techyhittools-org',
        'sentences': [
            'To explore automated web tools and social media utility services, read our breakdown on <a href="https://crackstube.blog/techyhittools-org" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">TechyHitTools web utility guide</a>.',
            'To streamline site management and social engagement automation for gaming hubs, consult our <a href="https://crackstube.blog/techyhittools-org" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">TechyHitTools SEO utility details</a>.',
            'Tech enthusiasts looking for automated web utilities can check out our <a href="https://crackstube.blog/techyhittools-org" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">TechyHitTools automated tools analysis</a> for feature reviews.'
        ]
    },
    17: {
        'url': 'https://crackstube.blog/thealitekeepsafe-com',
        'sentences': [
            'To ensure corporate data safety and prevent privacy leaks during login, consult our <a href="https://crackstube.blog/thealitekeepsafe-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">TheAliteKeepSafe safety platform details</a>.',
            'When acquiring backlinks on external sites, checking domain security is essential; see our <a href="https://crackstube.blog/thealitekeepsafe-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">TheAliteKeepSafe platform guide</a> for site safety analysis.',
            'When using online automation tools, verifying web security is critical; read our <a href="https://crackstube.blog/thealitekeepsafe-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">TheAliteKeepSafe security breakdown</a> for security practices.'
        ]
    },
    18: {
        'url': 'https://crackstube.blog/vocalnewsmedia-com',
        'sentences': [
            'For further comparative analysis on digital publishing credibility, examine our <a href="https://crackstube.blog/vocalnewsmedia-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">VocalNewsMedia news platform guide</a>.',
            'Marketers building links on news syndication platforms can also read our <a href="https://crackstube.blog/vocalnewsmedia-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">VocalNewsMedia content platform read</a> for press outreach strategies.',
            'Online safety applies to news reading and publishing portals as well; inspect our <a href="https://crackstube.blog/vocalnewsmedia-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">VocalNewsMedia publishing analysis</a> for digital media security standards.'
        ]
    },
    19: {
        'url': 'https://crackstube.blog/yonosamachar-com',
        'sentences': [
            'To stay informed about broader digital service portals and online news updates, explore our <a href="https://crackstube.blog/yonosamachar-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">YonoSamachar portal details</a>.',
            'Readers following online service portals and news platforms can also examine our <a href="https://crackstube.blog/yonosamachar-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">YonoSamachar banking portal information</a>.',
            'Readers following online news syndication and digital updates can also check out our <a href="https://crackstube.blog/yonosamachar-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">YonoSamachar news coverage breakdown</a> for financial news updates.'
        ]
    },
    20: {
        'url': 'https://crackstube.blog/zavalio-com',
        'sentences': [
            'To discover broader media coverage including online lifestyle and cultural trends, visit our <a href="https://crackstube.blog/zavalio-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Zavalio lifestyle portal guide</a>.',
            'Content creators utilizing web utilities for social media growth can also explore our <a href="https://crackstube.blog/zavalio-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Zavalio lifestyle platform review</a> for lifestyle media trends.',
            'Readers looking for general news and lifestyle trends beyond banking portals can check out our <a href="https://crackstube.blog/zavalio-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Zavalio media trends report</a>.'
        ]
    }
}

# Track usage of sentence variants per target article
target_incoming_count = {i: 0 for i in range(21)}

N = 21

for i in range(N):
    fname = articles[i]
    if not os.path.exists(fname):
        print(f"Error: {fname} missing")
        continue

    # Determine 3 target article indices for article i
    target_early_idx = (i + 1) % N
    target_mid_idx = (i + 4) % N
    target_late_idx = (i + 10) % N

    # Get target sentences
    s_early_sent = link_pool[target_early_idx]['sentences'][target_incoming_count[target_early_idx] % 3]
    target_incoming_count[target_early_idx] += 1

    s_mid_sent = link_pool[target_mid_idx]['sentences'][target_incoming_count[target_mid_idx] % 3]
    target_incoming_count[target_mid_idx] += 1

    s_late_sent = link_pool[target_late_idx]['sentences'][target_incoming_count[target_late_idx] % 3]
    target_incoming_count[target_late_idx] += 1

    p_early_html = f'\n\n        <p>{s_early_sent}</p>'
    p_mid_html = f'\n\n        <p>{s_mid_sent}</p>'
    p_late_html = f'\n\n        <p>{s_late_sent}</p>'

    with open(fname, 'r', encoding='utf-8') as fp:
        content = fp.read()

    m_art = re.search(r'<article[^>]*>', content, re.IGNORECASE)
    art_start = m_art.end()
    art_end = content.find('</article>', art_start)

    head_part = content[:art_start]
    art_content = content[art_start:art_end]
    tail_part = content[art_end:]

    h2_matches = list(re.finditer(r'<h2[^>]*>', art_content, re.IGNORECASE))
    p_ends = [m.end() for m in re.finditer(r'</p>', art_content, re.IGNORECASE)]

    if len(h2_matches) >= 3:
        h2_1 = h2_matches[0].end()
        h2_mid = h2_matches[len(h2_matches) // 2].end()
        h2_last = h2_matches[-1].end()

        pos_early = next((p for p in p_ends if p > h2_1), p_ends[1] if len(p_ends) > 1 else p_ends[0])
        pos_middle = next((p for p in p_ends if p > h2_mid), p_ends[len(p_ends)//2])
        pos_late = next((p for p in p_ends if p > h2_last), p_ends[-1])
    else:
        pos_early = p_ends[1] if len(p_ends) > 1 else p_ends[0]
        pos_middle = p_ends[len(p_ends)//2]
        pos_late = p_ends[-2] if len(p_ends) > 2 else p_ends[-1]

    # Perform insertions from highest offset to lowest offset!
    insertions = [(pos_late, p_late_html), (pos_middle, p_mid_html), (pos_early, p_early_html)]
    insertions.sort(key=lambda x: x[0], reverse=True)

    for pos, text in insertions:
        art_content = art_content[:pos] + text + art_content[pos:]

    full_new = head_part + art_content + tail_part
    with open(fname, 'w', encoding='utf-8') as fp:
        fp.write(full_new)
    print(f"Applied 3 distributed links to {fname}")

# Sync subfolders
subfolders = [
    ('is-charfen-co-uk-legit.html', 'Is-charfen-co-uk-Legit/index.html'),
    ('droven.io-enterprise-tech-innovation.html', 'droven.io-enterprise-tech-innovation/index.html'),
    ('techsized-com.html', 'Techsized-com/index.html'),
    ('thealitekeepsafe-com.html', 'thealitekeepsafe-com/index.html')
]

for src_file, sub_file in subfolders:
    if os.path.exists(src_file) and os.path.exists(os.path.dirname(sub_file)):
        with open(src_file, 'r', encoding='utf-8') as fp:
            root_html = fp.read()
        sub_html = root_html.replace('href="css/style.css"', 'href="/css/style.css"') \
                            .replace('src="images/', 'src="/images/') \
                            .replace('href="favicon', 'href="/favicon"') \
                            .replace('src="js/main.js"', 'src="/js/main.js"')
        with open(sub_file, 'w', encoding='utf-8') as fp:
            fp.write(sub_html)
        print(f"Synced {sub_file}")

print("\n--- LINKING COMPLETE ---")
