import os

card_html = """
        <!-- Published Blog Card: Droven.io Enterprise Tech Innovation (NEW) -->
        <article class="category-card" style="padding:0; overflow:hidden;">
          <div style="aspect-ratio:16/9; overflow:hidden; background:#e2e8f0;">
            <a href="droven.io-enterprise-tech-innovation.html">
              <img src="images/droven-io-enterprise-tech-guide.webp" alt="Droven.io Enterprise Tech Innovation banner showing modern digital dashboard and AI cloud network" style="width:100%; height:100%; object-fit:cover; transition:transform 0.3s ease;" loading="lazy" decoding="async">
            </a>
          </div>
          <div style="padding:1.5rem; display:flex; flex-direction:column; gap:0.75rem; flex-grow:1;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="background:rgba(2, 132, 199, 0.1); color:var(--accent-cyan); font-weight:700; font-size:0.75rem; padding:0.25rem 0.75rem; border-radius:var(--radius-full); text-transform:uppercase;">Technology</span>
              <span style="color:var(--text-muted); font-size:0.8rem;">Sep 9, 2026</span>
            </div>
            <h3 style="font-size:1.15rem; margin:0; line-height:1.35;">
              <a href="droven.io-enterprise-tech-innovation.html" style="color:var(--text-main);">Droven.io Enterprise Tech Innovation: A Practical Guide to Modern Business Technology</a>
            </h3>
            <p style="font-size:0.9rem; color:var(--text-muted); margin:0; line-height:1.5;">
              Explore Droven.io enterprise tech innovation, AI tools, machine learning, cloud computing, cybersecurity, automation, and digital business transformation.
            </p>
            <a href="droven.io-enterprise-tech-innovation.html" style="color:var(--accent-cyan); font-weight:600; font-size:0.9rem; margin-top:auto;">Read Article &#8594;</a>
          </div>
        </article>
"""

# Update tech.html
with open('tech.html', 'r', encoding='utf-8') as f:
    tech_content = f.read()
if 'droven.io-enterprise-tech-innovation.html' not in tech_content:
    tech_content = tech_content.replace('<div id="tech-blog-feed" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:2rem;">', '<div id="tech-blog-feed" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:2rem;">' + card_html)
    with open('tech.html', 'w', encoding='utf-8') as f:
        f.write(tech_content)
    print("Added card to tech.html!")

# Update blogs.html
with open('blogs.html', 'r', encoding='utf-8') as f:
    blogs_content = f.read()
if 'droven.io-enterprise-tech-innovation.html' not in blogs_content:
    blogs_content = blogs_content.replace('<div id="blog-feed-container" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:2rem;">', '<div id="blog-feed-container" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:2rem;">' + card_html)
    with open('blogs.html', 'w', encoding='utf-8') as f:
        f.write(blogs_content)
    print("Added card to blogs.html!")

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()
if 'droven.io-enterprise-tech-innovation.html' not in index_content:
    index_content = index_content.replace('<div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:2rem;">', '<div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:2rem;">' + card_html, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("Added card to index.html!")

# Update sitemap.xml
sitemap_urls = """  <url>
    <loc>http://crackstube.blog/droven.io-enterprise-tech-innovation.html</loc>
    <lastmod>2026-09-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>http://crackstube.blog/droven.io-enterprise-tech-innovation/</loc>
    <lastmod>2026-09-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
"""

with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap_content = f.read()
if 'droven.io-enterprise-tech-innovation' not in sitemap_content:
    sitemap_content = sitemap_content.replace('</urlset>', sitemap_urls + '</urlset>')
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    print("Added URLs to sitemap.xml!")

print("All card listings updated!")
