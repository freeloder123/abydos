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

"""abydos.tests.distance.test_distance_harris_lahey.

This module contains unit tests for abydos.distance.HarrisLahey
"""


import pytest

from abydos.distance import HarrisLahey


cmp = HarrisLahey()

cmp_no_d = HarrisLahey(alphabet=0)


def test_harris_lahey_sim():
    """Test abydos.distance.HarrisLahey.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.0012722563515202
    assert cmp.sim('', 'a') == 0.0012722563515202
    assert cmp.sim('abc', '') == 0.0025380049979175346
    assert cmp.sim('', 'abc') == 0.0025380049979175346
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.006296204706372345

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3383765798)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3383765798)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.3383765798)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.3383765798)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5065757722)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 1.0
    assert cmp_no_d.sim('a', '') == 0.0
    assert cmp_no_d.sim('', 'a') == 0.0
    assert cmp_no_d.sim('abc', '') == 0.0
    assert cmp_no_d.sim('', 'abc') == 0.0
    assert cmp_no_d.sim('abc', 'abc') == 1.0
    assert cmp_no_d.sim('abcd', 'efgh') == 0.0

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.1111111111)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.1111111111)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.1111111111)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.1111111111)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.125)

def test_harris_lahey_dist():
    """Test abydos.distance.HarrisLahey.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 0.9987277436484798
    assert cmp.dist('', 'a') == 0.9987277436484798
    assert cmp.dist('abc', '') == 0.9974619950020824
    assert cmp.dist('', 'abc') == 0.9974619950020824
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 0.9937037952936276

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6616234202)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6616234202)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.6616234202)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.6616234202)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4934242278)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 0.0
    assert cmp_no_d.dist('a', '') == 1.0
    assert cmp_no_d.dist('', 'a') == 1.0
    assert cmp_no_d.dist('abc', '') == 1.0
    assert cmp_no_d.dist('', 'abc') == 1.0
    assert cmp_no_d.dist('abc', 'abc') == 0.0
    assert cmp_no_d.dist('abcd', 'efgh') == 1.0

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.8888888889)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.8888888889)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.8888888889)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.8888888889)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.875)
