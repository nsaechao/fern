# Seed Go Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)
[![go shield](https://img.shields.io/badge/go-docs-blue)](https://pkg.go.dev/github.com/bytes/fern)

The Seed Go library provides convenient access to the Seed API from Go.

## Requirements

This SDK requires Go version >= 1.13.

## Installation

```sh
go get github.com/bytes/fern
```

## Usage

Instantiate the client with the following:

```go
import fernclient "github.com/bytes/fern/client"

client := fernclient.NewClient()
err := client.Service.Upload(
	ctx,
)
```

## Timeouts

Setting a timeout for each individual request is as simple as
using the standard `context` library. Setting a one second timeout
for an individual API call looks like the following:

```go
ctx, cancel := context.WithTimeout(context.Background(), time.Second)
defer cancel()

err := client.Service.Upload(
	ctx,
)
```

## Request Options

A variety of request options are included to adapt the behavior of the library,
which includes configuring authorization tokens, or providing your own instrumented
`*http.Client`. Both of these options are shown below:

```go
client := fernclient.NewClient()
err := client.Service.Upload(
	ctx,
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


## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!