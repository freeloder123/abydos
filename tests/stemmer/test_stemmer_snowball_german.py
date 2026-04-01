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

"""abydos.tests.stemmer.test_stemmer_snowball_german.

This module contains unit tests for abydos.stemmer.SnowballGerman
"""


from abydos.stemmer import SnowballGerman

from .. import _corpus_file


stmr = SnowballGerman()

stmr_av = SnowballGerman(alternate_vowels=True)


def test_snowball_german():
    """Test abydos.stemmer.SnowballGerman (Snowball testset).

    These test cases are from
    http://snowball.tartarus.org/algorithms/german/diffs.txt
    """
    # base case
    assert stmr.stem('') == ''

    #  Snowball German test set
    with open(
        _corpus_file('snowball_german.csv'), encoding='utf-8'
    ) as snowball_ts:
        next(snowball_ts)
        for line in snowball_ts:
            if line[0] != '#':
                line = line.strip().split(',')
                word, stem = line[0], line[1]
                assert stmr.stem(word) == stem.lower()

    # missed branch test cases
    assert stmr.stem('ikeit') == 'ikeit'

def test_sb_german_snowball_alt():
    """Test abydos.stemmer.SnowballGerman (alternate vowels)."""
    # base case
    assert stmr_av.stem('') == ''

    # dämmerung,dammer
    assert stmr_av.stem('dämmerung') == 'dammer'
    assert stmr_av.stem('daemmerung') == 'dammer'
    assert stmr.stem('dämmerung') == 'dammer'
    assert stmr.stem('daemmerung') == 'daemmer'

    # brötchen,brotch
    assert stmr_av.stem('brötchen') == 'brotch'
    assert stmr_av.stem('broetchen') == 'brotch'
    assert stmr.stem('brötchen') == 'brotch'
    assert stmr.stem('broetchen') == 'broetch'

    # büro,buro
    assert stmr_av.stem('büro') == 'buro'
    assert stmr_av.stem('buero') == 'buro'
    assert stmr.stem('büro') == 'buro'
    assert stmr.stem('buero') == 'buero'

    # häufen,hauf
    assert stmr_av.stem('häufen') == 'hauf'
    assert stmr_av.stem('haeufen') == 'hauf'
    assert stmr.stem('häufen') == 'hauf'
    assert stmr.stem('haeufen') == 'haeuf'

    # quelle,quell
    assert stmr_av.stem('qülle') == 'qull'
    assert stmr_av.stem('quelle') == 'quell'
    assert stmr.stem('qülle') == 'qull'
    assert stmr.stem('quelle') == 'quell'

    # feuer,feuer
    assert stmr_av.stem('feür') == 'feur'
    assert stmr_av.stem('feuer') == 'feu'
    assert stmr.stem('feür') == 'feur'
    assert stmr.stem('feuer') == 'feu'

    # über,uber
    assert stmr_av.stem('über') == 'uber'
    assert stmr_av.stem('ueber') == 'uber'
    assert stmr.stem('über') == 'uber'
    assert stmr.stem('ueber') == 'ueb'
