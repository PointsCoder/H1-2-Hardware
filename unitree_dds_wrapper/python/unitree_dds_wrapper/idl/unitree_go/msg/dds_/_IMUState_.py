"""
  Generated by Eclipse Cyclone DDS idlc Python Backend
  Cyclone DDS IDL version: v0.11.0
  Module: unitree_go.msg.dds_
  IDL file: IMUState_.idl

"""

from enum import auto
from typing import TYPE_CHECKING, Optional
from dataclasses import dataclass, field

import cyclonedds.idl as idl
import cyclonedds.idl.annotations as annotate
import cyclonedds.idl.types as types

@dataclass
@annotate.final
@annotate.autoid("sequential")
class IMUState_(idl.IdlStruct, typename="unitree_go.msg.dds_.IMUState_"):
    quaternion: types.array[types.float32, 4] = field(default_factory=lambda: [1, 0, 0, 0])
    gyroscope: types.array[types.float32, 3] = field(default_factory=lambda: [0, 0, 0])
    accelerometer: types.array[types.float32, 3] = field(default_factory=lambda: [0, 0, 0])
    rpy: types.array[types.float32, 3] = field(default_factory=lambda: [0, 0, 0])
    temperature: types.uint8 = field(default_factory=lambda: 0)


