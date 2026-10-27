"""Synchronize the organizer's single DCP required/optional admission choice."""
import argparse
import json
from pathlib import Path

from llm_verifier.config import normalize
from llm_verifier.files import read_json

from dcp_admission import configure_mode


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--mode", choices=("required", "optional"), required=True)
    args = parser.parse_args()
    config, benchmark = configure_mode(read_json(args.root / "verifier.json"),
                                       read_json(args.root / "benchmark.json"), args.mode)
    normalize(config)
    (args.root / "verifier.json").write_text(json.dumps(config, indent=2) + "\n")
    (args.root / "benchmark.json").write_text(json.dumps(benchmark, indent=2) + "\n")
    print("DCP structured bounds: " + args.mode + "; protected policy copies synchronized")


if __name__ == "__main__":
    main()
