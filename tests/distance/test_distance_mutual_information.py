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

"""abydos.tests.distance.test_distance_mutual_information.

This module contains unit tests for abydos.distance.MutualInformation
"""


import pytest

from abydos.distance import MutualInformation


cmp = MutualInformation()

cmp_no_d = MutualInformation(alphabet=0)


def test_mutual_information_sim():
    """Test abydos.distance.MutualInformation.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=0.17522996523538537)

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.9284965499)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.9284965499)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.9284965499)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.9284965499)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.9481813127)

    assert cmp_no_d.sim('a', 'eh') == pytest.approx(abs=1e-7, expected=-0.9036774610288023)

def test_mutual_information_dist():
    """Test abydos.distance.MutualInformation.dist."""
    # Base cases
    assert cmp.dist('', '') == 1.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=0.8247700347646146)

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.0715034501)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.0715034501)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.0715034501)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.0715034501)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.0518186873)

def test_mutual_information_sim_score():
    """Test abydos.distance.MutualInformation.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 0.0
    assert cmp.sim_score('a', '') == 0.0
    assert cmp.sim_score('', 'a') == 0.0
    assert cmp.sim_score('abc', '') == 0.0
    assert cmp.sim_score('', 'abc') == 0.0
    assert cmp.sim_score('abc', 'abc') == pytest.approx(abs=1e-7, expected=7.527706972593263)
    assert cmp.sim_score('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=-4.700439718141092)

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=5.9908322396)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=5.9908322396)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=5.9908322396)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=5.9908322396)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=5.6279117576)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim_score('', '') == 0.0
    assert cmp_no_d.sim_score('a', '') == 0.0
    assert cmp_no_d.sim_score('', 'a') == 0.0
    assert cmp_no_d.sim_score('abc', '') == 0.0
    assert cmp_no_d.sim_score('', 'abc') == 0.0
    assert cmp_no_d.sim_score('abc', 'abc') == 0.0
    assert cmp_no_d.sim_score('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=-4.700439718141092)

    assert cmp_no_d.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=-0.4020984436)
    assert cmp_no_d.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=-0.4020984436)
    assert cmp_no_d.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=-0.4020984436)
    assert cmp_no_d.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=-0.4020984436)
    assert cmp_no_d.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=-0.1650592463)
