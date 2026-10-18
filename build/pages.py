"""Interior page content. Answer-first: every page and section opens with the direct answer."""
from site_data import PRICE_FROM, PHONE, SINCE

L = lambda href, text: f'<a href="{href}">{text}</a>'
BDAY = "/birthday-party-magician-regina/"
CORP = "/corporate-event-magician-regina/"
WED = "/wedding-magician-regina/"
SCHOOL = "/school-library-magic-shows-saskatchewan/"
PRIV = "/private-party-community-event-magician-regina/"
REGINA = "/magician-regina/"
PB = "/magician-pilot-butte/"
WC = "/magician-white-city-emerald-park/"
BAL = "/magician-balgonie/"
MJ = "/magician-moose-jaw/"
ABOUT = "/about/"
CONTACT = "/contact/"

SERVICE_PAGES = {
"birthday-party-magician-regina": dict(
  title="Birthday Party Magician in Regina, SK | Tripp Coleman",
  desc=f"Kids' birthday party magician in Regina and area. Interactive card magic and comedy for ages 4+. Shows from {PRICE_FROM}. Book Tripp Coleman: {PHONE}.",
  h1="Birthday party magician in Regina",
  answer="Tripp Coleman is a Regina-area magician who turns kids' birthday parties into an interactive magic show, with the birthday child at the centre of the act. He performs for ages 4 and up across Regina, Pilot Butte, White City and southern Saskatchewan.",
  facts=[("Show length","60–120 min"),("Best for","Ages 4+"),("Starting at",f"Around {PRICE_FROM}"),("Setup","Living room or hall")],
  sections=[
   ("What a birthday magic show looks like",
    "<p><strong>Every show is hands-on.</strong> Kids don't just watch: they pick the cards, hold the props and get their own reactions out loud. Tripp's style mixes comedy, sleight of hand and street-style magic, so it plays for the little ones on the carpet and the adults at the back of the room at the same time.</p>"
    "<p>The birthday child gets the spotlight. Tripp builds moments into the show where they become the magician's assistant, and often the one who makes the impossible happen. That's the part the photos come from.</p>"
    "<p>Tripp has been performing since " + str(SINCE) + ", and his family shows have included birthday gatherings, backyard BBQs and public library shows billed for ages 4 and up.</p>"),
   ("What's included",
    "<ul><li>An interactive magic show of 60 to 120 minutes, depending on the package you choose</li>"
    "<li>A featured moment for the birthday child</li>"
    "<li>Close-up card magic performed right in kids' hands</li>"
    "<li>Comedy that keeps parents laughing too</li>"
    "<li>Travel within Regina and nearby communities (ask about farther locations)</li></ul>"
    "<p>Want something specific, like a theme, a surprise reveal or a mini lesson at the end? Mention it when you book and Tripp will tell you what's possible.</p>"),
   ("How much does a birthday party magician cost?",
    f"<p><strong>Tripp's shows start at around {PRICE_FROM}.</strong> Price depends on show length, number of kids and travel distance. Weekend afternoons are usually the first slots to go, so reach out early if your date is fixed.</p>"
    f"<p>The quickest way to a quote is to call or text {PHONE} with your date, the town and how many kids are coming.</p>"),
   ("Planning tips for parents",
    "<ul><li><strong>Timing:</strong> schedule magic after kids arrive and before cake. Attention is highest early, and sugar comes later.</li>"
    "<li><strong>Space:</strong> a cleared living room, basement or rented hall works. Kids sit on the floor in front, adults behind.</li>"
    "<li><strong>Age mix:</strong> if siblings and cousins span a wide age range, tell Tripp. He'll pitch the show to the whole group.</li>"
    "<li><strong>Photos:</strong> put one adult on camera duty. The reactions happen fast.</li></ul>"),
   ("Where Tripp performs birthday parties",
    f"<p>Tripp is based in {L(PB,'Pilot Butte')}, about 10 minutes from {L(REGINA,'Regina')}, so most Regina-area parties are a short drive. He also covers {L(WC,'White City and Emerald Park')}, {L(BAL,'Balgonie')} and {L(MJ,'Moose Jaw')}, and travels up to about 200 miles for events.</p>"),
  ],
  faq=[
   ("What age is a magic show good for?","Tripp's family shows are built for ages 4 and up. Younger siblings are welcome, and the comedy keeps adults engaged too."),
   ("How long is a kids' magic show?","Tripp's shows run 60 to 120 minutes. Most parents pick a length based on the age of the kids and the rest of the party schedule."),
   ("Do you need a lot of space?","No. A cleared living room, basement or party room is enough. Kids sit on the floor in front so everyone can see."),
   ("Can the birthday child be part of the show?","Yes. Tripp builds in moments where the birthday child helps with, and often performs, part of the magic."),
   ("How do I book?",f"Call or text {PHONE}, or send your date and details through the booking form. Tripp will confirm availability and price."),
  ],
  related=[CORP, PRIV, SCHOOL],
),
"corporate-event-magician-regina": dict(
  title="Corporate Event Magician in Regina | Tripp Coleman",
  desc=f"Corporate magician for Regina galas, client nights and trade shows. Clients include Capital GMC, John Deere and eXp Realty. Call {PHONE}.",
  h1="Corporate event magician in Regina",
  answer="Tripp Coleman is a corporate magician based near Regina who performs strolling close-up magic and stage shows for company events, client appreciation nights, galas and trade shows. His corporate clients include Capital GMC, John Deere, eXp Realty and the Conexus Arts Centre.",
  facts=[("Formats","Strolling or stage"),("Show length","60–120 min"),("Starting at",f"Around {PRICE_FROM}"),("Stage needs","Headset mic + PA")],
  sections=[
   ("Why companies book a magician",
    "<p><strong>Magic breaks the ice faster than anything on the agenda.</strong> At a mixer, people who don't know each other end up laughing at the same impossible moment, and then they're talking. At a client night, it gives your guests a story to take back to the office.</p>"
    "<p>Tripp has performed for Capital GMC, John Deere, eXp Realty and the Conexus Arts Centre, along with cocktail parties and private events in Regina. He has also performed on the streets of Las Vegas several times, which is about the toughest training ground there is for winning over a crowd that didn't plan to stop.</p>"),
   ("Formats for corporate events",
    "<h3>Strolling close-up magic</h3><p>Tripp moves table to table or group to group during a reception, performing card magic right in guests' hands. No stage or sound is needed, and it suits cocktail hours, networking events and trade-show booths.</p>"
    "<h3>Stage show</h3><p>A full show for a seated audience after dinner or as part of a program. For stage shows Tripp uses a wireless headset microphone and a PA system, so tell him about the room when you book.</p>"
    "<h3>Branded moments</h3><p>Want your product, logo or company message to show up in the magic? Ask. A custom reveal is a memorable way to close a launch or award night.</p>"),
   ("What's included",
    "<ul><li>Strolling, stage, or a mix of both, 60 to 120 minutes in total</li>"
    "<li>Clean, crowd-appropriate material for professional audiences</li>"
    "<li>A pre-event call to match the show to your guests and schedule</li>"
    "<li>Travel within the Regina area, with farther events quoted on request</li></ul>"),
   ("Cost of a corporate magician in Regina",
    f"<p><strong>Shows start at around {PRICE_FROM}</strong>, with the final quote based on format, length, audience size and travel. Send your date, venue and headcount to {PHONE} or through the booking form for an exact price.</p>"),
   ("Venues and areas served",
    f"<p>Tripp performs at hotels, restaurants, offices, arts venues and private halls across {L(REGINA,'Regina')}, {L(WC,'White City and Emerald Park')}, {L(BAL,'Balgonie')} and {L(MJ,'Moose Jaw')}, and travels up to about 200 miles for the right event.</p>"),
  ],
  faq=[
   ("Is the show appropriate for professional audiences?","Yes. Tripp tailors material to the crowd, and his corporate work includes events for Capital GMC, John Deere, eXp Realty and the Conexus Arts Centre."),
   ("Do you need a stage?","Not for strolling close-up magic. For a stage show, Tripp needs space at the front of the room plus a wireless headset microphone and PA system."),
   ("Can magic include our brand or product?","Yes. Ask about a branded reveal or a custom moment built around your company or launch."),
   ("How long does a corporate set run?","Tripp's sets run 60 to 120 minutes in total and can be split between a strolling portion and a stage portion."),
   ("Do you perform at trade shows?","Yes. Close-up magic at a booth draws a crowd and gives your team a reason to start conversations."),
  ],
  related=[WED, PRIV, BDAY],
),
"wedding-magician-regina": dict(
  title="Wedding Magician in Regina, SK | Tripp Coleman",
  desc="Wedding magician for Regina-area cocktail hours and receptions. Strolling close-up magic that keeps guests entertained between photos and dinner.",
  h1="Wedding magician in Regina",
  answer="Tripp Coleman performs strolling close-up magic at weddings in Regina and southern Saskatchewan, entertaining guests during the cocktail hour, the gap while the couple is at photos, or between dinner and the dance.",
  facts=[("Format","Strolling close-up"),("Show length","60–120 min"),("Starting at",f"Around {PRICE_FROM}"),("Setup","None needed")],
  sections=[
   ("Where magic fits in a wedding day",
    "<p><strong>The best slot is the cocktail hour.</strong> That's when the wedding party is off at photos and guests are standing around with a drink. Tripp moves group to group performing card magic in people's hands, so nobody notices the wait.</p>"
    "<p>Other couples book magic between dinner and the first dance, or as a short featured set during the reception. Because close-up magic needs no stage or sound, it fits any venue, from a downtown hall to a farmyard tent.</p>"),
   ("Why close-up magic works at weddings",
    "<ul><li><strong>It mixes the two families.</strong> Strangers react to the same moment and start talking.</li>"
    "<li><strong>It works for every age.</strong> Grandparents, kids and the groomsmen all get pulled in.</li>"
    "<li><strong>It's portable.</strong> Tripp performs standing, in small groups, indoors or outdoors.</li>"
    "<li><strong>It creates moments for your photographer.</strong> Guest reactions make great candid shots.</li></ul>"),
   ("What's included",
    "<ul><li>Strolling close-up magic for 60 to 120 minutes</li>"
    "<li>A planning call to match timing to your schedule</li>"
    "<li>Optional moment for the couple, such as a signed-card reveal</li>"
    "<li>Travel within the Regina area, with farther venues quoted on request</li></ul>"),
   ("Planning checklist for couples",
    "<ul><li><strong>Pick the slot first.</strong> Cocktail hour is the most common; tell Tripp your photo schedule so he knows how long guests will be waiting.</li>"
    "<li><strong>Loop in your planner or MC.</strong> They'll know when Tripp starts and where guests will be gathered.</li>"
    "<li><strong>Think about the space.</strong> Standing groups, lounge seating or tables all work. Outdoor ceremonies are fine too; just mention wind or shade.</li>"
    "<li><strong>Tell your photographer.</strong> Guest reactions to close-up magic make some of the best candid shots of the day.</li>"
    "<li><strong>Plan a moment for yourselves.</strong> Ask about a signed-card reveal or a short piece performed just for the two of you.</li></ul>"
    "<p>Have a large guest list? Strolling magic scales well, because Tripp works through the room group by group. Give him your headcount and he'll recommend how long to book.</p>"),
   ("Wedding magician pricing",
    f"<p><strong>Shows start at around {PRICE_FROM}.</strong> Your quote depends on how long you want Tripp there and how far the venue is. Call or text {PHONE} with your date and venue.</p>"),
   ("Areas served",
    f"<p>Tripp covers weddings in {L(REGINA,'Regina')}, {L(PB,'Pilot Butte')}, {L(WC,'White City and Emerald Park')}, {L(BAL,'Balgonie')} and {L(MJ,'Moose Jaw')}, plus rural venues within about 200 miles.</p>"),
  ],
  faq=[
   ("When should the magician perform at a wedding?","Most couples book the cocktail hour, while they're away for photos. Between dinner and the dance is another popular slot."),
   ("Does a wedding magician need a stage or microphone?","No. Strolling close-up magic needs no stage, sound or setup."),
   ("Is magic good for a mixed-age wedding crowd?","Yes. Close-up magic plays to kids, grandparents and everyone in between."),
   ("How far in advance should we book?","As soon as your date is set. Summer Saturdays are usually the first to go."),
  ],
  related=[CORP, PRIV, BDAY],
),
"school-library-magic-shows-saskatchewan": dict(
  title="School & Library Magic Shows in Saskatchewan | Tripp",
  desc="Magic shows for schools, libraries and day cares in Regina and southern Saskatchewan. Family-friendly for ages 4+. Tripp Coleman, Trippmagic.",
  h1="School and library magic shows in Saskatchewan",
  answer="Tripp Coleman performs family-friendly magic shows for schools, public libraries, day cares and seniors' programs across Regina and southern Saskatchewan. His Regina Public Library show at the Sherwood Village branch was billed for ages 4 and up.",
  facts=[("Audience","Ages 4+ and families"),("Show length","60–120 min"),("Starting at",f"Around {PRICE_FROM}"),("Large rooms","Headset mic + PA")],
  sections=[
   ("Shows built for young audiences",
    "<p><strong>Tripp's school and library shows are interactive from start to finish.</strong> Kids call out, volunteer and help make the magic happen, which keeps a room of young audience members engaged far better than a lecture-style show.</p>"
    "<p>He performed the Tripp Coleman Magic Show at the Regina Public Library's Sherwood Village branch on February 16, 2026, a free drop-in program for ages 4 and up. He has also performed for a combined seniors and day care audience, which is about as wide an age range as a magician gets.</p>"),
   ("Good fits for this show",
    "<ul><li>Public library programs, including school-break and summer reading events</li>"
    "<li>Elementary school assemblies and fun days</li>"
    "<li>Day cares and after-school programs</li>"
    "<li>Seniors' homes and intergenerational events</li>"
    "<li>Community centres and family nights</li></ul>"),
   ("What organizers need to provide",
    "<p>For a classroom or small room, nothing more than a clear space at the front. For a gym or large hall, Tripp uses a wireless headset microphone and a PA system, so let him know whether the venue has sound available.</p>"),
   ("Planning a school or library show",
    "<ul><li><strong>Choose the slot.</strong> Library programs often run during school breaks and summer reading season; schools often book assemblies or fun days. Give Tripp your preferred dates early.</li>"
    "<li><strong>Know your audience size.</strong> A library story room and a full gym need different setups. Tell Tripp roughly how many kids and adults to expect.</li>"
    "<li><strong>Set the seating.</strong> Kids on the floor up front and adults behind gives everyone a clear view and makes volunteering easy.</li>"
    "<li><strong>Check your photo policy.</strong> If your school or library has rules about photos of children, share them so the show runs smoothly.</li>"
    "<li><strong>Promote it.</strong> Billing the show by age (for example, ages 4 and up) helps families decide whether to come.</li></ul>"),
   ("Pricing for schools and libraries",
    f"<p><strong>Shows start at around {PRICE_FROM}</strong>, depending on length and travel. Library and school programmers can call or text {PHONE} with their date range and audience size.</p>"),
   ("Areas served",
    f"<p>Tripp performs at schools and libraries in {L(REGINA,'Regina')}, {L(PB,'Pilot Butte')}, {L(WC,'White City and Emerald Park')}, {L(BAL,'Balgonie')}, {L(MJ,'Moose Jaw')} and rural communities within about 200 miles.</p>"),
  ],
  faq=[
   ("Has Tripp performed at the Regina Public Library?","Yes. He performed a free drop-in magic show at the Sherwood Village branch on February 16, 2026, for ages 4 and up."),
   ("What age range is the show for?","Ages 4 and up. Tripp has also performed for combined seniors and day care audiences."),
   ("What equipment does the venue need?","A clear space at the front. In a gym or large hall, a wireless headset microphone and PA system."),
   ("How long is a school or library show?","Shows run 60 to 120 minutes. Tell Tripp your program slot and he'll fit the show to it."),
  ],
  related=[BDAY, PRIV, CORP],
),
"private-party-community-event-magician-regina": dict(
  title="Private Party & Community Event Magician | Regina",
  desc="Magician for private parties, family reunions, BBQs, festivals and nonprofit events across Regina and southern Saskatchewan. Tripp Coleman, Trippmagic.",
  h1="Private party and community event magician",
  answer="Tripp Coleman performs at private parties, family gatherings, backyard BBQs, nonprofit fundraisers and community events across Regina and southern Saskatchewan, using strolling magic that works its way through the whole crowd.",
  facts=[("Format","Strolling or show"),("Show length","60–120 min"),("Starting at",f"Around {PRICE_FROM}"),("Travel","Up to ~200 miles")],
  sections=[
   ("Magic that works the whole crowd",
    "<p><strong>At a party or community event, people are spread out and moving.</strong> Tripp's strolling style is built for that: he goes to the guests, group by group, so everyone gets a turn up close instead of craning to see a stage.</p>"
    "<p>At a family BBQ in Radville in July 2026, one host wrote that he \"moved through the crowd effortlessly, entertaining families one by one.\" He also performed at a nonprofit event in Radville and at a cocktail party in Regina.</p>"),
   ("Events Tripp performs at",
    "<ul><li>Milestone birthdays and anniversaries</li>"
    "<li>Family reunions and backyard BBQs</li>"
    "<li>Cocktail parties and house parties</li>"
    "<li>Nonprofit fundraisers and galas</li>"
    "<li>Community festivals, fairs and town events</li>"
    "<li>Seniors' homes and intergenerational events</li></ul>"),
   ("What's included",
    "<ul><li>Strolling close-up magic, a featured show, or both, 60 to 120 minutes in total</li>"
    "<li>Material pitched to your crowd, from kids to adults-only parties</li>"
    "<li>No stage needed for strolling sets; headset mic and PA for larger shows</li></ul>"),
   ("Tips for hosts",
    "<ul><li><strong>Time it right.</strong> Strolling magic works best while guests are arriving and mingling, before speeches or dinner pull everyone to their seats.</li>"
    "<li><strong>Outdoor events:</strong> card magic is happiest out of strong wind, so a patio, tent or shaded corner is ideal.</li>"
    "<li><strong>Mixed crowds:</strong> tell Tripp whether kids will be there. He'll adjust the material so it works for everyone.</li>"
    "<li><strong>Fundraisers:</strong> a short featured set can draw people to the main room before an auction or announcement.</li>"
    "<li><strong>Headcount:</strong> share your guest count so Tripp can suggest how long to book for everyone to get a turn up close.</li></ul>"),
   ("Pricing",
    f"<p><strong>Shows start at around {PRICE_FROM}.</strong> Community and nonprofit organizers should mention their event when asking for a quote. Call or text {PHONE}.</p>"),
   ("Areas served",
    f"<p>Tripp travels from {L(PB,'Pilot Butte')} to events in {L(REGINA,'Regina')}, {L(WC,'White City and Emerald Park')}, {L(BAL,'Balgonie')}, {L(MJ,'Moose Jaw')}, Radville and other communities within about 200 miles.</p>"),
  ],
  faq=[
   ("Can you perform at an outdoor event?","Yes. Strolling close-up magic works outdoors at BBQs, fairs and festivals."),
   ("Do you perform at nonprofit events?","Yes. Tripp has performed at a nonprofit event in Radville, SK."),
   ("Is the show suitable for adults-only parties?","Yes. Tripp adjusts his material to the crowd, from family events to adult cocktail parties."),
   ("How many guests can you entertain?","Strolling magic scales to the crowd: Tripp works group by group, so tell him your headcount and he'll recommend a length."),
  ],
  related=[BDAY, WED, CORP],
),
}

AREA_PAGES = {
"magician-regina": dict(
  title="Magician in Regina, SK | Tripp Coleman (Trippmagic)",
  desc=f"Regina magician for birthdays, corporate events, weddings and library shows. Performed for Capital GMC and the Conexus Arts Centre. Call {PHONE}.",
  h1="Magician in Regina, Saskatchewan",
  answer="Tripp Coleman (Trippmagic) is a magician who performs throughout Regina, just 10 minutes from his home base in Pilot Butte. His Regina work includes the Conexus Arts Centre, Capital GMC, a Regina Public Library show and private cocktail parties.",
  sections=[
   ("Tripp's Regina performance history",
    "<p><strong>Tripp has a track record across the city.</strong> Regina highlights include:</p>"
    "<ul><li>The <strong>Conexus Arts Centre</strong></li>"
    "<li><strong>Capital GMC</strong></li>"
    "<li>A free family magic show at the <strong>Regina Public Library, Sherwood Village branch</strong> (February 16, 2026)</li>"
    "<li>A private <strong>cocktail party in Regina</strong> (June 2024)</li></ul>"),
   ("Events Tripp performs in Regina",
    f"<p>{L(BDAY,'Kids birthday parties')} in homes and party rooms, {L(CORP,'corporate events')} at hotels, offices and dealerships, {L(WED,'wedding cocktail hours')}, {L(SCHOOL,'school and library programs')}, and {L(PRIV,'private and community events')} across the city.</p>"),
   ("Planning tips for Regina events",
    "<p><strong>Regina events range from basement birthday parties to ballroom galas</strong>, and Tripp adjusts the format to fit. For a home party, a cleared living room is plenty. For a hotel or hall, let him know the room size so he can decide between strolling magic and a stage set with a headset microphone and PA.</p>"
    "<p>If your event is downtown, tell Tripp about parking or loading so he arrives ready to start on time.</p>"),
   ("Travel and scheduling in Regina",
    "<p>Because Pilot Butte sits right on Regina's east edge, Tripp can usually reach any Regina neighbourhood in well under half an hour. If your date is fixed, reach out early: weekend evenings are usually the first slots to go.</p>"),
  ],
  faq=[
   ("Do you charge extra to travel into Regina?","Tripp is about 10 minutes from Regina, so Regina events are part of his core area. Your quote will spell out any travel cost."),
   ("Where in Regina have you performed?","Regina performances include the Conexus Arts Centre, Capital GMC, the Regina Public Library's Sherwood Village branch and private cocktail parties."),
   ("How much does a magician cost in Regina?",f"Tripp's shows start at around {PRICE_FROM}, depending on length, event type and audience size."),
  ],
),
"magician-pilot-butte": dict(
  title="Magician in Pilot Butte, SK | Tripp Coleman",
  desc="Pilot Butte's hometown magician. Tripp Coleman (Trippmagic) performs birthday parties, community events and corporate shows from his Pilot Butte base.",
  h1="Magician in Pilot Butte, Saskatchewan",
  answer="Tripp Coleman is Pilot Butte's hometown magician. He lives and books his shows from Pilot Butte, so local birthday parties, school events and community gatherings are right around the corner.",
  sections=[
   ("Book your hometown magician",
    "<p><strong>When you book Tripp in Pilot Butte, the magician is your neighbour.</strong> There's no long drive and no guessing about the area. He knows the community and the kind of crowd a Pilot Butte party draws.</p>"),
   ("Popular Pilot Butte bookings",
    f"<ul><li>{L(BDAY,'Birthday parties')} at home or in a rented hall</li>"
    f"<li>{L(SCHOOL,'School fun days and library programs')}</li>"
    f"<li>{L(PRIV,'Community events, BBQs and family reunions')}</li>"
    f"<li>{L(CORP,'Staff parties')} for local businesses</li></ul>"),
   ("Why booking local helps",
    "<p><strong>A local magician is easier to plan around.</strong> Short travel means more flexibility on start times, simpler scheduling for weeknight events, and less risk from winter roads. It also means you can reach Tripp directly by phone or text at {PHONE} instead of going through an agency.</p>".replace("{PHONE}", PHONE)),
   ("Nearby communities",
    f"<p>From Pilot Butte, Tripp regularly heads west to {L(REGINA,'Regina')}, south to {L(WC,'White City and Emerald Park')}, and east along Highway 1 to {L(BAL,'Balgonie')}.</p>"),
  ],
  faq=[
   ("Is Tripp Coleman based in Pilot Butte?","Yes. Tripp books all of his shows from Pilot Butte, Saskatchewan."),
   ("Can you perform at a small house party?","Yes. Close-up magic works for a handful of guests in a living room as well as for big crowds."),
   ("How do I check availability?",f"Call or text {PHONE} with your date."),
  ],
),
"magician-white-city-emerald-park": dict(
  title="Magician in White City & Emerald Park | Tripp Coleman",
  desc="Magician for White City and Emerald Park birthday parties, backyard events and business functions. Minutes from Tripp Coleman's Pilot Butte base.",
  h1="Magician in White City and Emerald Park",
  answer="Tripp Coleman performs magic for families and businesses in White City and Emerald Park, a short drive from his home base in Pilot Butte. Most bookings here are kids' birthday parties, backyard gatherings and staff events.",
  sections=[
   ("Why families here book Tripp",
    "<p><strong>White City and Emerald Park are growing family communities</strong>, with plenty of birthday parties and backyard get-togethers. Tripp's interactive style suits exactly that: kids up front, adults behind, and everybody involved.</p>"
    f"<p>See the {L(BDAY,'birthday party magic page')} for what a kids' show includes.</p>"),
   ("Business events in Emerald Park",
    f"<p>Emerald Park's business community makes it a natural fit for {L(CORP,'corporate magic')}: staff appreciation nights, customer events and holiday parties, with strolling close-up magic that needs no stage.</p>"),
   ("Planning tips for White City and Emerald Park",
    "<p><strong>Backyard parties are common here</strong>, so plan a spot out of strong wind for the magic: a patio, garage or shaded corner works. For indoor parties, a cleared basement or living room is plenty. Business events in Emerald Park can use strolling magic at a staff party or customer event with no stage or sound needed.</p>"),
   ("Getting here",
    f"<p>Both communities sit just south of Highway 1, minutes from Pilot Butte, so there's rarely any travel concern. Tripp also covers neighbouring {L(BAL,'Balgonie')} and {L(REGINA,'Regina')}.</p>"),
  ],
  faq=[
   ("Do you perform in White City and Emerald Park?","Yes. Both are minutes from Tripp's base in Pilot Butte."),
   ("Can you perform a backyard party?","Yes. Strolling close-up magic works outdoors as well as inside."),
   ("How much does a magician cost in White City?",f"Shows start at around {PRICE_FROM}; your quote depends on length and event type."),
  ],
),
"magician-balgonie": dict(
  title="Magician in Balgonie, SK | Tripp Coleman (Trippmagic)",
  desc="Magician for Balgonie birthday parties, school events and community gatherings. Tripp Coleman travels from nearby Pilot Butte. Call or text 306-209-8861.",
  h1="Magician in Balgonie, Saskatchewan",
  answer="Tripp Coleman performs magic in Balgonie, a short drive east of his home base in Pilot Butte along Highway 1. He's a fit for birthday parties, school and library programs, and community events in town.",
  sections=[
   ("Small-town events, big reactions",
    "<p><strong>In a community like Balgonie, the whole town shows up to the event.</strong> Tripp's strolling magic is built for that kind of crowd: he works through the room group by group, so the kids at the front and the grandparents at the back all get a turn.</p>"),
   ("Popular Balgonie bookings",
    f"<ul><li>{L(BDAY,'Birthday parties')}</li><li>{L(SCHOOL,'School and library shows')}</li>"
    f"<li>{L(PRIV,'Community events, fundraisers and family reunions')}</li><li>{L(WED,'Wedding receptions')}</li></ul>"),
   ("Planning tips for Balgonie events",
    "<p><strong>Community halls, rinks and school gyms are typical spaces for Balgonie events.</strong> In a big room, Tripp uses a wireless headset microphone and PA for a stage set, or he can stroll through the crowd group by group with no sound at all. Tell him which setup your venue has.</p>"),
   ("Travel",
    f"<p>Balgonie is a quick trip down Highway 1 from Pilot Butte. Tripp also covers {L(WC,'White City and Emerald Park')} and {L(REGINA,'Regina')}, and travels up to about 200 miles for events.</p>"),
  ],
  faq=[
   ("Do you travel to Balgonie?","Yes. Balgonie is a short drive east of Tripp's base in Pilot Butte."),
   ("Do you perform at community fundraisers?","Yes. Tripp has performed at nonprofit events, including one in Radville, SK."),
   ("How do I book a show in Balgonie?",f"Call or text {PHONE} or use the booking form."),
  ],
),
"magician-moose-jaw": dict(
  title="Magician in Moose Jaw, SK | Tripp Coleman (Trippmagic)",
  desc="Magician for Moose Jaw corporate events, weddings, birthday parties and school shows. Tripp Coleman travels from the Regina area. Call 306-209-8861.",
  h1="Magician in Moose Jaw, Saskatchewan",
  answer="Tripp Coleman travels to Moose Jaw for corporate events, weddings, birthday parties and school shows. Moose Jaw is about 70 km west of Regina, well within the roughly 200-mile range he covers from Pilot Butte.",
  sections=[
   ("Booking a Regina-area magician in Moose Jaw",
    "<p><strong>Moose Jaw events get the same full show</strong> Tripp performs in Regina. The only difference is planning: because it's a longer drive, give him your date as early as possible, and expect travel to be part of the quote.</p>"),
   ("Events Tripp performs in Moose Jaw",
    f"<ul><li>{L(CORP,'Corporate events')}: staff parties, client nights and conferences</li>"
    f"<li>{L(WED,'Wedding cocktail hours and receptions')}</li>"
    f"<li>{L(BDAY,'Birthday parties')}</li><li>{L(SCHOOL,'School and library programs')}</li></ul>"),
   ("Planning tips for Moose Jaw events",
    "<p><strong>Share the venue address and start time early</strong> so Tripp can plan the drive west on Highway 1. For hotels and halls, mention the room size so he can bring the right setup: strolling close-up magic needs nothing, while a stage set uses a headset microphone and PA.</p>"),
   ("Combining dates",
    "<p>Planning more than one event in Moose Jaw, like an afternoon school show and an evening private party? Ask about booking them on the same day.</p>"),
  ],
  faq=[
   ("Do you travel to Moose Jaw?","Yes. Moose Jaw is about 70 km west of Regina, well within Tripp's travel range."),
   ("Is there a travel fee for Moose Jaw?","Travel is included in your quote and depends on the event. Ask when you book."),
   ("How far ahead should I book for Moose Jaw?","As early as you can, since longer-distance dates need more planning."),
  ],
),
}
