# Convertit la source Markdown du chapitre 3 (format de writer_guide.md) en modules Dart, et remplace
# la liste chapter3Modules de lib/core/data/chapter3_data.dart. Repris de tool/exercices_ch2/md_vers_dart.py.
# La section 4 (défi facultatif sur les matières procédurales) est rédigée par sa propre session : tant
# qu'elle n'a pas les identifiants de son plan, assign_ids_sec4 la numérote comme les sections 1 à 3.
#
# Usage, depuis la racine du dépôt, avec le Python livré avec Blender :
#   "C:\Program Files\Blender Foundation\Blender 5.2\5.2\python\bin\python.exe" -I ^
#       tool\exercices_ch3\md_vers_dart.py
#
# Règles de lecture (celles du guide, précisées) :
# - « ## » : TitleModule ; « ### Recette… » ou « ### Consignes… » : ListModule (intro, puces, conclusion) ;
#   autre « ### » : TextModule, qui continue sur les paragraphes suivants ;
# - blocs ```side-by-side```, ```resource```, ```quiz``` ; « ![légende](chemin) » : FullMediaModule ;
# - encarts « > [!TYPE] » : NOTE et IMPORTANT -> info, TIP -> tip, WARNING -> warning,
#   CAUTION -> challenge, IDEA -> idea ;
# - identifiants des sections 1 à 3 : ch3_secN_title, puis ch3_secN_<type><n> (txt, list, side, media,
#   info, tip, warn, chal, idea, quiz, res), numérotés par section et par type, comme au chapitre 2.
#   L'atelier du second coloris fait partie de la section 3.

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(ROOT, "_resources", "PRC02-SU-26v01_chap3_matieres_finitions_sans_uv.md")
DART = os.path.join(ROOT, "lib", "core", "data", "chapter3_data.dart")
CHAPTER_TITLE = "Matières et finitions réalistes sans dépliage UV"

INFO = {"NOTE": "info", "IMPORTANT": "info", "TIP": "tip", "WARNING": "warning", "CAUTION": "challenge", "IDEA": "idea"}
SHORT = {"info": "info", "tip": "tip", "warning": "warn", "challenge": "chal", "idea": "idea"}


def dart_str(s):
    s = s.replace("\\", "\\\\").replace("'", "\\'").replace("$", "\\$").replace("\n", "\\n")
    return "'" + s + "'"


def yaml_block(lines):
    """YAML simple : clés « k: "v" », listes « - "v" » ou « - 0 »."""
    data, key = {}, None
    for ln in lines:
        if not ln.strip():
            continue
        m = re.match(r'^(\w+):\s*(.*)$', ln)
        if m and not ln.startswith(" "):
            key, val = m.group(1), m.group(2).strip()
            if val == "":
                data[key] = []
            else:
                data[key] = val[1:-1] if val.startswith('"') else val
            continue
        m = re.match(r'^\s+-\s+(.*)$', ln)
        if m and key is not None:
            v = m.group(1).strip()
            data[key].append(v[1:-1] if v.startswith('"') else int(v))
    return data


def parse(text):
    lines = text.splitlines()
    mods, i, n = [], 0, len(lines)

    def is_start(ln):
        return (ln.startswith("#") or ln.startswith("```") or ln.startswith("![") or ln.startswith(">"))

    while i < n:
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        if ln.startswith("## "):
            mods.append(("title", ln[3:].strip()))
            i += 1
        elif ln.startswith("```"):
            kind = ln[3:].strip()
            j = i + 1
            body = []
            while not lines[j].startswith("```"):
                body.append(lines[j])
                j += 1
            i = j + 1
            if kind == "side-by-side":
                k = body.index("---")
                d = yaml_block(body[:k])
                d["content"] = "\n".join(body[k + 1:]).strip()
                mods.append(("side", d))
            else:
                mods.append((kind, yaml_block(body)))
        elif ln.startswith("!["):
            m = re.match(r'^!\[(.*)\]\((.*)\)\s*$', ln)
            mods.append(("media", {"caption": m.group(1), "imagePath": m.group(2)}))
            i += 1
        elif ln.startswith("> [!"):
            t = re.match(r'^> \[!(\w+)\]', ln).group(1)
            j = i + 1
            body = []
            while j < n and lines[j].startswith(">"):
                body.append(lines[j][2:] if lines[j].startswith("> ") else "")
                j += 1
            i = j
            mods.append(("info", {"type": INFO[t], "text": "\n".join(body).strip()}))
        elif ln.startswith("### "):
            title = ln[4:].strip()
            j = i + 1
            if title.startswith(("Recette", "Consignes")):
                intro, items, outro = [], [], []
                while j < n and lines[j].strip() and not lines[j].startswith("- "):
                    intro.append(lines[j]); j += 1
                while j < n and lines[j].startswith("- "):
                    items.append(lines[j][2:].strip()); j += 1
                while j < n and lines[j].strip() and not is_start(lines[j]):
                    outro.append(lines[j]); j += 1
                i = j
                mods.append(("list", {"title": title, "intro": "\n".join(intro).strip() or None,
                                      "items": items, "outro": "\n".join(outro).strip() or None}))
            else:
                paras, cur = [], []
                while j < n:
                    if not lines[j].strip():
                        # le TextModule continue si le paragraphe suivant est du texte simple
                        k = j
                        while k < n and not lines[k].strip():
                            k += 1
                        if k < n and not is_start(lines[k]):
                            paras.append("\n".join(cur)); cur = []
                            j = k
                            continue
                        break
                    if is_start(lines[j]):
                        break
                    cur.append(lines[j]); j += 1
                if cur:
                    paras.append("\n".join(cur))
                i = j
                mods.append(("text", {"title": title, "content": "\n\n".join(paras).strip()}))
        else:
            j = i
            cur = []
            while j < n and lines[j].strip() and not is_start(lines[j]):
                cur.append(lines[j]); j += 1
            i = j
            mods.append(("text", {"title": None, "content": "\n".join(cur).strip()}))
    return mods


def assign_ids_sec4(mods):
    """Section 4 (défi facultatif) : numérotation générique, en attendant les identifiants de son plan."""
    out = []
    counters = {}
    for kind, d in mods:
        if kind == "title":
            out.append(("ch3_sec4_title", kind, d))
            continue
        short = {"text": "txt", "list": "list", "side": "side", "media": "media", "quiz": "quiz",
                 "resource": "res"}.get(kind) or SHORT[d["type"]]
        counters[short] = counters.get(short, 0) + 1
        out.append(("ch3_sec4_%s%d" % (short, counters[short]), kind, d))
    return out


def assign_ids(mods):
    """Sections 1 à 3 : numérotation par section et par type ; section 4, si elle existe : voir plus haut."""
    idx4 = next((i for i, (k, d) in enumerate(mods) if k == "title" and d.startswith("4.")), len(mods))
    out = []
    sec = None
    counters = {}
    for kind, d in mods[:idx4]:
        if kind == "title":
            sec = int(d.split(".")[0])
            assert sec in (1, 2, 3), d
            out.append(("ch3_sec%d_title" % sec, kind, d))
            continue
        assert sec is not None, "module avant le titre de la section 1"
        short = {"text": "txt", "list": "list", "side": "side", "media": "media", "quiz": "quiz",
                 "resource": "res"}.get(kind) or SHORT[d["type"]]
        key = (sec, short)
        counters[key] = counters.get(key, 0) + 1
        if kind == "text" and (d.get("title") or "").startswith("Atelier ·"):
            # identifiant stable, cible du point « Atelier » du programme ; le compteur avance quand même,
            # pour ne pas décaler les identifiants qui suivent
            out.append(("ch3_atelier", kind, d))
            continue
        out.append(("ch3_sec%d_%s%d" % (sec, short, counters[key]), kind, d))
    return out + assign_ids_sec4(mods[idx4:])


def dart_module(mid, kind, d):
    I = "    "
    if kind == "title":
        return "  TitleModule(\n%sid: %s,\n%stitle: %s,\n  )," % (I, dart_str(mid), I, dart_str(d))
    if kind == "text":
        t = ("%stitle: %s,\n" % (I, dart_str(d["title"]))) if d["title"] else ""
        return "  TextModule(\n%sid: %s,\n%s%scontent: %s,\n  )," % (I, dart_str(mid), t, I, dart_str(d["content"]))
    if kind == "side":
        lay = "ContentLayout.textLeft" if d["layout"] == "textLeft" else "ContentLayout.textRight"
        return ("  SideBySideModule(\n%sid: %s,\n%stitle: %s,\n%scontent: %s,\n%simagePath: %s,\n%scaption: %s,\n%slayout: %s,\n  ),"
                % (I, dart_str(mid), I, dart_str(d["title"]), I, dart_str(d["content"]), I, dart_str(d["imagePath"]),
                   I, dart_str(d["caption"]), I, lay))
    if kind == "media":
        return "  FullMediaModule(\n%sid: %s,\n%simagePath: %s,\n%scaption: %s,\n  )," % (
            I, dart_str(mid), I, dart_str(d["imagePath"]), I, dart_str(d["caption"]))
    if kind == "info":
        return "  InfoModule(\n%sid: %s,\n%stype: InfoType.%s,\n%stext: %s,\n  )," % (
            I, dart_str(mid), I, d["type"], I, dart_str(d["text"]))
    if kind == "resource":
        return ("  ResourceModule(\n%sid: %s,\n%stitle: %s,\n%sdescription: %s,\n%sfileName: %s,\n%sdownloadUrl: %s,\n  ),"
                % (I, dart_str(mid), I, dart_str(d["title"]), I, dart_str(d["description"]), I, dart_str(d["fileName"]),
                   I, dart_str(d["downloadUrl"])))
    if kind == "list":
        items = "".join("      %s,\n" % dart_str(x) for x in d["items"])
        s = "  ListModule(\n%sid: %s,\n%stitle: %s,\n" % (I, dart_str(mid), I, dart_str(d["title"]))
        if d["intro"]:
            s += "%sintro: %s,\n" % (I, dart_str(d["intro"]))
        s += "%sitems: [\n%s%s],\n" % (I, items, I)
        if d["outro"]:
            s += "%soutro: %s,\n" % (I, dart_str(d["outro"]))
        return s + "  ),"
    if kind == "quiz":
        opts = "".join("      %s,\n" % dart_str(x) for x in d["options"])
        return ("  QuizModule(\n%sid: %s,\n%squestion: %s,\n%soptions: [\n%s%s],\n%scorrectIndices: [%s],\n%sexplanation: %s,\n  ),"
                % (I, dart_str(mid), I, dart_str(d["question"]), I, opts, I, I,
                   ", ".join(str(x) for x in d["correctIndices"]), I, dart_str(d["explanation"])))
    raise ValueError(kind)


def main():
    text = open(SRC, encoding="utf-8").read()
    mods = assign_ids(parse(text))
    ids = [m[0] for m in mods]
    dup = {x for x in ids if ids.count(x) > 1}
    assert not dup, dup
    missing = []
    for mid, kind, d in mods:
        if kind in ("side", "media"):
            p = os.path.join(ROOT, d["imagePath"].replace("/", os.sep))
            if not os.path.exists(p):
                missing.append(d["imagePath"])
    assert not missing, missing
    body = ["  TitleModule(\n    id: 'ch3_title',\n    title: %s,\n  )," % dart_str(CHAPTER_TITLE)]
    body += [dart_module(*m) for m in mods]
    block = ("const List<ContentModule> chapter3Modules = [\n"
             "  // --- Sections 1 à 3, avec l'atelier ; la section 4 (défi facultatif) suit -------\n"
             "  // Généré par tool/exercices_ch3/md_vers_dart.py depuis\n"
             "  // _resources/PRC02-SU-26v01_chap3_matieres_finitions_sans_uv.md\n"
             + "\n".join(body) + "\n];")
    dart = open(DART, encoding="utf-8").read()
    pat = re.compile(r"const List<ContentModule> chapter3Modules = \[.*?\n\];|const List<ContentModule> chapter3Modules = \[\];", re.S)
    assert len(pat.findall(dart)) == 1, "liste chapter3Modules introuvable ou multiple"
    dart = pat.sub(lambda _: block, dart)
    with open(DART, "w", encoding="utf-8", newline="\n") as f:
        f.write(dart)
    kinds = {}
    for _, k, _d in mods:
        kinds[k] = kinds.get(k, 0) + 1
    print("MODULES", len(mods) + 1, kinds)
    for mid, kind, d in mods:
        print(" ", mid, kind)


if __name__ == "__main__":
    main()
