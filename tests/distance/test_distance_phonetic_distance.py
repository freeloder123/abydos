# Copyright 2019-2020 by Christopher C. Little.
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

"""abydos.tests.distance.test_distance_phonetic_distance.

This module contains unit tests for abydos.distance.PhoneticDistance
"""


import pytest

from abydos.distance import JaroWinkler, Levenshtein, PhoneticDistance
from abydos.fingerprint import OmissionKey
from abydos.phonetic import Metaphone, Soundex
from abydos.stemmer import Porter2


sdx = PhoneticDistance(transforms=Soundex)

sdx_lev = PhoneticDistance(transforms=Soundex(), metric=Levenshtein())

three_jaro = PhoneticDistance(


# Having mixed instantiated & uninstantiated classes is... weird... but
# this covers another line of code.
    transforms=[Porter2, Metaphone, OmissionKey()],
    metric=JaroWinkler,
    encode_alpha=True,
    )

def test_phonetic_distance_dist():
    """Test abydos.distance.PhoneticDistance.dist."""
    # Base cases
    assert sdx.dist('', '') == 0.0
    assert sdx.dist('a', '') == 1.0
    assert sdx.dist('', 'a') == 1.0
    assert sdx.dist('abc', '') == 1.0
    assert sdx.dist('', 'abc') == 1.0
    assert sdx.dist('abc', 'abc') == 0.0
    assert sdx.dist('abcd', 'efgh') == 1.0

    assert sdx.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=1.0)
    assert sdx.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=1.0)
    assert sdx.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0)
    assert sdx.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0)
    assert sdx.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=1.0)

    assert sdx_lev.dist('', '') == 0.0
    assert sdx_lev.dist('a', '') == 0.25
    assert sdx_lev.dist('', 'a') == 0.25
    assert sdx_lev.dist('abc', '') == 0.75
    assert sdx_lev.dist('', 'abc') == 0.75
    assert sdx_lev.dist('abc', 'abc') == 0.0
    assert sdx_lev.dist('abcd', 'efgh') == 0.5

    assert sdx_lev.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5)
    assert sdx_lev.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5)
    assert sdx_lev.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0)
    assert sdx_lev.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0)
    assert sdx_lev.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5)

    assert three_jaro.dist('', '') == 0.0
    assert three_jaro.dist('a', '') == 1.0
    assert three_jaro.dist('', 'a') == 1.0
    assert three_jaro.dist('abc', '') == 1.0
    assert three_jaro.dist('', 'abc') == 1.0
    assert three_jaro.dist('abc', 'abc') == 0.0
    assert three_jaro.dist('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=0.4722222)

    assert three_jaro.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=1.0)
    assert three_jaro.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=1.0)
    assert three_jaro.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0)
    assert three_jaro.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0)
    assert three_jaro.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.0)

    # More tests to complete coverage
    assert PhoneticDistance().dist('a', 'ab') == 1.0
    with pytest.raises(TypeError):
        PhoneticDistance(['hello!'])
    with pytest.raises(TypeError):
        PhoneticDistance(3.14)
    with pytest.raises(TypeError):
        PhoneticDistance(metric=3.14)
    assert PhoneticDistance(lambda s: s.lower()).dist('ONE', 'one') == 0.0

def test_phonetic_distance_dist_abs():
    """Test abydos.distance.PhoneticDistance.dist_abs."""
    # Base cases
    assert sdx.dist_abs('', '') == 0
    assert sdx.dist_abs('a', '') == 1
    assert sdx.dist_abs('', 'a') == 1
    assert sdx.dist_abs('abc', '') == 1
    assert sdx.dist_abs('', 'abc') == 1
    assert sdx.dist_abs('abc', 'abc') == 0
    assert sdx.dist_abs('abcd', 'efgh') == 1

    assert sdx.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=1)
    assert sdx.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=1)
    assert sdx.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0)
    assert sdx.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0)
    assert sdx.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=1)

    assert sdx_lev.dist_abs('', '') == 0
    assert sdx_lev.dist_abs('a', '') == 1
    assert sdx_lev.dist_abs('', 'a') == 1
    assert sdx_lev.dist_abs('abc', '') == 3
    assert sdx_lev.dist_abs('', 'abc') == 3
    assert sdx_lev.dist_abs('abc', 'abc') == 0
    assert sdx_lev.dist_abs('abcd', 'efgh') == 2

    assert sdx_lev.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=2)
    assert sdx_lev.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=2)
    assert sdx_lev.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0)
    assert sdx_lev.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0)
    assert sdx_lev.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=2)
