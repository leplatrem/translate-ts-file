import xml.etree.ElementTree as ET
from pathlib import Path
import typer
from deep_translator import GoogleTranslator


def main(
    path: Path = typer.Argument(
        ..., help="Path to the Qt Linguist .ts file to translate."
    ),
    target: str = typer.Argument(..., help="Target language code (e.g., 'fr')."),
    output: Path = typer.Option(
        None, help="Optional output file path. Defaults to '<input_stem>-<target>.ts'."
    ),
    source: str = typer.Option("en", help="Source language code (e.g., 'en')."),
    force: bool = typer.Option(
        False, help="Translate all strings, not just unfinished ones."
    ),
):
    """
    Translate a Qt Linguist `.ts` file from one language to another using Google Translate.

    This script will parse the given `.ts` XML file at PATH, translate them from
    the --source language to the --target language, and save the updated `.ts` file at --output

    Example:

        uv run main.py en_EN.ts --target=fr --output=fr_FR.ts
    """
    if output is None:
        output = path.with_name(f"{path.stem}-{target}.ts")

    translator = GoogleTranslator(source=source, target=target)

    # Load and parse XML
    tree = ET.parse(str(path))
    root = tree.getroot()

    # Iterate through all messages
    for context in root.findall("context"):
        for message in context.findall("message"):
            translation_el = message.find("translation")
            source_el = message.find("source")

            if translation_el is None or source_el is None:
                continue

            # Only translate if translation is unfinished
            if force or translation_el.get("type") == "unfinished":
                try:
                    translated_text = translator.translate(source_el.text)
                    translation_el.text = translated_text
                    translation_el.set("type", "finished")
                    print(f"Translated: '{source_el.text}' -> '{translated_text}'")
                except Exception as e:
                    print(f"Error translating '{source_el.text}': {e}")

    # Write updated XML to file
    tree.write(str(output), encoding="utf-8", xml_declaration=True)
    print(f"\n✅ Saved translated file as: {output}")


if __name__ == "__main__":
    typer.run(main)
