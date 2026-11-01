import os
import json
import re
import datetime

def build_fulltext_repository():
    base_dir = r"d:\医药RAG\data\raw\authentic_full_texts"
    os.makedirs(os.path.join(base_dir, "chp_2020"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "china_gmp"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "nmpa_regulations"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "fda_regulations"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "ich_guidelines"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "eu_mdr"), exist_ok=True)
    print(f"[Archivist] Created authentic full-text directories in {base_dir}")

if __name__ == "__main__":
    build_fulltext_repository()
