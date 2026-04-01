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

"""Tests for abydos.phonetic.Metaphone3."""

from abydos.phonetic import Metaphone3


def test_metaphone3_basic_words():
    """Test Metaphone 3 against public upstream examples."""
    pa = Metaphone3()

    assert pa.encode('') == ','
    assert pa.encode('A') == 'A,'
    assert pa.encode('ack') == 'AK,'
    assert pa.encode('eek') == 'AK,'
    assert pa.encode('ache') == 'AK,AX'
    assert pa.encode('Smith') == 'SM0,XMT'
    assert pa.encode('Schmidt') == 'XMT,'


def test_metaphone3_options():
    """Test Metaphone 3 option handling."""
    assert Metaphone3(encode_vowels=True).encode('supernode') == 'SAPARNAT,'
    assert Metaphone3(encode_exact=True).encode('bob') == 'BB,'
    assert (
        Metaphone3(encode_vowels=True, encode_exact=True).encode('dave')
        == 'DAV,'
    )
