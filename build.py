#!/usr/bin/env python3
"""Génère docs/{fr,ar,en}/*.html à partir de templates/ et i18n.json. Usage : python3 build.py"""
import json, re, shutil, sys
from datetime import date
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).parent
OUT = ROOT / "docs"
I18N = json.loads((ROOT / "i18n.json").read_text())
LANGS = list(I18N["_langs"])
DEFAULT = next(l for l, m in I18N["_langs"].items() if m.get("default"))
DATA = I18N["_data"]
PAGES = ["index", "about", "menu", "events", "booking", "contact"]
NAV = {"index": "home", "about": "about", "menu": "menu", "events": "events", "booking": "booking", "contact": "contact"}
SUB = [("smoked", "menu_smoked"), ("sides", "menu_sides"), ("sauces", "menu_sauces"), ("drinks", "menu_drinks")]
FONTS = {
    "latin": "https://fonts.googleapis.com/css2?family=Cormorant:wght@500;600;700&family=Montserrat:wght@400;500;600&display=swap",
    "ar": "https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@500;700&family=Noto+Sans+Arabic:wght@400;500;600&display=swap",
}
PAGE_TITLE = {"index": "site.tagline", "about": "about.title", "menu": "menu.title",
              "events": "events.title", "booking": "booking.title", "contact": "contact.title"}


def t(key, lang):
    node = I18N
    for part in key.split("."):
        node = node[part]  # KeyError = clé inconnue : on veut que ça casse
    if not node.get(lang):
        sys.exit(f"traduction manquante : {key} [{lang}]")
    return node[lang]


def js_str(s):
    return json.dumps(s, ensure_ascii=False)


def render(tpl, lang, extra):
    def sub(m):
        key, _, flt = m.group(1).partition("|")
        if key in extra:
            val = extra[key]
        else:
            val = t(key, lang)
        return {"": val, "url": quote(val), "js": js_str(val)}[flt]
    out = re.sub(r"\{\{([\w.|]+)\}\}", sub, tpl)
    left = re.findall(r"\{\{[^}]*\}\}", out)
    if left:
        sys.exit(f"placeholders non résolus : {left}")
    return out


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    OUT.mkdir()
    shutil.copy(ROOT / "logo.jpeg", OUT / "logo.jpeg")
    shutil.copy(ROOT / "style.css", OUT / "style.css")
    shutil.copytree(ROOT / "images", OUT / "images")
    (OUT / ".nojekyll").write_text("")
    layout = (ROOT / "templates/layout.html").read_text()

    for lang, meta in I18N["_langs"].items():
        (OUT / lang).mkdir()
        for page in PAGES:
            nav = ""
            for p in PAGES[1:]:
                label = t(f"nav.{NAV[p]}", lang)
                if p == "menu":
                    subs = "".join(f'<a href="menu.html#{a}">{t("nav." + k, lang)}</a>' for a, k in SUB)
                    nav += f'<span class="dd"><a href="menu.html">{label}</a><div>{subs}</div></span>'
                elif p != "booking":  # Réserver est déjà le bouton
                    nav += f'<a href="{p}.html">{label}</a>'
            langswitch = " ".join(
                f"<b>{m['label']}</b>" if l == lang else f'<a href="../{l}/{page}.html" hreflang="{l}">{m["label"]}</a>'
                for l, m in I18N["_langs"].items())
            hreflang = "\n".join(f'<link rel="alternate" hreflang="{l}" href="../{l}/{page}.html">' for l in LANGS)
            extra = {
                "lang": lang, "dir": meta["dir"], "page": page,
                "fonts": FONTS["ar" if lang == "ar" else "latin"].replace("&", "&amp;"), "year": str(date.today().year),
                "phone": DATA["phone"], "phone_raw": DATA["phone"].replace(" ", ""), "wa": DATA["whatsapp"],
                "hours": DATA["hours"] or t("common.tbc", lang),
                "nav": nav, "langswitch": langswitch, "hreflang": hreflang,
            }
            body = render((ROOT / f"templates/{page}.html").read_text(), lang, extra)
            name = t("site.name", lang)
            title = name if page == "index" else f"{t(PAGE_TITLE[page], lang)} — {name}"
            html = render(layout, lang, {**extra, "content": body, "title": title})
            (OUT / lang / f"{page}.html").write_text(html)

    # racine : redirige vers la langue du navigateur, sinon la langue par défaut
    (OUT / "index.html").write_text(f"""<!doctype html><meta charset="utf-8"><title>{t("site.name", DEFAULT)}</title>
<script>var l=(navigator.language||"").slice(0,2);location.replace(({js_str(LANGS)}.indexOf(l)>-1?l:"{DEFAULT}")+"/index.html")</script>
<meta http-equiv="refresh" content="0;url={DEFAULT}/index.html"><a href="{DEFAULT}/index.html">{t("site.name", DEFAULT)}</a>""")
    print(f"ok : {len(LANGS) * len(PAGES)} pages dans {OUT}")


if __name__ == "__main__":
    main()
