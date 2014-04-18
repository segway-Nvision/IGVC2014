"""autogenerated by genpy from vectornav/ins.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class ins(genpy.Message):
  _md5sum = "ac6f3c29ebbc55e6d11838d54bc5749b"
  _type = "vectornav/ins"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """std_msgs/Header       header
float64               Time
uint16                Week
uint16                Status
geometry_msgs/Vector3 RPY
geometry_msgs/Vector3 LLA
geometry_msgs/Vector3 NedVel
float32               AttUncerainty
float32               PosUncerainty
float32               VelUncerainty


uint16 STATUS_INSUFFICIENT_MOTION=1
uint16 STATUS_INS_OK=2
uint16 STATUS_GPS_FIX_OK=4
uint16 STATUS_SENSOR_ERROR_TIME=8
uint16 STATUS_SENSOR_ERROR_IMU=16
uint16 STATUS_SENSOR_ERROR_MAG=32
uint16 STATUS_SENSOR_ERROR_GPS=64



================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 

float64 x
float64 y
float64 z
"""
  # Pseudo-constants
  STATUS_INSUFFICIENT_MOTION = 1
  STATUS_INS_OK = 2
  STATUS_GPS_FIX_OK = 4
  STATUS_SENSOR_ERROR_TIME = 8
  STATUS_SENSOR_ERROR_IMU = 16
  STATUS_SENSOR_ERROR_MAG = 32
  STATUS_SENSOR_ERROR_GPS = 64

  __slots__ = ['header','Time','Week','Status','RPY','LLA','NedVel','AttUncerainty','PosUncerainty','VelUncerainty']
  _slot_types = ['std_msgs/Header','float64','uint16','uint16','geometry_msgs/Vector3','geometry_msgs/Vector3','geometry_msgs/Vector3','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,Time,Week,Status,RPY,LLA,NedVel,AttUncerainty,PosUncerainty,VelUncerainty

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ins, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.Time is None:
        self.Time = 0.
      if self.Week is None:
        self.Week = 0
      if self.Status is None:
        self.Status = 0
      if self.RPY is None:
        self.RPY = geometry_msgs.msg.Vector3()
      if self.LLA is None:
        self.LLA = geometry_msgs.msg.Vector3()
      if self.NedVel is None:
        self.NedVel = geometry_msgs.msg.Vector3()
      if self.AttUncerainty is None:
        self.AttUncerainty = 0.
      if self.PosUncerainty is None:
        self.PosUncerainty = 0.
      if self.VelUncerainty is None:
        self.VelUncerainty = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.Time = 0.
      self.Week = 0
      self.Status = 0
      self.RPY = geometry_msgs.msg.Vector3()
      self.LLA = geometry_msgs.msg.Vector3()
      self.NedVel = geometry_msgs.msg.Vector3()
      self.AttUncerainty = 0.
      self.PosUncerainty = 0.
      self.VelUncerainty = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_d2H9d3f.pack(_x.Time, _x.Week, _x.Status, _x.RPY.x, _x.RPY.y, _x.RPY.z, _x.LLA.x, _x.LLA.y, _x.LLA.z, _x.NedVel.x, _x.NedVel.y, _x.NedVel.z, _x.AttUncerainty, _x.PosUncerainty, _x.VelUncerainty))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.RPY is None:
        self.RPY = geometry_msgs.msg.Vector3()
      if self.LLA is None:
        self.LLA = geometry_msgs.msg.Vector3()
      if self.NedVel is None:
        self.NedVel = geometry_msgs.msg.Vector3()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 96
      (_x.Time, _x.Week, _x.Status, _x.RPY.x, _x.RPY.y, _x.RPY.z, _x.LLA.x, _x.LLA.y, _x.LLA.z, _x.NedVel.x, _x.NedVel.y, _x.NedVel.z, _x.AttUncerainty, _x.PosUncerainty, _x.VelUncerainty,) = _struct_d2H9d3f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_d2H9d3f.pack(_x.Time, _x.Week, _x.Status, _x.RPY.x, _x.RPY.y, _x.RPY.z, _x.LLA.x, _x.LLA.y, _x.LLA.z, _x.NedVel.x, _x.NedVel.y, _x.NedVel.z, _x.AttUncerainty, _x.PosUncerainty, _x.VelUncerainty))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.RPY is None:
        self.RPY = geometry_msgs.msg.Vector3()
      if self.LLA is None:
        self.LLA = geometry_msgs.msg.Vector3()
      if self.NedVel is None:
        self.NedVel = geometry_msgs.msg.Vector3()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 96
      (_x.Time, _x.Week, _x.Status, _x.RPY.x, _x.RPY.y, _x.RPY.z, _x.LLA.x, _x.LLA.y, _x.LLA.z, _x.NedVel.x, _x.NedVel.y, _x.NedVel.z, _x.AttUncerainty, _x.PosUncerainty, _x.VelUncerainty,) = _struct_d2H9d3f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_d2H9d3f = struct.Struct("<d2H9d3f")
_struct_3I = struct.Struct("<3I")
