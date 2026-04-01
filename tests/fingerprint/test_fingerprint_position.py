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

"""abydos.tests.fingerprint.test_fingerprint_position.

This module contains unit tests for abydos.fingerprint.Position
"""


from abydos.fingerprint import Position


fp = Position()


def test_position_fingerprint():
    """Test abydos.fingerprint.Position."""
    # Base case
    assert fp.fingerprint('') == '1111111111111111'

    # https://arxiv.org/pdf/1711.08475.pdf
    assert fp.fingerprint('instance') == '1110111001110001'

    assert fp.fingerprint('instance') == '1110111001110001'
    assert Position(15).fingerprint('instance') == '111011100111000'
    assert (
        Position(32).fingerprint('instance')
        == '11101110011100000101011111111111'
    )
    assert (
        Position(64).fingerprint('instance')
        == '11101110011100000101011111111111' + '11101111111111111111111111111111'
    )
