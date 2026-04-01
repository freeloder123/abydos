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

"""abydos.tests.phonetic.test_phonetic_daitch_mokotoff.

This module contains unit tests for abydos.phonetic.DaitchMokotoff
"""


from abydos.phonetic import DaitchMokotoff


class TestDaitchMokotoff:
    """Test Daitch-Mokotoff Soundex functions.

    test cases for abydos.phonetic.DaitchMokotoff
    """

    pa = DaitchMokotoff()

    def test_daitch_mokotoff(self):
        """Test abydos.phonetic.DaitchMokotoff."""
        # D-M tests
        assert self.pa.encode('') == '000000'

        # http://www.avotaynu.com/soundex.htm
        assert self.pa.encode('Augsburg') == '054795'
        assert self.pa.encode('Breuer') == '791900'
        assert self.pa.encode('Halberstadt') == '587433,587943'
        assert self.pa.encode('Mannheim') == '665600'
        assert self.pa.encode('Chernowitz') == '496740,596740'
        assert self.pa.encode('Cherkassy') == '495400,595400'
        assert self.pa.encode('Kleinman') == '586660'
        assert self.pa.encode('Berlin') == '798600'

        assert self.pa.encode('Ceniow') == '467000,567000'
        assert self.pa.encode('Tsenyuv') == '467000'
        assert self.pa.encode('Holubica') == '587400,587500'
        assert self.pa.encode('Golubitsa') == '587400'
        assert self.pa.encode('Przemysl') == '746480,794648'
        assert self.pa.encode('Pshemeshil') == '746480'
        assert (
            self.pa.encode('Rosochowaciec')
            == '944744,944745,944754,944755,945744,945745,945754,945755'
        )
        assert self.pa.encode('Rosokhovatsets') == '945744'

        # https://en.wikipedia.org/wiki/Daitch%E2%80%93Mokotoff_Soundex
        assert self.pa.encode('Peters') == '734000,739400'
        assert self.pa.encode('Peterson') == '734600,739460'
        assert self.pa.encode('Moskowitz') == '645740'
        assert self.pa.encode('Moskovitz') == '645740'
        assert self.pa.encode('Auerbach') == '097400,097500'
        assert self.pa.encode('Uhrbach') == '097400,097500'
        assert self.pa.encode('Jackson') == '145460,154600,445460,454600'
        assert (
            self.pa.encode('Jackson-Jackson')
            == '145464,145465,154644,154645,154654,445464,445465,454644,' + '454645,454654'
        )

        # http://www.jewishgen.org/infofiles/soundex.html
        assert self.pa.encode('OHRBACH') == '097400,097500'
        assert self.pa.encode('LIPSHITZ') == '874400'
        assert self.pa.encode('LIPPSZYC') == '874400,874500'
        assert self.pa.encode('LEWINSKY') == '876450'
        assert self.pa.encode('LEVINSKI') == '876450'
        assert self.pa.encode('SZLAMAWICZ') == '486740'
        assert self.pa.encode('SHLAMOVITZ') == '486740'

        # http://community.actian.com/wiki/OME_soundex_dm()
        assert self.pa.encode('Schwarzenegger') == '474659,479465'
        assert self.pa.encode('Shwarzenegger') == '474659,479465'
        assert self.pa.encode('Schwartsenegger') == '479465'

        # max_length bounds tests
        assert DaitchMokotoff(max_length=-1).encode('Niall') == '68' + '0' * 62
        assert DaitchMokotoff(max_length=0).encode('Niall') == '680000'

        # zero_pad tests
        assert DaitchMokotoff(max_length=-1, zero_pad=False).encode('Niall') == '68'
        assert DaitchMokotoff(max_length=0, zero_pad=False).encode('Niall') == '68'
        assert DaitchMokotoff(max_length=0, zero_pad=True).encode('Niall') == '680000'
        assert DaitchMokotoff(max_length=6, zero_pad=False).encode('') == '0'
        assert DaitchMokotoff(max_length=6, zero_pad=True).encode('') == '000000'

        # encode_alpha
        assert self.pa.encode_alpha('Augsburg') == 'AKSPRK'
        assert self.pa.encode_alpha('Breuer') == 'PRAR'
        assert self.pa.encode_alpha('Halberstadt') == 'KLPSTT,KLPRST'
        assert self.pa.encode_alpha('Mannheim') == 'NNKN'
        assert self.pa.encode_alpha('Chernowitz') == 'SRNPS,KRNPS'
