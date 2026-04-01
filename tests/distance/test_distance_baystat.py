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

"""abydos.tests.distance.test_distance_baystat.

This module contains unit tests for abydos.distance.Baystat
"""


import pytest

from abydos.distance import Baystat


cmp = Baystat()


def test_baystat_sim():
    """Test abydos.distance.Baystat.sim."""
    # Base cases
    assert cmp.sim('', '') == 1
    assert cmp.sim('Colin', '') == 0
    assert cmp.sim('Colin', 'Colin') == 1

    # Examples given in the paper
    # https://www.statistik.bayern.de/medien/statistik/zensus/zusammenf__hrung_von_datenbest__nden_ohne_numerische_identifikatoren.pdf
    assert cmp.sim('DRAKOMENA', 'DRAOMINA') == pytest.approx(abs=1e-7, expected=7 / 9)
    assert cmp.sim('RIEKI', 'RILKI') == pytest.approx(abs=1e-7, expected=4 / 5)
    assert cmp.sim('ATANASSIONI', 'ATANASIOU') == pytest.approx(abs=1e-7, expected=8 / 11)
    assert cmp.sim('LIESKOVSKY', 'LIESZKOVSZKY') == pytest.approx(abs=1e-7, expected=10 / 12)
    assert cmp.sim('JEANETTE', 'JEANNETTE') == pytest.approx(abs=1e-7, expected=8 / 9)
    assert cmp.sim('JOHANNES', 'JOHAN') == pytest.approx(abs=1e-7, expected=0.625)
    assert cmp.sim('JOHANNES', 'HANS') == pytest.approx(abs=1e-7, expected=0.375)
    assert cmp.sim('JOHANNES', 'HANNES') == pytest.approx(abs=1e-7, expected=0.75)
    assert cmp.sim('ZIMMERMANN', 'SEMMERMANN') == pytest.approx(abs=1e-7, expected=0.8)
    assert cmp.sim('ZIMMERMANN', 'ZIMMERER') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.sim('ZIMMERMANN', 'ZIMMER') == pytest.approx(abs=1e-7, expected=0.6)

    # Tests to maximize coverage
    assert Baystat(2, 2, 2).sim('ZIMMERMANN', 'SEMMERMANN') == pytest.approx(abs=1e-7, expected=0.8)
    assert cmp.sim('ZIMMER', 'ZIMMERMANN') == pytest.approx(abs=1e-7, expected=0.6)

def test_baystat_dist():
    """Test abydos.distance.Baystat.dist."""
    # Base cases
    assert cmp.dist('', '') == 0
    assert cmp.dist('Colin', '') == 1
    assert cmp.dist('Colin', 'Colin') == 0

    # Examples given in the paper
    # https://www.statistik.bayern.de/medien/statistik/zensus/zusammenf__hrung_von_datenbest__nden_ohne_numerische_identifikatoren.pdf
    assert cmp.dist('DRAKOMENA', 'DRAOMINA') == pytest.approx(abs=1e-7, expected=2 / 9)
    assert cmp.dist('RIEKI', 'RILKI') == pytest.approx(abs=1e-7, expected=1 / 5)
    assert cmp.dist('ATANASSIONI', 'ATANASIOU') == pytest.approx(abs=1e-7, expected=3 / 11)
    assert cmp.dist('LIESKOVSKY', 'LIESZKOVSZKY') == pytest.approx(abs=1e-7, expected=2 / 12)
    assert cmp.dist('JEANETTE', 'JEANNETTE') == pytest.approx(abs=1e-7, expected=1 / 9)
    assert cmp.dist('JOHANNES', 'JOHAN') == pytest.approx(abs=1e-7, expected=0.375)
    assert cmp.dist('JOHANNES', 'HANS') == pytest.approx(abs=1e-7, expected=0.625)
    assert cmp.dist('JOHANNES', 'HANNES') == pytest.approx(abs=1e-7, expected=0.25)
    assert cmp.dist('ZIMMERMANN', 'SEMMERMANN') == pytest.approx(abs=1e-7, expected=0.2)
    assert cmp.dist('ZIMMERMANN', 'ZIMMERER') == pytest.approx(abs=1e-7, expected=0.4)
    assert cmp.dist('ZIMMERMANN', 'ZIMMER') == pytest.approx(abs=1e-7, expected=0.4)
