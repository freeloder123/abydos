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

"""abydos.tests.util.test_ncr.

This module contains unit tests for abydos.util._ncr
"""


import pytest

from abydos.util._ncr import _ncr


def test_ncr():
    """Test abydos.util._ncr."""
    assert _ncr(1, 0) == 1
    assert _ncr(5, 0) == 1

    assert _ncr(1, 2) == 0
    assert _ncr(1, 2) == 0

    assert _ncr(2, 2) == 1
    assert _ncr(10, 10) == 1

    assert _ncr(7, 2) == 21
    assert _ncr(7, 3) == 35
    assert _ncr(4, 3) == 4
    assert _ncr(5, 3) == 10
    assert _ncr(10, 2) == 45
    assert _ncr(100, 3) == 161700
    assert _ncr(80, 5) == 24040016

    # gamma variant
    assert _ncr(10, 2.5) == pytest.approx(abs=1e-7, expected=77.8023559942)
    assert _ncr(0, 2.5) == pytest.approx(abs=1e-7, expected=0.12732395447)
    assert _ncr(2.5, 2.5) == pytest.approx(abs=1e-7, expected=1)
    assert _ncr(2.5, 2.1) == pytest.approx(abs=1e-7, expected=1.7043970865)
