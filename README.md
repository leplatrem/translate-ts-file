# translate-ts-file

Translate Qt Linguist TS files

```
uv run main.py --help

 Usage: main.py [OPTIONS] PATH TARGET

 Translate a Qt Linguist `.ts` file from one language to another using Google Translate.

 This script will parse the given `.ts` XML file at PATH, translate them from the --source language to the --target language, and save the updated `.ts` file at --output
 Example:
 uv run main.py en_EN.ts --target=fr --output=fr_FR.ts

╭─ Arguments ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    path        PATH  Path to the Qt Linguist .ts file to translate. [default: None] [required]                                                                                                                                                                           │
│ *    target      TEXT  Target language code (e.g., 'fr'). [default: None] [required]                                                                                                                                                                                       │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --output                  PATH  Optional output file path. Defaults to '<input_stem>-<target>.ts'. [default: None]                                                                                                                                                         │
│ --source                  TEXT  Source language code (e.g., 'en'). [default: en]                                                                                                                                                                                           │
│ --force     --no-force          Translate all strings, not just unfinished ones. [default: no-force]                                                                                                                                                                       │
│ --help                          Show this message and exit.                                                                                                                                                                                                                │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
