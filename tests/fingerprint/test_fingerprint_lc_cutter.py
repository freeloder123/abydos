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

"""abydos.tests.fingerprint.test_fingerprint_lc_cutter.

This module contains unit tests for abydos.fingerprint.LCCutter
"""


from abydos.fingerprint import LCCutter


fp = LCCutter()


def test_lc_cutter_fingerprint():
    """Test abydos.fingerprint.LCCutter."""
    # Base case
    assert fp.fingerprint('') == ''
    assert fp.fingerprint('S') == 'S'

    # Test cases drawn from http://calculate.alptown.com/
    assert fp.fingerprint('Cutter') == 'C88847'
    assert fp.fingerprint('Quiet') == 'Q548'
    assert fp.fingerprint('Schmidt') == 'S36538'
    assert fp.fingerprint('Anderson') == 'A5347766'
    assert fp.fingerprint('Aziz') == 'A959'
    assert fp.fingerprint('I.B.M.') == 'I26'
    assert fp.fingerprint('Import') == 'I47678'
    assert fp.fingerprint('Sadron') == 'S23766'
    assert fp.fingerprint('Stinson') == 'S756766'
    assert fp.fingerprint('Cymbal') == 'C96335'
    assert fp.fingerprint('Ipswich') == 'I679534'
    assert fp.fingerprint('Rhododendron') == 'R46363463766'
    assert fp.fingerprint('Colin') == 'C6556'
    assert fp.fingerprint('Szelazek') == 'S9453945'
    assert fp.fingerprint('Quyen') == 'Q946'

    # Coverage
    assert fp.fingerprint('Qdoba') == 'Q2633'
    assert LCCutter(max_length=-1).fingerprint('Qdoba') == 'Q2633'
    assert LCCutter(max_length=3).fingerprint('Qdoba') == 'Q26'
