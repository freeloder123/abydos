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

"""abydos.tests.stemmer.test_stemmer_porter2.

This module contains unit tests for abydos.stemmer.Porter2
"""


from abydos.stemmer import Porter2


from .. import _corpus_file


class TestPorter2:
    """Test Porter2 functions.

    abydos.stemmer.Porter2
    """

    stmr = Porter2()
    stmr._vowels = set('aeiouy')  # noqa: SF01
    stmr_ee = Porter2(early_english=True)
    stmr_ee._vowels = set('aeiouy')  # noqa: SF01

    def test_porter2(self):
        """Test abydos.stemmer.Porter2."""
        # base case
        assert self.stmr.stem('') == ''

        # simple cases
        assert self.stmr.stem('c') == 'c'
        assert self.stmr.stem('da') == 'da'
        assert self.stmr.stem('ad') == 'ad'
        assert self.stmr.stem('sing') == 'sing'
        assert self.stmr.stem('singing') == 'sing'

        # missed branch test cases
        assert self.stmr.stem('capitalism') == 'capit'
        assert self.stmr.stem('fatalism') == 'fatal'
        assert self.stmr.stem("dog's") == 'dog'
        assert self.stmr.stem("A's'") == 'a'
        assert self.stmr.stem('agreedly') == 'agre'
        assert self.stmr.stem('feedly') == 'feed'
        assert self.stmr.stem('stional') == 'stional'
        assert self.stmr.stem('palism') == 'palism'
        assert self.stmr.stem('sization') == 'sizat'
        assert self.stmr.stem('licated') == 'licat'
        assert self.stmr.stem('lical') == 'lical'
        assert self.stmr.stem('clessly') == 'clessli'
        assert self.stmr.stem('tably') == 'tabli'
        assert self.stmr.stem('sizer') == 'sizer'
        assert self.stmr.stem('livity') == 'liviti'

    def test_porter2_early_english(self):
        """Test abydos.stemmer.Porter2 (early English)."""
        # base case
        assert self.stmr_ee.stem('') == ''

        # simple cases (no different from regular stemmer)
        assert self.stmr_ee.stem('c') == 'c'
        assert self.stmr_ee.stem('da') == 'da'
        assert self.stmr_ee.stem('ad') == 'ad'
        assert self.stmr_ee.stem('sing') == 'sing'
        assert self.stmr_ee.stem('singing') == 'sing'

        # make
        assert self.stmr_ee.stem('make') == 'make'
        assert self.stmr_ee.stem('makes') == 'make'
        assert self.stmr_ee.stem('maketh') == 'make'
        assert self.stmr_ee.stem('makest') == 'make'

        # say
        assert self.stmr_ee.stem('say') == 'say'
        assert self.stmr_ee.stem('says') == 'say'
        assert self.stmr_ee.stem('sayeth') == 'say'
        assert self.stmr_ee.stem('sayest') == 'say'

        # missed branch test cases
        assert self.stmr_ee.stem('best') == 'best'
        assert self.stmr_ee.stem('meth') == 'meth'

    def test_porter2_snowball(self):
        """Test abydos.stemmer.Porter2 (Snowball testset).

        These test cases are from
        http://snowball.tartarus.org/algorithms/english/diffs.txt
        """
        #  Snowball Porter test set
        with open(_corpus_file('snowball_porter2.csv')) as snowball_ts:
            next(snowball_ts)
            for line in snowball_ts:
                if line[0] != '#':
                    line = line.strip().split(',')
                    word, stem = line[0], line[1]
                    assert self.stmr.stem(word) == stem.lower()
