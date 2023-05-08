# fast-request-logger

This is a simple python app that acts as a sandbox for you to send requests to. 

The following request methods are supported:
- `GET`
- `PUT`
- `POST`
- `DELETE`
- `PATCH`

## Demo

![Kapture 2023-05-09 at 00 21 03](https://user-images.githubusercontent.com/56479869/236950896-3b3060bf-edbb-43b4-8858-7b05c6bc58e0.gif)


## Prerequisites

- [Python](https://www.python.org) - tested on 3.11
- [hatch](https://hatch.pypa.io/latest/) - `pipx install hatch` or `pip install hatch`

## Quick Start

1. Clone the repo

```sh
git clone https://github.com/RatulMaharaj/fast-request-logger.git
cd fast-request-logger
```

2. Start the app using [hatch](https://hatch.pypa.io/latest/)
```sh
hatch run start
```

3. Send a POST or PUT request to the app
```sh
curl -X POST -H "Content-Type: application/json" -d '{"message": "Howdy!"}' http://127.0.0.1:8000
```

## License

`fast-request-logger` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
