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

"""abydos.tests.fingerprint.test_fingerprint_bwtf.

This module contains unit tests for abydos.fingerprint.BWTF
"""


from abydos.fingerprint import BWTF


bwt = BWTF()

bwt_pipe = BWTF('|')

bwt_dollar = BWTF('$')


def test_consonant_bwtf():
    """Test abydos.fingerprint.BWTF."""
    # Examples from Wikipedia entry on BWT
    assert bwt.fingerprint('') == '\x00'
    assert bwt_pipe.fingerprint('^BANANA') == 'BNN^AA|A'
    assert (
        bwt_pipe.fingerprint( 'SIX.MIXED.PIXIES.SIFT.SIXTY.PIXIE.DUST.BOXES' )
        == 'TEXYDST.E.IXIXIXXSSMPPS.B..E.|.UESFXDIIOIIITS'
    )

    assert bwt_dollar.fingerprint('aardvark') == 'k$avrraad'
