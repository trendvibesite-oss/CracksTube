import os
import re

data = {
    '418dsg7-error.html': {
        'early': ('https://crackstube.blog/modcityusa-com-guide', 'ModCityUSA community details',
                  'If this error code appears while running modified applications or custom digital tools, check out our <a href="https://crackstube.blog/modcityusa-com-guide" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">ModCityUSA community details</a> for troubleshooting user software setups.'),
        'middle': ('https://crackstube.blog/crackstube-alternatives', 'CracksTube alternative platforms list',
                   'For users experiencing unexpected script errors across web media utilities, browse our <a href="https://crackstube.blog/crackstube-alternatives" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">CracksTube alternative platforms list</a> to compare reliable web streaming choices.'),
        'late': ('https://crackstube.blog/anko-dango-near-me', 'Anko Dango Japanese food guide',
                 'After resolving system errors and browser glitches, take a quick break and explore our <a href="https://crackstube.blog/anko-dango-near-me" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Anko Dango Japanese food guide</a> for popular cultural culinary treats.')
    },
    'anko-dango-near-me.html': {
        'early': ('https://crackstube.blog/pressvibepulse-com', 'PressVibePulse news platform details',
                  'Beyond local sweet shops, readers tracking food trends and digital news can explore our <a href="https://crackstube.blog/pressvibepulse-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">PressVibePulse news platform details</a> for trending media coverage.'),
        'middle': ('https://crackstube.blog/brumeblog-com-review', 'BrumeBlog tech review article',
                   'If you enjoy discovering independent lifestyle publications and culinary reviews, read our <a href="https://crackstube.blog/brumeblog-com-review" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">BrumeBlog tech review article</a> analyzing online content channels.'),
        'late': ('https://crackstube.blog/crackstube-everything-explained', 'CracksTube platform explained guide',
                 'To learn more about how online media hubs syndicate lifestyle and entertainment content, check out our <a href="https://crackstube.blog/crackstube-everything-explained" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">CracksTube platform explained guide</a>.')
    },
    'brumeblog-com-review.html': {
        'early': ('https://crackstube.blog/clickfor-net', 'Clickfor Net platform guide',
                  'When analyzing new publishing sites, comparing domain structures is essential; review our <a href="https://crackstube.blog/clickfor-net" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Clickfor Net platform guide</a> for domain safety and publishing standards.'),
        'middle': ('https://crackstube.blog/glorvix-com', 'Glorvix information hub overview',
                   'Digital content creators evaluating tech platforms can also read our <a href="https://crackstube.blog/glorvix-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Glorvix information hub overview</a> to compare modern content architecture.'),
        'late': ('https://crackstube.blog/quikconsole-com', 'QuikConsole gaming insights',
                 'For creators focused specifically on gaming portals and interactive media, consult our <a href="https://crackstube.blog/quikconsole-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">QuikConsole gaming insights</a> for performance strategies.')
    },
    'clickfor-net.html': {
        'early': ('https://crackstube.blog/crackstube-alternatives', 'CracksTube alternative site recommendations',
                  'Users researching online utility portals often compare web service choices; explore our <a href="https://crackstube.blog/crackstube-alternatives" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">CracksTube alternative site recommendations</a> to evaluate safe media choices.'),
        'middle': ('https://crackstube.blog/hrms-globex', 'HRMS Globex portal information',
                   'While general web tools focus on public content, administrative portals handle corporate access; read our <a href="https://crackstube.blog/hrms-globex" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">HRMS Globex portal information</a> for enterprise system details.'),
        'late': ('https://crackstube.blog/serp-insight-guest-post', 'SERP Insight guest post publishing guide',
                 'To improve search visibility and authority for new web projects, consult our <a href="https://crackstube.blog/serp-insight-guest-post" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">SERP Insight guest post publishing guide</a> for content outreach tips.')
    },
    'crackstube-alternatives.html': {
        'early': ('https://crackstube.blog/crackstube-everything-explained', 'CracksTube digital streaming details',
                  'Before selecting third-party alternatives, understand how the main platform is structured by reading our comprehensive <a href="https://crackstube.blog/crackstube-everything-explained" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">CracksTube digital streaming details</a>.'),
        'middle': ('https://crackstube.blog/is-charfen-co-uk-legit', 'Charfen.co.uk website safety assessment',
                   'When visiting unfamiliar media portals, assessing security signals is critical; inspect our <a href="https://crackstube.blog/is-charfen-co-uk-legit" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Charfen.co.uk website safety assessment</a> for trust score evaluation guidelines.'),
        'late': ('https://crackstube.blog/serp-insight-link-insertion', 'SERP Insight link insertion strategy',
                 'Website operators building media aggregation platforms can also review our <a href="https://crackstube.blog/serp-insight-link-insertion" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">SERP Insight link insertion strategy</a> for backlink optimization techniques.')
    },
    'crackstube-everything-explained.html': {
        'early': ('https://crackstube.blog/glorvix-com', 'Glorvix technology portal details',
                  'To see how modern media portals organize digital content feeds, read our <a href="https://crackstube.blog/glorvix-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Glorvix technology portal details</a> covering online publishing architecture.'),
        'middle': ('https://crackstube.blog/modcityusa-com-guide', 'ModCityUSA modding community overview',
                   'Users seeking interactive media utilities and gaming mod networks can check out our <a href="https://crackstube.blog/modcityusa-com-guide" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">ModCityUSA modding community overview</a>.'),
        'late': ('https://crackstube.blog/techsized-com', 'TechSized platform evaluation details',
                 'When researching digital platforms, verifying domain authority is essential; explore our <a href="https://crackstube.blog/techsized-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">TechSized platform evaluation details</a> for domain trust analysis.')
    },
    'glorvix-com.html': {
        'early': ('https://crackstube.blog/hrms-globex', 'HRMS Globex portal guide',
                  'While public tech portals publish general information, enterprise systems manage secure data; examine our <a href="https://crackstube.blog/hrms-globex" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">HRMS Globex portal guide</a> for organization management tools.'),
        'middle': ('https://crackstube.blog/pressvibepulse-com', 'PressVibePulse news platform overview',
                   'Readers interested in trending news channels and online press platforms can view our <a href="https://crackstube.blog/pressvibepulse-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">PressVibePulse news platform overview</a>.'),
        'late': ('https://crackstube.blog/techyhittools-org', 'TechyHitTools web utility guide',
                 'To explore automated web tools and social media utility services, read our breakdown on <a href="https://crackstube.blog/techyhittools-org" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">TechyHitTools web utility guide</a>.')
    },
    'hrms-globex.html': {
        'early': ('https://crackstube.blog/is-charfen-co-uk-legit', 'Charfen.co.uk Legit Review',
                  'When accessing enterprise portals, verifying website security signals is vital; review our <a href="https://crackstube.blog/is-charfen-co-uk-legit" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Charfen.co.uk Legit Review</a> for domain trust assessment methods.'),
        'middle': ('https://crackstube.blog/quikconsole-com', 'QuikConsole gaming platform guide',
                   'For insights into system performance tuning and portal loading speeds, check out our <a href="https://crackstube.blog/quikconsole-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">QuikConsole gaming platform guide</a>.'),
        'late': ('https://crackstube.blog/thealitekeepsafe-com', 'TheAliteKeepSafe safety platform details',
                 'To ensure corporate data safety and prevent privacy leaks during login, consult our <a href="https://crackstube.blog/thealitekeepsafe-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">TheAliteKeepSafe safety platform details</a>.')
    },
    'is-charfen-co-uk-legit.html': {
        'early': ('https://crackstube.blog/modcityusa-com-guide', 'ModCityUSA community details',
                  'When evaluating specialized web portals and user communities, compare trust factors using our <a href="https://crackstube.blog/modcityusa-com-guide" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">ModCityUSA community details</a> covering online network safety.'),
        'middle': ('https://crackstube.blog/serp-insight-guest-post', 'SERP Insight guest post overview',
                   'Domain owners seeking to build legitimate editorial trust and search authority can consult our <a href="https://crackstube.blog/serp-insight-guest-post" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">SERP Insight guest post overview</a>.'),
        'late': ('https://crackstube.blog/vocalnewsmedia-com', 'VocalNewsMedia news platform guide',
                 'For further comparative analysis on digital publishing credibility, examine our <a href="https://crackstube.blog/vocalnewsmedia-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">VocalNewsMedia news platform guide</a>.')
    },
    'modcityusa-com-guide.html': {
        'early': ('https://crackstube.blog/pressvibepulse-com', 'PressVibePulse news platform details',
                  'Modding enthusiasts looking for breaking tech news and media updates can read our <a href="https://crackstube.blog/pressvibepulse-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">PressVibePulse news platform details</a>.'),
        'middle': ('https://crackstube.blog/serp-insight-link-insertion', 'SERP Insight link insertion guide',
                   'Web developers managing online forums or mod repositories can benefit from our <a href="https://crackstube.blog/serp-insight-link-insertion" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">SERP Insight link insertion guide</a> for search visibility.'),
        'late': ('https://crackstube.blog/yonosamachar-com', 'YonoSamachar portal details',
                 'To stay informed about broader digital service portals and online news updates, explore our <a href="https://crackstube.blog/yonosamachar-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">YonoSamachar portal details</a>.')
    },
    'pressvibepulse-com.html': {
        'early': ('https://crackstube.blog/quikconsole-com', 'QuikConsole gaming insights',
                  'Readers tracking gaming industry headlines can also check out our <a href="https://crackstube.blog/quikconsole-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">QuikConsole gaming insights</a> for console news and hardware advice.'),
        'middle': ('https://crackstube.blog/techsized-com', 'TechSized website trust review',
                   'For insights into how tech blogs structure news content and maintain editorial quality, read our <a href="https://crackstube.blog/techsized-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">TechSized website trust review</a>.'),
        'late': ('https://crackstube.blog/zavalio-com', 'Zavalio lifestyle portal guide',
                 'To discover broader media coverage including online lifestyle and cultural trends, visit our <a href="https://crackstube.blog/zavalio-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Zavalio lifestyle portal guide</a>.')
    },
    'quikconsole-com.html': {
        'early': ('https://crackstube.blog/serp-insight-guest-post', 'SERP Insight guest post publishing guide',
                  'Gaming site owners looking to publish tech content and increase domain authority should explore our <a href="https://crackstube.blog/serp-insight-guest-post" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">SERP Insight guest post publishing guide</a>.'),
        'middle': ('https://crackstube.blog/techyhittools-org', 'TechyHitTools SEO utility details',
                   'To streamline site management and social engagement automation for gaming hubs, consult our <a href="https://crackstube.blog/techyhittools-org" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">TechyHitTools SEO utility details</a>.'),
        'late': ('https://crackstube.blog/418dsg7-error', '418dsg7 error troubleshooting guide',
                 'If you encounter unexpected system error prompts while running web console tools, refer to our <a href="https://crackstube.blog/418dsg7-error" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">418dsg7 error troubleshooting guide</a> for step-by-step solutions.')
    },
    'serp-insight-guest-post.html': {
        'early': ('https://crackstube.blog/serp-insight-link-insertion', 'SERP Insight link insertion strategy',
                  'In addition to publishing full guest articles, digital marketers should review our <a href="https://crackstube.blog/serp-insight-link-insertion" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">SERP Insight link insertion strategy</a> for contextual backlinking.'),
        'middle': ('https://crackstube.blog/thealitekeepsafe-com', 'TheAliteKeepSafe platform guide',
                   'When acquiring backlinks on external sites, checking domain security is essential; see our <a href="https://crackstube.blog/thealitekeepsafe-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">TheAliteKeepSafe platform guide</a> for site safety analysis.'),
        'late': ('https://crackstube.blog/anko-dango-near-me', 'Anko Dango sweet dumplings guide',
                 'For SEO agencies working on local search optimization for food and lifestyle niches, check out our <a href="https://crackstube.blog/anko-dango-near-me" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Anko Dango sweet dumplings guide</a> for localized content examples.')
    },
    'serp-insight-link-insertion.html': {
        'early': ('https://crackstube.blog/techsized-com', 'TechSized website trust review',
                  'When placing contextual links across technology sites, evaluating domain quality is vital; explore our <a href="https://crackstube.blog/techsized-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">TechSized website trust review</a> for publisher trust criteria.'),
        'middle': ('https://crackstube.blog/vocalnewsmedia-com', 'VocalNewsMedia content platform read',
                   'Marketers building links on news syndication platforms can also read our <a href="https://crackstube.blog/vocalnewsmedia-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">VocalNewsMedia content platform read</a> for press outreach strategies.'),
        'late': ('https://crackstube.blog/brumeblog-com-review', 'BrumeBlog digital publishing guide',
                 'For an in-depth review of independent blog networks and publishing platforms, view our <a href="https://crackstube.blog/brumeblog-com-review" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">BrumeBlog digital publishing guide</a>.')
    },
    'techsized-com.html': {
        'early': ('https://crackstube.blog/techyhittools-org', 'TechyHitTools web utility guide',
                  'Tech enthusiasts looking for automated web utilities can check out our <a href="https://crackstube.blog/techyhittools-org" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">TechyHitTools web utility guide</a> for tool feature reviews.'),
        'middle': ('https://crackstube.blog/yonosamachar-com', 'YonoSamachar banking portal information',
                   'Readers following online service portals and news platforms can also examine our <a href="https://crackstube.blog/yonosamachar-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">YonoSamachar banking portal information</a>.'),
        'late': ('https://crackstube.blog/clickfor-net', 'Clickfor Net digital review',
                 'To compare domain trust signals across different online platforms, consult our <a href="https://crackstube.blog/clickfor-net" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Clickfor Net digital review</a> for domain safety evaluation.')
    },
    'techyhittools-org.html': {
        'early': ('https://crackstube.blog/thealitekeepsafe-com', 'TheAliteKeepSafe safety platform details',
                  'When using online automation tools, verifying web security is critical; read our <a href="https://crackstube.blog/thealitekeepsafe-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">TheAliteKeepSafe safety platform details</a> for security practices.'),
        'middle': ('https://crackstube.blog/zavalio-com', 'Zavalio lifestyle platform review',
                   'Content creators utilizing web utilities for social media growth can also explore our <a href="https://crackstube.blog/zavalio-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Zavalio lifestyle platform review</a> for lifestyle media trends.'),
        'late': ('https://crackstube.blog/crackstube-alternatives', 'CracksTube alternative platforms list',
                 'For users interested in discovering secondary web tools and media utilities, browse our <a href="https://crackstube.blog/crackstube-alternatives" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">CracksTube alternative platforms list</a>.')
    },
    'thealitekeepsafe-com.html': {
        'early': ('https://crackstube.blog/vocalnewsmedia-com', 'VocalNewsMedia news platform guide',
                  'Online safety applies to news reading and publishing portals as well; inspect our <a href="https://crackstube.blog/vocalnewsmedia-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">VocalNewsMedia news platform guide</a> for digital media security standards.'),
        'middle': ('https://crackstube.blog/418dsg7-error', '418dsg7 error code details',
                   'If digital security tools flag unusual browser errors or server codes during navigation, see our <a href="https://crackstube.blog/418dsg7-error" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">418dsg7 error code details</a> for troubleshooting.'),
        'late': ('https://crackstube.blog/crackstube-everything-explained', 'CracksTube platform explained guide',
                 'To learn more about how online media hubs maintain digital security and user protection, read our <a href="https://crackstube.blog/crackstube-everything-explained" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">CracksTube platform explained guide</a>.')
    },
    'vocalnewsmedia-com.html': {
        'early': ('https://crackstube.blog/yonosamachar-com', 'YonoSamachar portal details',
                  'Readers following online news syndication and digital updates can also check out our <a href="https://crackstube.blog/yonosamachar-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">YonoSamachar portal details</a> for financial news coverage.'),
        'middle': ('https://crackstube.blog/anko-dango-near-me', 'Anko Dango Japanese food guide',
                   'For journalists and content creators writing about cultural food trends, explore our <a href="https://crackstube.blog/anko-dango-near-me" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Anko Dango Japanese food guide</a> for localized culinary reporting.'),
        'late': ('https://crackstube.blog/glorvix-com', 'Glorvix information hub overview',
                 'To compare modern tech news hubs with general news platforms, examine our <a href="https://crackstube.blog/glorvix-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Glorvix information hub overview</a>.')
    },
    'yonosamachar-com.html': {
        'early': ('https://crackstube.blog/zavalio-com', 'Zavalio lifestyle portal guide',
                  'Readers looking for general news and lifestyle trends beyond banking portals can check out our <a href="https://crackstube.blog/zavalio-com" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Zavalio lifestyle portal guide</a>.'),
        'middle': ('https://crackstube.blog/brumeblog-com-review', 'BrumeBlog tech review article',
                   'To explore how independent digital publishers cover tech and business news, read our <a href="https://crackstube.blog/brumeblog-com-review" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">BrumeBlog tech review article</a>.'),
        'late': ('https://crackstube.blog/hrms-globex', 'HRMS Globex portal guide',
                 'Individuals navigating secure login portals and administrative portals should also review our <a href="https://crackstube.blog/hrms-globex" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">HRMS Globex portal guide</a> for enterprise access security.')
    },
    'zavalio-com.html': {
        'early': ('https://crackstube.blog/418dsg7-error', '418dsg7 error code details',
                  'If you encounter unexpected browser errors while reading digital blogs, consult our <a href="https://crackstube.blog/418dsg7-error" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">418dsg7 error code details</a> for troubleshooting solutions.'),
        'middle': ('https://crackstube.blog/clickfor-net', 'Clickfor Net digital review',
                   'For readers interested in exploring online web utility platforms, review our <a href="https://crackstube.blog/clickfor-net" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Clickfor Net digital review</a> for domain analysis.'),
        'late': ('https://crackstube.blog/is-charfen-co-uk-legit', 'Charfen.co.uk website safety assessment',
                 'When discovering new online blogs, verifying site security is essential; see our <a href="https://crackstube.blog/is-charfen-co-uk-legit" style="color:var(--accent-cyan); font-weight:600; text-decoration:underline;">Charfen.co.uk website safety assessment</a> for domain trust evaluation.')
    }
}

for fname, info in data.items():
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
    print(f'Successfully distributed 3 links across article body in {fname}!')

# Update Is-charfen-co-uk-Legit/index.html
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
