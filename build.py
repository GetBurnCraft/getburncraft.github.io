"""Builds index.html from template.html, putting the ant mark's outline into the hero animation."""
import re, pathlib
here = pathlib.Path(__file__).parent
svg = (here / "img" / "ant-mark.svg").read_text()
d = re.search(r' d="([^"]+)"', svg).group(1)
t = re.search(r'transform="([^"]+)"', svg).group(1)
html = (here / "template.html").read_text().replace("{{ANT_D}}", d).replace("{{ANT_T}}", t)
(here / "index.html").write_text(html)
print("index.html", len(html), "bytes")
