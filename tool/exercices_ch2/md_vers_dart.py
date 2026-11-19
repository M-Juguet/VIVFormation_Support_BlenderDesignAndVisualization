# Convertit toute la source Markdown du chapitre 2 (format de writer_guide.md) en modules Dart, et
# remplace la liste chapter2Modules de lib/core/data/chapter2_data.dart.
# Étend tool/exercices_ch2_defi/md_vers_dart.py aux sections 1 à 3 (contenu de base) ; la section 4
# (défi facultatif) garde exactement ses identifiants.
#
# Usage, depuis la racine du dépôt, avec le Python livré avec Blender :
#   "C:\Program Files\Blender Foundation\Blender 5.2\5.2\python\bin\python.exe" -I ^
#       tool\exercices_ch2\md_vers_dart.py
#
# Règles de lecture (celles du guide, précisées) :
# - « ## » : TitleModule ; « ### Recette… » ou « ### Consignes… » : ListModule (intro, puces, conclusion) ;
#   autre « ### » : TextModule, qui continue sur les paragraphes suivants ;
# - blocs ```side-by-side```, ```resource```, ```quiz``` ; « ![légende](chemin) » : FullMediaModule ;
# - encarts « > [!TYPE] » : NOTE et IMPORTANT -> info, TIP -> tip, WARNING -> warning,
#   CAUTION -> challenge, IDEA -> idea ;
# - identifiants des sections 1 à 3 : ch2_secN_title, puis ch2_secN_<type><n> (txt, list, side, media,
#   info, tip, warn, chal, idea, quiz, res), numérotés par section et par type, comme au chapitre 1 ;
# - identifiants de la section 4 : ceux du plan du défi (ch2_sec4_<étape>_<type><n>), inchangés.

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(ROOT, "_resources", "PRC02-SU-26v01_chap2_modelisation_non_destructive.md")
DART = os.path.join(ROOT, "lib", "core", "data", "chapter2_data.dart")
CHAPTER_TITLE = "Modélisation non destructive : modificateurs et courbes"

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
    out = []
    step = "intro"
    counters = {}
    quiz = 0
    seen_title = False
    first_infos = []
    for kind, d in mods:
        if kind == "title":
            out.append(("ch2_sec4_title", kind, d)); seen_title = True; continue
        if not seen_title:
            out.append(("ch2_info_base_a_venir", kind, d)); continue
        if kind in ("text", "list") and d.get("title"):
            t = d["title"]
            m = re.match(r'^Étape (\d)', t)
            if m:
                step = "e" + m.group(1)
            elif t.startswith("Avant de commencer"):
                step = "e0"
            elif t.startswith("Palier 1"):
                step = "pal1"
            elif t.startswith("Palier 2"):
                step = "pal2"
            elif t.startswith("Atelier"):
                step = "atelier"
        if kind == "quiz":
            quiz += 1
            out.append(("ch2_sec4_quiz%d" % quiz, kind, d)); continue
        if kind == "resource":
            out.append(("ch2_sec4_res1", kind, d)); continue
        if kind == "info" and step == "intro":
            first_infos.append(1)
            special = {1: "ch2_sec4_info_intro", 2: "ch2_sec4_info_rappels"}.get(len(first_infos))
            if d["type"] == "warning":
                special = "ch2_sec4_info_eevee"
            if special:
                out.append((special, kind, d)); continue
        short = {"text": "txt", "list": "list", "side": "side", "media": "media"}.get(kind) or SHORT[d["type"]]
        key = (step, short)
        counters[key] = counters.get(key, 0) + 1
        prefix = "ch2_sec4_" + (step + "_" if step != "intro" else "")
        out.append(("%s%s%d" % (prefix, short, counters[key]), kind, d))
    return out


def assign_ids(mods):
    """Sections 1 à 3 : numérotation par section et par type ; section 4 : logique du défi, inchangée."""
    idx4 = next(i for i, (k, d) in enumerate(mods) if k == "title" and d.startswith("4."))
    out = []
    sec = None
    counters = {}
    for kind, d in mods[:idx4]:
        if kind == "title":
            sec = int(d.split(".")[0])
            assert sec in (1, 2, 3), d
            out.append(("ch2_sec%d_title" % sec, kind, d))
            continue
        assert sec is not None, "module avant le titre de la section 1"
        short = {"text": "txt", "list": "list", "side": "side", "media": "media", "quiz": "quiz",
                 "resource": "res"}.get(kind) or SHORT[d["type"]]
        key = (sec, short)
        counters[key] = counters.get(key, 0) + 1
        out.append(("ch2_sec%d_%s%d" % (sec, short, counters[key]), kind, d))
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
    body = ["  TitleModule(\n    id: 'ch2_title',\n    title: %s,\n  )," % dart_str(CHAPTER_TITLE)]
    body += [dart_module(*m) for m in mods]
    block = ("const List<ContentModule> chapter2Modules = [\n"
             "  // --- Sections 1 à 4 : contenu de base et défi facultatif ---------------------\n"
             "  // Généré par tool/exercices_ch2/md_vers_dart.py depuis\n"
             "  // _resources/PRC02-SU-26v01_chap2_modelisation_non_destructive.md\n"
             + "\n".join(body) + "\n];")
    dart = open(DART, encoding="utf-8").read()
    pat = re.compile(r"const List<ContentModule> chapter2Modules = \[.*?\n\];|const List<ContentModule> chapter2Modules = \[\];", re.S)
    assert len(pat.findall(dart)) == 1, "liste chapter2Modules introuvable ou multiple"
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
