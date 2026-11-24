# Flag assets

Ten public-domain national flag SVGs used as the city chip on `index.html`.
Every file is stored locally under `assets/flags/<country-code>.svg`; nothing is
hotlinked and no page loads an image from another origin.

- **Source:** `https://flagcdn.com/<code>.svg` — Flagpedia's CDN (`flagpedia.net`).
  Retrieved 2026-11-24 for the H3 direction mockups and copied unchanged from
  `local/mockups/home-v2/images/flags/` into this directory.
- **Licence: public domain.** Flagpedia states that its flag images are in the
  public domain (exempt from copyright); `<code>` is the ISO 3166-1 alpha-2
  country code.
- **Geometry:** the SVGs keep their own source coordinates and aspect ratios
  (viewBoxes from `8×5` to `9600×4800`; Hong Kong, Japan and Portugal carry
  `width`/`height` instead). The chip is a fixed 24×18 CSS box and each flag keeps
  its own aspect inside it, so no flag is stretched. Each `<img>` carries `alt=""`
  because the city name is the adjacent text; the flag adds recognition, not information.

## Files in use

- `ca.svg` — Canada (Montreal)
- `us.svg` — United States (Boston, New York, San Francisco)
- `hu.svg` — Hungary (Budapest)
- `ch.svg` — Switzerland (Geneva)
- `pt.svg` — Portugal (Lisbon)
- `pl.svg` — Poland (Warsaw)
- `hk.svg` — Hong Kong SAR
- `jp.svg` — Japan (Kyoto)
- `kr.svg` — South Korea (Seoul)
- `sg.svg` — Singapore

`plan-event/scripts/city_index.py` fails loudly if a city in
`research/published-cities.json` names a country code with no SVG here.
