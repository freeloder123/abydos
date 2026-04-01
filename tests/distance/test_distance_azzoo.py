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

"""abydos.tests.distance.test_distance_azzoo.

This module contains unit tests for abydos.distance.AZZOO
"""


import pytest

from abydos.distance import AZZOO


cmp = AZZOO()

cmp_no_d = AZZOO(alphabet=0)


def test_azzoo_sim():
    """Test abydos.distance.AZZOO.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.9949109414758269
    assert cmp.sim('', 'a') == 0.9949109414758269
    assert cmp.sim('abc', '') == 0.9898477157360406
    assert cmp.sim('', 'abc') == 0.9898477157360406
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.9809885931558935

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.9886075949)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.9886075949)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.9886075949)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.9886075949)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.986163522)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 1.0
    assert cmp_no_d.sim('a', '') == 0.0
    assert cmp_no_d.sim('', 'a') == 0.0
    assert cmp_no_d.sim('abc', '') == 0.0
    assert cmp_no_d.sim('', 'abc') == 0.0
    assert cmp_no_d.sim('abc', 'abc') == 1.0
    assert cmp_no_d.sim('abcd', 'efgh') == 0.0

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6363636364)

def test_azzoo_sim_score():
    """Test abydos.distance.AZZOO.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 392.0
    assert cmp.sim_score('a', '') == 391.0
    assert cmp.sim_score('', 'a') == 391.0
    assert cmp.sim_score('abc', '') == 390.0
    assert cmp.sim_score('', 'abc') == 390.0
    assert cmp.sim_score('abc', 'abc') == 394.0
    assert cmp.sim_score('abcd', 'efgh') == 387.0

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=390.5)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=390.5)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=390.5)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=390.5)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=392.0)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim_score('', '') == 0.0
    assert cmp_no_d.sim_score('a', '') == 0.0
    assert cmp_no_d.sim_score('', 'a') == 0.0
    assert cmp_no_d.sim_score('abc', '') == 0.0
    assert cmp_no_d.sim_score('', 'abc') == 0.0
    assert cmp_no_d.sim_score('abc', 'abc') == 4.0
    assert cmp_no_d.sim_score('abcd', 'efgh') == 0.0

    assert cmp_no_d.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=3.0)
    assert cmp_no_d.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=3.0)
    assert cmp_no_d.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=3.0)
    assert cmp_no_d.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=3.0)
    assert cmp_no_d.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=7.0)
