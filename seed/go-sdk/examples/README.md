# Seed Go Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)
[![go shield](https://img.shields.io/badge/go-docs-blue)](https://pkg.go.dev/github.com/examples/fern)

The Seed Go library provides convenient access to the Seed API from Go.

## Requirements

This SDK requires Go version >= 1.13.

## Installation

```sh
go get github.com/examples/fern
```

## Usage

Instantiate the client with the following:

```go
import (
	fern "github.com/examples/fern"
	fernclient "github.com/examples/fern/client"
	option "github.com/examples/fern/option"
)

client := fernclient.NewClient(
	option.WithToken(
		"<YOUR_AUTH_TOKEN>",
	),
	option.WithBaseURL(
		fern.Environments.Production,
	),
)
response, err := client.Echo(
	ctx,
	"Hello world!\\n\\nwith\\n\\tnewlines",
)
```

## Timeouts

Setting a timeout for each individual request is as simple as
using the standard `context` library. Setting a one second timeout
for an individual API call looks like the following:

```go
ctx, cancel := context.WithTimeout(context.Background(), time.Second)
defer cancel()

response, err := client.Echo(
	ctx,
	"Hello world!\\n\\nwith\\n\\tnewlines",
)
```

## Errors

Structured error types are returned from API calls that return non-success status codes.
For example, you can check if the error was of a particular type with the following:

```go
response, err := client.File.Service.GetFile(
	ctx,
	"file.txt",
	&file.GetFileRequest{
		XFileApiVersion: "0.0.2",
	},
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