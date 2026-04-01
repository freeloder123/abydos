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

"""abydos.tests.distance.test_distance_complete_linkage.

This module contains unit tests for abydos.distance.CompleteLinkage
"""


import pytest

from abydos.distance import CompleteLinkage, JaroWinkler
from abydos.tokenizer import QGrams


cmp = CompleteLinkage()

cmp_q4 = CompleteLinkage(tokenizer=QGrams(qval=4, start_stop=''))

cmp_q4_jw = CompleteLinkage(


    tokenizer=QGrams(qval=4, start_stop=''), metric=JaroWinkler()
    )

def test_complete_linkage_dist():
    """Test abydos.distance.CompleteLinkage.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 0.0
    assert cmp.dist('', 'a') == 0.0
    assert cmp.dist('abc', '') == 0.0
    assert cmp.dist('', 'abc') == 0.0
    assert cmp.dist('abc', 'abc') == 1.0
    assert cmp.dist('abcd', 'efgh') == 1.0

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=1.0)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=1.0)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=1.0)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=1.0)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=1.0)

    assert cmp_q4.dist('AAAT', 'AATT') == 0.25
    assert cmp_q4_jw.dist('AAAT', 'AATT') == pytest.approx(abs=1e-7, expected=0.133333333333)

def test_complete_linkage_sim():
    """Test abydos.distance.CompleteLinkage.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 1.0
    assert cmp.sim('', 'a') == 1.0
    assert cmp.sim('abc', '') == 1.0
    assert cmp.sim('', 'abc') == 1.0
    assert cmp.sim('abc', 'abc') == 0.0
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.0)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.0)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.0)

def test_complete_linkage_dist_abs():
    """Test abydos.distance.CompleteLinkage.dist_abs."""
    # Base cases
    assert cmp.dist_abs('', '') == float('-inf')
    assert cmp.dist_abs('a', '') == float('-inf')
    assert cmp.dist_abs('', 'a') == float('-inf')
    assert cmp.dist_abs('abc', '') == float('-inf')
    assert cmp.dist_abs('', 'abc') == float('-inf')
    assert cmp.dist_abs('abc', 'abc') == 2
    assert cmp.dist_abs('abcd', 'efgh') == 2

    assert cmp.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=2)
    assert cmp.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=2)
    assert cmp.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=2)
    assert cmp.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=2)
    assert cmp.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=2)
