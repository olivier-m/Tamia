# -*- coding: utf-8 -*-
#
# This file is part of Octopus released under the FreeBSD license.
# See the LICENSE for more information.
from __future__ import (print_function, division, absolute_import, unicode_literals)


class OctopusError(Exception):
    pass

class RepositoryNotFound(OctopusError):
    pass


class NodeNotFound(OctopusError):
    pass


class RevisionNotFound(OctopusError):
    pass