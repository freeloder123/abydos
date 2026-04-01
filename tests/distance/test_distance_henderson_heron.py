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

"""abydos.tests.distance.test_distance_henderson_heron.

This module contains unit tests for abydos.distance.HendersonHeron
"""


import pytest

from abydos.distance import HendersonHeron


cmp = HendersonHeron()


def test_henderson_heron_dist():
    """Test abydos.distance.HendersonHeron.dist."""
    # Base cases
    assert cmp.dist('', '') == 1.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('a', 'a') == pytest.approx(abs=1e-7, expected=3.258008184e-06)
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == pytest.approx(abs=1e-7, expected=6.40140979487e-11)
    assert cmp.dist('abcd', 'efgh') == 0.9684367974410505

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=4.94203602e-06)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=4.94203602e-06)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=4.94203602e-06)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=4.94203602e-06)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=1.108779488e-12)
