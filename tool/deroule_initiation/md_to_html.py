# Convertit un déroulé formateur (_resources/PRC02-deroule-*.md : l'initiation, puis un par
# chapitre) en HTML imprimable (A4 portrait), à la charte VIV Formation. Sans dépendance : il suffit
# du Python fourni avec Blender.
# Sous-ensemble Markdown pris en charge : titres #, ## et ###, paragraphes, listes à puces
# et numérotées (un niveau d'imbrication), cases [ ], tableaux, citations >, ---,
# code `…`, gras **…**, italique *…*, et le commentaire <!-- pagebreak -->.
# Le surtitre de l'en-tête suit le nom du fichier : « Chapitre N » pour PRC02-deroule-chapN.md,
# « Planche CMF · Mémo participant » pour PRC02-memo-cmf.md, « Initiation » sinon.
# Le mémo seul accepte une image sur sa ligne, ![légende](chemin relatif au .md), et une mise en page
# resserrée sur une page : la sortie des déroulés ne change pas.
#
# Usage : python md_to_html.py <source.md> <sortie.html>

import html, os, re, sys

SRC, OUT = sys.argv[1], sys.argv[2]
_chap = re.search(r"chap(\d+)", os.path.basename(SRC))
MEMO = "memo-cmf" in os.path.basename(SRC)
OVERLINE = f"PRC02 · Chapitre {_chap.group(1)} · Document formateur" if _chap else "PRC02 · Initiation · Document formateur"
if MEMO:
    OVERLINE = "PRC02 · Planche CMF · Mémo participant"

CSS = r"""
@page { size: A4 portrait; margin: 14mm 15mm 16mm; }
@page { @bottom-right { content: counter(page) " / " counter(pages); font: 9pt 'Noto Sans', sans-serif; color: #8a7f86; } }
html, body { margin: 0; padding: 0; background: #fff; }
body { -webkit-print-color-adjust: exact; print-color-adjust: exact; color: var(--ink);
       font-family: var(--font-sans); font-size: 10pt; line-height: 1.45; }
.top-line { height: 5px; background: var(--gradient-brand); margin: 0 0 14px; border-radius: 3px; }
header.doc { display: flex; justify-content: space-between; align-items: flex-end; gap: 24px;
             padding-bottom: 12px; border-bottom: 1px solid var(--border); margin-bottom: 14px; }
header.doc img { height: 30px; width: auto; display: block; margin-bottom: 4px; }
.overline { color: var(--ink-muted); margin: 0 0 4px; font-size: 8.5pt; letter-spacing: .08em; text-transform: uppercase; }
h1 { font-family: var(--font-display); font-style: italic; font-weight: 700; font-size: 25pt; line-height: 1.15; margin: 0; }
.subtitle { margin: 4px 0 0; font-size: 9.5pt; color: var(--ink-muted); }
h2 { font-family: var(--font-sans); font-style: italic; font-weight: 700; font-size: 15pt; line-height: 1.25;
     color: var(--accent-deep); margin: 20px 0 8px; padding-top: 8px; border-top: 2px solid var(--brand-rose);
     break-after: avoid; }
h3 { font-family: var(--font-sans); font-style: italic; font-weight: 700; font-size: 11.5pt; line-height: 1.3;
     margin: 14px 0 6px; break-after: avoid; }
p { margin: 0 0 7px; }
ul, ol { margin: 0 0 8px; padding-left: 20px; }
li { margin: 0 0 3px; }
li > ul, li > ol { margin: 3px 0 0; }
ul.checks { list-style: none; padding-left: 4px; }
ul.checks li::before { content: "☐"; margin-right: 7px; color: var(--accent-deep); }
strong { font-weight: 700; }
code { font-family: var(--font-mono); font-size: 8.6pt; background: var(--surface-code); border: 1px solid var(--border);
       border-radius: 4px; padding: 0 4px; white-space: nowrap; }
table { width: 100%; border-collapse: collapse; margin: 4px 0 10px; font-size: 8.8pt; line-height: 1.35; }
th { text-align: left; font-weight: 700; background: var(--surface-brand); padding: 5px 7px; border-bottom: 1px solid var(--border-strong); }
td { padding: 5px 7px; border-bottom: 1px solid var(--border); vertical-align: top; }
tr { break-inside: avoid; }
td code { white-space: normal; }
blockquote { margin: 8px 0 10px; padding: 8px 12px; background: var(--surface-sunken); border-left: 3px solid var(--action);
             border-radius: 0 8px 8px 0; break-inside: avoid; }
blockquote p { margin: 0; }
hr { border: 0; border-top: 1px solid var(--border); margin: 18px 0 8px; }
hr + p { font-size: 8.5pt; color: var(--ink-subtle); }
.pagebreak { break-before: page; }
.pagebreak + h2 { border-top: 0; margin-top: 0; }
"""


def inline(text):
    codes = []

    def keep(m):
        codes.append("<code>" + html.escape(m.group(1)) + "</code>")
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", keep, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)
    return text


def convert(md):
    lines = md.splitlines()
    out = []
    i = 0
    # En-tête : titre, puis lignes de sous-titre jusqu'au premier ##
    title = lines[0].lstrip("# ").strip()
    i = 1
    sub = []
    while i < len(lines) and not lines[i].startswith("## "):
        if lines[i].strip():
            sub.append(inline(lines[i].strip()))
        i += 1
    out.append('<div class="top-line"></div><header class="doc"><div>')
    out.append(f'<p class="overline">{OVERLINE}</p>')
    out.append(f"<h1>{inline(title)}</h1>")
    for s in sub:
        out.append(f'<p class="subtitle">{s}</p>')
    out.append('</div><img src="../../viv-formation-design-system/assets/logos/viv-formation-couleur.svg" alt="VIV Formation"></header>')

    para = []

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    list_re = re.compile(r"^(\s*)(- \[ \] |- |\d+\. )(.*)$")
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            flush_para(); i += 1; continue
        if s == "<!-- pagebreak -->":
            flush_para(); out.append('<div class="pagebreak"></div>'); i += 1; continue
        if s == "---":
            flush_para(); out.append("<hr>"); i += 1; continue
        img = re.match(r"^!\[(.*)\]\((.+)\)$", s) if MEMO else None
        if img:
            flush_para()
            src = os.path.relpath(os.path.join(os.path.dirname(os.path.abspath(SRC)), img.group(2)),
                                  os.path.dirname(os.path.abspath(OUT))).replace(os.sep, "/")
            out.append(f'<figure><img src="{html.escape(src)}" alt=""><figcaption>{inline(img.group(1))}</figcaption></figure>')
            i += 1; continue
        if s.startswith("### "):
            flush_para(); out.append(f"<h3>{inline(s[4:])}</h3>"); i += 1; continue
        if s.startswith("## "):
            flush_para(); out.append(f"<h2>{inline(s[3:])}</h2>"); i += 1; continue
        if s.startswith(">"):
            flush_para()
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip()); i += 1
            out.append("<blockquote><p>" + inline(" ".join(buf)) + "</p></blockquote>")
            continue
        if s.startswith("|"):
            flush_para()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            head, body = rows[0], [r for r in rows[2:]]
            out.append("<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>")
            for r in body:
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            out.append("</tbody></table>")
            continue
        m = list_re.match(line)
        if m:
            flush_para()
            items = []          # (niveau, type, texte)
            while i < len(lines):
                m = list_re.match(lines[i])
                if not m:
                    if lines[i].strip() and lines[i].startswith("  ") and items:
                        lvl, kind, txt = items[-1]
                        items[-1] = (lvl, kind, txt + " " + lines[i].strip()); i += 1; continue
                    break
                lvl = 1 if len(m.group(1)) >= 2 else 0
                kind = "check" if m.group(2) == "- [ ] " else ("ol" if m.group(2)[0].isdigit() else "ul")
                items.append((lvl, kind, m.group(3))); i += 1
            def tag(kind):
                return ("ol", "") if kind == "ol" else ("ul", ' class="checks"' if kind == "check" else "")
            top_tag, top_attr = tag(items[0][1])
            out.append(f"<{top_tag}{top_attr}>")
            j = 0
            while j < len(items):
                lvl, kind, txt = items[j]
                out.append("<li>" + inline(txt))
                j += 1
                if j < len(items) and items[j][0] == 1:
                    st, sa = tag(items[j][1])
                    out.append(f"<{st}{sa}>")
                    while j < len(items) and items[j][0] == 1:
                        out.append("<li>" + inline(items[j][2]) + "</li>"); j += 1
                    out.append(f"</{st}>")
                out.append("</li>")
            out.append(f"</{top_tag}>")
            continue
        para.append(s); i += 1
    flush_para()
    return "\n".join(out)


MEMO_CSS = r"""
@page { margin: 10mm 12mm 10mm; }
body { font-size: 9pt; line-height: 1.34; }
h1 { font-size: 21pt; }
h2 { font-size: 12.5pt; margin: 10px 0 5px; padding-top: 5px; }
header.doc { margin-bottom: 8px; padding-bottom: 8px; }
li { margin: 0 0 4px; }
figure { margin: 4px 0 6px; }
figure img { display: block; width: 62%; margin: 0 auto; border: 1px solid var(--border); border-radius: 6px; }
figcaption { font-size: 8pt; color: var(--ink-muted); margin-top: 3px; text-align: center; }
"""
if MEMO:
    CSS += MEMO_CSS

md = open(SRC, encoding="utf-8").read()
body = convert(md)
TITLE = html.escape(md.splitlines()[0].lstrip("# ").strip(), quote=False)
doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{TITLE}</title>
<!-- Fichier généré par tool/deroule_initiation/md_to_html.py depuis _resources/{os.path.basename(SRC)} : ne pas modifier à la main. -->
<link rel="stylesheet" href="../../viv-formation-design-system/styles.css">
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>
"""
open(OUT, "w", encoding="utf-8").write(doc)
print("HTML", OUT, len(doc))
