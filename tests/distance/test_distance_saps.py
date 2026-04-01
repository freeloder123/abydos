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

"""abydos.tests.distance.test_distance_saps.

This module contains unit tests for abydos.distance.SAPS
"""


import pytest

from abydos.distance import SAPS
from abydos.tokenizer import QGrams


cmp = SAPS()

cmp_q2 = SAPS(tokenizer=QGrams(2))


def test_saps_sim():
    """Test abydos.distance.SAPS.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.0666666667)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.0666666667)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0666666667)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0666666667)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4333333333)

    # Coverage
    assert cmp_q2.sim('Stevenson', 'Stinson') == pytest.approx(abs=1e-7, expected=0.3857142857)

    # Examples from paper
    assert cmp.sim('Stevenson', 'Stinson') == pytest.approx(abs=1e-7, expected=0.551724138)

def test_saps_dist():
    """Test abydos.distance.SAPS.dist."""
    # Base cases
    assert cmp.dist('', '') == 1.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 1.0

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.9333333333)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.9333333333)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.9333333333)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.9333333333)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5666666667)

    # Coverage
    assert cmp_q2.dist('Stevenson', 'Stinson') == pytest.approx(abs=1e-7, expected=0.614285714)

    # Examples from paper
    assert cmp.dist('Stevenson', 'Stinson') == pytest.approx(abs=1e-7, expected=0.448275862)

def test_saps_sim_score():
    """Test abydos.distance.SAPS.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 0
    assert cmp.sim_score('a', '') == -3
    assert cmp.sim_score('', 'a') == -3
    assert cmp.sim_score('abc', '') == -7
    assert cmp.sim_score('', 'abc') == -7
    assert cmp.sim_score('abc', 'abc') == 13
    assert cmp.sim_score('abcd', 'efgh') == -7

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=1)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=1)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=1)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=1)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=13)

    # Coverage
    assert cmp_q2.sim_score('Stevenson', 'Stinson') == 27

    # Examples from paper
    assert cmp.sim_score('Stevenson', 'Stinson') == 16
