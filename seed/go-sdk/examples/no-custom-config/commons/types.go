// This file was auto-generated by Fern from our API Definition.

package commons

import (
	json "encoding/json"
	fmt "fmt"
	core "github.com/examples/fern/core"
)

type Data struct {
	Type   string
	String string
	Base64 []byte
}

func NewDataFromString(value string) *Data {
	return &Data{Type: "string", String: value}
}

func NewDataFromBase64(value []byte) *Data {
	return &Data{Type: "base64", Base64: value}
}

func (d *Data) UnmarshalJSON(data []byte) error {
	var unmarshaler struct {
		Type string `json:"type"`
	}
	if err := json.Unmarshal(data, &unmarshaler); err != nil {
		return err
	}
	d.Type = unmarshaler.Type
	switch unmarshaler.Type {
	case "string":
		var valueUnmarshaler struct {
			String string `json:"value"`
		}
		if err := json.Unmarshal(data, &valueUnmarshaler); err != nil {
			return err
		}
		d.String = valueUnmarshaler.String
	case "base64":
		var valueUnmarshaler struct {
			Base64 []byte `json:"value"`
		}
		if err := json.Unmarshal(data, &valueUnmarshaler); err != nil {
			return err
		}
		d.Base64 = valueUnmarshaler.Base64
	}
	return nil
}

func (d Data) MarshalJSON() ([]byte, error) {
	switch d.Type {
	default:
		return nil, fmt.Errorf("invalid type %s in %T", d.Type, d)
	case "string":
		var marshaler = struct {
			Type   string `json:"type"`
			String string `json:"value"`
		}{
			Type:   "string",
			String: d.String,
		}
		return json.Marshal(marshaler)
	case "base64":
		var marshaler = struct {
			Type   string `json:"type"`
			Base64 []byte `json:"value"`
		}{
			Type:   "base64",
			Base64: d.Base64,
		}
		return json.Marshal(marshaler)
	}
}

type DataVisitor interface {
	VisitString(string) error
	VisitBase64([]byte) error
}

func (d *Data) Accept(visitor DataVisitor) error {
	switch d.Type {
	default:
		return fmt.Errorf("invalid type %s in %T", d.Type, d)
	case "string":
		return visitor.VisitString(d.String)
	case "base64":
		return visitor.VisitBase64(d.Base64)
	}
}

type EventInfo struct {
	Type     string
	Metadata *Metadata
	Tag      Tag
}

func NewEventInfoFromMetadata(value *Metadata) *EventInfo {
	return &EventInfo{Type: "metadata", Metadata: value}
}

func NewEventInfoFromTag(value Tag) *EventInfo {
	return &EventInfo{Type: "tag", Tag: value}
}

func (e *EventInfo) UnmarshalJSON(data []byte) error {
	var unmarshaler struct {
		Type string `json:"type"`
	}
	if err := json.Unmarshal(data, &unmarshaler); err != nil {
		return err
	}
	e.Type = unmarshaler.Type
	switch unmarshaler.Type {
	case "metadata":
		value := new(Metadata)
		if err := json.Unmarshal(data, &value); err != nil {
			return err
		}
		e.Metadata = value
	case "tag":
		var valueUnmarshaler struct {
			Tag Tag `json:"value"`
		}
		if err := json.Unmarshal(data, &valueUnmarshaler); err != nil {
			return err
		}
		e.Tag = valueUnmarshaler.Tag
	}
	return nil
}

func (e EventInfo) MarshalJSON() ([]byte, error) {
	switch e.Type {
	default:
		return nil, fmt.Errorf("invalid type %s in %T", e.Type, e)
	case "metadata":
		return core.MarshalJSONWithExtraProperty(e.Metadata, "type", "metadata")
	case "tag":
		var marshaler = struct {
			Type string `json:"type"`
			Tag  Tag    `json:"value"`
		}{
			Type: "tag",
			Tag:  e.Tag,
		}
		return json.Marshal(marshaler)
	}
}

type EventInfoVisitor interface {
	VisitMetadata(*Metadata) error
	VisitTag(Tag) error
}

func (e *EventInfo) Accept(visitor EventInfoVisitor) error {
	switch e.Type {
	default:
		return fmt.Errorf("invalid type %s in %T", e.Type, e)
	case "metadata":
		return visitor.VisitMetadata(e.Metadata)
	case "tag":
		return visitor.VisitTag(e.Tag)
	}
}

type Metadata struct {
	Id         string            `json:"id" url:"id"`
	Data       map[string]string `json:"data,omitempty" url:"data,omitempty"`
	JsonString *string           `json:"jsonString,omitempty" url:"jsonString,omitempty"`

	extraProperties map[string]interface{}
	_rawJSON        json.RawMessage
}

func (m *Metadata) GetExtraProperties() map[string]interface{} {
	return m.extraProperties
}

func (m *Metadata) UnmarshalJSON(data []byte) error {
	type unmarshaler Metadata
	var value unmarshaler
	if err := json.Unmarshal(data, &value); err != nil {
		return err
	}
	*m = Metadata(value)

	extraProperties, err := core.ExtractExtraProperties(data, *m)
	if err != nil {
		return err
	}
	m.extraProperties = extraProperties

	m._rawJSON = json.RawMessage(data)
	return nil
}

func (m *Metadata) String() string {
	if len(m._rawJSON) > 0 {
		if value, err := core.StringifyJSON(m._rawJSON); err == nil {
			return value
		}
	}
	if value, err := core.StringifyJSON(m); err == nil {
		return value
	}
	return fmt.Sprintf("%#v", m)
}

type Tag = string
