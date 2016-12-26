// Code generated by protoc-gen-go.
// source: protos/errors.proto
// DO NOT EDIT!

/*
Package disposable is a generated protocol buffer package.

It is generated from these files:
	protos/errors.proto
	protos/service.proto

It has these top-level messages:
	Error
	DisposableRequest
	DisposableResponse
*/
package disposable

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

type Error struct {
	Message string            `protobuf:"bytes,1,opt,name=message" json:"message,omitempty"`
	Type    string            `protobuf:"bytes,2,opt,name=type" json:"type,omitempty"`
	Info    map[string]string `protobuf:"bytes,3,rep,name=info" json:"info,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
}

func (m *Error) Reset()                    { *m = Error{} }
func (m *Error) String() string            { return proto.CompactTextString(m) }
func (*Error) ProtoMessage()               {}
func (*Error) Descriptor() ([]byte, []int) { return fileDescriptor0, []int{0} }

func (m *Error) GetInfo() map[string]string {
	if m != nil {
		return m.Info
	}
	return nil
}

func init() {
	proto.RegisterType((*Error)(nil), "disposable.Error")
}

func init() { proto.RegisterFile("protos/errors.proto", fileDescriptor0) }

var fileDescriptor0 = []byte{
	// 198 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x09, 0x6e, 0x88, 0x02, 0xff, 0xe2, 0x12, 0x2e, 0x28, 0xca, 0x2f,
	0xc9, 0x2f, 0xd6, 0x4f, 0x2d, 0x2a, 0xca, 0x2f, 0x2a, 0xd6, 0x03, 0xf3, 0x84, 0xb8, 0x52, 0x32,
	0x8b, 0x0b, 0xf2, 0x8b, 0x13, 0x93, 0x72, 0x52, 0x95, 0xe6, 0x33, 0x72, 0xb1, 0xba, 0x82, 0x24,
	0x85, 0x24, 0xb8, 0xd8, 0x73, 0x53, 0x8b, 0x8b, 0x13, 0xd3, 0x53, 0x25, 0x18, 0x15, 0x18, 0x35,
	0x38, 0x83, 0x60, 0x5c, 0x21, 0x21, 0x2e, 0x96, 0x92, 0xca, 0x82, 0x54, 0x09, 0x26, 0xb0, 0x30,
	0x98, 0x2d, 0xa4, 0xcf, 0xc5, 0x92, 0x99, 0x97, 0x96, 0x2f, 0xc1, 0xac, 0xc0, 0xac, 0xc1, 0x6d,
	0x24, 0xad, 0x87, 0x30, 0x52, 0x0f, 0x6c, 0x9c, 0x9e, 0x27, 0x50, 0xd6, 0x35, 0xaf, 0xa4, 0xa8,
	0x32, 0x08, 0xac, 0x50, 0xca, 0x9c, 0x8b, 0x13, 0x2e, 0x24, 0x24, 0xc0, 0xc5, 0x9c, 0x9d, 0x5a,
	0x09, 0xb5, 0x07, 0xc4, 0x14, 0x12, 0xe1, 0x62, 0x2d, 0x4b, 0xcc, 0x29, 0x85, 0x59, 0x02, 0xe1,
	0x58, 0x31, 0x59, 0x30, 0x3a, 0x99, 0x72, 0x49, 0x19, 0x54, 0x18, 0x5a, 0xea, 0xa5, 0x67, 0x96,
	0x64, 0x94, 0x26, 0xe9, 0x25, 0xe7, 0xe7, 0x22, 0x59, 0x16, 0x85, 0xe4, 0x97, 0x45, 0x4c, 0x5c,
	0x2e, 0x70, 0x4e, 0x12, 0x1b, 0xd8, 0xaf, 0xc6, 0x80, 0x00, 0x00, 0x00, 0xff, 0xff, 0x10, 0xba,
	0xdd, 0x31, 0x02, 0x01, 0x00, 0x00,
}