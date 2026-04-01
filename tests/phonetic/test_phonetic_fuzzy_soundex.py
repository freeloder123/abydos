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

"""abydos.tests.phonetic.test_phonetic_fuzzy_soundex.

This module contains unit tests for abydos.phonetic.FuzzySoundex
"""


from abydos.phonetic import FuzzySoundex


class TestFuzzySoundex:
    """Test Fuzzy Soundex functions.

    test cases for abydos.phonetic.FuzzySoundex
    """

    pa = FuzzySoundex()
    pa_4 = FuzzySoundex(4)

    def test_fuzzy_soundex(self):
        """Test abydos.phonetic.FuzzySoundex."""
        assert self.pa.encode('') == '00000'
        # http://wayback.archive.org/web/20100629121128/http://www.ir.iit.edu/publications/downloads/IEEESoundexV5.pdf
        assert self.pa.encode('Kristen') == 'K6935'
        assert self.pa.encode('Krissy') == 'K6900'
        assert self.pa.encode('Christen') == 'K6935'

        # http://books.google.com/books?id=LZrT6eWf9NMC&lpg=PA76&ots=Tex3FqNwGP&dq=%22phonix%20algorithm%22&pg=PA75#v=onepage&q=%22phonix%20algorithm%22&f=false
        assert self.pa_4.encode('peter') == 'P360'
        assert self.pa_4.encode('pete') == 'P300'
        assert self.pa_4.encode('pedro') == 'P360'
        assert self.pa_4.encode('stephen') == 'S315'
        assert self.pa_4.encode('steve') == 'S310'
        assert self.pa_4.encode('smith') == 'S530'
        assert self.pa_4.encode('smythe') == 'S530'
        assert self.pa_4.encode('gail') == 'G400'
        assert self.pa_4.encode('gayle') == 'G400'
        assert self.pa_4.encode('christine') == 'K693'
        assert self.pa_4.encode('christina') == 'K693'
        assert self.pa_4.encode('kristina') == 'K693'

        # etc. (for code coverage)
        assert self.pa.encode('Wight') == 'W3000'
        assert self.pa.encode('Hardt') == 'H6000'
        assert self.pa.encode('Knight') == 'N3000'
        assert self.pa.encode('Czech') == 'S7000'
        assert self.pa.encode('Tsech') == 'S7000'
        assert self.pa.encode('gnomic') == 'N5900'
        assert self.pa.encode('Wright') == 'R3000'
        assert self.pa.encode('Hrothgar') == 'R3760'
        assert self.pa.encode('Hwaet') == 'W3000'
        assert self.pa.encode('Grant') == 'G6300'
        assert self.pa.encode('Hart') == 'H6000'
        assert self.pa.encode('Hardt') == 'H6000'

        # max_length bounds tests
        assert (
            FuzzySoundex(max_length=-1).encode('Niall')
            == 'N400000000000000000000000000000000000000000000000000000000000000'
        )
        assert FuzzySoundex(max_length=0).encode('Niall') == 'N400'

        # zero_pad tests
        assert FuzzySoundex(max_length=-1, zero_pad=False).encode('Niall') == 'N4'
        assert FuzzySoundex(max_length=0, zero_pad=False).encode('Niall') == 'N4'
        assert FuzzySoundex(max_length=0, zero_pad=True).encode('Niall') == 'N400'
        assert FuzzySoundex(max_length=4, zero_pad=False).encode('') == '0'
        assert FuzzySoundex(max_length=4, zero_pad=True).encode('') == '0000'

        # encode_alpha
        assert self.pa.encode_alpha('pete') == 'PT'
        assert self.pa.encode_alpha('pedro') == 'PTR'
        assert self.pa.encode_alpha('stephen') == 'STPN'
        assert self.pa.encode_alpha('steve') == 'STP'
