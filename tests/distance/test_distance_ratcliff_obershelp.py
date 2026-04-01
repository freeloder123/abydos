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

"""abydos.tests.distance.test_distance_ratcliff_obershelp.

This module contains unit tests for abydos.distance.RatcliffObershelp
"""

import pytest

from difflib import SequenceMatcher

from abydos.distance import RatcliffObershelp

from .. import _corpus_file


cmp = RatcliffObershelp()


def test_ratcliff_obershelp_sim():
    """Test abydos.distance.RatcliffObershelp.sim."""
    # https://github.com/rockymadden/stringmetric/blob/master/core/src/test/scala/com/rockymadden/stringmetric/similarity/RatcliffObershelpMetricSpec.scala
    assert cmp.sim('', '') == 1
    assert cmp.sim('abc', '') == 0
    assert cmp.sim('', 'xyz') == 0
    assert cmp.sim('abc', 'abc') == 1
    assert cmp.sim('123', '123') == 1
    assert cmp.sim('abc', 'xyz') == 0
    assert cmp.sim('123', '456') == 0
    assert cmp.sim('aleksander', 'alexandre') == pytest.approx(abs=1e-7, expected=0.7368421052631579)
    assert cmp.sim('alexandre', 'aleksander') == pytest.approx(abs=1e-7, expected=0.7368421052631579)
    assert cmp.sim('pennsylvania', 'pencilvaneya') == pytest.approx(abs=1e-7, expected=0.6666666666666666)
    assert cmp.sim('pencilvaneya', 'pennsylvania') == pytest.approx(abs=1e-7, expected=0.6666666666666666)
    assert cmp.sim('abcefglmn', 'abefglmo') == pytest.approx(abs=1e-7, expected=0.8235294117647058)
    assert cmp.sim('abefglmo', 'abcefglmn') == pytest.approx(abs=1e-7, expected=0.8235294117647058)

    with open(_corpus_file('variantNames.csv')) as cav_testset:
        next(cav_testset)
        for line in cav_testset:
            line = line.strip().split(',')
            word1, word2 = line[0], line[4]
            assert cmp.sim(word1, word2) == pytest.approx(abs=1e-7, expected=SequenceMatcher(None, word1, word2).ratio())

    with open(_corpus_file('wikipediaCommonMisspellings.csv')) as missp:
        next(missp)
        for line in missp:
            line = line.strip().upper()
            line = ''.join(
                [
                    _
                    for _ in line.strip()
                    if _ in tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ,')
                ]
            )
            word1, word2 = line.split(',')
            # print(word1, word2e)
            assert cmp.sim(word1, word2) == pytest.approx(abs=1e-7, expected=SequenceMatcher(None, word1, word2).ratio())

def test_ratcliff_obershelp_dist():
    """Test abydos.distance.RatcliffObershelp.dist."""
    # https://github.com/rockymadden/stringmetric/blob/master/core/src/test/scala/com/rockymadden/stringmetric/similarity/RatcliffObershelpMetricSpec.scala
    assert cmp.dist('', '') == 0
    assert cmp.dist('abc', '') == 1
    assert cmp.dist('', 'xyz') == 1
    assert cmp.dist('abc', 'abc') == 0
    assert cmp.dist('123', '123') == 0
    assert cmp.dist('abc', 'xyz') == 1
    assert cmp.dist('123', '456') == 1
    assert cmp.dist('aleksander', 'alexandre') == pytest.approx(abs=1e-7, expected=0.2631578947368421)
    assert cmp.dist('alexandre', 'aleksander') == pytest.approx(abs=1e-7, expected=0.2631578947368421)
    assert cmp.dist('pennsylvania', 'pencilvaneya') == pytest.approx(abs=1e-7, expected=0.3333333333333333)
    assert cmp.dist('pencilvaneya', 'pennsylvania') == pytest.approx(abs=1e-7, expected=0.3333333333333333)
    assert cmp.dist('abcefglmn', 'abefglmo') == pytest.approx(abs=1e-7, expected=0.1764705882352941)
    assert cmp.dist('abefglmo', 'abcefglmn') == pytest.approx(abs=1e-7, expected=0.1764705882352941)
