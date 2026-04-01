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

"""abydos.tests.distance.test_distance__distance.

This module contains unit tests for abydos.distance._Distance
"""


from abydos.distance import Dice, Levenshtein


lev = Levenshtein()

dice = Dice()


def test_sim():
    """Test abydos.distance._Distance.sim."""
    assert lev.sim('Niall', 'Nigel') == 1.0 - lev.dist('Niall', 'Nigel')
    assert dice.dist('Niall', 'Nigel') == 1.0 - dice.sim('Niall', 'Nigel')

def test_dist():
    """Test abydos.distance._Distance.dist."""
    assert 1.0 - lev.sim('Niall', 'Nigel') == lev.dist('Niall', 'Nigel')
    assert 1.0 - dice.dist('Niall', 'Nigel') == dice.sim('Niall', 'Nigel')

def test_dist_abs():
    """Test abydos.distance._Distance.dist_abs."""
    assert dice.dist('Niall', 'Nigel') == dice.dist_abs('Niall', 'Nigel')
