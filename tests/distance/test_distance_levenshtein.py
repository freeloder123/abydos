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

"""abydos.tests.distance.test_distance_levenshtein.

This module contains unit tests for abydos.distance.Levenshtein
"""


import pytest

from abydos.distance import Levenshtein


cmp = Levenshtein()

cmp_taper = Levenshtein(taper=True)


def test_levenshtein_dist_abs():
    """Test abydos.distance.Levenshtein.dist_abs."""
    assert cmp.dist_abs('', '') == 0

    # http://oldfashionedsoftware.com/tag/levenshtein-distance/
    assert cmp.dist_abs('a', '') == 1
    assert cmp.dist_abs('', 'a') == 1
    assert cmp.dist_abs('abc', '') == 3
    assert cmp.dist_abs('', 'abc') == 3
    assert cmp.dist_abs('', '') == 0
    assert cmp.dist_abs('a', 'a') == 0
    assert cmp.dist_abs('abc', 'abc') == 0
    assert cmp.dist_abs('', 'a') == 1
    assert cmp.dist_abs('a', 'ab') == 1
    assert cmp.dist_abs('b', 'ab') == 1
    assert cmp.dist_abs('ac', 'abc') == 1
    assert cmp.dist_abs('abcdefg', 'xabxcdxxefxgx') == 6
    assert cmp.dist_abs('a', '') == 1
    assert cmp.dist_abs('ab', 'a') == 1
    assert cmp.dist_abs('ab', 'b') == 1
    assert cmp.dist_abs('abc', 'ac') == 1
    assert cmp.dist_abs('xabxcdxxefxgx', 'abcdefg') == 6
    assert cmp.dist_abs('a', 'b') == 1
    assert cmp.dist_abs('ab', 'ac') == 1
    assert cmp.dist_abs('ac', 'bc') == 1
    assert cmp.dist_abs('abc', 'axc') == 1
    assert cmp.dist_abs('xabxcdxxefxgx', '1ab2cd34ef5g6') == 6
    assert cmp.dist_abs('example', 'samples') == 3
    assert cmp.dist_abs('sturgeon', 'urgently') == 6
    assert cmp.dist_abs('levenshtein', 'frankenstein') == 6
    assert cmp.dist_abs('distance', 'difference') == 5
    assert cmp.dist_abs('java was neat', 'scala is great') == 7

    # https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
    assert Levenshtein(mode='osa').dist_abs('CA', 'ABC') == 3

    # test cost of insert
    assert Levenshtein(mode='lev', cost=(5, 7, 10, 10)).dist_abs('', 'b') == 5
    assert Levenshtein(mode='osa', cost=(5, 7, 10, 10)).dist_abs('', 'b') == 5
    assert (
        Levenshtein(mode='lev', cost=(5, 7, 10, 10)).dist_abs('a', 'ab')
        == 5
    )
    assert (
        Levenshtein(mode='osa', cost=(5, 7, 10, 10)).dist_abs('a', 'ab')
        == 5
    )

    # test cost of delete
    assert Levenshtein(mode='lev', cost=(5, 7, 10, 10)).dist_abs('b', '') == 7
    assert Levenshtein(mode='osa', cost=(5, 7, 10, 10)).dist_abs('b', '') == 7
    assert (
        Levenshtein(mode='lev', cost=(5, 7, 10, 10)).dist_abs('ab', 'a')
        == 7
    )
    assert (
        Levenshtein(mode='osa', cost=(5, 7, 10, 10)).dist_abs('ab', 'a')
        == 7
    )

    # test cost of substitute
    assert (
        Levenshtein(mode='lev', cost=(10, 10, 5, 10)).dist_abs('a', 'b')
        == 5
    )
    assert (
        Levenshtein(mode='osa', cost=(10, 10, 5, 10)).dist_abs('a', 'b')
        == 5
    )
    assert (
        Levenshtein(mode='lev', cost=(10, 10, 5, 10)).dist_abs('ac', 'bc')
        == 5
    )
    assert (
        Levenshtein(mode='osa', cost=(10, 10, 5, 10)).dist_abs('ac', 'bc')
        == 5
    )

    # test cost of transpose
    assert (
        Levenshtein(mode='lev', cost=(10, 10, 10, 5)).dist_abs('ab', 'ba')
        == 20
    )
    assert (
        Levenshtein(mode='osa', cost=(10, 10, 10, 5)).dist_abs('ab', 'ba')
        == 5
    )
    assert (
        Levenshtein(mode='lev', cost=(10, 10, 10, 5)).dist_abs( 'abc', 'bac' )
        == 20
    )
    assert (
        Levenshtein(mode='osa', cost=(10, 10, 10, 5)).dist_abs( 'abc', 'bac' )
        == 5
    )
    assert (
        Levenshtein(mode='lev', cost=(10, 10, 10, 5)).dist_abs( 'cab', 'cba' )
        == 20
    )
    assert (
        Levenshtein(mode='osa', cost=(10, 10, 10, 5)).dist_abs( 'cab', 'cba' )
        == 5
    )

    # tapered variant
    assert cmp_taper.dist_abs('abc', 'ac') == pytest.approx(abs=1e-7, expected=1.33333333333)
    assert cmp_taper.dist_abs('xabxcdxxefxgx', 'abcdefg') == pytest.approx(abs=1e-7, expected=8.615384615384617)
    assert cmp_taper.dist_abs('levenshtein', 'frankenstein') == pytest.approx(abs=1e-7, expected=10)
    assert cmp_taper.dist_abs('distance', 'difference') == pytest.approx(abs=1e-7, expected=7.499999999999999)

def test_levenshtein_dist():
    """Test abydos.distance.Levenshtein.dist."""
    assert cmp.dist('', '') == 0

    assert cmp.dist('a', 'a') == 0
    assert cmp.dist('ab', 'ab') == 0
    assert cmp.dist('', 'a') == 1
    assert cmp.dist('', 'ab') == 1
    assert cmp.dist('a', 'c') == 1

    assert cmp.dist('abc', 'ac') == pytest.approx(abs=1e-7, expected=1 / 3)
    assert cmp.dist('abbc', 'ac') == pytest.approx(abs=1e-7, expected=1 / 2)
    assert cmp.dist('abbc', 'abc') == pytest.approx(abs=1e-7, expected=1 / 4)

    # tapered variant
    assert cmp_taper.dist('abc', 'ac') == pytest.approx(abs=1e-7, expected=0.2666666666666666)
    assert cmp_taper.dist('abbc', 'ac') == pytest.approx(abs=1e-7, expected=0.4230769230769231)
    assert cmp_taper.dist('abbc', 'abc') == pytest.approx(abs=1e-7, expected=0.19230769230769232)

def test_levenshtein_sim():
    """Test abydos.distance.Levenshtein.sim."""
    assert cmp.sim('', '') == 1

    assert cmp.sim('a', 'a') == 1
    assert cmp.sim('ab', 'ab') == 1
    assert cmp.sim('', 'a') == 0
    assert cmp.sim('', 'ab') == 0
    assert cmp.sim('a', 'c') == 0

    assert cmp.sim('abc', 'ac') == pytest.approx(abs=1e-7, expected=2 / 3)
    assert cmp.sim('abbc', 'ac') == pytest.approx(abs=1e-7, expected=1 / 2)
    assert cmp.sim('abbc', 'abc') == pytest.approx(abs=1e-7, expected=3 / 4)

def test_levenshtein_alignment():
    """Test abydos.distance.Levenshtein.alignment."""
    assert cmp.alignment('', '') == (0, '', '')

    assert cmp.alignment('a', 'a') == (0.0, 'a', 'a')
    assert cmp.alignment('ab', 'ab') == (0.0, 'ab', 'ab')
    assert cmp.alignment('', 'a') == (1.0, '-', 'a')
    assert cmp.alignment('', 'ab') == (2.0, '--', 'ab')
    assert cmp.alignment('a', 'c') == (1.0, 'a', 'c')

    assert cmp.alignment('abc', 'ac') == (1.0, 'abc', 'a-c')
    assert cmp.alignment('abbc', 'ac') == (2.0, 'abbc', 'a--c')
    assert cmp.alignment('abbc', 'abc') == (1.0, 'abbc', 'ab-c')

    assert (
        Levenshtein(mode='osa').alignment('Niall', 'Naill')
        == (1.0, 'Niall', 'Naill')
    )
