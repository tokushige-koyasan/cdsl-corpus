#!/usr/bin/env python3
"""
generate_lookup.py — cdsl-corpus lookup層生成スクリプト

dicts/ 配下の各辞書本文（CDSL標準のエントリ形式）から lookup/ 配下の
検索用タブ区切りテーブルを機械的に生成する。

生成規則（編集判断を含まない決定的処理のみ）:
1. 各エントリ（<L>行〜<LEND>行）を1行とし、列は
   headword_iast / headword_slp1 / entry_id / page / body とする
2. headword_slp1 は <k1> の値、headword_iast はそのSLP1→IAST機械変換
   （indic-transliteration ライブラリによる）
3. body はエントリ本文の全行を空白連結したもの（原マークアップ保持）。
   行内のタブは空白1つに置換する（TSV整合のため）

使い方: python3 scripts/generate_lookup.py <dicts_dir> <out_dir>
依存:   pip install indic-transliteration
"""
import sys, os, re, csv
from indic_transliteration import sanscript


def to_iast(s):
    try:
        return sanscript.transliterate(s, sanscript.SLP1, sanscript.IAST)
    except Exception:
        return s


def convert_dict(src_txt, out_tsv):
    rows = []
    cur = None
    body = []
    for line in open(src_txt, encoding='utf-8', errors='replace'):
        line = line.rstrip('\n')
        if line.startswith('<L>'):
            m = re.match(r'<L>([^<]*)<pc>([^<]*)<k1>([^<]*)', line)
            cur = (m.group(1), m.group(2), m.group(3)) if m else ('', '', '')
            body = []
        elif line.startswith('<LEND>'):
            if cur:
                L, pc, k1 = cur
                b = re.sub(r'[\t\r]', ' ', ' '.join(body)).strip()
                rows.append([to_iast(k1), k1, L, pc, b])
            cur = None
        elif cur is not None:
            body.append(line)
    with open(out_tsv, 'w', newline='', encoding='utf-8') as o:
        w = csv.writer(o, delimiter='\t')
        w.writerow(['headword_iast', 'headword_slp1', 'entry_id', 'page', 'body'])
        w.writerows(rows)
    return len(rows)


def main(dicts_dir, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    total = 0
    for d in sorted(os.listdir(dicts_dir)):
        src = os.path.join(dicts_dir, d, d + '.txt')
        if not os.path.isfile(src):
            print(f'{d}: 本文txtなし（スキップ）')
            continue
        n = convert_dict(src, os.path.join(out_dir, d + '.tsv'))
        total += n
        print(f'{d:8s} {n:8,d} entries')
    print(f'total: {total:,}')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
