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

"""abydos.tests.distance.test_distance_chao_jaccard.

This module contains unit tests for abydos.distance.ChaoJaccard
"""

import pytest

import random
import sys

from abydos.distance import ChaoJaccard


cmp = ChaoJaccard()


def test_chao_jaccard_sim():
    """Test abydos.distance.ChaoJaccard.sim."""
    # Skip testing for Python <= 3.5
    if sys.version_info[0:2] < (3, 6):
        return
    random.seed(0)

    # Base cases
    assert cmp.sim('', '') == 0.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('a', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4461538462)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3885505481)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.44)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.27137634)

def test_chao_jaccard_sim_score():
    """Test abydos.distance.ChaoJaccard.sim_score."""
    # Skip testing for Python <= 3.5
    if sys.version_info[0:2] < (3, 6):
        return

    random.seed(0)

    # Base cases
    assert cmp.sim_score('', '') == 0.0
    assert cmp.sim_score('a', '') == 0.0
    assert cmp.sim_score('', 'a') == 0.0
    assert cmp.sim_score('a', 'a') == 0.0
    assert cmp.sim_score('abc', '') == 0.0
    assert cmp.sim_score('', 'abc') == 0.0
    assert cmp.sim_score('abc', 'abc') == pytest.approx(abs=1e-7, expected=3.5714285714)
    assert cmp.sim_score('abcd', 'efgh') == 0.0

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4461538462)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3885505481)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.44)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.27137634)
