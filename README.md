# Tripp Coleman website

Static site for magician Tripp Coleman (Trippmagic), Pilot Butte, SK.

- Edit content in `build/site_data.py` (facts, contact, services, areas) and `build/pages.py` (page copy).
- Rebuild: `python3 build/build.py` → writes `public/`.
- Vercel serves `public/` (see `vercel.json`). No build step on Vercel.
- Before launch: set `SITE` in `build/site_data.py` to the real domain and rebuild.
- Analytics: set `GA_ID` (or `PLAUSIBLE_DOMAIN`) and `GSC_VERIFY` in `build/build.py`.
