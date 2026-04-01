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

"""abydos.tests.phonetic.test_phonetic_alpha_sis.

This module contains unit tests for abydos.phonetic.AlphaSIS
"""


from abydos.phonetic import AlphaSIS


class TestAlphaSIS:
    """Test Alpha-SIS functions.

    test cases for abydos.phonetic.AlphaSIS
    """

    pa = AlphaSIS()

    def test_alpha_sis_encode(self):
        """Test abydos.phonetic.AlphaSIS."""
        assert self.pa.encode('') == '00000000000000'

        assert self.pa.encode('Rodgers') == '04740000000000'
        assert self.pa.encode('Rogers') == '04740000000000'
        assert self.pa.encode('Kant') == '07210000000000,06210000000000'
        assert self.pa.encode('Knuth') == '02100000000000'
        assert self.pa.encode('Harper') == '24940000000000'
        assert self.pa.encode('Collier') == '07540000000000,06540000000000'
        assert self.pa.encode('Schultz') == '06500000000000,06510000000000'
        assert self.pa.encode('Livingston') == '05827012000000'

        # tests of repeated letters
        assert self.pa.encode('Colllier') == '07554000000000,06554000000000'
        assert self.pa.encode('Collllier') == '07554000000000,06554000000000'
        assert self.pa.encode('Colllllier') == '07555400000000,06555400000000'
        assert self.pa.encode('Collllllier') == '07555400000000,06555400000000'
        assert self.pa.encode('Colalalier') == '07555400000000,06555400000000'

        # max_length bounds tests
        assert (
            AlphaSIS(max_length=-1).encode('Niall')
            == '0250000000000000000000000000000000000000000000000000000000000000'
        )
        assert AlphaSIS(max_length=0).encode('Niall') == '0250'

        # encode_alpha
        assert self.pa.encode_alpha('Rogers') == 'RKR'
        assert self.pa.encode_alpha('Kant') == 'KNT,JNT'
        assert self.pa.encode_alpha('Knuth') == 'NT'
        assert self.pa.encode_alpha('Harper') == 'HRPR'
