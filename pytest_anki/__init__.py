# pytest-anki
#
# Copyright (C)  2019-2021 Aristotelis P. <https://glutanimate.com/>
#                and contributors (see CONTRIBUTORS file)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version, with the additions
# listed at the end of the license file that accompanied this program.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# NOTE: This program is subject to certain additional terms pursuant to
# Section 7 of the GNU Affero General Public License.  You should have
# received a copy of these additional terms immediately following the
# terms and conditions of the GNU Affero General Public License that
# accompanied this program.
#
# If not, please request a copy through one of the means of contact
# listed here: <https://glutanimate.com/contact/>.
#
# Any modifications to this file must keep this entire header intact.


"""
A simple pytest plugin for testing Anki add-ons
"""

__all__ = ["AnkiStateUpdate", "AnkiWebViewType", "AnkiSessionError", "AnkiSession"]

from ._anki import AnkiStateUpdate, AnkiWebViewType  # noqa: F401
from ._errors import AnkiSessionError  # noqa: F401
from ._session import AnkiSession  # noqa: F401

__version__ = "1.0.0-beta.3"
__author__ = "Aristotelis P. (Glutanimate), Michal Krassowski"
__title__ = "pytest-anki"
__homepage__ = "https://github.com/glutanimate/pytest-anki"
