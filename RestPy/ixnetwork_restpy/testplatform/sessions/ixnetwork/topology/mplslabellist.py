
# Copyright 1997 - 2018 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
    
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MplsLabelList(Base):
	"""The MplsLabelList class encapsulates a system managed mplsLabelList node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the MplsLabelList property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'mplsLabelList'

	def __init__(self, parent):
		super(MplsLabelList, self).__init__(parent)

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def MplsEXP(self):
		"""EXP bits in the MPLS Label

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('mplsEXP')

	@property
	def MplsLabel(self):
		"""MPLS Label. Note that 3 is treated as Implicit NULL and not included in the SBFD Packet sent on the wire. This can be used to create assymetric label stacks for different Initiator S-BFD sessions.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('mplsLabel')

	@property
	def MplsTTL(self):
		"""MPLS TTL in the MPLS Label field.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('mplsTTL')

	@property
	def Name(self):
		"""Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	def find(self, Count=None, DescriptiveName=None, Name=None):
		"""Finds and retrieves mplsLabelList data from the server.

		All named parameters support regex and can be used to selectively retrieve mplsLabelList data from the server.
		By default the find method takes no parameters and will retrieve all mplsLabelList data from the server.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			self: This instance with matching mplsLabelList data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of mplsLabelList data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the mplsLabelList data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
