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

"""abydos.tests.phonetic.test_phonetic_nysiis.

This module contains unit tests for abydos.phonetic.NYSIIS
"""


from abydos.phonetic import NYSIIS


class TestNysiis:
    """Test NYSIIS functions.

    test cases for abydos.phonetic.NYSIIS
    """

    pa = NYSIIS()
    pa_20 = NYSIIS(max_length=20)
    pa_8mod = NYSIIS(max_length=8, modified=True)
    pa_mod = NYSIIS(modified=True)

    def test_nysiis(self):
        """Test abydos.phonetic.NYSIIS."""
        assert self.pa.encode('') == ''

        # http://coryodaniel.com/index.php/2009/12/30/ruby-nysiis-implementation/
        assert self.pa.encode("O'Daniel") == 'ODANAL'
        assert self.pa.encode("O'Donnel") == 'ODANAL'
        assert self.pa.encode('Cory') == 'CARY'
        assert self.pa.encode('Corey') == 'CARY'
        assert self.pa.encode('Kory') == 'CARY'

        # http://ntz-develop.blogspot.com/2011/03/phonetic-algorithms.html
        assert self.pa.encode('Diggell') == 'DAGAL'
        assert self.pa.encode('Dougal') == 'DAGAL'
        assert self.pa.encode('Doughill') == 'DAGAL'
        assert self.pa.encode('Dougill') == 'DAGAL'
        assert self.pa.encode('Dowgill') == 'DAGAL'
        assert self.pa.encode('Dugall') == 'DAGAL'
        assert self.pa.encode('Dugall') == 'DAGAL'
        assert self.pa.encode('Glinde') == 'GLAND'
        assert self.pa_20.encode('Plumridge') == 'PLANRADG'
        assert self.pa.encode('Chinnick') == 'CANAC'
        assert self.pa.encode('Chinnock') == 'CANAC'
        assert self.pa.encode('Chinnock') == 'CANAC'
        assert self.pa.encode('Chomicki') == 'CANAC'
        assert self.pa.encode('Chomicz') == 'CANAC'
        assert self.pa.encode('Schimek') == 'SANAC'
        assert self.pa.encode('Shimuk') == 'SANAC'
        assert self.pa.encode('Simak') == 'SANAC'
        assert self.pa.encode('Simek') == 'SANAC'
        assert self.pa.encode('Simic') == 'SANAC'
        assert self.pa.encode('Sinnock') == 'SANAC'
        assert self.pa.encode('Sinnocke') == 'SANAC'
        assert self.pa.encode('Sunnex') == 'SANAX'
        assert self.pa.encode('Sunnucks') == 'SANAC'
        assert self.pa.encode('Sunock') == 'SANAC'
        assert self.pa_20.encode('Webberley') == 'WABARLY'
        assert self.pa_20.encode('Wibberley') == 'WABARLY'

        # etc. (for code coverage)
        assert self.pa.encode('Alpharades') == 'ALFARA'
        assert self.pa.encode('Aschenputtel') == 'ASANPA'
        assert self.pa.encode('Beverly') == 'BAFARL'
        assert self.pa.encode('Hardt') == 'HARD'
        assert self.pa.encode('acknowledge') == 'ACNALA'
        assert self.pa.encode('MacNeill') == 'MCNAL'
        assert self.pa.encode('MacNeill') == self.pa.encode('McNeill')
        assert self.pa.encode('Knight') == 'NAGT'
        assert self.pa.encode('Knight') == self.pa.encode('Night')
        assert self.pa.encode('Pfarr') == 'FAR'
        assert self.pa.encode('Phair') == 'FAR'
        assert self.pa.encode('Phair') == self.pa.encode('Pfarr')
        assert self.pa.encode('Cherokee') == 'CARACY'
        assert self.pa.encode('Iraq') == 'IRAG'

        # max_length bounds tests
        assert NYSIIS(max_length=-1).encode('Niall') == 'NAL'
        assert NYSIIS(max_length=0).encode('Niall') == 'NAL'

    def test_modified_nysiis(self):
        """Test abydos.phonetic.NYSIIS (modified version)."""
        assert NYSIIS(max_length=-1, modified=True).encode('') == ''

        # https://naldc.nal.usda.gov/download/27833/PDF
        # Some of these were... wrong... and have been corrected
        assert self.pa_8mod.encode('Daves') == 'DAV'
        assert self.pa_8mod.encode('Davies') == 'DAVY'
        assert self.pa_8mod.encode('Devies') == 'DAFY'
        assert self.pa_8mod.encode('Divish') == 'DAVAS'
        assert self.pa_8mod.encode('Dove') == 'DAV'
        assert self.pa_8mod.encode('Devese') == 'DAFAS'
        assert self.pa_8mod.encode('Devies') == 'DAFY'
        assert self.pa_8mod.encode('Devos') == 'DAF'

        assert self.pa_8mod.encode('Schmit') == 'SNAT'
        assert self.pa_8mod.encode('Schmitt') == 'SNAT'
        assert self.pa_8mod.encode('Schmitz') == 'SNAT'
        assert self.pa_8mod.encode('Schmoutz') == 'SNAT'
        assert self.pa_8mod.encode('Schnitt') == 'SNAT'
        assert self.pa_8mod.encode('Smit') == 'SNAT'
        assert self.pa_8mod.encode('Smite') == 'SNAT'
        assert self.pa_8mod.encode('Smits') == 'SNAT'
        assert self.pa_8mod.encode('Smoot') == 'SNAT'
        assert self.pa_8mod.encode('Smuts') == 'SNAT'
        assert self.pa_8mod.encode('Sneath') == 'SNAT'
        assert self.pa_8mod.encode('Smyth') == 'SNAT'
        assert self.pa_8mod.encode('Smithy') == 'SNATY'
        assert self.pa_8mod.encode('Smithey') == 'SNATY'

        # http://www.dropby.com/NYSIISTextStrings.html
        # Some of these have been altered since the above uses a different set
        # of modifications.
        assert self.pa_8mod.encode('Edwards') == 'EDWAD'
        assert self.pa_8mod.encode('Perez') == 'PAR'
        assert self.pa_8mod.encode('Macintosh') == 'MCANTAS'
        assert self.pa_8mod.encode('Phillipson') == 'FALAPSAN'
        assert self.pa_8mod.encode('Haddix') == 'HADAC'
        assert self.pa_8mod.encode('Essex') == 'ESAC'
        assert self.pa_8mod.encode('Moye') == 'MY'
        assert self.pa_8mod.encode('McKee') == 'MCY'
        assert self.pa_8mod.encode('Mackie') == 'MCY'
        assert self.pa_8mod.encode('Heitschmidt') == 'HATSNAD'
        assert self.pa_8mod.encode('Bart') == 'BAD'
        assert self.pa_8mod.encode('Hurd') == 'HAD'
        assert self.pa_8mod.encode('Hunt') == 'HAN'
        assert self.pa_8mod.encode('Westerlund') == 'WASTARLA'
        assert self.pa_8mod.encode('Evers') == 'EVAR'
        assert self.pa_8mod.encode('Devito') == 'DAFAT'
        assert self.pa_8mod.encode('Rawson') == 'RASAN'
        assert self.pa_8mod.encode('Shoulders') == 'SALDAR'
        assert self.pa_8mod.encode('Leighton') == 'LATAN'
        assert self.pa_8mod.encode('Wooldridge') == 'WALDRAG'
        assert self.pa_8mod.encode('Oliphant') == 'OLAFAN'
        assert self.pa_8mod.encode('Hatchett') == 'HATCAT'
        assert self.pa_8mod.encode('McKnight') == 'MCNAT'
        assert self.pa_8mod.encode('Rickert') == 'RACAD'
        assert self.pa_8mod.encode('Bowman') == 'BANAN'
        assert self.pa_8mod.encode('Vasquez') == 'VASG'
        assert self.pa_8mod.encode('Bashaw') == 'BAS'
        assert self.pa_8mod.encode('Schoenhoeft') == 'SANAFT'
        assert self.pa_8mod.encode('Heywood') == 'HAD'
        assert self.pa_8mod.encode('Hayman') == 'HANAN'
        assert self.pa_8mod.encode('Seawright') == 'SARAT'
        assert self.pa_8mod.encode('Kratzer') == 'CRATSAR'
        assert self.pa_8mod.encode('Canaday') == 'CANADY'
        assert self.pa_8mod.encode('Crepeau') == 'CRAP'

        # Additional tests from @Yomguithereal's talisman
        # https://github.com/Yomguithereal/talisman/blob/master/test/phonetics/nysiis.js
        assert self.pa_8mod.encode('Andrew') == 'ANDR'
        assert self.pa_8mod.encode('Robertson') == 'RABARTSA'
        assert self.pa_8mod.encode('Nolan') == 'NALAN'
        assert self.pa_8mod.encode('Louis XVI') == 'LASXV'
        assert self.pa_8mod.encode('Case') == 'CAS'
        assert self.pa_8mod.encode('Mclaughlin') == 'MCLAGLAN'
        assert self.pa_8mod.encode('Awale') == 'AL'
        assert self.pa_8mod.encode('Aegir') == 'AGAR'
        assert self.pa_8mod.encode('Lundgren') == 'LANGRAN'
        assert self.pa_8mod.encode('Philbert') == 'FALBAD'
        assert self.pa_8mod.encode('Harry') == 'HARY'
        assert self.pa_8mod.encode('Mackenzie') == 'MCANSY'

        # max_length bounds tests
        assert NYSIIS(max_length=-1, modified=True).encode('Niall') == 'NAL'
        assert NYSIIS(max_length=0, modified=True).encode('Niall') == 'NAL'

        # coverage
        assert self.pa_mod.encode('Sam Jr.') == 'ERROR'
        assert self.pa_mod.encode('John Sr.') == 'ERROR'
        assert self.pa_mod.encode('Wright') == 'RAT'
        assert self.pa_mod.encode('Rhodes') == 'RAD'
        assert self.pa_mod.encode('Dgagoda') == 'GAGAD'
        assert self.pa_mod.encode('Bosch') == 'BAS'
        assert self.pa_mod.encode('Schrader') == 'SRADAR'
