[![License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://travis-ci.org/0x19/disposable/tree/master/LICENSE)
[![Build Status](https://travis-ci.org/0x19/goesl.svg)](https://travis-ci.org/0x19/disposable)
[![GoDoc](https://godoc.org/github.com/0x19/disposable?status.svg)](https://godoc.org/github.com/0x19/disposable)
[![Go 1.5 Ready](https://img.shields.io/badge/Go%201.5-Ready-green.svg?style=flat)](https://github.com/0x19/disposable)
[![Go 1.6 Ready](https://img.shields.io/badge/Go%201.6-Ready-green.svg?style=flat)](https://github.com/0x19/disposable)
[![Go 1.7 Ready](https://img.shields.io/badge/Go%201.7-Ready-green.svg?style=flat)](https://github.com/0x19/disposable)

<p align="center">
  <img src ="https://github.com/0x19/disposable/raw/master/assets/disposable.jpg" width="300px" />
</div>

Disposable
===
[Disposable] in short is a robust disposable email (burner emails) API designed to help you verify
whenever email address is coming from disposable service.

[Disposable] utilizes [Burner Email Providers] list and provides GRPC and REST API layer on top of it.

[Disposable] is written in [Go]. It's highly concurrent and very reliable.

### Installation

#### Docker Hub

```shell
docker pull 0x19/disposable
```

#### Manual

```shell
export GRPC_ADDR=":5911"
export HTTP_ADDR=":8015"
# You can use certificates located under /travis/certs if you want to get started fast
export GRPC_CA="...generated CA file..."
export GRPC_KEY="...generated KEY file..."
make install

# You can always do a go run or just use disposable however, if you want to fetch
# latest list of burned email domains you have to update submodules. `make run` is here
# to help you do all of it in one-liner. Use `make run` for development 'make start' for
# production.
make run
```


[Burner Email Providers]: <https://github.com/wesbos/burner-email-providers>
[Go]: <http://golang.org>
[Disposable]: <https://github.com/0x19/disposable>
