from enum import Enum
from pathlib import Path
import subprocess

REMAKE_ALL = False  # whether to remake cardsheets that have already been built

TEX_MAIN = "src/main.tex"
TMP_DIR = Path("tmp")
OUTPUT_DIR = Path("output")
SETS_DIR = Path("sets")

# depends on main.tex
NUM_ROWS = 7
NUM_COLUMNS = 10
MAX_CARDS = NUM_ROWS * NUM_COLUMNS

UNSAFE_CHARACTERS = {"$", "%"}


class Colour(Enum):
    WHITE = "white"
    BLACK = "black"


def main():
    TMP_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)
    for cat in SETS_DIR.iterdir():
        colour = Colour(cat.stem.split("_")[-1])
        cards = cat.read_text().splitlines()
        for i, card_batch in enumerate(_batch(cards, MAX_CARDS)):
            name = OUTPUT_DIR / f"{cat.stem}_{i}_{len(card_batch)}.png"
            if name.exists() and not REMAKE_ALL:
                continue
            create_cardsheet(name, colour, card_batch)


def _batch(items: list, size: int) -> list:
    for i in range(0, len(items), size):
        yield items[i: i + size]


def create_cardsheet(name: Path, colour: Colour, cards: list[str]) -> None:
    tmp = TMP_DIR / f"{colour.value}.csv"
    with open(tmp, "w") as f:
        f.write("Text\n")
        f.write("\n".join(map(_safe_card, cards)))
    try:
        subprocess.check_call(["pdflatex", f"-output-directory={TMP_DIR}", f"src/{colour.value}.tex"])
    finally:
        tmp.unlink()
    
    subprocess.run(
        [
            "convert",
            "-density",
            "300",
            "-background",
            "white",
            "-alpha",
            "off",
            str(TMP_DIR / f"{colour.value}.pdf"),
            str(name),
        ],
        shell=True
    )


def _safe_card(card: str) -> str:
    card = card.replace("_", r"\underscores")
    for char in UNSAFE_CHARACTERS:
        card = card.replace(char, "\\" + char)
    return card


if __name__ == "__main__":
    main()
