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

"""abydos.tests.distance.test_distance_sift4.

This module contains unit tests for abydos.distance.Sift4
"""


import pytest

from abydos.distance import Sift4


cmp = Sift4()

cmp55 = Sift4(5, 5)


def test_sift4_dist_abs():
    """Test abydos.distance.Sift4.dist_abs."""
    # tests copied from Lukas Benedix's post at
    # https://siderite.blogspot.com/2014/11/super-fast-and-accurate-string-distance.html
    assert cmp.dist_abs('', '') == 0
    assert cmp.dist_abs('a', '') == 1
    assert cmp.dist_abs('', 'a') == 1
    assert cmp.dist_abs('abc', '') == 3
    assert cmp.dist_abs('', 'abc') == 3

    assert cmp.dist_abs('a', 'a') == 0
    assert cmp.dist_abs('abc', 'abc') == 0

    assert cmp.dist_abs('a', 'ab') == 1
    assert cmp.dist_abs('ac', 'abc') == 1
    assert cmp.dist_abs('abcdefg', 'xabxcdxxefxgx') == 7

    assert cmp.dist_abs('ab', 'b') == 1
    assert cmp.dist_abs('ab', 'a') == 1
    assert cmp.dist_abs('abc', 'ac') == 1
    assert cmp.dist_abs('xabxcdxxefxgx', 'abcdefg') == 7

    assert cmp.dist_abs('a', 'b') == 1
    assert cmp.dist_abs('ab', 'ac') == 1
    assert cmp.dist_abs('ac', 'bc') == 1
    assert cmp.dist_abs('abc', 'axc') == 1
    assert cmp.dist_abs('xabxcdxxefxgx', '1ab2cd34ef5g6') == 6

    assert cmp.dist_abs('example', 'samples') == 2
    assert cmp.dist_abs('sturgeon', 'urgently') == 3
    assert cmp.dist_abs('levenshtein', 'frankenstein') == 6
    assert cmp.dist_abs('distance', 'difference') == 5

    # Tests copied from
    # https://github.com/tdebatty/java-string-similarity/blob/master/src/test/java/info/debatty/java/stringsimilarity/experimental/Sift4Test.java
    assert (
        Sift4(5).dist_abs( 'This is the first string', 'And this is another string' )
        == 11
    )
    assert (
        Sift4(10).dist_abs( 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'Amet Lorm ispum dolor sit amet, consetetur adixxxpiscing' + ' elit.', )
        == 12
    )

    # cases with max_distance
    assert cmp55.dist_abs('example', 'samples') == 5
    assert cmp55.dist_abs('sturgeon', 'urgently') == 5
    assert cmp55.dist_abs('levenshtein', 'frankenstein') == 5
    assert cmp55.dist_abs('distance', 'difference') == 5

def test_sift4_dist():
    """Test abydos.distance.Sift4.dist."""
    # tests copied from Lukas Benedix's post at
    # https://siderite.blogspot.com/2014/11/super-fast-and-accurate-string-distance.html
    assert cmp.dist('', '') == 0
    assert cmp.dist('a', '') == 1
    assert cmp.dist('', 'a') == 1
    assert cmp.dist('abc', '') == 1
    assert cmp.dist('', 'abc') == 1

    assert cmp.dist('a', 'a') == 0
    assert cmp.dist('abc', 'abc') == 0

    assert cmp.dist('a', 'ab') == 0.5
    assert cmp.dist('ac', 'abc') == 1 / 3
    assert cmp.dist('abcdefg', 'xabxcdxxefxgx') == pytest.approx(abs=1e-7, expected=0.538461538)

    assert cmp.dist('ab', 'b') == 0.5
    assert cmp.dist('ab', 'a') == 0.5
    assert cmp.dist('abc', 'ac') == 1 / 3
    assert cmp.dist('xabxcdxxefxgx', 'abcdefg') == pytest.approx(abs=1e-7, expected=0.538461538)

    assert cmp.dist('a', 'b') == 1
    assert cmp.dist('ab', 'ac') == 0.5
    assert cmp.dist('ac', 'bc') == 0.5
    assert cmp.dist('abc', 'axc') == 1 / 3
    assert cmp.dist('xabxcdxxefxgx', '1ab2cd34ef5g6') == pytest.approx(abs=1e-7, expected=0.461538461)

    assert cmp.dist('example', 'samples') == pytest.approx(abs=1e-7, expected=0.285714285)
    assert cmp.dist('sturgeon', 'urgently') == pytest.approx(abs=1e-7, expected=0.375)
    assert cmp.dist('levenshtein', 'frankenstein') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp.dist('distance', 'difference') == pytest.approx(abs=1e-7, expected=0.5)

    # Tests copied from
    # https://github.com/tdebatty/java-string-similarity/blob/master/src/test/java/info/debatty/java/stringsimilarity/experimental/Sift4Test.java
    assert Sift4(5).dist(
            'This is the first string', 'And this is another string'
        ) == pytest.approx(abs=1e-7, expected=0.423076923)
    assert Sift4(10).dist(
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'Amet Lorm ispum dolor sit amet, consetetur adixxxpiscing'
            + ' elit.',
        ) == pytest.approx(abs=1e-7, expected=0.193548387)

    # cases with max_distance
    assert cmp55.dist('example', 'samples') == pytest.approx(abs=1e-7, expected=0.714285714)
    assert cmp55.dist('sturgeon', 'urgently') == pytest.approx(abs=1e-7, expected=0.625)
    assert cmp55.dist('levenshtein', 'frankenstein') == pytest.approx(abs=1e-7, expected=0.416666666)
    assert cmp55.dist('distance', 'difference') == pytest.approx(abs=1e-7, expected=0.5)

def test_sift4_sim():
    """Test abydos.distance.Sift4.sim."""
    # tests copied from Lukas Benedix's post at
    # https://siderite.blogspot.com/2014/11/super-fast-and-accurate-string-distance.html
    assert cmp.sim('', '') == 1
    assert cmp.sim('a', '') == 0
    assert cmp.sim('', 'a') == 0
    assert cmp.sim('abc', '') == 0
    assert cmp.sim('', 'abc') == 0

    assert cmp.sim('a', 'a') == 1
    assert cmp.sim('abc', 'abc') == 1

    assert cmp.sim('a', 'ab') == 0.5
    assert cmp.sim('ac', 'abc') == pytest.approx(abs=1e-7, expected=2 / 3)
    assert cmp.sim('abcdefg', 'xabxcdxxefxgx') == pytest.approx(abs=1e-7, expected=0.461538461)

    assert cmp.sim('ab', 'b') == 0.5
    assert cmp.sim('ab', 'a') == 0.5
    assert cmp.sim('abc', 'ac') == pytest.approx(abs=1e-7, expected=2 / 3)
    assert cmp.sim('xabxcdxxefxgx', 'abcdefg') == pytest.approx(abs=1e-7, expected=0.461538461)

    assert cmp.sim('a', 'b') == 0
    assert cmp.sim('ab', 'ac') == 0.5
    assert cmp.sim('ac', 'bc') == 0.5
    assert cmp.sim('abc', 'axc') == pytest.approx(abs=1e-7, expected=2 / 3)
    assert cmp.sim('xabxcdxxefxgx', '1ab2cd34ef5g6') == pytest.approx(abs=1e-7, expected=0.538461538)

    assert cmp.sim('example', 'samples') == pytest.approx(abs=1e-7, expected=0.714285714)
    assert cmp.sim('sturgeon', 'urgently') == pytest.approx(abs=1e-7, expected=0.625)
    assert cmp.sim('levenshtein', 'frankenstein') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp.sim('distance', 'difference') == pytest.approx(abs=1e-7, expected=0.5)

    # Tests copied from
    # https://github.com/tdebatty/java-string-similarity/blob/master/src/test/java/info/debatty/java/stringsimilarity/experimental/Sift4Test.java
    assert Sift4(5).sim(
            'This is the first string', 'And this is another string'
        ) == pytest.approx(abs=1e-7, expected=0.576923077)
    assert Sift4(10).sim(
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'Amet Lorm ispum dolor sit amet, consetetur adixxxpiscing'
            + ' elit.',
        ) == pytest.approx(abs=1e-7, expected=0.806451613)

    # cases with max_distance
    assert cmp55.sim('example', 'samples') == pytest.approx(abs=1e-7, expected=0.285714286)
    assert cmp55.sim('sturgeon', 'urgently') == pytest.approx(abs=1e-7, expected=0.375)
    assert cmp55.sim('levenshtein', 'frankenstein') == pytest.approx(abs=1e-7, expected=0.583333333)
    assert cmp55.sim('distance', 'difference') == pytest.approx(abs=1e-7, expected=0.5)
