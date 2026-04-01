# CLAUDE.md

## Project Overview

Abydos is a production-grade Python NLP/IR library implementing 70+ phonetic algorithms, string distance metrics, fingerprinting, stemming, tokenization, compression, and statistical functions.

## Quick Reference

```bash
# Install dependencies
pip install -r requirements.txt -r requirements-test.txt
pip install -e .

# Run tests
python -m pytest

# Run linter
ruff check abydos/

# Build docs
cd docs && make html
```

## Architecture

- **Python >=3.11**, tested on 3.11-3.14
- **Single runtime dependency**: numpy>=2.3
- **Build system**: setuptools via `pyproject.toml`
- **License**: GPLv3+

### Package Structure

Each algorithm lives in its own file and class, inheriting from a base class:

| Package | Base Class | Purpose |
|---------|-----------|---------|
| `abydos/phonetic/` | `_Phonetic` | Phonetic encoding algorithms |
| `abydos/distance/` | `_Distance` | String distance/similarity metrics |
| `abydos/fingerprint/` | Base fingerprint class | String fingerprinting |
| `abydos/stemmer/` | Base stemmer class | Stemming algorithms |
| `abydos/tokenizer/` | Base tokenizer class | Tokenization methods |
| `abydos/compression/` | — | Compression algorithms |

### Key Constants (`_Phonetic` base class)

- `MIN_CODE_LENGTH = 4` — Minimum phonetic code length
- `MAX_CODE_LENGTH = 64` — Maximum phonetic code length
- `UNLIMITED_LENGTH = -1` — Sentinel for unlimited length
- `SOUNDEX_VARIANTS` — Valid Soundex variant names

## Code Conventions

- **Docstrings**: NumPy format with Sphinx `:cite:` directives
- **Line length**: 79 characters (PEP 8)
- **Linter**: ruff (target py311)
- **Type hints**: On all public method signatures
- **Parameter validation**: `TypeError` for wrong types, `ValueError` for invalid values

## Testing

- **Framework**: pytest with `--cov=abydos --cov-branch`
- **Style**: Plain `assert` statements (no `unittest.TestCase`)
- **Coverage**: 100% required before pushing
- **Test layout**: mirrors source (e.g., `tests/phonetic/test_phonetic_soundex.py`)

## Making Changes

- Each algorithm is self-contained in its own file
- Always validate inputs via `_validate_word()` and `_validate_max_length()` from the base class
- Run `python -m pytest` before committing
- Run `ruff check abydos/` to check for lint issues
