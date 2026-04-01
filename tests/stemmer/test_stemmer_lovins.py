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

"""abydos.tests.stemmer.test_stemmer_lovins.

This module contains unit tests for abydos.stemmer.Lovins
"""


from abydos.stemmer import Lovins

from .. import _corpus_file


stmr = Lovins()


def test_lovins():
    """Test abydos.stemmer.Lovins."""
    # base case
    assert stmr.stem('') == ''

    # test cases from Lovins' "Development of a Stemming Algorithm":
    # http://www.mt-archive.info/MT-1968-Lovins.pdf
    assert stmr.stem('magnesia') == 'magnes'
    assert stmr.stem('magnesite') == 'magnes'
    assert stmr.stem('magnesian') == 'magnes'
    assert stmr.stem('magnesium') == 'magnes'
    assert stmr.stem('magnet') == 'magnet'
    assert stmr.stem('magnetic') == 'magnet'
    assert stmr.stem('magneto') == 'magnet'
    assert stmr.stem('magnetically') == 'magnet'
    assert stmr.stem('magnetism') == 'magnet'
    assert stmr.stem('magnetite') == 'magnet'
    assert stmr.stem('magnetitic') == 'magnet'
    assert stmr.stem('magnetizable') == 'magnet'
    assert stmr.stem('magnetization') == 'magnet'
    assert stmr.stem('magnetize') == 'magnet'
    assert stmr.stem('magnetometer') == 'magnetometer'
    assert stmr.stem('magnetometric') == 'magnetometer'
    assert stmr.stem('magnetometry') == 'magnetometer'
    assert stmr.stem('magnetomotive') == 'magnetomot'
    assert stmr.stem('magnetron') == 'magnetron'
    assert stmr.stem('metal') == 'metal'
    assert stmr.stem('metall') == 'metal'
    assert stmr.stem('metallically') == 'metal'
    assert stmr.stem('metalliferous') == 'metallifer'
    assert stmr.stem('metallize') == 'metal'
    assert stmr.stem('metallurgical') == 'metallurg'
    assert stmr.stem('metallurgy') == 'metallurg'
    assert stmr.stem('induction') == 'induc'
    assert stmr.stem('inductance') == 'induc'
    assert stmr.stem('induced') == 'induc'
    assert stmr.stem('angular') == 'angl'
    assert stmr.stem('angle') == 'angl'

    # missed branch test cases
    assert stmr.stem('feminism') == 'fem'

def test_lovins_snowball():
    """Test abydos.stemmer.Lovins (Snowball testset).

    These test cases are from
    https://github.com/snowballstem/snowball-data/tree/master/lovins
    """
    #  Snowball Lovins test set
    with open(
        _corpus_file('snowball_lovins.csv'), encoding='utf-8'
    ) as snowball_ts:
        next(snowball_ts)
        for line in snowball_ts:
            if line[0] != '#':
                line = line.strip().split(',')
                word, stem = line[0], line[1]
                assert stmr.stem(word) == stem.lower()
