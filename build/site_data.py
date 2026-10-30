"""Facts and page content for tripp-coleman-site.

Every fact here comes from a public source Travis confirmed belongs to Tripp
(GigSalad trippmagic_pilot_butte, AGNT talent/Tripp, Regina Public Library program 15613483)
or from Travis directly (phone, email, Instagram, Facebook). Do not add claims without a source.
Items marked CONFIRM still need Tripp's sign-off.
"""

SITE = "https://trippmagic.ca"
NAME = "Tripp Coleman"
ALT_NAME = "Trippmagic"
BIZ_NAME = "Tripp Coleman – Trippmagic"
PHONE = "306-209-8861"
PHONE_E164 = "+13062098861"
EMAIL = "trippmagic317@gmail.com"
AREA_LINE = "Pilot Butte, Saskatchewan · Serving Regina & southern Saskatchewan"
FACEBOOK = "https://www.facebook.com/TrippMagic317"
INSTAGRAM = "https://www.instagram.com/trippcoleman317/"
GIGSALAD = "https://www.gigsalad.com/trippmagic_pilot_butte"
AGNT = "https://agnt.com/talent/Tripp"
SAME_AS = [FACEBOOK, INSTAGRAM, AGNT, GIGSALAD]
PRICE_FROM = "$400"          # CONFIRM: GigSalad lists "starts at $400"; BookMyGig360 lists $500
SINCE = 2017                 # AGNT: performing since 2017

SERVICES = [
    # slug, short name, nav label, suit, hero image, image alt
    dict(slug="birthday-party-magician-regina", name="Birthday party magic", label="Birthday parties", suit="&hearts;", red=True,
         img="rain.webp", alt="Regina birthday party magician Tripp Coleman throwing a deck of cards into the air"),
    dict(slug="corporate-event-magician-regina", name="Corporate event magic", label="Corporate events", suit="&clubs;", red=False,
         img="aces.webp", alt="Corporate magician Tripp Coleman fanning the four aces toward the camera"),
    dict(slug="wedding-magician-regina", name="Wedding magic", label="Weddings", suit="&diams;", red=True,
         img="ace.webp", alt="Wedding magician Tripp Coleman holding up the ace of hearts"),
    dict(slug="school-library-magic-shows-saskatchewan", name="School & library shows", label="School & library shows", suit="&spades;", red=False,
         img="phoenix.webp", alt="Tripp Coleman holding up a playing card in front of his face"),
    dict(slug="private-party-community-event-magician-regina", name="Private parties & community events", label="Private & community events", suit="&hearts;", red=True,
         img="throw.webp", alt="Tripp Coleman flinging playing cards against a brick wall"),
]

AREAS = [
    dict(slug="magician-regina", town="Regina", img="spring.webp",
         alt="Regina magician Tripp Coleman springing cards from hand to hand", map="Regina, SK"),
    dict(slug="magician-pilot-butte", town="Pilot Butte", img="levitate.webp",
         alt="Pilot Butte magician Tripp Coleman shaping his hands around an invisible floating object", map="Pilot Butte, SK"),
    dict(slug="magician-white-city-emerald-park", town="White City & Emerald Park", img="hands.webp",
         alt="Close-up of magician Tripp Coleman's hands cutting a red-backed deck", map="White City, SK"),
    dict(slug="magician-balgonie", town="Balgonie", img="aces.webp",
         alt="Magician Tripp Coleman fanning four aces", map="Balgonie, SK"),
    dict(slug="magician-moose-jaw", town="Moose Jaw", img="rain.webp",
         alt="Magician Tripp Coleman throwing cards into the air", map="Moose Jaw, SK"),
]

TESTIMONIALS = [
    dict(quote="Absolutely amazing! From start to finish, Tripp was fantastic and created the perfect atmosphere for our event! His talent and ability to keep everyone entertained made the experience truly memorable.",
         name="Debbie P.", event="Google review", town="", date="October 2026"),
    dict(quote="He moved through the crowd effortlessly, entertaining families one by one.",
         name="Yolanda K.", event="Family BBQ", town="Radville, SK", date="July 2026"),
    dict(quote="Fun, unique.", name="Kaitlyn S.", event="Birthday gathering for 10", town="", date="January 2025"),
    dict(quote="Thank you for doing some amazing magic acts.", name="Christine M.",
         event="Seniors and day care show", town="", date="August 2026"),
]

CLIENTS = ["Capital GMC", "John Deere", "eXp Realty", "Conexus Arts Centre", "Regina Public Library"]

HOME_FAQ = [
    ("How much does a magician cost in Regina?",
     f"Tripp Coleman's shows start at around {PRICE_FROM}. The final price depends on show length, the type of event, audience size and travel. Call or text {PHONE} with your date for an exact quote."),
    ("How long is a magic show?",
     "Tripp's shows run 60 to 120 minutes. Strolling close-up sets for receptions and corporate events can be scheduled across the event instead of as one block."),
    ("What age is magic best for?",
     "Tripp's family shows are built for ages 4 and up, and his close-up and comedy magic works for teens and adults. Mixed-age crowds are normal at his events."),
    ("Do you travel outside Regina?",
     "Yes. Tripp is based in Pilot Butte, about 10 minutes from Regina, and travels up to about 200 miles (320 km) for events, including White City, Emerald Park, Balgonie, Moose Jaw and Radville."),
    ("How far in advance should I book a magician?",
     "Book as soon as you have a date. Weekends around the holidays and in summer fill first, so a few weeks' notice gives you the best chance at your preferred time."),
    ("Do you need a stage or special setup?",
     "No stage is needed for close-up or strolling magic. For larger stage shows, Tripp uses a wireless headset microphone and a PA system, so let him know your room size when you book."),
]
