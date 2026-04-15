# city_data.py — Atlas Roofing & Restoration
# Master city data for hyper-local SEO page generation
# Each entry: slug, display name, ZIP, county, housing_era, landmarks, streets, neighbors, notes

CITIES = [

  # ── TIER 1 — Core service area ──────────────────────────────────────────────

  {
    "slug": "beachwood",
    "name": "Beachwood",
    "state": "OH",
    "zip": "44122",
    "county": "Cuyahoga County",
    "housing_era": "1950s–1980s",
    "landmarks": ["Beachwood Place Mall", "Beachwood City Schools", "Beachwood Community Center", "Legacy Village (nearby)"],
    "streets": ["Richmond Road", "Cedar Road", "Chagrin Boulevard", "Shaker Boulevard", "Green Road"],
    "neighbors": ["Pepper Pike", "Shaker Heights", "South Euclid", "Lyndhurst", "Orange"],
    "notes": "Atlas Roofing's home base. Many ranch and colonial homes from the 1960s–70s on large wooded lots. HOA communities common.",
    "review": {
      "text": "I asked them to take a look at my roof based on my home inspection report. They were very honest when inspecting and only recommended the exact work that needed to be done, and nothing more.",
      "author": "Benjamin Kaplan",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "shaker-heights",
    "name": "Shaker Heights",
    "state": "OH",
    "zip": "44120",
    "county": "Cuyahoga County",
    "housing_era": "1920s–1950s",
    "landmarks": ["Shaker Square", "Van Aken District", "Shaker Heights High School", "Horseshoe Lake Park"],
    "streets": ["Van Aken Boulevard", "South Woodland Road", "Fairmount Boulevard", "Chagrin Boulevard", "Lee Road"],
    "neighbors": ["Cleveland Heights", "University Heights", "Beachwood", "Pepper Pike", "East Cleveland"],
    "notes": "Historic Tudor, Colonial, and English-style homes. Many roofs are 30–50+ years old and original to the home. Strict architectural review board standards.",
    "review": {
      "text": "Quick and professional roofing service. Great communication throughout the entire process and left a very clean job site.",
      "author": "Tawn Kramer",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "cleveland-heights",
    "name": "Cleveland Heights",
    "state": "OH",
    "zip": "44118",
    "county": "Cuyahoga County",
    "housing_era": "1920s–1950s",
    "landmarks": ["Cedar-Lee Theatre", "Taylor Road Corridor", "Forest Hill Park", "Heights Arts"],
    "streets": ["Cedar Road", "Lee Road", "Taylor Road", "Mayfield Road", "South Taylor Road"],
    "neighbors": ["University Heights", "Shaker Heights", "East Cleveland", "South Euclid", "Lyndhurst"],
    "notes": "Dense urban suburb with lots of older Colonial, Tudor, and Cape Cod homes. Many roofs are original or were last replaced in the 1980s–90s.",
    "review": {
      "text": "Showed the highest level of professionalism from start to finish. Great price and I never felt taken advantage of.",
      "author": "Joseph Reichman",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "university-heights",
    "name": "University Heights",
    "state": "OH",
    "zip": "44118",
    "county": "Cuyahoga County",
    "housing_era": "1930s–1960s",
    "landmarks": ["John Carroll University", "Gesu Catholic Church", "Cedar Road shopping district"],
    "streets": ["Cedar Road", "Warrensville Center Road", "Silsby Road", "Kenilworth Road", "Fenwick Road"],
    "neighbors": ["Cleveland Heights", "South Euclid", "Lyndhurst", "Shaker Heights"],
    "notes": "Quiet residential suburb with well-kept Colonial and brick homes. Many properties approaching 60–80 years old — prime candidates for roof replacement.",
    "review": {
      "text": "I asked them to take a look at my roof based on my home inspection report. They were very honest when inspecting and only recommended the exact work that needed to be done.",
      "author": "Benjamin Kaplan",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "south-euclid",
    "name": "South Euclid",
    "state": "OH",
    "zip": "44121",
    "county": "Cuyahoga County",
    "housing_era": "1940s–1970s",
    "landmarks": ["South Euclid Community Center", "Anderson's General Store area", "Bexley Park"],
    "streets": ["Mayfield Road", "South Green Road", "Argonne Road", "Anderson Road", "Belvoir Boulevard"],
    "neighbors": ["Lyndhurst", "University Heights", "Cleveland Heights", "Beachwood", "Highland Heights"],
    "notes": "Mix of Cape Cod, Colonial, and ranch-style homes. Many homes built post-WWII — roofs are frequently original or overdue for replacement.",
    "review": {
      "text": "What a divine appointment — I love my new roof and would highly recommend Atlas Roofing to anyone in the area.",
      "author": "Lorna Joy Larkin",
      "source": "South Euclid, OH · Google Review"
    }
  },
  {
    "slug": "lyndhurst",
    "name": "Lyndhurst",
    "state": "OH",
    "zip": "44124",
    "county": "Cuyahoga County",
    "housing_era": "1940s–1970s",
    "landmarks": ["Legacy Village", "Lyndhurst Community Center", "Notre Dame-Cathedral Latin School"],
    "streets": ["Mayfield Road", "Richmond Road", "Lyndhurst Drive", "Murwood Drive", "Sunview Road"],
    "neighbors": ["South Euclid", "Beachwood", "Highland Heights", "Willoughby Hills", "Gates Mills"],
    "notes": "Primarily single-family ranch and colonial homes from the mid-century era. Strong community pride — homeowners take exterior appearance seriously.",
    "review": {
      "text": "Quick and professional roofing service. Great communication throughout the entire process and left a very clean job site.",
      "author": "Tawn Kramer",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "pepper-pike",
    "name": "Pepper Pike",
    "state": "OH",
    "zip": "44124",
    "county": "Cuyahoga County",
    "housing_era": "1960s–1990s",
    "landmarks": ["Orange High School area", "Pepper Pike City Club", "Lander Circle shopping"],
    "streets": ["Lander Road", "Fairmount Boulevard", "Pinetree Road", "Chagrin Boulevard", "South Woodland Road"],
    "neighbors": ["Orange", "Beachwood", "Moreland Hills", "Lyndhurst", "Gates Mills"],
    "notes": "Affluent suburb with large custom homes on wooded lots. Many homes have complex rooflines and premium shingle requirements. High-value jobs.",
    "review": {
      "text": "Showed the highest level of professionalism from start to finish. Great price and I never felt taken advantage of.",
      "author": "Joseph Reichman",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "highland-heights",
    "name": "Highland Heights",
    "state": "OH",
    "zip": "44143",
    "county": "Cuyahoga County",
    "housing_era": "1960s–1990s",
    "landmarks": ["Hillcrest Hospital area", "Bishop Boardman High School", "Highland Heights Community Park"],
    "streets": ["Wilson Mills Road", "Beta Drive", "Highland Road", "Miner Road", "Bishop Road"],
    "neighbors": ["Lyndhurst", "Mayfield Heights", "Mayfield Village", "South Euclid", "Richmond Heights"],
    "notes": "Suburban community with mix of ranch homes and newer construction. Many homeowners are long-term residents whose roofs are reaching end of life.",
    "review": {
      "text": "Quick and professional roofing service. Great communication throughout the entire process and left a very clean job site.",
      "author": "Tawn Kramer",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "mayfield-heights",
    "name": "Mayfield Heights",
    "state": "OH",
    "zip": "44124",
    "county": "Cuyahoga County",
    "housing_era": "1950s–1980s",
    "landmarks": ["Eastgate Shopping Center", "Mayfield Heights City Hall", "Hillcrest Hospital"],
    "streets": ["Mayfield Road", "SOM Center Road", "Beta Drive", "Eastgate Road", "Lander Road"],
    "neighbors": ["Lyndhurst", "Highland Heights", "Mayfield Village", "South Euclid", "Richmond Heights"],
    "notes": "Active suburb with many post-war ranches and split-levels. Hillcrest area sees heavy foot traffic and homeowners are value-conscious.",
    "review": {
      "text": "I asked them to take a look at my roof based on my home inspection report. They were very honest when inspecting and only recommended the exact work that needed to be done.",
      "author": "Benjamin Kaplan",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "richmond-heights",
    "name": "Richmond Heights",
    "state": "OH",
    "zip": "44143",
    "county": "Cuyahoga County",
    "housing_era": "1950s–1980s",
    "landmarks": ["Richmond Mall area", "Richmond Heights Community Center", "Richmond Heights Local Schools"],
    "streets": ["Wilson Mills Road", "Richmond Road", "Highland Road", "Glendale Road", "Chardon Road"],
    "neighbors": ["Highland Heights", "Mayfield Heights", "South Euclid", "Euclid", "Wickliffe"],
    "notes": "Affordable suburban community with many ranch homes. Common storm damage from Lake Erie weather systems. Insurance claims are frequent.",
    "review": {
      "text": "What a divine appointment — I love my new roof and would highly recommend Atlas Roofing to anyone in the area.",
      "author": "Lorna Joy Larkin",
      "source": "South Euclid, OH · Google Review"
    }
  },
  {
    "slug": "orange",
    "name": "Orange",
    "state": "OH",
    "zip": "44022",
    "county": "Cuyahoga County",
    "housing_era": "1970s–2000s",
    "landmarks": ["Orange City Schools", "Pinecrest development (nearby)", "Chagrin Valley area"],
    "streets": ["Chagrin Boulevard", "Harvard Road", "Miles Road", "Lander Road", "Som Center Road"],
    "neighbors": ["Pepper Pike", "Moreland Hills", "Beachwood", "Chagrin Falls", "Solon"],
    "notes": "Upscale suburb with large newer homes. Homeowners prioritize quality and aesthetics — premium shingle and warranty upgrades are common.",
    "review": {
      "text": "Showed the highest level of professionalism from start to finish. Great price and I never felt taken advantage of.",
      "author": "Joseph Reichman",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "solon",
    "name": "Solon",
    "state": "OH",
    "zip": "44139",
    "county": "Cuyahoga County",
    "housing_era": "1970s–2000s",
    "landmarks": ["Solon Community Park", "Solon City Schools", "Solon Center for the Arts", "SOM Center Road corridor"],
    "streets": ["SOM Center Road", "Aurora Road", "Bainbridge Road", "Harper Road", "Pettibone Road"],
    "neighbors": ["Orange", "Chagrin Falls", "Twinsburg", "Aurora", "Moreland Hills"],
    "notes": "Fast-growing suburb with newer subdivisions and older ranch communities. Mix of homeowners — younger families and long-term residents both active.",
    "review": {
      "text": "Quick and professional roofing service. Great communication throughout the entire process and left a very clean job site.",
      "author": "Tawn Kramer",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "chagrin-falls",
    "name": "Chagrin Falls",
    "state": "OH",
    "zip": "44022",
    "county": "Cuyahoga County",
    "housing_era": "1880s–1960s",
    "landmarks": ["Chagrin Falls Village", "Triangle Park", "Chagrin River waterfall", "Main Street shops"],
    "streets": ["Main Street", "Bell Street", "Miles Road", "Washington Street", "Maple Street"],
    "neighbors": ["Orange", "Solon", "Moreland Hills", "Bainbridge", "Russell Township"],
    "notes": "Charming historic village with older Victorian, Colonial, and craftsman homes. Many original or early-replacement roofs. Architectural character is important to homeowners.",
    "review": {
      "text": "I asked them to take a look at my roof based on my home inspection report. They were very honest when inspecting and only recommended the exact work that needed to be done.",
      "author": "Benjamin Kaplan",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "woodmere",
    "name": "Woodmere",
    "state": "OH",
    "zip": "44122",
    "county": "Cuyahoga County",
    "housing_era": "1950s–1980s",
    "landmarks": ["Pinecrest area", "Chagrin Boulevard corridor", "Village of Woodmere"],
    "streets": ["Chagrin Boulevard", "Richmond Road", "Green Road", "Shaker Boulevard"],
    "neighbors": ["Beachwood", "Orange", "Pepper Pike", "Warrensville Heights"],
    "notes": "Small village with well-maintained homes. Close proximity to Beachwood commercial corridor. Homeowners tend to be long-term residents.",
    "review": {
      "text": "What a divine appointment — I love my new roof and would highly recommend Atlas Roofing to anyone in the area.",
      "author": "Lorna Joy Larkin",
      "source": "South Euclid, OH · Google Review"
    }
  },
  {
    "slug": "moreland-hills",
    "name": "Moreland Hills",
    "state": "OH",
    "zip": "44022",
    "county": "Cuyahoga County",
    "housing_era": "1960s–1990s",
    "landmarks": ["Chagrin Valley area", "Orange City Schools", "South Chagrin Reservation"],
    "streets": ["Chagrin Boulevard", "Lander Road", "Solon Road", "Bentleyville Road", "Miles Road"],
    "neighbors": ["Pepper Pike", "Orange", "Chagrin Falls", "Solon", "Hunting Valley"],
    "notes": "Affluent township with large estate homes on multi-acre lots. Premium exterior materials are expected. High-ticket roofing jobs common.",
    "review": {
      "text": "Showed the highest level of professionalism from start to finish. Great price and I never felt taken advantage of.",
      "author": "Joseph Reichman",
      "source": "Northeast Ohio · Google Review"
    }
  },

  # ── TIER 2 — Mid-range suburbs ───────────────────────────────────────────────

  {
    "slug": "parma",
    "name": "Parma",
    "state": "OH",
    "zip": "44129",
    "county": "Cuyahoga County",
    "housing_era": "1940s–1970s",
    "landmarks": ["Parmatown Mall area", "Parma City Hall", "Veterans Memorial Park", "Ridge Road corridor"],
    "streets": ["Ridge Road", "State Road", "Broadview Road", "Pleasant Valley Road", "Stumph Road"],
    "neighbors": ["Parma Heights", "Brooklyn", "Seven Hills", "Independence", "Garfield Heights"],
    "notes": "One of Ohio's largest suburbs. Dense with 1950s–60s ranch homes — many are on their second or third roof. Value-oriented buyers who compare multiple quotes.",
    "review": {
      "text": "Quick and professional roofing service. Great communication throughout the entire process and left a very clean job site.",
      "author": "Tawn Kramer",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "parma-heights",
    "name": "Parma Heights",
    "state": "OH",
    "zip": "44130",
    "county": "Cuyahoga County",
    "housing_era": "1950s–1970s",
    "landmarks": ["Parma Heights City Hall", "Shady Lake Park", "Pearl Road corridor"],
    "streets": ["Pearl Road", "York Road", "Stumph Road", "Huffman Road", "West Ridgewood Drive"],
    "neighbors": ["Parma", "Middleburg Heights", "Seven Hills", "North Royalton", "Broadview Heights"],
    "notes": "Compact suburb next to Parma. Older ranch homes with brick facades common. Many homeowners are retirees maintaining long-held homes.",
    "review": {
      "text": "I asked them to take a look at my roof based on my home inspection report. They were very honest when inspecting and only recommended the exact work that needed to be done.",
      "author": "Benjamin Kaplan",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "seven-hills",
    "name": "Seven Hills",
    "state": "OH",
    "zip": "44131",
    "county": "Cuyahoga County",
    "housing_era": "1950s–1980s",
    "landmarks": ["Seven Hills City Hall", "Hillside Park", "Broadview Road corridor"],
    "streets": ["Broadview Road", "Hillside Road", "Royalview Drive", "Crossview Road", "Pleasant Valley Road"],
    "neighbors": ["Parma", "Independence", "Parma Heights", "North Royalton", "Broadview Heights"],
    "notes": "Hilly suburb south of Parma. Mix of colonial and split-level homes. Lake Erie storms funnel through the valley — hail damage is common.",
    "review": {
      "text": "What a divine appointment — I love my new roof and would highly recommend Atlas Roofing to anyone in the area.",
      "author": "Lorna Joy Larkin",
      "source": "South Euclid, OH · Google Review"
    }
  },
  {
    "slug": "independence",
    "name": "Independence",
    "state": "OH",
    "zip": "44131",
    "county": "Cuyahoga County",
    "housing_era": "1960s–1990s",
    "landmarks": ["Independence City Hall", "The Flats area access", "Rockside Road business corridor", "I-77 interchange"],
    "streets": ["Rockside Road", "Brecksville Road", "East Bagley Road", "Hillside Road", "Selig Drive"],
    "neighbors": ["Seven Hills", "Parma", "Garfield Heights", "Cuyahoga Heights", "Brecksville"],
    "notes": "Strong business community and upscale residential. Newer construction mixed with 1970s–80s colonials. Both residential and commercial roofing opportunities.",
    "review": {
      "text": "Showed the highest level of professionalism from start to finish. Great price and I never felt taken advantage of.",
      "author": "Joseph Reichman",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "north-royalton",
    "name": "North Royalton",
    "state": "OH",
    "zip": "44133",
    "county": "Cuyahoga County",
    "housing_era": "1970s–2000s",
    "landmarks": ["North Royalton City Hall", "Royalton Road corridor", "North Royalton High School"],
    "streets": ["Royalton Road", "Broadview Road", "Bennett Road", "Akins Road", "State Road"],
    "neighbors": ["Parma Heights", "Seven Hills", "Broadview Heights", "Brecksville", "Strongsville"],
    "notes": "Growing suburb with strong residential activity. Mix of established older neighborhoods and newer subdivisions. Many homeowners comparing roofing contractors.",
    "review": {
      "text": "Quick and professional roofing service. Great communication throughout the entire process and left a very clean job site.",
      "author": "Tawn Kramer",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "broadview-heights",
    "name": "Broadview Heights",
    "state": "OH",
    "zip": "44147",
    "county": "Cuyahoga County",
    "housing_era": "1970s–2000s",
    "landmarks": ["Broadview Heights City Hall", "Broadview Road corridor", "Cuyahoga Valley National Park proximity"],
    "streets": ["Broadview Road", "Royalton Road", "Center Road", "East Wallings Road", "Nagle Road"],
    "neighbors": ["North Royalton", "Parma Heights", "Brecksville", "Seven Hills", "Strongsville"],
    "notes": "Newer suburban development with large colonials and split-levels. Active housing market — real estate transactions often trigger roof inspections.",
    "review": {
      "text": "I asked them to take a look at my roof based on my home inspection report. They were very honest when inspecting and only recommended the exact work that needed to be done.",
      "author": "Benjamin Kaplan",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "strongsville",
    "name": "Strongsville",
    "state": "OH",
    "zip": "44136",
    "county": "Cuyahoga County",
    "housing_era": "1970s–2000s",
    "landmarks": ["SouthPark Mall", "Strongsville City Center", "Strongsville High School", "Bagley Road corridor"],
    "streets": ["Pearl Road", "Royalton Road", "Bagley Road", "Prospect Road", "Howe Road"],
    "neighbors": ["North Royalton", "Broadview Heights", "Middleburg Heights", "Brunswick", "North Olmsted"],
    "notes": "One of Cuyahoga County's fastest growing suburbs. Active homebuilding with newer subdivisions alongside 1980s–90s ranches. High demand for roofing services.",
    "review": {
      "text": "What a divine appointment — I love my new roof and would highly recommend Atlas Roofing to anyone in the area.",
      "author": "Lorna Joy Larkin",
      "source": "South Euclid, OH · Google Review"
    }
  },
  {
    "slug": "garfield-heights",
    "name": "Garfield Heights",
    "state": "OH",
    "zip": "44125",
    "county": "Cuyahoga County",
    "housing_era": "1930s–1960s",
    "landmarks": ["Garfield Heights City Hall", "Elmwood Park", "Turney Road corridor"],
    "streets": ["Turney Road", "Granger Road", "Garfield Boulevard", "Maple Heights Road", "Broadway Avenue"],
    "neighbors": ["Maple Heights", "Bedford Heights", "Warrensville Heights", "Independence", "Parma"],
    "notes": "Older inner-ring suburb with many Depression-era and post-WWII homes. Roofs are frequently overdue — this is strong replacement territory.",
    "review": {
      "text": "Showed the highest level of professionalism from start to finish. Great price and I never felt taken advantage of.",
      "author": "Joseph Reichman",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "maple-heights",
    "name": "Maple Heights",
    "state": "OH",
    "zip": "44137",
    "county": "Cuyahoga County",
    "housing_era": "1930s–1960s",
    "landmarks": ["Maple Heights High School", "Rockside Road area", "Maple Heights City Hall"],
    "streets": ["Dunham Road", "Rockside Road", "Broadway Avenue", "Lee Road", "Warrensville Center Road"],
    "neighbors": ["Garfield Heights", "Bedford Heights", "Warrensville Heights", "Bedford", "South Euclid"],
    "notes": "Dense inner-ring suburb. Many bungalow and cape cod homes built 60–90 years ago. Insurance claims and full replacements are both common.",
    "review": {
      "text": "Quick and professional roofing service. Great communication throughout the entire process and left a very clean job site.",
      "author": "Tawn Kramer",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "bedford",
    "name": "Bedford",
    "state": "OH",
    "zip": "44146",
    "county": "Cuyahoga County",
    "housing_era": "1920s–1960s",
    "landmarks": ["Bedford City Hall", "Bedford Reservation", "Broadway shopping corridor"],
    "streets": ["Broadway Avenue", "Northfield Road", "Willis Street", "Center Road", "Dunham Road"],
    "neighbors": ["Bedford Heights", "Maple Heights", "Walton Hills", "Glenwillow", "Solon"],
    "notes": "Historic suburb with many older homes. Bedford Reservation nearby creates heavy tree canopy — moss and debris buildup on roofs is common.",
    "review": {
      "text": "I asked them to take a look at my roof based on my home inspection report. They were very honest when inspecting and only recommended the exact work that needed to be done.",
      "author": "Benjamin Kaplan",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "bedford-heights",
    "name": "Bedford Heights",
    "state": "OH",
    "zip": "44128",
    "county": "Cuyahoga County",
    "housing_era": "1950s–1980s",
    "landmarks": ["Randall Park area", "Northfield Road corridor", "Bedford Heights City Hall"],
    "streets": ["Northfield Road", "Rockside Road", "Forbes Road", "Libby Road", "Dunham Road"],
    "neighbors": ["Warrensville Heights", "Bedford", "Maple Heights", "Garfield Heights", "North Randall"],
    "notes": "Mix of residential and light commercial. Many older ranch homes. Active storm damage area — insurance claims are common.",
    "review": {
      "text": "What a divine appointment — I love my new roof and would highly recommend Atlas Roofing to anyone in the area.",
      "author": "Lorna Joy Larkin",
      "source": "South Euclid, OH · Google Review"
    }
  },
  {
    "slug": "warrensville-heights",
    "name": "Warrensville Heights",
    "state": "OH",
    "zip": "44128",
    "county": "Cuyahoga County",
    "housing_era": "1950s–1980s",
    "landmarks": ["Warrensville Heights City Hall", "Emery Road corridor", "South Green Road"],
    "streets": ["Emery Road", "Chagrin Boulevard", "Warrensville Center Road", "Harvard Road", "Lee Road"],
    "neighbors": ["Beachwood", "Orange", "Bedford Heights", "Maple Heights", "North Randall"],
    "notes": "Suburban community with many mid-century homes. Close to Beachwood — many homeowners familiar with Atlas from Beachwood neighbors.",
    "review": {
      "text": "Showed the highest level of professionalism from start to finish. Great price and I never felt taken advantage of.",
      "author": "Joseph Reichman",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "euclid",
    "name": "Euclid",
    "state": "OH",
    "zip": "44117",
    "county": "Cuyahoga County",
    "housing_era": "1920s–1960s",
    "landmarks": ["Euclid Beach area", "Lake Shore Boulevard corridor", "Euclid Square area", "Lakeshore Park"],
    "streets": ["Lake Shore Boulevard", "Euclid Avenue", "Chardon Road", "East 222nd Street", "Babbitt Road"],
    "neighbors": ["Wickliffe", "Richmond Heights", "South Euclid", "East Cleveland", "Willoughby"],
    "notes": "Lakefront community with many older bungalows and colonials. Proximity to Lake Erie means heavier ice dam and wind damage exposure.",
    "review": {
      "text": "Quick and professional roofing service. Great communication throughout the entire process and left a very clean job site.",
      "author": "Tawn Kramer",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "wickliffe",
    "name": "Wickliffe",
    "state": "OH",
    "zip": "44092",
    "county": "Lake County",
    "housing_era": "1940s–1970s",
    "landmarks": ["Wickliffe City Hall", "Bishop Hartley area", "Euclid Avenue corridor"],
    "streets": ["Euclid Avenue", "Bishop Road", "Vine Street", "Lloyd Road", "Rockefeller Road"],
    "neighbors": ["Willoughby", "Euclid", "Richmond Heights", "Highland Heights", "Willoughby Hills"],
    "notes": "Lake County border community. Older ranch and colonial homes — many are approaching or past their expected roof lifespan of 20–25 years.",
    "review": {
      "text": "I asked them to take a look at my roof based on my home inspection report. They were very honest when inspecting and only recommended the exact work that needed to be done.",
      "author": "Benjamin Kaplan",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "willoughby",
    "name": "Willoughby",
    "state": "OH",
    "zip": "44094",
    "county": "Lake County",
    "housing_era": "1940s–1980s",
    "landmarks": ["Downtown Willoughby", "Lost Nation Airport area", "Lake Shore Boulevard", "Willoughby-Eastlake Schools"],
    "streets": ["Erie Street", "Lake Shore Boulevard", "Lost Nation Road", "Glen Eagles Drive", "Euclid Avenue"],
    "neighbors": ["Willoughby Hills", "Eastlake", "Wickliffe", "Mentor", "Kirtland"],
    "notes": "Active Lake County suburb with a mix of historic downtown homes and post-war subdivisions. Lake effect weather drives frequent storm damage.",
    "review": {
      "text": "What a divine appointment — I love my new roof and would highly recommend Atlas Roofing to anyone in the area.",
      "author": "Lorna Joy Larkin",
      "source": "South Euclid, OH · Google Review"
    }
  },
  {
    "slug": "willoughby-hills",
    "name": "Willoughby Hills",
    "state": "OH",
    "zip": "44094",
    "county": "Lake County",
    "housing_era": "1960s–1990s",
    "landmarks": ["Willoughby Hills Community Center", "SOM Center Road corridor", "Chagrin River Park"],
    "streets": ["SOM Center Road", "Bishop Road", "Chardon Road", "Shank Road", "Willoughby Hills Drive"],
    "neighbors": ["Willoughby", "Lyndhurst", "Kirtland", "Mayfield Village", "Highland Heights"],
    "notes": "Quiet residential suburb between Lyndhurst and Willoughby. Many colonial and ranch homes from the 1970s–80s. Strong upgrade market.",
    "review": {
      "text": "Showed the highest level of professionalism from start to finish. Great price and I never felt taken advantage of.",
      "author": "Joseph Reichman",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "mentor",
    "name": "Mentor",
    "state": "OH",
    "zip": "44060",
    "county": "Lake County",
    "housing_era": "1960s–1990s",
    "landmarks": ["Great Lakes Mall", "Mentor Civic Center", "Mentor Lagoons", "Mentor Avenue corridor"],
    "streets": ["Mentor Avenue", "Heisley Road", "Hopkins Road", "Reynolds Road", "Tyler Boulevard"],
    "neighbors": ["Willoughby", "Eastlake", "Painesville", "Kirtland", "Concord Township"],
    "notes": "Lake County's largest city. Heavy mix of subdivisions from the 1970s–90s. Active storm insurance market — one of the best hail damage claim areas in NE Ohio.",
    "review": {
      "text": "Quick and professional roofing service. Great communication throughout the entire process and left a very clean job site.",
      "author": "Tawn Kramer",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "eastlake",
    "name": "Eastlake",
    "state": "OH",
    "zip": "44095",
    "county": "Lake County",
    "housing_era": "1950s–1980s",
    "landmarks": ["Eastlake City Hall", "Lake Shore Boulevard", "SportsEast facility", "Lakeshore Park"],
    "streets": ["Lake Shore Boulevard", "Vine Street", "Euclid Avenue", "Glendale Avenue", "Erie Road"],
    "neighbors": ["Willoughby", "Willowick", "Mentor", "Wickliffe", "Richmond Heights"],
    "notes": "Lakefront community highly exposed to ice dams, wind, and winter storm damage. Insurance claim jobs are common. Older ranch and bungalow housing stock.",
    "review": {
      "text": "I asked them to take a look at my roof based on my home inspection report. They were very honest when inspecting and only recommended the exact work that needed to be done.",
      "author": "Benjamin Kaplan",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "twinsburg",
    "name": "Twinsburg",
    "state": "OH",
    "zip": "44087",
    "county": "Summit County",
    "housing_era": "1970s–2000s",
    "landmarks": ["Twinsburg City Hall", "Twins Days Festival grounds", "Darrowville area", "Route 91 corridor"],
    "streets": ["Darrow Road", "Ravenna Road", "Glenwood Drive", "Hadden Road", "Chamberlin Road"],
    "neighbors": ["Solon", "Aurora", "Macedonia", "Hudson", "Reminderville"],
    "notes": "Growing Summit County suburb south of Solon. Many newer subdivisions with 15–25 year old roofs hitting replacement age. Active homebuilding.",
    "review": {
      "text": "What a divine appointment — I love my new roof and would highly recommend Atlas Roofing to anyone in the area.",
      "author": "Lorna Joy Larkin",
      "source": "South Euclid, OH · Google Review"
    }
  },
  {
    "slug": "hudson",
    "name": "Hudson",
    "state": "OH",
    "zip": "44236",
    "county": "Summit County",
    "housing_era": "1970s–2000s",
    "landmarks": ["Hudson Village area", "Western Reserve Academy", "Hudson Springs Park", "Route 303 corridor"],
    "streets": ["Main Street", "Streetsboro Road", "Barlow Road", "Stow Road", "Prospect Street"],
    "neighbors": ["Twinsburg", "Stow", "Macedonia", "Aurora", "Cuyahoga Falls"],
    "notes": "Affluent Summit County community with a strong historic character. Large custom homes and upscale subdivisions. Premium roofing materials are the norm.",
    "review": {
      "text": "Showed the highest level of professionalism from start to finish. Great price and I never felt taken advantage of.",
      "author": "Joseph Reichman",
      "source": "Northeast Ohio · Google Review"
    }
  },

  # ── CLEVELAND NEIGHBORHOODS ───────────────────────────────────────────────────

  {
    "slug": "tremont-cleveland",
    "name": "Tremont",
    "state": "OH",
    "zip": "44113",
    "county": "Cuyahoga County",
    "housing_era": "1880s–1930s",
    "landmarks": ["Lincoln Park", "Tremont Arts District", "Professor Avenue", "St. Theodosius Cathedral"],
    "streets": ["Professor Avenue", "West 14th Street", "Literary Road", "Starkweather Avenue", "Kenilworth Avenue"],
    "neighbors": ["Ohio City", "Brooklyn Centre", "Old Brooklyn", "Clark-Fulton"],
    "notes": "Historic urban neighborhood with Victorian and craftsman homes. Many century-old roofs. Renovation boom has created strong demand for quality roofing.",
    "review": {
      "text": "Quick and professional roofing service. Great communication throughout the entire process and left a very clean job site.",
      "author": "Tawn Kramer",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "ohio-city-cleveland",
    "name": "Ohio City",
    "state": "OH",
    "zip": "44113",
    "county": "Cuyahoga County",
    "housing_era": "1880s–1930s",
    "landmarks": ["West Side Market", "Market District", "Detroit Avenue corridor", "Hingetown"],
    "streets": ["Detroit Avenue", "West 25th Street", "Bridge Avenue", "Franklin Avenue", "Lorain Avenue"],
    "neighbors": ["Tremont", "Gordon Square", "Clark-Fulton", "Downtown Cleveland"],
    "notes": "Cleveland's most popular urban neighborhood for renovation. Historic homes being fully restored — roofing is a priority upgrade for buyers and investors.",
    "review": {
      "text": "I asked them to take a look at my roof based on my home inspection report. They were very honest when inspecting and only recommended the exact work that needed to be done.",
      "author": "Benjamin Kaplan",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "west-park-cleveland",
    "name": "West Park",
    "state": "OH",
    "zip": "44111",
    "county": "Cuyahoga County",
    "housing_era": "1920s–1960s",
    "landmarks": ["Kamm's Corners", "Rocky River Valley", "West Park neighborhood", "Lorain Avenue corridor"],
    "streets": ["Lorain Avenue", "West 130th Street", "Rocky River Drive", "Kamms Corners", "Bellaire Road"],
    "neighbors": ["Kamm's Corners", "Lakewood", "Fairview Park", "Old Brooklyn"],
    "notes": "One of Cleveland's largest residential neighborhoods. Dense with colonial and cape cod homes from the 1940s–60s. High volume of replacement-age roofs.",
    "review": {
      "text": "What a divine appointment — I love my new roof and would highly recommend Atlas Roofing to anyone in the area.",
      "author": "Lorna Joy Larkin",
      "source": "South Euclid, OH · Google Review"
    }
  },
  {
    "slug": "old-brooklyn-cleveland",
    "name": "Old Brooklyn",
    "state": "OH",
    "zip": "44144",
    "county": "Cuyahoga County",
    "housing_era": "1920s–1960s",
    "landmarks": ["Pearl-Denison area", "Big Creek Parkway", "Brookside Park", "State Road corridor"],
    "streets": ["Pearl Road", "State Road", "Denison Avenue", "Broadview Road", "West 25th Street"],
    "neighbors": ["Brooklyn", "Parma", "Tremont", "West Park", "Garfield Heights"],
    "notes": "Large inner-city neighborhood with many post-war ranches and bungalows. Affordable housing stock where deferred maintenance is common — strong repair and replacement market.",
    "review": {
      "text": "Showed the highest level of professionalism from start to finish. Great price and I never felt taken advantage of.",
      "author": "Joseph Reichman",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "collinwood-cleveland",
    "name": "Collinwood",
    "state": "OH",
    "zip": "44110",
    "county": "Cuyahoga County",
    "housing_era": "1900s–1950s",
    "landmarks": ["Waterloo Arts District", "Euclid Avenue corridor", "Collinwood Recreation Center", "Lakeshore area"],
    "streets": ["Waterloo Road", "Euclid Avenue", "East 185th Street", "Lake Shore Boulevard", "St. Clair Avenue"],
    "neighbors": ["Glenville", "South Euclid", "Euclid", "Willoughby"],
    "notes": "Historic near-east neighborhood undergoing revitalization. Mix of century homes and post-war housing. Waterloo Arts District driving renovation interest.",
    "review": {
      "text": "Quick and professional roofing service. Great communication throughout the entire process and left a very clean job site.",
      "author": "Tawn Kramer",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "glenville-cleveland",
    "name": "Glenville",
    "state": "OH",
    "zip": "44108",
    "county": "Cuyahoga County",
    "housing_era": "1900s–1950s",
    "landmarks": ["Wade Park area", "East 105th Street corridor", "Cleveland Museum of Natural History (nearby)", "Rockefeller Park"],
    "streets": ["East 105th Street", "St. Clair Avenue", "Superior Avenue", "East 105th Street", "Parkwood Drive"],
    "neighbors": ["University Circle", "Collinwood", "South Euclid", "East Cleveland"],
    "notes": "Near-east Cleveland neighborhood with many large older homes on tree-lined streets. Many homes haven't had roofwork in decades — replacement demand is high.",
    "review": {
      "text": "I asked them to take a look at my roof based on my home inspection report. They were very honest when inspecting and only recommended the exact work that needed to be done.",
      "author": "Benjamin Kaplan",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "kamms-corners-cleveland",
    "name": "Kamm's Corners",
    "state": "OH",
    "zip": "44111",
    "county": "Cuyahoga County",
    "housing_era": "1920s–1960s",
    "landmarks": ["Kamm's Corners intersection", "Lorain Avenue shops", "West 117th Street corridor"],
    "streets": ["Lorain Avenue", "West 117th Street", "Bellaire Road", "West 130th Street", "Puritas Road"],
    "neighbors": ["West Park", "Fairview Park", "Lakewood", "Old Brooklyn"],
    "notes": "Active westside neighborhood centered around the Lorain-117th intersection. Dense residential blocks with aging housing stock — high volume potential.",
    "review": {
      "text": "What a divine appointment — I love my new roof and would highly recommend Atlas Roofing to anyone in the area.",
      "author": "Lorna Joy Larkin",
      "source": "South Euclid, OH · Google Review"
    }
  },
  {
    "slug": "mount-pleasant-cleveland",
    "name": "Mount Pleasant",
    "state": "OH",
    "zip": "44120",
    "county": "Cuyahoga County",
    "housing_era": "1910s–1950s",
    "landmarks": ["Shaker Square (nearby)", "Mount Pleasant Recreation Center", "Union Avenue corridor"],
    "streets": ["Union Avenue", "Lee Road", "Harvard Avenue", "East 131st Street", "Kinsman Road"],
    "neighbors": ["Shaker Heights", "Warrensville Heights", "Lee-Harvard", "Garfield Heights"],
    "notes": "Southeast Cleveland neighborhood bordering Shaker Heights. Older housing stock with many homes needing full replacement. Strong community investment in home ownership.",
    "review": {
      "text": "Showed the highest level of professionalism from start to finish. Great price and I never felt taken advantage of.",
      "author": "Joseph Reichman",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "lee-harvard-cleveland",
    "name": "Lee-Harvard",
    "state": "OH",
    "zip": "44128",
    "county": "Cuyahoga County",
    "housing_era": "1940s–1970s",
    "landmarks": ["Lee-Harvard Shopping Center", "Harvard-Lee Library", "Garfield Park Reservation"],
    "streets": ["Lee Road", "Harvard Avenue", "East 131st Street", "Miles Avenue", "East 116th Street"],
    "neighbors": ["Garfield Heights", "Warrensville Heights", "Mount Pleasant", "Bedford Heights"],
    "notes": "Southeast Cleveland neighborhood with many mid-century ranch homes. Homeowners are value-conscious — competitive pricing and warranty matters.",
    "review": {
      "text": "Quick and professional roofing service. Great communication throughout the entire process and left a very clean job site.",
      "author": "Tawn Kramer",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "slavic-village-cleveland",
    "name": "Slavic Village",
    "state": "OH",
    "zip": "44105",
    "county": "Cuyahoga County",
    "housing_era": "1880s–1940s",
    "landmarks": ["Fleet Avenue corridor", "Broadway Avenue", "St. Hyacinth Church", "Morgana Run Trail"],
    "streets": ["Fleet Avenue", "Broadway Avenue", "East 65th Street", "Sowinski Avenue", "Holton Avenue"],
    "neighbors": ["Garfield Heights", "Old Brooklyn", "Brooklyn", "Tremont"],
    "notes": "Historic southeast Cleveland neighborhood. Many century-old homes with original or very old rooflines. Strong renovation interest from investors and homeowners alike.",
    "review": {
      "text": "I asked them to take a look at my roof based on my home inspection report. They were very honest when inspecting and only recommended the exact work that needed to be done.",
      "author": "Benjamin Kaplan",
      "source": "Northeast Ohio · Google Review"
    }
  },

  # ── NEW ADDITIONS ─────────────────────────────────────────────────────────────

  {
    "slug": "hunting-valley",
    "name": "Hunting Valley",
    "state": "OH",
    "zip": "44022",
    "county": "Cuyahoga County",
    "housing_era": "1960s–1990s",
    "landmarks": ["South Chagrin Reservation", "Chagrin Valley Polo Club", "Hunting Valley Village Hall"],
    "streets": ["Chagrin River Road", "Fairmount Boulevard", "SOM Center Road", "Shaker Boulevard"],
    "neighbors": ["Moreland Hills", "Pepper Pike", "Gates Mills", "Orange", "Chagrin Falls"],
    "notes": "One of the wealthiest villages in Ohio. Large estate homes on expansive wooded lots. Premium roofing materials and high attention to architectural detail.",
    "review": {
      "text": "Showed the highest level of professionalism from start to finish. Great price and I never felt taken advantage of.",
      "author": "Joseph Reichman",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "highland-hills",
    "name": "Highland Hills",
    "state": "OH",
    "zip": "44128",
    "county": "Cuyahoga County",
    "housing_era": "1950s–1980s",
    "landmarks": ["Beachwood adjacent corridor", "Harvard Road area", "Cuyahoga County border"],
    "streets": ["Harvard Road", "Warrensville Center Road", "Green Road", "Chagrin Boulevard"],
    "neighbors": ["Beachwood", "Warrensville Heights", "Orange", "Bedford Heights", "North Randall"],
    "notes": "Small village tucked between Beachwood and Warrensville Heights. Many mid-century ranch and colonial homes. Proximity to Beachwood means many neighbors are familiar with Atlas.",
    "review": {
      "text": "I asked them to take a look at my roof based on my home inspection report. They were very honest when inspecting and only recommended the exact work that needed to be done.",
      "author": "Benjamin Kaplan",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "shaker",
    "name": "Shaker",
    "state": "OH",
    "zip": "44120",
    "county": "Cuyahoga County",
    "housing_era": "1920s–1950s",
    "landmarks": ["Shaker Square", "Van Aken District", "Shaker Heights High School", "Horseshoe Lake Park"],
    "streets": ["Van Aken Boulevard", "South Woodland Road", "Fairmount Boulevard", "Chagrin Boulevard", "Lee Road"],
    "neighbors": ["Cleveland Heights", "University Heights", "Beachwood", "Pepper Pike", "East Cleveland"],
    "notes": "Short-form name commonly used by locals when referring to Shaker Heights. Targets searches like 'roof repair shaker' and 'roofing contractor shaker ohio'. Historic Tudor and Colonial homes, many 70–100 years old.",
    "review": {
      "text": "Quick and professional roofing service. Great communication throughout the entire process and left a very clean job site.",
      "author": "Tawn Kramer",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "north-randall",
    "name": "North Randall",
    "state": "OH",
    "zip": "44128",
    "county": "Cuyahoga County",
    "housing_era": "1950s–1980s",
    "landmarks": ["JACK Thistledown Racino", "Randall Park area", "Northfield Road corridor"],
    "streets": ["Northfield Road", "Miles Road", "Emery Road", "Warrensville Center Road"],
    "neighbors": ["Warrensville Heights", "Bedford Heights", "Orange", "Highland Hills", "Beachwood"],
    "notes": "Small village with a mix of residential and commercial. Home to Thistledown Racino. Residential areas feature older ranch homes with roofs frequently at or past replacement age.",
    "review": {
      "text": "What a divine appointment — I love my new roof and would highly recommend Atlas Roofing to anyone in the area.",
      "author": "Lorna Joy Larkin",
      "source": "South Euclid, OH · Google Review"
    }
  },
  {
    "slug": "gates-mills",
    "name": "Gates Mills",
    "state": "OH",
    "zip": "44040",
    "county": "Cuyahoga County",
    "housing_era": "1940s–1980s",
    "landmarks": ["Chagrin River corridor", "Gates Mills Village Hall", "Fox Chapel area", "Mayfield Road"],
    "streets": ["Mayfield Road", "Chagrin River Road", "Glenwood Drive", "Strawberry Lane", "Millbrook Road"],
    "neighbors": ["Lyndhurst", "Pepper Pike", "Hunting Valley", "Mayfield Village", "Highland Heights"],
    "notes": "Exclusive rural village along the Chagrin River. Large custom homes on private wooded lots. Residents expect premium materials and meticulous workmanship.",
    "review": {
      "text": "Showed the highest level of professionalism from start to finish. Great price and I never felt taken advantage of.",
      "author": "Joseph Reichman",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "bentleyville",
    "name": "Bentleyville",
    "state": "OH",
    "zip": "44022",
    "county": "Cuyahoga County",
    "housing_era": "1960s–1990s",
    "landmarks": ["Bentleyville Village Hall", "South Chagrin Reservation", "Chagrin River area", "Solon Road"],
    "streets": ["Solon Road", "Bentleyville Road", "Miles Road", "Aurora Road", "Chagrin River Road"],
    "neighbors": ["Moreland Hills", "Chagrin Falls", "Orange", "Solon", "Hunting Valley"],
    "notes": "Small village in the Chagrin Valley area. Upscale homes on large wooded lots. Residents are quality-focused and value a contractor who understands architectural character.",
    "review": {
      "text": "I asked them to take a look at my roof based on my home inspection report. They were very honest when inspecting and only recommended the exact work that needed to be done.",
      "author": "Benjamin Kaplan",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "south-russell",
    "name": "South Russell",
    "state": "OH",
    "zip": "44022",
    "county": "Geauga County",
    "housing_era": "1970s–2000s",
    "landmarks": ["Chagrin Falls adjacent", "Russell Township area", "Route 306 corridor"],
    "streets": ["Chillicothe Road", "Fairmount Road", "South Russell Road", "Bell Street", "Caves Road"],
    "neighbors": ["Chagrin Falls", "Bentleyville", "Bainbridge", "Aurora", "Chester Township"],
    "notes": "Quiet Geauga County township adjacent to Chagrin Falls. Larger homes on acreage. Homeowners are selective and value quality over price.",
    "review": {
      "text": "What a divine appointment — I love my new roof and would highly recommend Atlas Roofing to anyone in the area.",
      "author": "Lorna Joy Larkin",
      "source": "South Euclid, OH · Google Review"
    }
  },
  {
    "slug": "oakwood",
    "name": "Oakwood",
    "state": "OH",
    "zip": "44146",
    "county": "Cuyahoga County",
    "housing_era": "1950s–1980s",
    "landmarks": ["Oakwood Village Hall", "Northfield Road corridor", "Bedford Reservation nearby"],
    "streets": ["Northfield Road", "Oakwood Road", "Dunham Road", "Forbes Road", "Libby Road"],
    "neighbors": ["Bedford", "Bedford Heights", "Glenwillow", "Solon", "Walton Hills"],
    "notes": "Small village south of Bedford. Quiet residential community with ranch and colonial homes. Many homeowners are long-term residents with aging roofs.",
    "review": {
      "text": "Quick and professional roofing service. Great communication throughout the entire process and left a very clean job site.",
      "author": "Tawn Kramer",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "glenwillow",
    "name": "Glenwillow",
    "state": "OH",
    "zip": "44139",
    "county": "Cuyahoga County",
    "housing_era": "1990s–2010s",
    "landmarks": ["Glenwillow Industrial Park", "Route 422 corridor", "Solon adjacent"],
    "streets": ["Cochran Road", "Route 422", "Pettibone Road", "SOM Center Road", "Harper Road"],
    "neighbors": ["Solon", "Bedford", "Oakwood", "Twinsburg", "Glenwillow"],
    "notes": "Small newer village near Solon. Mix of newer residential developments and industrial. Newer homes means roofs hitting 20–25 year replacement age in the coming years.",
    "review": {
      "text": "Showed the highest level of professionalism from start to finish. Great price and I never felt taken advantage of.",
      "author": "Joseph Reichman",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "mayfield",
    "name": "Mayfield",
    "state": "OH",
    "zip": "44143",
    "county": "Cuyahoga County",
    "housing_era": "1950s–1980s",
    "landmarks": ["Mayfield Village Hall", "Mayfield Road corridor", "Hillcrest area", "SOM Center Road"],
    "streets": ["Mayfield Road", "SOM Center Road", "Beta Drive", "Wilson Mills Road", "Highland Road"],
    "neighbors": ["Mayfield Heights", "Highland Heights", "Gates Mills", "Lyndhurst", "Willoughby Hills"],
    "notes": "Targets residents who search 'Mayfield' without specifying Heights or Village. Covers the broader Mayfield Road corridor community. Mix of older ranch homes and newer construction.",
    "review": {
      "text": "I asked them to take a look at my roof based on my home inspection report. They were very honest when inspecting and only recommended the exact work that needed to be done.",
      "author": "Benjamin Kaplan",
      "source": "Northeast Ohio · Google Review"
    }
  },
  {
    "slug": "wilson-mills",
    "name": "Wilson Mills",
    "state": "OH",
    "zip": "44143",
    "county": "Cuyahoga County",
    "housing_era": "1960s–1990s",
    "landmarks": ["Wilson Mills Road corridor", "Highland Heights border", "Mayfield Village border", "Hillcrest Hospital area"],
    "streets": ["Wilson Mills Road", "Bishop Road", "Miner Road", "Highland Road", "Beta Drive"],
    "neighbors": ["Highland Heights", "Mayfield Village", "Mayfield Heights", "Richmond Heights", "Lyndhurst"],
    "notes": "Wilson Mills Road is a key local corridor that homeowners identify as their area. Targets 'Wilson Mills roofing' and related searches from residents along this stretch of Highland Heights and Mayfield Village.",
    "review": {
      "text": "What a divine appointment — I love my new roof and would highly recommend Atlas Roofing to anyone in the area.",
      "author": "Lorna Joy Larkin",
      "source": "South Euclid, OH · Google Review"
    }
  },
  {
    "slug": "chesterland",
    "name": "Chesterland",
    "state": "OH",
    "zip": "44026",
    "county": "Geauga County",
    "housing_era": "1970s–2000s",
    "landmarks": ["Chester Township", "Caves Road", "Chardon Road corridor", "West Geauga High School area"],
    "streets": ["Chardon Road", "Caves Road", "Mayfield Road", "Chillicothe Road", "Mulberry Road"],
    "neighbors": ["Kirtland", "Mentor", "Willoughby Hills", "Auburn Township", "Hambden Township"],
    "notes": "Rural Geauga County community with a mix of older farmhouses, ranches, and newer custom homes. Residents often have larger roofs due to lot sizes. Willingness to pay for quality.",
    "review": {
      "text": "Quick and professional roofing service. Great communication throughout the entire process and left a very clean job site.",
      "author": "Tawn Kramer",
      "source": "Northeast Ohio · Google Review"
    }
  },
]

# Quick lookup helpers
CITY_BY_SLUG = {c["slug"]: c for c in CITIES}

def get_city(slug):
    return CITY_BY_SLUG.get(slug)

def all_slugs():
    return [c["slug"] for c in CITIES]

if __name__ == "__main__":
    print(f"Total cities: {len(CITIES)}")
    tier1 = [c for c in CITIES if c["slug"] in [
        "beachwood","shaker-heights","cleveland-heights","university-heights",
        "south-euclid","lyndhurst","pepper-pike","highland-heights",
        "mayfield-heights","richmond-heights","orange","solon",
        "chagrin-falls","woodmere","moreland-hills"
    ]]
    tier2 = [c for c in CITIES if "cleveland" not in c["slug"] and c not in tier1]
    neighborhoods = [c for c in CITIES if "cleveland" in c["slug"]]
    print(f"Tier 1: {len(tier1)} cities")
    print(f"Tier 2: {len(tier2)} cities")
    print(f"Cleveland neighborhoods: {len(neighborhoods)}")
    print(f"Total pages to generate (×9 phrases): {len(CITIES) * 9}")
