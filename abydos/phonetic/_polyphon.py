# Copyright 2026 by OpenAI.
# This file is part of Abydos.
#
# Abydos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abydos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.
#
# Portions of this file are adapted from the MIT-licensed `Krokochik/polyphon`
# implementation by Pavel Petrov.

"""abydos.phonetic._polyphon.

Polyphon
"""

from __future__ import annotations

import unicodedata

from ._phonetic import _Phonetic

__all__ = ['Polyphon']


_LATIN_MAP = {
    'a': 'а',
    'e': 'е',
    'o': 'о',
    'c': 'с',
    'x': 'х',
    'b': 'в',
    'm': 'м',
    'h': 'н',
}

_VOWELS = frozenset('иаоуыэяёею')

_LETTER_MAP = {
    'е': 'а',
    'ё': 'а',
    'и': 'а',
    'о': 'а',
    'ы': 'а',
    'э': 'а',
    'я': 'а',
    'б': 'п',
    'в': 'ф',
    'г': 'к',
    'д': 'т',
    'з': 'с',
    'щ': 'ш',
    'ж': 'ш',
    'м': 'н',
    'ю': 'у',
}

_SEQUENCE_RULES = sorted(
    {
        'ака': 'афа',
        'ан': 'н',
        'зч': 'ш',
        'лнц': 'нц',
        'лфстф': 'лстф',
        'нат': 'н',
        'нтц': 'нц',
        'нт': 'н',
        'нта': 'на',
        'нтк': 'нк',
        'нтс': 'нс',
        'нтск': 'нск',
        'нтш': 'нш',
        'око': 'офо',
        'пал': 'пл',
        'ртч': 'рч',
        'ртц': 'рц',
        'сп': 'сф',
        'тся': 'ц',
        'стл': 'сл',
        'стн': 'сн',
        'сч': 'ш',
        'сш': 'ш',
        'тат': 'т',
        'тса': 'ц',
        'таф': 'тф',
        'тс': 'тц',
        'тц': 'ц',
        'тч': 'ч',
        'фак': 'фк',
        'фстф': 'стф',
        'шч': 'ч',
    }.items(),
    key=lambda item: len(item[0]),
    reverse=True,
)


def _replace_latin(text: str) -> str:
    return ''.join(_LATIN_MAP.get(char, char) for char in text)


def _repair_cyrillic_diacritics(text: str) -> str:
    repaired = []
    idx = 0
    while idx < len(text):
        char = text[idx]
        next_char = text[idx + 1] if idx + 1 < len(text) else ''
        if char == 'е' and next_char == '\u0308':
            repaired.append('ё')
            idx += 2
        elif char == 'и' and next_char == '\u0306':
            repaired.append('й')
            idx += 2
        else:
            repaired.append(char)
            idx += 1
    return ''.join(repaired)


def _remove_noise_lowercase(text: str) -> str:
    return ''.join(
        char
        for char in text
        if (('а' <= char <= 'я') or char == 'ё') and char not in {'ь', 'ъ'}
    )


def _normalize(text: str) -> str:
    text = unicodedata.normalize('NFKD', text)
    text = text.lower()
    text = _replace_latin(text)
    text = _repair_cyrillic_diacritics(text)
    return _remove_noise_lowercase(text)


def _remove_repeats(text: str) -> str:
    if not text:
        return text
    reduced = [text[0]]
    for char in text[1:]:
        if char != reduced[-1]:
            reduced.append(char)
    return ''.join(reduced)


def _reduce_vowels(text: str) -> str:
    chars = list(text)
    syllables = 0
    consonants = 0
    first_vowel_idx = None
    enough_syllables = False

    for idx, char in enumerate(chars):
        if char in _VOWELS:
            if first_vowel_idx is None:
                first_vowel_idx = idx
            syllables += 1
        else:
            consonants += 1
        if syllables >= 3 or (syllables >= 1 and consonants >= 4):
            enough_syllables = True
            break

    if not enough_syllables:
        return text

    reduced = []
    one_skipped = False
    for idx in range(len(chars) - 1, -1, -1):
        char = chars[idx]
        if char in _VOWELS:
            if one_skipped and idx != first_vowel_idx:
                continue
            one_skipped = True
        reduced.append(char)
    return ''.join(reversed(reduced))


def _replace_letters(text: str) -> str:
    return ''.join(_LETTER_MAP.get(char, char) for char in text)


def _replace_sequences(text: str) -> str:
    chars = list(text)
    output = []
    idx = 0
    while idx < len(chars):
        matched = False
        for pattern, replacement in _SEQUENCE_RULES:
            end = idx + len(pattern)
            if ''.join(chars[idx:end]) == pattern:
                output.append(replacement)
                idx = end
                matched = True
                break
        if not matched:
            output.append(chars[idx])
            idx += 1
    return ''.join(output)


class Polyphon(_Phonetic):
    """Polyphon.

    Russian-language phonetic matching algorithm operating directly on
    Cyrillic text.

    Examples
    --------
    >>> pe = Polyphon()
    >>> pe.encode('Литие')
    'лата'
    >>> pe.encode('ладо')
    'лата'
    """

    def encode(self, word: str) -> str:
        word = _normalize(word)
        word = _remove_repeats(word)
        word = _reduce_vowels(word)
        word = _replace_letters(word)
        word = _replace_sequences(word)
        return word
