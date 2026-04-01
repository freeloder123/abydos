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

"""abydos.tests.distance.test_distance_mcewen_michael.

This module contains unit tests for abydos.distance.McEwenMichael
"""


import pytest

from abydos.distance import McEwenMichael


cmp = McEwenMichael()

cmp_no_d = McEwenMichael(alphabet=0)


def test_mcewen_michael_sim():
    """Test abydos.distance.McEwenMichael.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.5
    assert cmp.sim('a', '') == 0.5
    assert cmp.sim('', 'a') == 0.5
    assert cmp.sim('abc', '') == 0.5
    assert cmp.sim('', 'abc') == 0.5
    assert cmp.sim('abc', 'abc') == 0.5101520199916701
    assert cmp.sim('abcd', 'efgh') == 0.4999165520648357

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5076521509)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5076521509)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5076521509)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5076521509)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5178144947)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 0.5
    assert cmp_no_d.sim('a', '') == 0.5
    assert cmp_no_d.sim('', 'a') == 0.5
    assert cmp_no_d.sim('abc', '') == 0.5
    assert cmp_no_d.sim('', 'abc') == 0.5
    assert cmp_no_d.sim('abc', 'abc') == 0.5
    assert cmp_no_d.sim('abcd', 'efgh') == 0.0

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.1)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.1)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.1)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.1)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.2551020408)

def test_mcewen_michael_dist():
    """Test abydos.distance.McEwenMichael.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.5
    assert cmp.dist('a', '') == 0.5
    assert cmp.dist('', 'a') == 0.5
    assert cmp.dist('abc', '') == 0.5
    assert cmp.dist('', 'abc') == 0.5
    assert cmp.dist('abc', 'abc') == 0.48984798000832985
    assert cmp.dist('abcd', 'efgh') == 0.5000834479351643

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4923478491)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4923478491)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4923478491)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4923478491)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4821855053)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 0.5
    assert cmp_no_d.dist('a', '') == 0.5
    assert cmp_no_d.dist('', 'a') == 0.5
    assert cmp_no_d.dist('abc', '') == 0.5
    assert cmp_no_d.dist('', 'abc') == 0.5
    assert cmp_no_d.dist('abc', 'abc') == 0.5
    assert cmp_no_d.dist('abcd', 'efgh') == 1.0

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.9)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.9)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.9)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.9)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.7448979592)

def test_mcewen_michael_corr():
    """Test abydos.distance.McEwenMichael.corr."""
    # Base cases
    assert cmp.corr('', '') == 0.0
    assert cmp.corr('a', '') == 0.0
    assert cmp.corr('', 'a') == 0.0
    assert cmp.corr('abc', '') == 0.0
    assert cmp.corr('', 'abc') == 0.0
    assert cmp.corr('abc', 'abc') == 0.020304039983340273
    assert cmp.corr('abcd', 'efgh') == -0.00016689587032858459

    assert cmp.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.0153043019)
    assert cmp.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.0153043019)
    assert cmp.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0153043019)
    assert cmp.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0153043019)
    assert cmp.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.0356289895)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.corr('', '') == 0.0
    assert cmp_no_d.corr('a', '') == 0.0
    assert cmp_no_d.corr('', 'a') == 0.0
    assert cmp_no_d.corr('abc', '') == 0.0
    assert cmp_no_d.corr('', 'abc') == 0.0
    assert cmp_no_d.corr('abc', 'abc') == 0.0
    assert cmp_no_d.corr('abcd', 'efgh') == -1.0

    assert cmp_no_d.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=-0.8)
    assert cmp_no_d.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=-0.8)
    assert cmp_no_d.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=-0.8)
    assert cmp_no_d.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=-0.8)
    assert cmp_no_d.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=-0.4897959184)
