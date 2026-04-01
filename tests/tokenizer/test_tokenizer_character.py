# Copyright 2019-2020 by Christopher C. Little.
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

"""abydos.tests.tokenizer.test_tokenizer_qgrams.

This module contains unit tests for abydos.tokenizer.QGrams
"""


from abydos.tokenizer import CharacterTokenizer


def test_character_tokenizer():
    """Test abydos.tokenizer.CharacterTokenizer."""
    assert sorted(CharacterTokenizer().tokenize('').get_list()) == []
    assert sorted(CharacterTokenizer().tokenize('a').get_list()) == ['a']

    assert (
        sorted(CharacterTokenizer().tokenize('NELSON').get_list())
        == sorted(['N', 'E', 'L', 'S', 'O', 'N'])
    )

def test_character_tokenizer_intersections():
    """Test abydos.tokenizer.CharacterTokenizer intersections."""
    assert (
        sorted( CharacterTokenizer().tokenize('NELSON') & CharacterTokenizer().tokenize('') )
        == []
    )
    assert (
        sorted( CharacterTokenizer().tokenize('') & CharacterTokenizer().tokenize('NEILSEN') )
        == []
    )
    assert (
        sorted( CharacterTokenizer().tokenize('NELSON') & CharacterTokenizer().tokenize('NEILSEN') )
        == sorted(['N', 'E', 'L', 'S'])
    )
    assert (
        sorted( CharacterTokenizer().tokenize('NAIL') & CharacterTokenizer().tokenize('LIAN') )
        == sorted(['N', 'A', 'I', 'L'])
    )

def test_character_tokenizer_counts():
    """Test abydos.tokenizer.CharacterTokenizer counts."""
    assert CharacterTokenizer().tokenize('').count() == 0
    assert len(CharacterTokenizer().tokenize('').get_list()) == 0

    assert CharacterTokenizer().tokenize('NEILSEN').count() == 7
    assert CharacterTokenizer().tokenize('NELSON').count() == 6

    assert len(CharacterTokenizer().tokenize('NEILSEN').get_list()) == 7
    assert len(CharacterTokenizer().tokenize('NELSON').get_list()) == 6
