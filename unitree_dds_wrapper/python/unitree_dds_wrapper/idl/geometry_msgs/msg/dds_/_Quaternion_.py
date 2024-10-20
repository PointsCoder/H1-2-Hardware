"""
  Generated by Eclipse Cyclone DDS idlc Python Backend
  Cyclone DDS IDL version: v0.11.0
  Module: geometry_msgs.msg.dds_
  IDL file: Quaternion_.idl

"""

from enum import auto
from typing import TYPE_CHECKING, Optional
from dataclasses import dataclass, field

import cyclonedds.idl as idl
import cyclonedds.idl.annotations as annotate
import cyclonedds.idl.types as types

# root module import for resolving types
# import geometry_msgs


@dataclass
@annotate.final
@annotate.autoid("sequential")
class Quaternion_(idl.IdlStruct, typename="geometry_msgs.msg.dds_.Quaternion_"):
    x: types.float64 = field(default_factory=lambda: 0.0)
    y: types.float64 = field(default_factory=lambda: 0.0)
    z: types.float64 = field(default_factory=lambda: 0.0)
    w: types.float64 = field(default_factory=lambda: 0.0)


