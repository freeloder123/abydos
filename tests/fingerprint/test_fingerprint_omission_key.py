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

"""abydos.tests.fingerprint.test_fingerprint_omission_key.

This module contains unit tests for abydos.fingerprint.OmissionKey
"""


from abydos.fingerprint import OmissionKey


fp = OmissionKey()


def test_omission_key():
    """Test abydos.fingerprint.OmissionKey."""
    # Base case
    assert fp.fingerprint('') == ''

    # http://dl.acm.org/citation.cfm?id=358048
    assert fp.fingerprint('microelectronics') == 'MCLNTSRIOE'
    assert fp.fingerprint('circumstantial') == 'MCLNTSRIUA'
    assert fp.fingerprint('luminescent') == 'MCLNTSUIE'
    assert fp.fingerprint('multinucleate') == 'MCLNTUIEA'
    assert fp.fingerprint('multinucleon') == 'MCLNTUIEO'
    assert fp.fingerprint('cumulene') == 'MCLNUE'
    assert fp.fingerprint('luminance') == 'MCLNUIAE'
    assert fp.fingerprint('coelomic') == 'MCLOEI'
    assert fp.fingerprint('molecule') == 'MCLOEU'
    assert fp.fingerprint('cameral') == 'MCLRAE'
    assert fp.fingerprint('caramel') == 'MCLRAE'
    assert fp.fingerprint('maceral') == 'MCLRAE'
    assert fp.fingerprint('lacrimal') == 'MCLRAI'
