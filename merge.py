#!/usr/bin/env python3

import json
from argparse import ArgumentParser
from pathlib import Path

parser = ArgumentParser()
parser.add_argument("source", type=Path, nargs="?", default="wordlist.json")
parser.add_argument(
    "mix_with", type=Path, nargs="?", default="wordlist.en.json"
)
parser.add_argument(
    "target", type=Path, nargs="?", default="wordlist.merged.json"
)
parser.add_argument("--overrides", type=Path, default="overrides.json")
parser.add_argument(
    "-p",
    "--patch",
    type=str,
    nargs="+",
    action="append",
    choices=["all", "songs", "modes", "folders", "default"],
    default=[["default"]],
)
args = parser.parse_args()

PREFIXES = {
    "songs": ["song_"],
    "folders": ["genre_", "folder_"],
    "modes": ["mode_select_"],
}
PREFIXES["all"] = [""]
PREFIXES["default"] = PREFIXES["songs"] + PREFIXES["folders"]


def read_file(path: Path):
    with path.open("r") as f:
        return json.load(f)


def save_file(path: Path, json_data):
    with path.open("w") as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)


def matcher(key: str):
    for patch in args.patch:
        patch = patch[0]
        for prefix in PREFIXES[patch]:
            if key.startswith(prefix):
                return True
    return False


def read_as_dict(path: Path):
    data = read_file(path)
    if "items" not in data:
        raise ValueError(f"Invalid file: {path}, missing 'items' key")
    return {item["key"]: item for item in data["items"]}


mix_data = read_as_dict(args.mix_with)

data = read_file(args.source)
if args.overrides.exists():
    overrides = {x["key"]: x for x in read_file(args.overrides)}
else:
    overrides = {}
if "items" not in data:
    raise ValueError(f"Invalid file: {data}, missing 'items' key")
for index, item in enumerate(data["items"]):
    if item["key"] in overrides:
        data["items"][index] = overrides[item["key"]]
        continue
    if item["key"] in mix_data and matcher(item["key"]):
        data["items"][index] = mix_data[item["key"]]

save_file(args.target, data)
