# Copyright 2018-2020 by Christopher C. Little.
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

"""abydos.tests.distance.test_distance_eudex.

This module contains unit tests for abydos.distance.Eudex
"""


import pytest

from abydos.distance import Eudex


def _yield_1():
    while True:
        yield 1


class TestEudex:
    """Test Eudex distance functions.

    abydos.distance.Eudex
    """

    cmp = Eudex()

    def test_eudex_dist_abs(self):
        """Test abydos.distance.Eudex.dist_abs."""
        # Base cases
        assert self.cmp.dist_abs('', '') == 0
        assert Eudex(None).dist_abs('', '') == 0
        assert Eudex('fibonacci').dist_abs('', '') == 0
        assert Eudex([10, 1, 1, 1]).dist_abs('', '') == 0
        assert Eudex(_yield_1).dist_abs('', '') == 0
        assert self.cmp.dist_abs('', '', normalized=True) == 0

        assert self.cmp.dist_abs('Niall', 'Niall') == 0
        assert Eudex(None).dist_abs('Niall', 'Niall') == 0
        assert Eudex('fibonacci').dist_abs('Niall', 'Niall') == 0
        assert Eudex([10, 1, 1, 1]).dist_abs('Niall', 'Niall') == 0
        assert Eudex(_yield_1).dist_abs('Niall', 'Niall') == 0
        assert self.cmp.dist_abs('Niall', 'Niall', normalized=True) == 0

        assert self.cmp.dist_abs('Niall', 'Neil') == 2
        assert Eudex(None).dist_abs('Niall', 'Neil') == 1
        assert Eudex('fibonacci').dist_abs('Niall', 'Neil') == 2
        assert Eudex([10, 1, 1, 1]).dist_abs('Niall', 'Neil') == 1
        assert Eudex(_yield_1).dist_abs('Niall', 'Neil') == 1
        assert self.cmp.dist_abs('Niall', 'Neil', normalized=True) == pytest.approx(abs=1e-7, expected=0.00098039)

        assert self.cmp.dist_abs('Niall', 'Colin') == 524
        assert Eudex(None).dist_abs('Niall', 'Colin') == 10
        assert Eudex('fibonacci').dist_abs('Niall', 'Colin') == 146
        assert Eudex([10, 1, 1, 1]).dist_abs('Niall', 'Colin') == 42
        assert Eudex(_yield_1).dist_abs('Niall', 'Colin') == 10
        assert self.cmp.dist_abs('Niall', 'Colin', normalized=True) == pytest.approx(abs=1e-7, expected=0.25686274)

    def test_eudex_dist(self):
        """Test abydos.distance.Eudex.dist."""
        # Base cases
        assert self.cmp.dist('', '') == 0
        assert Eudex(None).dist('', '') == 0
        assert Eudex('fibonacci').dist('', '') == 0

        assert self.cmp.dist('Niall', 'Niall') == 0
        assert Eudex(None).dist('Niall', 'Niall') == 0
        assert Eudex('fibonacci').dist('Niall', 'Niall') == 0

        assert self.cmp.dist('Niall', 'Neil') == pytest.approx(abs=1e-7, expected=0.00098039)
        assert Eudex(None).dist('Niall', 'Neil') == pytest.approx(abs=1e-7, expected=0.11111111)
        assert Eudex('fibonacci').dist('Niall', 'Neil') == pytest.approx(abs=1e-7, expected=0.00287356)

        assert self.cmp.dist('Niall', 'Colin') == pytest.approx(abs=1e-7, expected=0.25686275)
        assert Eudex(None).dist('Niall', 'Colin') == pytest.approx(abs=1e-7, expected=0.16666667)
        assert Eudex('fibonacci').dist('Niall', 'Colin') == pytest.approx(abs=1e-7, expected=0.20977011)

        with pytest.raises(ValueError):
            Eudex('veryLarge').dist_abs('Niall', 'Colin')

    def test_eudex_sim(self):
        """Test abydos.distance.Eudex.sim."""
        # Base cases
        assert self.cmp.sim('', '') == 1
        assert Eudex(None).sim('', '') == 1
        assert Eudex('fibonacci').sim('', '') == 1

        assert self.cmp.sim('Niall', 'Niall') == 1
        assert Eudex(None).sim('Niall', 'Niall') == 1
        assert Eudex('fibonacci').sim('Niall', 'Niall') == 1

        assert self.cmp.sim('Niall', 'Neil') == pytest.approx(abs=1e-7, expected=0.99901961)
        assert Eudex(None).sim('Niall', 'Neil') == pytest.approx(abs=1e-7, expected=0.88888889)
        assert Eudex('fibonacci').sim('Niall', 'Neil') == pytest.approx(abs=1e-7, expected=0.99712644)

        assert self.cmp.sim('Niall', 'Colin') == pytest.approx(abs=1e-7, expected=0.74313725)
        assert Eudex(None).sim('Niall', 'Colin') == pytest.approx(abs=1e-7, expected=0.83333333)
        assert Eudex('fibonacci').sim('Niall', 'Colin') == pytest.approx(abs=1e-7, expected=0.79022989)
