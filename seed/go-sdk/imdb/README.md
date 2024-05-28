# Seed Go Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)
[![go shield](https://img.shields.io/badge/go-docs-blue)](https://pkg.go.dev/github.com/imdb/fern)

The Seed Go library provides convenient access to the Seed API from Go.

## Requirements

This SDK requires Go version >= 1.13.

## Installation

```sh
go get github.com/imdb/fern
```

## Usage

Instantiate the client with the following:

```go
import (
	fern "github.com/imdb/fern"
	fernclient "github.com/imdb/fern/client"
	option "github.com/imdb/fern/option"
)

client := fernclient.NewClient(
	option.WithToken(
		"<YOUR_AUTH_TOKEN>",
	),
)
response, err := client.Imdb.CreateMovie(
	ctx,
	&fern.CreateMovieRequest{
		Title:  "string",
		Rating: 1.1,
	},
)
```

## Timeouts

Setting a timeout for each individual request is as simple as
using the standard `context` library. Setting a one second timeout
for an individual API call looks like the following:

```go
ctx, cancel := context.WithTimeout(context.Background(), time.Second)
defer cancel()

response, err := client.Imdb.CreateMovie(
	ctx,
	&fern.CreateMovieRequest{
		Title:  "string",
		Rating: 1.1,
	},
)
```

## Request Options

A variety of request options are included to adapt the behavior of the library,
which includes configuring authorization tokens, or providing your own instrumented
`*http.Client`. Both of these options are shown below:

```go
client := fernclient.NewClient(
	option.WithToken(
		"<YOUR_AUTH_TOKEN>",
	),
)
response, err := client.Imdb.CreateMovie(
	ctx,
	&fern.CreateMovieRequest{
		Title:  "string",
		Rating: 1.1,
	},
	option.WithHTTPClient(
		&http.Client{
			Timeout: 5 * time.Second,
		},
	),
)
```
As you can see, these request options can either be specified on the client so that
they're applied on _every_ request or for an individual request.

> Providing your own `*http.Client` on the client constructor is recommended. Otherwise,
> the `http.DefaultClient` is used, and your client will wait indefinitely for a response
> (unless the per-request, context-based timeout is used).


## Errors

Structured error types are returned from API calls that return non-success status codes.
For example, you can check if the error was of a particular type with the following:

```go
response, err := client.Imdb.GetMovie(
	ctx,
	"string",
)
if err != nil {
	var apiError *core.APIError
	if errors.As(err, &apiError) {
		// Handle the error.
	}
	return nil, err
}
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!