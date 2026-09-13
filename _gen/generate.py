# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from entries import ENTRIES

ROOT = os.path.expanduser("~/mnt/redshiftlabs")

PAGE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">

	<!-- SEO Meta Tags -->
	<title>{title_plain} | Devlog | Redshift Labs</title>
	<meta name="description" content="{teaser}">
	<meta name="author" content="Redshift Labs">
	<meta name="robots" content="index, follow">
	<link rel="canonical" href="https://mfgoes.github.io/redshiftlabs/devlog-{slug}.html">

	<!-- Open Graph -->
	<meta property="og:type" content="article">
	<meta property="og:site_name" content="Redshift Labs">
	<meta property="og:title" content="{title_plain}">
	<meta property="og:description" content="{teaser}">
	<meta property="og:url" content="https://mfgoes.github.io/redshiftlabs/devlog-{slug}.html">

	<!-- Favicon -->
	<link rel="icon" type="image/x-icon" href="images/moon_icon.png">

	<!-- Google Fonts - Orbitron -->
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

	<!-- Bootstrap CSS -->
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
	<link rel="stylesheet" href="css/main.css">
	<link rel="stylesheet" href="css/devlog-styles.css">
	<link rel="stylesheet" href="css/kosmograd.css">
</head>
<body class="bg-dark text-white dark-mode">

	<!-- Navbar Component -->
	<div id="navbar-container"></div>

	<!-- Devlog Post Header -->
	<section class="py-5 kg-hero">
		<div class="container">
			<a href="devlog.html" class="kg-text-link mb-3 d-inline-block">&larr; All devlogs</a>
			<p class="kg-kicker mb-2">Kosmograd / field record</p>
			<h1 class="rl-hero-title mb-2" style="font-size: clamp(1.75rem, 4.5vw, 2.75rem); text-align: left;">{title}</h1>
			<p class="hero-subtitle mb-0">{date} &middot; {read} &middot; {author}</p>
		</div>
	</section>

	<!-- Devlog Post -->
	<section class="kg-page-shell kg-devlog-section">
		<div class="container">
			<div class="row">
				<!-- Main Content -->
				<div class="col-lg-8">
					<article class="devlog-entry kg-devlog-entry kg-devlog-entry--solo">
						<div class="devlog-content">
{body}
						</div>

						<div class="devlog-footer d-flex justify-content-between align-items-center flex-wrap gap-2">
							<span>
								<img src="images/moon_icon.png" alt="{author}" style="width: 20px; height: 20px; border-radius: 50%; object-fit: cover; margin-right: 6px; vertical-align: middle;">
								<small class="text-muted">{author}</small>
							</span>
							<a href="https://mischa.itch.io/kosmograd/devlog" target="_blank" rel="noopener noreferrer" class="kg-text-link" style="font-size: .85rem;">Also on itch.io &#8599;</a>
						</div>
					</article>

					<nav class="article-navigation">
{prevnext}
					</nav>
				</div>

				<!-- Sidebar -->
				<div class="col-lg-4">
					<aside class="kg-devlog-rail sticky-top" style="top: 2rem;">

						<!-- About -->
						<div class="kg-rail-block">
							<p class="kg-label mb-2">Transmission</p>
							<p class="kg-copy mb-2">A Soviet lunar colony RTS built solo in Godot.</p>
							<a href="index.html" class="kg-text-link">Return to mission control</a>
						</div>

						<!-- More posts -->
						<div class="kg-rail-block">
							<h2 class="kg-rail-title mb-3">More posts</h2>
							<div class="d-flex flex-column gap-3">
{more_posts}
							</div>
						</div>

						<!-- Bluesky Feed -->
						<div class="kg-rail-block">
							<h2 class="kg-rail-title mb-3">Follow development</h2>
								<div class="d-flex flex-column gap-2">
									<a href="https://bsky.app/profile/mishotofu.bsky.social" class="kg-text-link">Bluesky</a>
									<a href="https://x.com/MishoWave" class="kg-text-link">X / Twitter</a>
									<a href="https://store.steampowered.com/app/387060/Earth_Overclocked/" class="kg-text-link">Previous game</a>
								</div>
						</div>

					</aside>
				</div>
			</div>
		</div>
	</section>

	<!-- Footer Component -->
	<div id="footer-container"></div>

	<!-- Bootstrap JS -->
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

	<!-- Component Loader -->
	<script src="js/ComponentLoader.js"></script>
	<script src="js/navbar-init.js"></script>
</body>
</html>
'''

def strip_tags(s):
    import re
    return re.sub('<[^<]+?>', '', s)

n = len(ENTRIES)
for i, e in enumerate(ENTRIES):
    title_plain = strip_tags(e["title"])

    # Prev/next: index 0 is newest. "Newer" = i-1, "Older" = i+1
    parts = []
    if i + 1 < n:
        older = ENTRIES[i+1]
        parts.append(
            '\t\t\t\t\t\t<a href="devlog-%s.html" class="article-nav-link">'
            '<span class="article-nav-label">Older</span>'
            '<span class="article-nav-title">%s</span></a>' % (older["slug"], strip_tags(older["title"]))
        )
    if i - 1 >= 0:
        newer = ENTRIES[i-1]
        parts.append(
            '\t\t\t\t\t\t<a href="devlog-%s.html" class="article-nav-link next">'
            '<span class="article-nav-label">Newer</span>'
            '<span class="article-nav-title">%s</span></a>' % (newer["slug"], strip_tags(newer["title"]))
        )
    prevnext = "\n".join(parts) if parts else ""

    more_links = []
    for j, o in enumerate(ENTRIES):
        if j == i:
            continue
        more_links.append(
            '\t\t\t\t\t\t\t\t<a href="devlog-%s.html" class="kg-text-link d-flex justify-content-between gap-2">'
            '<span>%s</span><span class="kg-dispatch-meta" style="padding-top:0;">%s</span></a>'
            % (o["slug"], strip_tags(o["title"]), o["date"])
        )
    more_posts = "\n".join(more_links)

    html = PAGE_TEMPLATE.format(
        title_plain=title_plain,
        title=e["title"],
        slug=e["slug"],
        date=e["date"],
        read=e["read"],
        author=e["author"],
        teaser=e["teaser"],
        body=e["body"].rstrip("\n"),
        prevnext=prevnext,
        more_posts=more_posts,
    )

    out_path = os.path.join(ROOT, "devlog-%s.html" % e["slug"])
    with open(out_path, "w") as f:
        f.write(html)
    print("wrote", out_path)
