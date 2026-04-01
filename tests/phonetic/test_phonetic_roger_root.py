# Copyright 2018-2020 by Christopher C. Little.
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

"""abydos.tests.phonetic.test_phonetic_roger_root.

This module contains unit tests for abydos.phonetic.RogerRoot
"""

from abydos.phonetic import RogerRoot


pa = RogerRoot()

def test_roger_root():
    """Test abydos.phonetic.RogerRoot."""
    assert pa.encode('') == '00000'

    # https://naldc.nal.usda.gov/download/27833/PDF
    assert pa.encode('BROWNER') == '09424'
    assert pa.encode('STANLEY') == '00125'
    assert pa.encode('CHALMAN') == '06532'
    assert pa.encode('CHING') == '06270'
    assert pa.encode('ANDERSON') == '12140'
    assert pa.encode('OVERSTREET') == '18401'
    assert pa.encode('HECKEL') == '27500'
    assert pa.encode('WYSZYNSKI') == '40207'
    assert pa.encode('WHITTED') == '41100'
    assert pa.encode('ONGOQO') == '12770'  # PDF had a typo?
    assert pa.encode('JOHNSON') == '32020'
    assert pa.encode('WILLIAMS') == '45300'
    assert pa.encode('SMITH') == '00310'
    assert pa.encode('JONES') == '32000'
    assert pa.encode('BROWN') == '09420'
    assert pa.encode('DAVIS') == '01800'
    assert pa.encode('JACKSON') == '37020'
    assert pa.encode('WILSON') == '45020'
    assert pa.encode('LEE') == '05000'
    assert pa.encode('THOMAS') == '01300'

    assert pa.encode('Defouw') == '01800'
    assert pa.encode('Dauphi') == '01800'
    assert pa.encode('Defazio') == '01800'
    assert pa.encode('Defay') == '01800'
    assert pa.encode('Davy') == '01800'
    assert pa.encode('Defee') == '01800'
    assert pa.encode('Dayhoff') == '01800'
    assert pa.encode('Davie') == '01800'
    assert pa.encode('Davey') == '01800'
    assert pa.encode('Davies') == '01800'
    assert pa.encode('Daves') == '01800'
    assert pa.encode('Deife') == '01800'
    assert pa.encode('Dehoff') == '01800'
    assert pa.encode('Devese') == '01800'
    assert pa.encode('Devoe') == '01800'
    assert pa.encode('Devee') == '01800'
    assert pa.encode('Devies') == '01800'
    assert pa.encode('Devos') == '01800'
    assert pa.encode('Dafoe') == '01800'
    assert pa.encode('Dove') == '01800'
    assert pa.encode('Duff') == '01800'
    assert pa.encode('Duffey') == '01800'
    assert pa.encode('Duffie') == '01800'
    assert pa.encode('Duffy') == '01800'
    assert pa.encode('Duyava') == '01800'
    assert pa.encode('Tafoya') == '01800'
    assert pa.encode('Tevis') == '01800'
    assert pa.encode('Tiffee') == '01800'
    assert pa.encode('Tivis') == '01800'
    assert pa.encode('Thevis') == '01800'
    assert pa.encode('Tovey') == '01800'
    assert pa.encode('Toeves') == '01800'
    assert pa.encode('Tuffs') == '01800'

    assert pa.encode('Samotid') == '00311'
    assert pa.encode('Simmet') == '00310'
    assert pa.encode('Simot') == '00310'
    assert pa.encode('Smead') == '00310'
    assert pa.encode('Smeda') == '00310'
    assert pa.encode('Smit') == '00310'
    assert pa.encode('Smite') == '00310'
    assert pa.encode('Smithe') == '00310'
    assert pa.encode('Smithey') == '00310'
    assert pa.encode('Smithson') == '00310'
    assert pa.encode('Smithy') == '00310'
    assert pa.encode('Smoot') == '00310'
    assert pa.encode('Smyth') == '00310'
    assert pa.encode('Szmodis') == '00310'
    assert pa.encode('Zemaitis') == '00310'
    assert pa.encode('Zmuda') == '00310'

    # Additional tests from @Yomguithereal's talisman
    # https://github.com/Yomguithereal/talisman/blob/master/test/phonetics/roger-root.js
    assert pa.encode('Guillaume') == '07530'
    assert pa.encode('Arlène') == '14520'
    assert pa.encode('Lüdenscheidt') == '05126'

    # no zero_pad
    nzp = RogerRoot(zero_pad=False)
    assert nzp.encode('BROWNER') == '09424'
    assert nzp.encode('STANLEY') == '00125'
    assert nzp.encode('CHALMAN') == '06532'
    assert nzp.encode('CHING') == '0627'
    assert nzp.encode('ANDERSON') == '12140'
    assert nzp.encode('OVERSTREET') == '18401'
    assert nzp.encode('HECKEL') == '275'
    assert nzp.encode('WYSZYNSKI') == '40207'
    assert nzp.encode('WHITTED') == '411'
    assert nzp.encode('ONGOQO') == '1277'
    assert nzp.encode('JOHNSON') == '3202'
    assert nzp.encode('WILLIAMS') == '4530'
    assert nzp.encode('SMITH') == '0031'
    assert nzp.encode('JONES') == '320'
    assert nzp.encode('BROWN') == '0942'
    assert nzp.encode('DAVIS') == '0180'
    assert nzp.encode('JACKSON') == '3702'
    assert nzp.encode('WILSON') == '4502'
    assert nzp.encode('LEE') == '05'
    assert nzp.encode('THOMAS') == '0130'

    # encode_alpha
    assert pa.encode_alpha('BROWNER') == 'PRNR'
    assert pa.encode_alpha('STANLEY') == 'STNL'
    assert pa.encode_alpha('CHALMAN') == 'JLMN'
    assert pa.encode_alpha('CHING') == 'JNK'
