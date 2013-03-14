# Copyright (c) 2012-2013 SHIFT.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import thunderdome
from thunderdome import OUT
from thunderdome_logging.graph_handler import Errors


def get_errors(vid, max_num_errors=5):
    """
    Returns the last max_num_errors for the vertex with the given vid.

    :param vid: The UUID uniquely identifying the vertex in the graph
    :type vid: str
    :param max_num_errors: The maximum number of errors to be returned
    :type max_num_errors: int

    :rtype: list
    
    """
    vert = thunderdome.Vertex.get(vid)
    q = vert.query()
    return q.labels(Errors).direction(OUT).limit(max_num_errors).vertices()
