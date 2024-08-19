// This file was auto-generated by Fern from our API Definition.

package api

type DeleteRequest struct {
	Ids       []string  `json:"ids,omitempty" url:"-"`
	DeleteAll *bool     `json:"deleteAll,omitempty" url:"-"`
	Namespace *string   `json:"namespace,omitempty" url:"-"`
	Filter    *Metadata `json:"filter,omitempty" url:"-"`
}

type DescribeRequest struct {
	Filter *Metadata `json:"filter,omitempty" url:"-"`
}

type FetchRequest struct {
	Ids       []*string `query:"ids"`
	Namespace *string   `query:"namespace"`
}

type ListRequest struct {
	Prefix          *string `query:"prefix"`
	Limit           *int    `query:"limit"`
	PaginationToken *string `query:"paginationToken"`
	Namespace       *string `query:"namespace"`
}

type QueryRequest struct {
	Namespace       *string        `json:"namespace,omitempty" url:"-"`
	TopK            int            `json:"topK" url:"-"`
	Filter          *Metadata      `json:"filter,omitempty" url:"-"`
	IncludeValues   *bool          `json:"includeValues,omitempty" url:"-"`
	IncludeMetadata *bool          `json:"includeMetadata,omitempty" url:"-"`
	Queries         []*QueryColumn `json:"queries,omitempty" url:"-"`
	Column          []float64      `json:"column,omitempty" url:"-"`
	Id              *string        `json:"id,omitempty" url:"-"`
	IndexedData     *IndexedData   `json:"indexedData,omitempty" url:"-"`
}

type UpdateRequest struct {
	Id          string       `json:"id" url:"-"`
	Values      []float64    `json:"values,omitempty" url:"-"`
	SetMetadata *Metadata    `json:"setMetadata,omitempty" url:"-"`
	Namespace   *string      `json:"namespace,omitempty" url:"-"`
	IndexedData *IndexedData `json:"indexedData,omitempty" url:"-"`
}

type UploadRequest struct {
	Columns   []*Column `json:"columns,omitempty" url:"-"`
	Namespace *string   `json:"namespace,omitempty" url:"-"`
}
