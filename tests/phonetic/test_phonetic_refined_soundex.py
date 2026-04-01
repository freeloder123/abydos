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

"""abydos.tests.phonetic.test_phonetic_refined_soundex.

This module contains unit tests for abydos.phonetic.RefinedSoundex
"""

from abydos.phonetic import RefinedSoundex


pa = RefinedSoundex()

def test_refined_soundex():
    """Test abydos.phonetic.RefinedSoundex."""
    # http://ntz-develop.blogspot.com/2011/03/phonetic-algorithms.html
    assert pa.encode('Braz') == 'B95'
    assert pa.encode('Broz') == 'B95'
    assert pa.encode('Caren') == 'C98'
    assert pa.encode('Caron') == 'C98'
    assert pa.encode('Carren') == 'C98'
    assert pa.encode('Charon') == 'C98'
    assert pa.encode('Corain') == 'C98'
    assert pa.encode('Coram') == 'C98'
    assert pa.encode('Corran') == 'C98'
    assert pa.encode('Corrin') == 'C98'
    assert pa.encode('Corwin') == 'C98'
    assert pa.encode('Curran') == 'C98'
    assert pa.encode('Curreen') == 'C98'
    assert pa.encode('Currin') == 'C98'
    assert pa.encode('Currom') == 'C98'
    assert pa.encode('Currum') == 'C98'
    assert pa.encode('Curwen') == 'C98'
    assert pa.encode('Hairs') == 'H93'
    assert pa.encode('Hark') == 'H93'
    assert pa.encode('Hars') == 'H93'
    assert pa.encode('Hayers') == 'H93'
    assert pa.encode('Heers') == 'H93'
    assert pa.encode('Hiers') == 'H93'
    assert pa.encode('Lambard') == 'L8196'
    assert pa.encode('Lambart') == 'L8196'
    assert pa.encode('Lambert') == 'L8196'
    assert pa.encode('Lambird') == 'L8196'
    assert pa.encode('Lampaert') == 'L8196'
    assert pa.encode('Lampard') == 'L8196'
    assert pa.encode('Lampart') == 'L8196'
    assert pa.encode('Lamperd') == 'L8196'
    assert pa.encode('Lampert') == 'L8196'
    assert pa.encode('Lamport') == 'L8196'
    assert pa.encode('Limbert') == 'L8196'
    assert pa.encode('Lombard') == 'L8196'
    assert pa.encode('Nolton') == 'N768'
    assert pa.encode('Noulton') == 'N768'

    # http://trimc-nlp.blogspot.com/2015/03/the-soundex-algorithm.html
    assert pa.encode('Craig') == 'C94'
    assert pa.encode('Crag') == 'C94'
    assert pa.encode('Crejg') == 'C94'
    assert pa.encode('Creig') == 'C94'
    assert pa.encode('Craigg') == 'C94'
    assert pa.encode('Craug') == 'C94'
    assert pa.encode('Craiggg') == 'C94'
    assert pa.encode('Creg') == 'C94'
    assert pa.encode('Cregg') == 'C94'
    assert pa.encode('Creag') == 'C94'
    assert pa.encode('Greg') == 'G94'
    assert pa.encode('Gregg') == 'G94'
    assert pa.encode('Graig') == 'G94'
    assert pa.encode('Greig') == 'G94'
    assert pa.encode('Greggg') == 'G94'
    assert pa.encode('Groeg') == 'G94'
    assert pa.encode('Graj') == 'G94'
    assert pa.encode('Grej') == 'G94'
    assert pa.encode('Grreg') == 'G94'
    assert pa.encode('Greag') == 'G94'
    assert pa.encode('Grig') == 'G94'
    assert pa.encode('Kregg') == 'K94'
    assert pa.encode('Kraig') == 'K94'
    assert pa.encode('Krag') == 'K94'
    assert pa.encode('Kreig') == 'K94'
    assert pa.encode('Krug') == 'K94'
    assert pa.encode('Kreg') == 'K94'
    assert pa.encode('Krieg') == 'K94'
    assert pa.encode('Krijg') == 'K94'

    # Apache Commons test cases
    # http://svn.apache.org/viewvc/commons/proper/codec/trunk/src/test/java/org/apache/commons/codec/language/RefinedSoundexTest.java?view=markup
    assert pa.encode('testing') == 'T3684'
    assert pa.encode('TESTING') == 'T3684'
    assert pa.encode('The') == 'T'
    assert pa.encode('quick') == 'Q3'
    assert pa.encode('brown') == 'B98'
    assert pa.encode('fox') == 'F5'
    assert pa.encode('jumped') == 'J816'
    assert pa.encode('over') == 'O29'
    assert pa.encode('the') == 'T'
    assert pa.encode('lazy') == 'L5'
    assert pa.encode('dogs') == 'D43'

    # Test with retain_vowels=True
    # http://ntz-develop.blogspot.com/2011/03/phonetic-algorithms.html
    pa_vowels = RefinedSoundex(retain_vowels=True)
    assert pa_vowels.encode('Braz') == 'B905'
    assert pa_vowels.encode('Broz') == 'B905'
    assert pa_vowels.encode('Caren') == 'C0908'
    assert pa_vowels.encode('Caron') == 'C0908'
    assert pa_vowels.encode('Carren') == 'C0908'
    assert pa_vowels.encode('Charon') == 'C0908'
    assert pa_vowels.encode('Corain') == 'C0908'
    assert pa_vowels.encode('Coram') == 'C0908'
    assert pa_vowels.encode('Corran') == 'C0908'
    assert pa_vowels.encode('Corrin') == 'C0908'
    assert pa_vowels.encode('Corwin') == 'C0908'
    assert pa_vowels.encode('Curran') == 'C0908'
    assert pa_vowels.encode('Curreen') == 'C0908'
    assert pa_vowels.encode('Currin') == 'C0908'
    assert pa_vowels.encode('Currom') == 'C0908'
    assert pa_vowels.encode('Currum') == 'C0908'
    assert pa_vowels.encode('Curwen') == 'C0908'
    assert pa_vowels.encode('Hairs') == 'H093'
    assert pa_vowels.encode('Hark') == 'H093'
    assert pa_vowels.encode('Hars') == 'H093'
    assert pa_vowels.encode('Hayers') == 'H093'
    assert pa_vowels.encode('Heers') == 'H093'
    assert pa_vowels.encode('Hiers') == 'H093'
    assert pa_vowels.encode('Lambard') == 'L081096'
    assert pa_vowels.encode('Lambart') == 'L081096'
    assert pa_vowels.encode('Lambert') == 'L081096'
    assert pa_vowels.encode('Lambird') == 'L081096'
    assert pa_vowels.encode('Lampaert') == 'L081096'
    assert pa_vowels.encode('Lampard') == 'L081096'
    assert pa_vowels.encode('Lampart') == 'L081096'
    assert pa_vowels.encode('Lamperd') == 'L081096'
    assert pa_vowels.encode('Lampert') == 'L081096'
    assert pa_vowels.encode('Lamport') == 'L081096'
    assert pa_vowels.encode('Limbert') == 'L081096'
    assert pa_vowels.encode('Lombard') == 'L081096'
    assert pa_vowels.encode('Nolton') == 'N07608'
    assert pa_vowels.encode('Noulton') == 'N07608'

    # http://trimc-nlp.blogspot.com/2015/03/the-soundex-algorithm.html
    assert pa_vowels.encode('Craig') == 'C904'
    assert pa_vowels.encode('Crag') == 'C904'
    assert pa_vowels.encode('Crejg') == 'C904'
    assert pa_vowels.encode('Creig') == 'C904'
    assert pa_vowels.encode('Craigg') == 'C904'
    assert pa_vowels.encode('Craug') == 'C904'
    assert pa_vowels.encode('Craiggg') == 'C904'
    assert pa_vowels.encode('Creg') == 'C904'
    assert pa_vowels.encode('Cregg') == 'C904'
    assert pa_vowels.encode('Creag') == 'C904'
    assert pa_vowels.encode('Greg') == 'G904'
    assert pa_vowels.encode('Gregg') == 'G904'
    assert pa_vowels.encode('Graig') == 'G904'
    assert pa_vowels.encode('Greig') == 'G904'
    assert pa_vowels.encode('Greggg') == 'G904'
    assert pa_vowels.encode('Groeg') == 'G904'
    assert pa_vowels.encode('Graj') == 'G904'
    assert pa_vowels.encode('Grej') == 'G904'
    assert pa_vowels.encode('Grreg') == 'G904'
    assert pa_vowels.encode('Greag') == 'G904'
    assert pa_vowels.encode('Grig') == 'G904'
    assert pa_vowels.encode('Kregg') == 'K904'
    assert pa_vowels.encode('Kraig') == 'K904'
    assert pa_vowels.encode('Krag') == 'K904'
    assert pa_vowels.encode('Kreig') == 'K904'
    assert pa_vowels.encode('Krug') == 'K904'
    assert pa_vowels.encode('Kreg') == 'K904'
    assert pa_vowels.encode('Krieg') == 'K904'
    assert pa_vowels.encode('Krijg') == 'K904'

    # Apache Commons test cases
    # http://svn.apache.org/viewvc/commons/proper/codec/trunk/src/test/java/org/apache/commons/codec/language/RefinedSoundexTest.java?view=markup
    assert pa_vowels.encode('testing') == 'T036084'
    assert pa_vowels.encode('TESTING') == 'T036084'
    assert pa_vowels.encode('The') == 'T0'
    assert pa_vowels.encode('quick') == 'Q03'
    assert pa_vowels.encode('brown') == 'B908'
    assert pa_vowels.encode('fox') == 'F05'
    assert pa_vowels.encode('jumped') == 'J08106'
    assert pa_vowels.encode('over') == 'O209'
    assert pa_vowels.encode('the') == 'T0'
    assert pa_vowels.encode('lazy') == 'L050'
    assert pa_vowels.encode('dogs') == 'D043'

    # length tests
    pa_40 = RefinedSoundex(max_length=4, zero_pad=True)
    assert pa_40.encode('testing') == 'T368'
    assert pa_40.encode('TESTING') == 'T368'
    assert pa_40.encode('The') == 'T000'
    assert pa_40.encode('quick') == 'Q300'
    assert pa_40.encode('brown') == 'B980'
    assert pa_40.encode('fox') == 'F500'
    assert pa_40.encode('jumped') == 'J816'
    assert pa_40.encode('over') == 'O290'
    assert pa_40.encode('the') == 'T000'
    assert pa_40.encode('lazy') == 'L500'
    assert pa_40.encode('dogs') == 'D430'
    pa_4 = RefinedSoundex(max_length=4)
    assert pa_4.encode('The') == 'T'
    assert pa_4.encode('quick') == 'Q3'
    assert pa_4.encode('brown') == 'B98'
    assert pa_4.encode('fox') == 'F5'
    assert pa_4.encode('jumped') == 'J816'
    assert pa_4.encode('over') == 'O29'
    assert pa_4.encode('the') == 'T'
    assert pa_4.encode('lazy') == 'L5'
    assert pa_4.encode('dogs') == 'D43'

    # encode_alpha
    assert pa.encode_alpha('Broz') == 'BRZ'
    assert pa.encode_alpha('Caren') == 'CRN'
    assert pa.encode_alpha('Hairs') == 'HRK'
    assert pa.encode_alpha('Lamperd') == 'LNPRT'
