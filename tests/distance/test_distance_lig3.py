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

"""abydos.tests.distance.test_distance_lig3.

This module contains unit tests for abydos.distance.LIG3
"""


from abydos.distance import LIG3


cmp = LIG3()


def test_lig3_sim():
    """Test abydos.distance.LIG3.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('a', 'a') == 1.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.0

    # Testcases from paper
    assert cmp.sim('Glavin', 'Glawyn') == 0.8
    assert cmp.sim('Williams', 'Vylliems') == 0.7692307692307693
    assert cmp.sim('Lewis', 'Louis') == 0.75
    assert cmp.sim('Alex', 'Alexander') == 0.6153846153846154
    assert cmp.sim('Wild', 'Wildsmith') == 0.6153846153846154
    assert cmp.sim('Bram', 'Bramberley') == 0.5714285714285714
