# Copyright 2014-2020 by Christopher C. Little.
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

"""abydos.tests.distance.test_distance_monge_elkan.

This module contains unit tests for abydos.distance.MongeElkan
"""


import pytest

from abydos.distance import Jaccard, MongeElkan


cmp = MongeElkan()

cmp_sym = MongeElkan(symmetric=True)

cmp_jac = MongeElkan(sim_func=Jaccard())

cmp_jac_sim = MongeElkan(sim_func=Jaccard().sim)


def test_monge_elkan_sim():
    """Test abydos.distance.MongeElkan.sim."""
    assert cmp.sim('', '') == 1
    assert cmp.sim('', 'a') == 0
    assert cmp.sim('a', 'a') == 1

    assert cmp.sim('Niall', 'Neal') == 3 / 4
    assert cmp.sim('Niall', 'Njall') == 5 / 6
    assert cmp.sim('Niall', 'Niel') == 3 / 4
    assert cmp.sim('Niall', 'Nigel') == 3 / 4

    assert cmp_sym.sim('Niall', 'Neal') == 31 / 40
    assert cmp_sym.sim('Niall', 'Njall') == 5 / 6
    assert cmp_sym.sim('Niall', 'Niel') == 31 / 40
    assert cmp_sym.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=17 / 24)

    assert cmp_jac.sim('Njall', 'Neil') == 29 / 60
    assert cmp_jac_sim.sim('Njall', 'Neil') == 29 / 60

def test_monge_elkan_dist():
    """Test abydos.distance.MongeElkan.dist."""
    assert cmp.dist('', '') == 0
    assert cmp.dist('', 'a') == 1

    assert cmp.dist('Niall', 'Neal') == 1 / 4
    assert cmp.dist('Niall', 'Njall') == pytest.approx(abs=1e-7, expected=1 / 6)
    assert cmp.dist('Niall', 'Niel') == 1 / 4
    assert cmp.dist('Niall', 'Nigel') == 1 / 4

    assert cmp_sym.dist('Niall', 'Neal') == pytest.approx(abs=1e-7, expected=9 / 40)
    assert cmp_sym.dist('Niall', 'Njall') == pytest.approx(abs=1e-7, expected=1 / 6)
    assert cmp_sym.dist('Niall', 'Niel') == pytest.approx(abs=1e-7, expected=9 / 40)
    assert cmp_sym.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=7 / 24)
