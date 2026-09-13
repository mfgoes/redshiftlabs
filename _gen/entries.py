# -*- coding: utf-8 -*-
ENTRIES = [
  {
    "slug": "making-survival-matter",
    "title": "Making Survival Matter",
    "date": "Sep 13, 2026",
    "read": "5 min read",
    "author": "Mischa",
    "teaser": "The early food loop gets a big overhaul — Food Fabricator becomes an emergency fallback, Hydroponics Bay ties long-term survival to a real supply line, plus a continued pixel-art UI pass across the whole interface.",
    "body": '''
			<p class="mb-4">This week I’ve been making survival a little less automatic.</p>

			<img class="img-fluid rounded mb-4" src="images/devlog-images/colony-base-day1.png" alt="Kosmograd colony base with HUD and colonist dialogue">

			<h5>Food &amp; Logistics</h5>
			<p class="mb-3">The early food loop has had a pretty big overhaul:</p>
			<ul class="mb-3">
				<li>Food Fabricator is now an emergency solution — lower output, higher mineral cost.</li>
				<li>Hydroponics Bay provides sustainable food, but requires Cryo Shards from a hazardous crater biome.</li>
				<li>Food can spoil when you exceed your cold-storage capacity.</li>
				<li>Cold Store gives you more capacity and lets you prepare for difficult periods.</li>
			</ul>
			<p class="mb-4">So the early game now becomes a choice between buying time and building a proper supply chain.</p>

			<h5>Smoother Opening</h5>
			<p class="mb-3">A few changes should make the first minutes less frustrating:</p>
			<ul class="mb-4">
				<li>Contacting Earth now works with a free hail from the Comms Center.</li>
				<li>Initial lander rations give the crew some breathing room.</li>
				<li>Workers are better at recovering when construction sites are unreachable.</li>
				<li>HUD/tooltips make storage and spoilage easier to understand.</li>
			</ul>

			<h5>More Personality</h5>
			<p class="mb-3">I’ve also continued the pixel-art UI pass across the pause menu, save/load screens, quests, building panels and colonist priorities.</p>
			<p class="mb-3">Colonists now have expressive portraits, and the HUD has a much stronger visual identity.</p>
			<p class="mb-4">Still in progress: storms, crises, day/night visuals, biome zones, and the consequences of losing colonists.</p>

			<p class="mb-0"><em>The goal: survival should never be automatic — but every problem should have a readable, satisfying solution.</em></p>
'''
  },
  {
    "slug": "quest-system-planning",
    "title": "Quest System Planning",
    "date": "Dec 13, 2025",
    "read": "3 min read",
    "author": "Mischa (with Claude)",
    "teaser": "A goal-driven progression layer for the colony's next phase. Objectives now unlock new buildings as rewards, replacing idle waiting with a clear sense of progress.",
    "body": '''
			<p class="mb-4">Planned comprehensive quest system to solve core engagement issues and transform gameplay from passive waiting into goal-driven progression.</p>

			<h5>The Problem</h5>
			<ul class="mb-4">
				<li>Players had "nothing to do while waiting for resources"</li>
				<li>Building system felt "too free" - could build anything anywhere</li>
				<li>No sense of progression or accomplishment</li>
			</ul>

			<h5>Design Philosophy</h5>
			<p class="mb-3">Inspired by <strong>Terrafactor</strong> (quest-gated unlocks), <strong>Factorio</strong> (production milestones), and <strong>Stronghold</strong> (mission objectives), the quest system will provide clear objectives and unlock buildings as rewards.</p>

			<h5>Quest Progression</h5>
			<ol class="mb-4">
				<li><strong>First Light:</strong> Build 2 Solar Panels → unlocks Battery</li>
				<li><strong>Through the Night:</strong> Survive until Day 2 → unlocks Food Fabricator</li>
				<li><strong>Colony Nutrition:</strong> Produce 30 Food → unlocks Comms Center</li>
				<li><strong>Earth Contact:</strong> Order supply drop → unlocks Pressure Dome</li>
				<li><strong>Lunar Permanence:</strong> Survive 7 days with 3+ colonists → Victory!</li>
			</ol>

			<h5>Technical Architecture</h5>
			<ul class="mb-4">
				<li><strong>QuestManager:</strong> Tracks quest status, progress, and triggers unlocks</li>
				<li><strong>Quest Panel UI:</strong> Side panel showing active objective and rewards</li>
				<li><strong>Comms Center:</strong> New building for ordering supply drops from Earth</li>
				<li><strong>Building locks:</strong> Only starter buildings available, rest unlocked via quests</li>
			</ul>

			<p class="mb-0"><em>Target: 7-day implementation sprint. This system is critical for establishing a clear gameplay loop and sense of accomplishment.</em></p>
'''
  },
  {
    "slug": "food-survival-system",
    "title": "Food & Survival System",
    "date": "Nov 16, 2025",
    "read": "4 min read",
    "author": "Mischa (with Claude)",
    "teaser": "Colonist survival stats turn the stockpile into a meaningful decision. Stronghold-style food mechanics track hunger per colonist, so a shortage has real consequences.",
    "body": '''
			<p class="mb-4">Implemented Stronghold-style food mechanics and individual survival stats to create a compelling survival loop for Kosmograd.</p>

			<img class="img-fluid rounded mb-4" src="https://i.imgur.com/wo6xADv.gif" alt="">

			<h5>Food System</h5>
			<ul class="mb-4">
				<li>Global consumption: 10 food/colonist/day from stockpile</li>
				<li>If sufficient food → colonists eat, hunger resets</li>
				<li>If insufficient → nobody eats, health/morale decline begins</li>
			</ul>

			<h5>Survival Stats (UnitDetails.gd)</h5>
			<ul class="mb-4">
				<li><strong>Hunger:</strong> Depletes 33%/day without food, critical at day 3</li>
				<li><strong>Health:</strong> Master stat, damaged by starvation (-34/day) and oxygen loss (-20/min)</li>
				<li><strong>Morale:</strong> Crashes during starvation (-40/day), slow decay otherwise (-2/day)</li>
			</ul>

			<h5>Death &amp; Game Over</h5>
			<ul class="mb-4">
				<li>Colonists die at 0 health</li>
				<li>Game over screen shows death causes by type (starvation, oxygen deprivation)</li>
			</ul>

			<h5>UI Improvements</h5>
			<ul class="mb-4">
				<li>Day counter tracks current sol</li>
				<li>Resource panel displays consumption rates (e.g., "Food: 500 (-30/day)")</li>
				<li>Unit details panel ready for stat visualization</li>
				<li>Debug key ']' to skip days for testing</li>
			</ul>

			<p class="mb-0"><em>Timeline example: 500 food + 3 colonists = starvation begins ~day 17, deaths ~day 21</em></p>
'''
  },
  {
    "slug": "oxygen-consumption-system",
    "title": "Oxygen Consumption System",
    "date": "Nov 15, 2025",
    "read": "3 min read",
    "author": "Mischa",
    "teaser": "Pressure zones and aluminium upkeep create immediate environmental risk. Buildings now consume oxygen locally, so a single failure can cascade fast.",
    "body": '''
			<p class="mb-4">Added atmospheric pressure zones to buildings with aluminium-based oxygen generation, creating a critical resource management layer.</p>

			<img src="https://i.imgur.com/vkWi1L7.jpeg" alt="Oxygen system UI" class="img-fluid rounded mb-4">

			<h5>Oxygen System</h5>
			<ul class="mb-4">
				<li><strong>Renamed zones:</strong> InsideZone → PressureZone across all buildings</li>
				<li><strong>Aluminium consumption:</strong> Buildings with pressure zones consume aluminium to maintain oxygen</li>
				<li><strong>Zone failure:</strong> Oxygen zones fail when aluminium depleted (collision disabled)</li>
				<li><strong>Immediate danger:</strong> Units inside failed zones start losing oxygen immediately</li>
			</ul>

			<h5>Building Details Panel</h5>
			<ul class="mb-4">
				<li>Shows oxygen consumption: "Generates oxygen zone. Cost: 1 alu/10s"</li>
				<li>Displays oxygen status (Active/FAILING) for pressure zone buildings</li>
				<li>Updated power display formatting for cleaner units</li>
				<li>ResourcesLabel repurposed for oxygen info display</li>
			</ul>

			<h5>Design Improvements</h5>
			<ul class="mb-4">
				<li>Made building UI panel larger to accommodate oxygen and power information</li>
				<li>Better visual hierarchy for critical system status</li>
			</ul>

			<p class="mb-0"><em>This system creates tension between expansion and resource management - every pressurized building needs constant aluminium supply to keep colonists alive.</em></p>
'''
  },
  {
    "slug": "game-direction-technical-overview",
    "title": "Game Direction &amp; Technical Overview",
    "date": "Oct 28, 2025",
    "read": "2 min read",
    "author": "Mischa",
    "teaser": "Created a comprehensive design document to establish the game's vision, core mechanics, and technical architecture before building further.",
    "body": '''
			<p class="mb-4">Created comprehensive CLAUDE.md document to establish the game's vision, core mechanics, and technical architecture.</p>

			<div class="mb-4">
				<audio controls style="width: 100%;">
					<source src="audio/Track 1 Moon.mp3" type="audio/mpeg">
					Your browser does not support the audio element.
				</audio>
			</div>

			<h5>Game Vision</h5>
			<ul class="mb-4">
				<li>Soviet lunar colony management with 1970s aesthetic and Cold War tension</li>
				<li>Focus on survival, resource scarcity, and tough moral decisions</li>
				<li><strong>Inspired by classics:</strong> Stronghold Crusader's economic chains and castle-building, RimWorld's emergent storytelling and colonist management</li>
				<li>Every decision matters: balance expansion vs. survival, production vs. consumption, safety vs. efficiency</li>
				<li><strong>Estimated price:</strong> 15 EUR at launch</li>
				<li>Target platform: Steam (PC), January 2026 demo release</li>
			</ul>

			<h5>Core Mechanics Documented</h5>
			<ul class="mb-4">
				<li><strong>Resource management:</strong> Minerals, food, power, oxygen, aluminium</li>
				<li><strong>Building systems:</strong> Placement, power grids, production chains</li>
				<li><strong>Unit systems:</strong> Worker assignment, survival stats, pathfinding</li>
				<li><strong>Day/night cycle:</strong> 24-hour sol system for pacing</li>
			</ul>

			<h5>Technical Stack</h5>
			<ul class="mb-4">
				<li>Engine: Godot 4.4</li>
				<li>Language: GDScript</li>
				<li>Architecture: Scene-based with singleton managers</li>
				<li>UI: Custom panels with real-time stat tracking</li>
			</ul>

			<p class="mb-0"><em>This document serves as the development north star - defining scope, mechanics, and technical decisions to keep the project focused during solo development.</em></p>
'''
  },
]
