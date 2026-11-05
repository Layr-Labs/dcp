"""Small strict checks for current-run derivation artifact delivery."""

import hashlib
from pathlib import Path
import re
from llm_verifier.errors import VerifierError


def require(condition, field):
    if not condition:
        raise VerifierError("dcp_derivation_hosted_" + field)


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def positive_integer(value, field):
    require(type(value) is str and re.fullmatch(r"[1-9][0-9]{0,19}", value), field)
    return int(value)


def sha256(value, field):
    require(type(value) is str and re.fullmatch(r"[0-9a-f]{64}", value), field)
    return value
