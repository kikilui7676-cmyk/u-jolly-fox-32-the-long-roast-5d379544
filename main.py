import os


def _tulis_roast_panjang():
    baris = "My agent delegates so well it outsourced this roast to me, then committed it under its own name."
    keluar = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(keluar, exist_ok=True)
    with open(os.path.join(keluar, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(baris + "\n")


if __name__ == "__main__":
    _tulis_roast_panjang()
