# -*- coding: utf-8 -*-
#
#  SelfTest/Util/test_winrandom.py: Self-test for the winrandom module
#
# Written in 2008 by Dwayne C. Litzenberger <dlitz@dlitz.net>
#
# ===================================================================
# The contents of this file are dedicated to the public domain.  To
# the extent that dedication to the public domain is not available,
# everyone is granted a worldwide, perpetual, royalty-free,
# non-exclusive license to exercise all rights associated with the
# contents of this file for any purpose whatsoever.
# No rights are reserved.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ===================================================================

"""Self-test for the Crypto.Util.randpool.RandomPool wrapper class"""

__revision__ = "$Id$"

import sys
import unittest

class SimpleTest(unittest.TestCase):
    def runTest(self):
        """Crypto.Util.randpool.RandomPool"""
        # Import the winrandom module and try to use it
        from micropsi_core.world.MinecraftWorld.MinecraftClient.Crypto.Util.randpool import RandomPool
        sys.stderr.write("SelfTest: You can ignore the RandomPool_DeprecationWarning that follows.\n")
        rpool = RandomPool()
        x = rpool.get_bytes(16)
        y = rpool.get_bytes(16)
        self.assertNotEqual(x, y)
        self.assertNotEqual(rpool.entropy, 0)

        rpool.randomize()
        rpool.stir('foo')
        rpool.add_event('foo')

def get_tests(config={}):
    return [SimpleTest()]

if __name__ == '__main__':
    suite = lambda: unittest.TestSuite(get_tests())
    unittest.main(defaultTest='suite')

# vim:set ts=4 sw=4 sts=4 expandtab:
