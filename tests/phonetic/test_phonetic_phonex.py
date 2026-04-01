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

"""abydos.tests.phonetic.test_phonetic_phonex.

This module contains unit tests for abydos.phonetic.Phonex
"""


from abydos.phonetic import Phonex


class TestPhonex:
    """Test Phonex functions.

    test cases for abydos.phonetic.Phonex
    """

    pa = Phonex()

    def test_phonex(self):
        """Test abydos.phonetic.Phonex."""
        assert self.pa.encode('') == '0000'

        # http://homepages.cs.ncl.ac.uk/brian.randell/Genealogy/NameMatching.pdf
        assert self.pa.encode('Ewell') == 'A400'
        assert self.pa.encode('Filp') == 'F100'
        assert self.pa.encode('Heames') == 'A500'
        assert self.pa.encode('Kneves') == 'N100'
        assert self.pa.encode('River') == 'R160'
        assert self.pa.encode('Corley') == 'C400'
        assert self.pa.encode('Carton') == 'C350'
        assert self.pa.encode('Cachpole') == 'C214'

        assert self.pa.encode('Ewell') == self.pa.encode('Ule')
        assert self.pa.encode('Filp') == self.pa.encode('Philp')
        assert self.pa.encode('Yule') == self.pa.encode('Ewell')
        assert self.pa.encode('Heames') == self.pa.encode('Eames')
        assert self.pa.encode('Kneves') == self.pa.encode('Neves')
        assert self.pa.encode('River') == self.pa.encode('Rivers')
        assert self.pa.encode('Corley') == self.pa.encode('Coley')
        assert self.pa.encode('Carton') == self.pa.encode('Carlton')
        assert self.pa.encode('Cachpole') == self.pa.encode('Catchpole')

        # etc. (for code coverage)
        assert self.pa.encode('Saxon') == 'S250'
        assert self.pa.encode('Wright') == 'R230'
        assert self.pa.encode('Ai') == 'A000'
        assert self.pa.encode('Barth') == 'B300'
        assert self.pa.encode('Perry') == 'B600'
        assert self.pa.encode('Garth') == 'G300'
        assert self.pa.encode('Jerry') == 'G600'
        assert self.pa.encode('Gerry') == 'G600'
        assert self.pa.encode('Camden') == 'C500'
        assert self.pa.encode('Ganges') == 'G500'
        assert self.pa.encode('A-1') == 'A000'

        # max_length bounds tests
        assert (
            Phonex(max_length=-1).encode('Niall')
            == 'N400000000000000000000000000000000000000000000000000000000000000'
        )
        assert Phonex(max_length=0).encode('Niall') == 'N400'

        # zero_pad tests
        assert Phonex(max_length=0, zero_pad=False).encode('Niall') == 'N4'
        assert Phonex(max_length=0, zero_pad=True).encode('Niall') == 'N400'
        assert Phonex(max_length=4, zero_pad=False).encode('') == '0'
        assert Phonex(max_length=4, zero_pad=True).encode('') == '0000'

        # encode_alpha
        assert self.pa.encode_alpha('Ewell') == 'AL'
        assert self.pa.encode_alpha('Filp') == 'FP'
        assert self.pa.encode_alpha('Heames') == 'AN'
        assert self.pa.encode_alpha('Kneves') == 'NP'
