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

"""abydos.tests.distance.test_distance_ssk.

This module contains unit tests for abydos.distance.SSK
"""


import pytest

from abydos.distance import SSK

import numpy as np


cmp = SSK()

cmp_05 = SSK(ssk_lambda=0.05)


def test_ssk_sim():
    """Test abydos.distance.SSK.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.341958748279)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.341958748279)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.875737900641)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.875737900641)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.932931869)

    # Examples from paper
    assert cmp.sim('cat', 'car') == pytest.approx(abs=1e-7, expected=0.3558718861209964)
    assert cmp_05.sim('cat', 'car') == pytest.approx(abs=1e-7, expected=0.4993757802746567)

def test_ssk_sim_score():
    """Test abydos.distance.SSK.sim_score."""
    # Base cases
    assert cmp.sim_score('', '') == 0
    assert cmp.sim_score('a', '') == 0
    assert cmp.sim_score('', 'a') == 0
    assert cmp.sim_score('abc', '') == 0
    assert cmp.sim_score('', 'abc') == 0
    assert cmp.sim_score('abc', 'abc') == pytest.approx(abs=1e-7, expected=1.843641)
    assert cmp.sim_score('abcd', 'efgh') == 0

    assert cmp.sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=2.3009630391)
    assert cmp.sim_score('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=2.3009630391)
    assert cmp.sim_score('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=4.7537994501)
    assert cmp.sim_score('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=4.7537994501)
    assert cmp.sim_score('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=59.67083050606762)

    # Examples from paper
    assert cmp.sim_score('cat', 'car') == 0.6561000000000001
    assert cmp_05.sim_score('cat', 'car') == 6.250000000000003e-06

    # multiple lambdas
    assert SSK(ssk_lambda=0.05).sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=6.250822363281253e-06)
    assert SSK(ssk_lambda=0.5).sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.0771484375)
    assert SSK(ssk_lambda=np.arange(0.05, 0.5, 0.05)).sim_score(
            'Nigel', 'Niall'
        ) == pytest.approx(abs=1e-7, expected=0.5461411944067384)
    assert SSK(ssk_lambda=(0.05, 0.5)).sim_score('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.07841429769736327)
