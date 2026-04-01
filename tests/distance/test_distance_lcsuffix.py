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

"""abydos.tests.distance.test_distance_lcsuffix.

This module contains unit tests for abydos.distance.LCSuffix
"""


import pytest

from abydos.distance import LCSuffix


class TestLCSuffix:
    """Test LCSuffix functions.

    abydos.distance.LCSuffix
    """

    cmp = LCSuffix()

    def test_lcsuffix_sim(self):
        """Test abydos.distance.LCSuffix.sim."""
        # Base cases
        assert self.cmp.sim('', '') == 1.0
        assert self.cmp.sim('a', '') == 0.0
        assert self.cmp.sim('', 'a') == 0.0
        assert self.cmp.sim('abc', '') == 0.0
        assert self.cmp.sim('', 'abc') == 0.0
        assert self.cmp.sim('abc', 'abc') == 1.0
        assert self.cmp.sim('abcd', 'efgh') == 0.0

        assert self.cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.2)
        assert self.cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.2)
        assert self.cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.2)
        assert self.cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.2)
        assert self.cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.0)

    def test_lcsuffix_dist(self):
        """Test abydos.distance.LCSuffix.dist."""
        # Base cases
        assert self.cmp.dist('', '') == 0.0
        assert self.cmp.dist('a', '') == 1.0
        assert self.cmp.dist('', 'a') == 1.0
        assert self.cmp.dist('abc', '') == 1.0
        assert self.cmp.dist('', 'abc') == 1.0
        assert self.cmp.dist('abc', 'abc') == 0.0
        assert self.cmp.dist('abcd', 'efgh') == 1.0

        assert self.cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.8)
        assert self.cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.8)
        assert self.cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.8)
        assert self.cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.8)
        assert self.cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=1.0)

    def test_lcsuffix_dist_abs(self):
        """Test abydos.distance.LCSuffix.dist_abs."""
        # Base cases
        assert self.cmp.dist_abs('', '') == 0
        assert self.cmp.dist_abs('a', '') == 0
        assert self.cmp.dist_abs('', 'a') == 0
        assert self.cmp.dist_abs('abc', '') == 0
        assert self.cmp.dist_abs('', 'abc') == 0
        assert self.cmp.dist_abs('abc', 'abc') == 3
        assert self.cmp.dist_abs('abcd', 'efgh') == 0

        assert self.cmp.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=1)
        assert self.cmp.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=1)
        assert self.cmp.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=1)
        assert self.cmp.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=1)
        assert self.cmp.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0)

        assert self.cmp.dist_abs('Nigel', 'Niall', 'Niel') == pytest.approx(abs=1e-7, expected=1)
        with pytest.raises(TypeError):
            self.cmp.dist_abs('Nigel', 'Niall', 5)
