
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


class BgpExtendedCommunitiesList(Base):
	"""The BgpExtendedCommunitiesList class encapsulates a system managed bgpExtendedCommunitiesList node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the BgpExtendedCommunitiesList property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'bgpExtendedCommunitiesList'

	def __init__(self, parent):
		super(BgpExtendedCommunitiesList, self).__init__(parent)

	@property
	def AsNumber2Bytes(self):
		"""AS 2-Bytes

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('asNumber2Bytes')

	@property
	def AsNumber4Bytes(self):
		"""AS 4-Bytes

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('asNumber4Bytes')

	@property
	def AssignedNumber2Bytes(self):
		"""Assigned Number(2 Octets)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('assignedNumber2Bytes')

	@property
	def AssignedNumber4Bytes(self):
		"""Assigned Number(4 Octets)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('assignedNumber4Bytes')

	@property
	def ColorCOBits(self):
		"""Color CO Bits

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('colorCOBits')

	@property
	def ColorReservedBits(self):
		"""Color Reserved Bits

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('colorReservedBits')

	@property
	def ColorValue(self):
		"""Color Value

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('colorValue')

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
	def Ip(self):
		"""IP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ip')

	@property
	def LinkBandwidth(self):
		"""Link Bandwidth

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('linkBandwidth')

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

	@property
	def OpaqueData(self):
		"""Opaque Data

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('opaqueData')

	@property
	def SubType(self):
		"""SubType

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('subType')

	@property
	def Type(self):
		"""Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('type')

	def find(self, Count=None, DescriptiveName=None, Name=None):
		"""Finds and retrieves bgpExtendedCommunitiesList data from the server.

		All named parameters support regex and can be used to selectively retrieve bgpExtendedCommunitiesList data from the server.
		By default the find method takes no parameters and will retrieve all bgpExtendedCommunitiesList data from the server.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			self: This instance with matching bgpExtendedCommunitiesList data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of bgpExtendedCommunitiesList data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the bgpExtendedCommunitiesList data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
