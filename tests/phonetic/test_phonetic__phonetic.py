# Copyright 2014-2020 by Christopher C. Little.
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

"""abydos.tests.phonetic.test_phonetic__phonetic.

This module contains unit tests for abydos.phonetic._Phonetic
"""


from abydos.phonetic import Davidson

# noinspection PyProtectedMember
from abydos.phonetic._phonetic import _Phonetic


class TestPhonetic:
    """Test _Phonetic base class.

    test cases for abydos.phonetic._Phonetic
    """

    pa = _Phonetic()
    dav = Davidson()

    def test_phonetic_delete_consecutive_repeats(self):
        """Test abydos.phonetic._Phonetic_delete_consecutive_repeats."""
        assert self.pa._delete_consecutive_repeats('REDDEE') == 'REDE' # noqa: SF01
        assert self.pa._delete_consecutive_repeats('AEIOU') == 'AEIOU' # noqa: SF01
        assert (
            self.pa._delete_consecutive_repeats('AAACCCTTTGGG')
            == 'ACTG'  # noqa: SF01
        )

    def test_phonetic_encode(self):
        """Test abydos.phonetic._Phonetic.encode."""
        assert self.pa.encode('') == ''
        assert self.pa.encode('word') == 'word'

    def test_phonetic_encode_alpha(self):
        """Test abydos.phonetic._Phonetic.encode_alpha."""
        assert self.pa.encode_alpha('') == ''
        assert self.pa.encode_alpha('word') == 'word'
        assert self.dav.encode_alpha('word') == self.dav.encode('word')
