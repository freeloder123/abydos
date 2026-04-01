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

"""abydos.tests.distance.test_distance_fellegi_sunter.

This module contains unit tests for abydos.distance.FellegiSunter
"""


import pytest

from abydos.distance import FellegiSunter


cmp = FellegiSunter()

cmp_simp = FellegiSunter(simplified=True)


def test_fellegi_sunter_sim():
    """Test abydos.distance.FellegiSunter.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 0.586895558534099
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.270318312)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.270318312)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.270318312)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.270318312)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.2814144756)

    # Simplified variant cases
    assert cmp_simp.sim('', '') == 0.0
    assert cmp_simp.sim('a', '') == 0.0
    assert cmp_simp.sim('', 'a') == 0.0
    assert cmp_simp.sim('abc', '') == 0.0
    assert cmp_simp.sim('', 'abc') == 0.0
    assert cmp_simp.sim('abc', 'abc') == 0.9241962407465937
    assert cmp_simp.sim('abcd', 'efgh') == 0.0
    assert cmp_simp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.2687639203842084)
    assert cmp_simp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.2687639203842084)
    assert cmp_simp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.2687639203842084)
    assert cmp_simp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.2687639203842084)
    assert cmp_simp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5959107950190301)

def test_fellegi_sunter_dist():
    """Test abydos.distance.FellegiSunter.dist."""
    # Base cases
    assert cmp.dist('', '') == 1.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.413104441465901
    assert cmp.dist('abcd', 'efgh') == 1.0

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.729681688)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.729681688)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.729681688)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.729681688)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.7185855244)

    # Simplified variant cases
    assert cmp_simp.dist('', '') == 1.0
    assert cmp_simp.dist('a', '') == 1.0
    assert cmp_simp.dist('', 'a') == 1.0
    assert cmp_simp.dist('abc', '') == 1.0
    assert cmp_simp.dist('', 'abc') == 1.0
    assert cmp_simp.dist('abc', 'abc') == 0.07580375925340632
    assert cmp_simp.dist('abcd', 'efgh') == 1.0
    assert cmp_simp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7312360796157916)
    assert cmp_simp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7312360796157916)
    assert cmp_simp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.7312360796157916)
    assert cmp_simp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.7312360796157916)
    assert cmp_simp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4040892049809699)

def test_fellegi_sunter_sim_score():
    """Test abydos.distance.FellegiSunter.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 0.0
    assert cmp.sim_score('a', '') == 0.0
    assert cmp.sim_score('', 'a') == 0.0
    assert cmp.sim_score('abc', '') == 0.0
    assert cmp.sim_score('', 'abc') == 0.0
    assert cmp.sim_score('abc', 'abc') == 1.760686675602297
    assert cmp.sim_score('abcd', 'efgh') == 0.0

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=1.3515915598)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=1.3515915598)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=1.3515915598)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=1.3515915598)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=2.8141447562)

    # Simplified variant cases
    assert cmp_simp.sim_score('', '') == 0.0
    assert cmp_simp.sim_score('a', '') == -0.6931471805599453
    assert cmp_simp.sim_score('', 'a') == 0.0
    assert cmp_simp.sim_score('abc', '') == -2.772588722239781
    assert cmp_simp.sim_score('', 'abc') == 0.0
    assert cmp_simp.sim_score('abc', 'abc') == 5.545177444479562
    assert cmp_simp.sim_score('abcd', 'efgh') == -4.023594781085251
    assert cmp_simp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=2.6876392038420835)
    assert cmp_simp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=2.6876392038420835)
    assert cmp_simp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=2.6876392038420835)
    assert cmp_simp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=2.6876392038420835)
    assert cmp_simp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=11.322305105361572)
