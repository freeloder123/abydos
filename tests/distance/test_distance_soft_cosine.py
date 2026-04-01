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

"""abydos.tests.distance.test_distance_soft_cosine.

This module contains unit tests for abydos.distance.SoftCosine
"""


import pytest

from abydos.distance import SoftCosine


class TestSoftCosine:
    """Test SoftCosine functions.

    abydos.distance.SoftCosine
    """

    cmp = SoftCosine()
    cmp_b = SoftCosine(sim_method='b')
    cmp_c = SoftCosine(sim_method='c')
    cmp_d = SoftCosine(sim_method='d')

    def test_soft_cosine_sim(self):
        """Test abydos.distance.SoftCosine.sim."""
        # Base cases
        assert self.cmp.sim('', '') == 1.0
        assert self.cmp.sim('a', '') == 0.0
        assert self.cmp.sim('', 'a') == 0.0
        assert self.cmp.sim('abc', '') == 0.0
        assert self.cmp.sim('', 'abc') == 0.0
        assert self.cmp.sim('abc', 'abc') == 1.0
        assert self.cmp.sim('abcd', 'efgh') == 0.7428571428571427

        assert self.cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.898146239)
        assert self.cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.898146239)
        assert self.cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.9375)
        assert self.cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.9375)
        assert self.cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.9731507012)

        # Constructor exception
        with pytest.raises(ValueError):
            SoftCosine(sim_method='e')

        # Alternate sim_methods
        # Base cases
        assert self.cmp_b.sim('', '') == 1.0
        assert self.cmp_b.sim('a', '') == 0.0
        assert self.cmp_b.sim('', 'a') == 0.0
        assert self.cmp_b.sim('abc', '') == 0.0
        assert self.cmp_b.sim('', 'abc') == 0.0
        assert self.cmp_b.sim('abc', 'abc') == 1.0
        assert self.cmp_b.sim('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=0.2)

        assert self.cmp_b.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.721687836)
        assert self.cmp_b.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.721687836)
        assert self.cmp_b.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=1.0)
        assert self.cmp_b.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=1.0)
        assert self.cmp_b.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.98328200498)

        # Base cases
        assert self.cmp_c.sim('', '') == 1.0
        assert self.cmp_c.sim('a', '') == 0.0
        assert self.cmp_c.sim('', 'a') == 0.0
        assert self.cmp_c.sim('abc', '') == 0.0
        assert self.cmp_c.sim('', 'abc') == 0.0
        assert self.cmp_c.sim('abc', 'abc') == 1.0
        assert self.cmp_c.sim('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=0.2828427124746)

        assert self.cmp_c.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.800818463)
        assert self.cmp_c.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.800818463)
        assert self.cmp_c.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=1.207106781)
        assert self.cmp_c.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=1.207106781)
        assert self.cmp_c.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=1.023072064)

        # Base cases
        assert self.cmp_d.sim('', '') == 1.0
        assert self.cmp_d.sim('a', '') == 0.0
        assert self.cmp_d.sim('', 'a') == 0.0
        assert self.cmp_d.sim('abc', '') == 0.0
        assert self.cmp_d.sim('', 'abc') == 0.0
        assert self.cmp_d.sim('abc', 'abc') == 1.0
        assert self.cmp_d.sim('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=0.1)

        assert self.cmp_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6172133998)
        assert self.cmp_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6172133998)
        assert self.cmp_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.75)
        assert self.cmp_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.75)
        assert self.cmp_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.89597867038)

    def test_soft_cosine_dist(self):
        """Test abydos.distance.SoftCosine.dist."""
        # Base cases
        assert self.cmp.dist('', '') == 0.0
        assert self.cmp.dist('a', '') == 1.0
        assert self.cmp.dist('', 'a') == 1.0
        assert self.cmp.dist('abc', '') == 1.0
        assert self.cmp.dist('', 'abc') == 1.0
        assert self.cmp.dist('abc', 'abc') == 0.0
        assert self.cmp.dist('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=0.25714285714285734)

        assert self.cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.101853761)
        assert self.cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.101853761)
        assert self.cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0625)
        assert self.cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0625)
        assert self.cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.0268492988)
