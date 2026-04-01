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

"""abydos.tests.distance.test_distance_fossum.

This module contains unit tests for abydos.distance.Fossum
"""


import pytest

from abydos.distance import Fossum


cmp = Fossum()

cmp_no_d = Fossum(alphabet=0)


def test_fossum_sim():
    """Test abydos.distance.Fossum.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.2222222222222222
    assert cmp.sim('', 'a') == 0.2222222222222222
    assert cmp.sim('abc', '') == 0.08163265306122448
    assert cmp.sim('', 'abc') == 0.08163265306122448
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.01234567901234568

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.2066115702)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.2066115702)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.2066115702)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.2066115702)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4215419501)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 0.0
    assert cmp_no_d.sim('a', '') == 0.2222222222222222
    assert cmp_no_d.sim('', 'a') == 0.2222222222222222
    assert cmp_no_d.sim('abc', '') == 0.08163265306122448
    assert cmp_no_d.sim('', 'abc') == 0.08163265306122448
    assert cmp_no_d.sim('abc', 'abc') == 1.0
    assert cmp_no_d.sim('abcd', 'efgh') == 0.02469135802469136

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3099173554)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3099173554)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.3099173554)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.3099173554)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5365079365)

def test_fossum_dist():
    """Test abydos.distance.Fossum.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 0.7777777777777778
    assert cmp.dist('', 'a') == 0.7777777777777778
    assert cmp.dist('abc', '') == 0.9183673469387755
    assert cmp.dist('', 'abc') == 0.9183673469387755
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 0.9876543209876543

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7933884298)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7933884298)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.7933884298)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.7933884298)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5784580499)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 1.0
    assert cmp_no_d.dist('a', '') == 0.7777777777777778
    assert cmp_no_d.dist('', 'a') == 0.7777777777777778
    assert cmp_no_d.dist('abc', '') == 0.9183673469387755
    assert cmp_no_d.dist('', 'abc') == 0.9183673469387755
    assert cmp_no_d.dist('abc', 'abc') == 0.0
    assert cmp_no_d.dist('abcd', 'efgh') == 0.9753086419753086

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6900826446)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6900826446)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.6900826446)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.6900826446)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4634920635)

def test_fossum_sim_score():
    """Test abydos.distance.Fossum.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 196.0
    assert cmp.sim_score('a', '') == 98.0
    assert cmp.sim_score('', 'a') == 98.0
    assert cmp.sim_score('abc', '') == 49.0
    assert cmp.sim_score('', 'abc') == 49.0
    assert cmp.sim_score('abc', 'abc') == 600.25
    assert cmp.sim_score('abcd', 'efgh') == 7.84

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=136.1111111111)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=136.1111111111)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=136.1111111111)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=136.1111111111)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=301.1272727273)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim_score('', '') == 0.0
    assert cmp_no_d.sim_score('a', '') == 0.25
    assert cmp_no_d.sim_score('', 'a') == 0.25
    assert cmp_no_d.sim_score('abc', '') == 0.25
    assert cmp_no_d.sim_score('', 'abc') == 0.25
    assert cmp_no_d.sim_score('abc', 'abc') == 3.0625
    assert cmp_no_d.sim_score('abcd', 'efgh') == 0.1

    assert cmp_no_d.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=1.5625)
    assert cmp_no_d.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=1.5625)
    assert cmp_no_d.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=1.5625)
    assert cmp_no_d.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=1.5625)
    assert cmp_no_d.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=5.3772727273)
