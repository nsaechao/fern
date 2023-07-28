// This file was auto-generated by Fern from our API Definition.

package api

import (
	core "github.com/fern-api/fern-go/internal/testdata/sdk/bearer-token-name/fixtures/core"
	http "net/http"
)

type Client interface {
	User() UserClient
}

func NewClient(opts ...core.ClientOption) Client {
	options := core.NewClientOptions()
	for _, opt := range opts {
		opt(options)
	}
	return &client{
		baseURL:    options.BaseURL,
		httpClient: options.HTTPClient,
		header:     options.ToHeader(),
		userClient: NewUserClient(opts...),
	}
}

type client struct {
	baseURL    string
	httpClient core.HTTPClient
	header     http.Header
	userClient UserClient
}

func (c *client) User() UserClient {
	return c.userClient
}
