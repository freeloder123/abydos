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

"""abydos.tests.distance.test_distance_typo.

This module contains unit tests for abydos.distance.Typo
"""


import pytest

from abydos.distance import Typo


cmp = Typo()

cmp_auto = Typo(layout='auto', failsafe=True)


def test_typo_dist_abs():
    """Test abydos.distance.Typo.dist_abs."""
    # Base cases
    assert cmp.dist_abs('', '') == 0
    assert cmp.dist_abs('', 'typo') == 4
    assert cmp.dist_abs('typo', '') == 4

    assert cmp.dist_abs('asdf', 'zxcv') == 2
    assert cmp.dist_abs('asdf', 'ASDF') == 1
    assert cmp.dist_abs('asdf', 'qsdf') == 0.5

    assert Typo(metric='euclidean').dist_abs('asdf', 'asdt') == pytest.approx(abs=1e-7, expected=0.70710677)
    assert Typo(metric='manhattan').dist_abs('asdf', 'asdt') == pytest.approx(abs=1e-7, expected=1)
    assert Typo(metric='log-euclidean').dist_abs('asdf', 'asdt') == pytest.approx(abs=1e-7, expected=0.4406868)
    assert Typo(metric='log-manhattan').dist_abs('asdf', 'asdt') == pytest.approx(abs=1e-7, expected=0.54930615)

    assert cmp_auto.dist_abs('Schluß', 'Schluss') == 3
    assert cmp_auto.dist_abs('délicat', 'delicate') == pytest.approx(abs=1e-7, expected=1.7071068)
    assert cmp_auto.dist_abs('비빔밥', 'Bibimbap') == 11

    with pytest.raises(ValueError):
        cmp.dist_abs('asdf', 'Ösdf')

def test_typo_sim():
    """Test abydos.distance.Typo.sim."""
    # Base cases
    assert cmp.sim('', '') == 1
    assert cmp.sim('', 'typo') == 0
    assert cmp.sim('typo', '') == 0

    assert cmp.sim('asdf', 'zxcv') == 0.5
    assert cmp.sim('asdf', 'ASDF') == 0.75
    assert cmp.sim('asdf', 'qsdf') == 0.875

    assert Typo(metric='euclidean').sim('asdf', 'asdt') == pytest.approx(abs=1e-7, expected=1 - (0.70710677 / 4))
    assert Typo(metric='manhattan').sim('asdf', 'asdt') == pytest.approx(abs=1e-7, expected=0.75)
    assert Typo(metric='log-euclidean').sim('asdf', 'asdt') == pytest.approx(abs=1e-7, expected=1 - (0.4406868 / 4))
    assert Typo(metric='log-manhattan').sim('asdf', 'asdt') == pytest.approx(abs=1e-7, expected=1 - (0.54930615 / 4))

def test_typo_dist():
    """Test abydos.distance.Typo.dist."""
    # Base cases
    assert cmp.dist('', '') == 0
    assert cmp.dist('', 'typo') == 1
    assert cmp.dist('typo', '') == 1

    assert cmp.dist('asdf', 'zxcv') == 0.5
    assert cmp.dist('asdf', 'ASDF') == 0.25
    assert cmp.dist('asdf', 'qsdf') == 0.125

    assert Typo(metric='euclidean').dist('asdf', 'asdt') == pytest.approx(abs=1e-7, expected=0.70710677 / 4)
    assert Typo(metric='manhattan').dist('asdf', 'asdt') == pytest.approx(abs=1e-7, expected=0.25)
    assert Typo(metric='log-euclidean').dist('asdf', 'asdt') == pytest.approx(abs=1e-7, expected=0.4406868 / 4)
    assert Typo(metric='log-manhattan').dist('asdf', 'asdt') == pytest.approx(abs=1e-7, expected=0.54930615 / 4)
