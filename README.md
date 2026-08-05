# cdsl-corpus

ケルン大学CDSL（Cologne Digital Sanskrit Dictionaries）のデジタル化辞書群のうち、原著作物がパブリックドメインである30辞書（1832〜1928年刊行の29点＋ケルン自作編纂1点）を収録した辞書コーパスである。Monier-Williams（1899）、Apte（1890）、Böhtlingk-Roth大辞典（1855–75）、Grassmann『リグヴェーダ辞典』、Sörensen『マハーバーラタ固有名索引』、『Śabdakalpadruma』『Vācaspatyam』等を含む。

## 底本

- 取得元: [sanskrit-lexicon/csl-orig](https://github.com/sanskrit-lexicon/csl-orig)（CDSLの正典ソースストア、v02層）
- コミット: `cc2d19927f0c39cd039f39e4a0fd585a8d3a7295`（2026-08-04取得）
- 原機関: Institute of Indology and Tamil Studies, Cologne University（1994年〜）
- CDSL本体: https://www.sanskrit-lexicon.uni-koeln.de/

## 構成

```
dicts/<code>/   各辞書（本文txt＋書誌header.xml＋関連データファイル、無加工）
catalog.csv     全30辞書の書誌・権利判定根拠
```

各辞書フォルダはcsl-origのv02/<code>/直下ファイルをそのまま収録した（作業用prep/サブディレクトリのみ除外）。本文は一切改変していない。

## 符号化に関する注意

サンスクリット語形は**SLP1転写**で符号化されている（IASTではない）。SLP1⇔IAST⇔デーヴァナーガリーの変換は機械的に可能である（例: indic-transliterationライブラリ）。

## 収録範囲と権利

CDSLが公開する44辞書のうち、原著作物の著作権保護期間が満了していることを個別に確認できた29点と、ケルンチーム自身の編纂（pwkvn, 2022）1点のみを収録した。戦後刊行等で著作権が存続しうる14辞書（Edgerton BHSD 1953等）は収録していない。判定根拠はcatalog.csvのunderlying_rights列に記録した。

## catalog.csv

path / code / title / author / year / underlying_rights / license / files / bytes / source_commit

書誌は各辞書のheader.xmlからの機械抽出であり、表記の細部は未検証である。

## ライセンス

CC BY-SA 4.0（csl-origリポジトリの表示を継承。ケルンのデジタル化・マークアップ階層に対するライセンス）。原著作物29点はパブリックドメイン。利用の際はCologne Digital Sanskrit Dictionariesへの帰属表示を行うこと。詳細はNOTICE_CDSL.mdを参照。

## 姉妹リポジトリ

- [pali-corpus](https://github.com/tokushige-koyasan/pali-corpus) ・ [kanseki-corpus](https://github.com/tokushige-koyasan/kanseki-corpus) ・ [kr5-corpus](https://github.com/tokushige-koyasan/kr5-corpus) ・ [gretil-corpus](https://github.com/tokushige-koyasan/gretil-corpus) ・ [sarit-corpus](https://github.com/tokushige-koyasan/sarit-corpus) ・ [dcs-corpus](https://github.com/tokushige-koyasan/dcs-corpus) ・ [muktabodha-corpus](https://github.com/tokushige-koyasan/muktabodha-corpus) ・ [84000-tm-corpus](https://github.com/tokushige-koyasan/84000-tm-corpus)
