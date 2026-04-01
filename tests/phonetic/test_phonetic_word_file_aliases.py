# Copyright 2026 by OpenAI.
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

"""Tests for aliases matching the external phonetic algorithm checklist."""

from abydos.phonetic import (
    AmericanSoundex,
    BeiderMorse,
    BMPM,
    Caverphone,
    Caverphone2,
    CFE,
    ColognePhonetics,
    Koelner,
    MatchRatingApproach,
    MRA,
    OriginalSoundex,
    PhoneticSpanish,
    Soundex,
)


def test_word_file_alias_identities():
    """Test that word-file aliases resolve to the expected implementations."""
    assert AmericanSoundex is Soundex
    assert OriginalSoundex is Soundex
    assert ColognePhonetics is Koelner
    assert Caverphone2 is Caverphone
    assert BMPM is BeiderMorse
    assert MatchRatingApproach is MRA
    assert CFE is PhoneticSpanish


def test_word_file_alias_behaviors():
    """Test that aliased names retain the expected algorithm behavior."""
    assert AmericanSoundex().encode('Christopher') == Soundex().encode(
        'Christopher'
    )
    assert ColognePhonetics().encode('Muller') == Koelner().encode('Muller')
    assert Caverphone2().encode('Christopher') == Caverphone().encode(
        'Christopher'
    )
    assert BMPM().encode('Schmidt') == BeiderMorse().encode('Schmidt')
    assert MatchRatingApproach().encode('Smith') == MRA().encode('Smith')
    assert CFE().encode('Perez') == PhoneticSpanish().encode('Perez')
