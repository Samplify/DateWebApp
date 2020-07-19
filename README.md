# Simple web app to return date and time (UTC) as json

## Usage

This is a simple web app that returns the current **UTC date and time** as a json object

### Json response example:

```json
{
  "year": "2020",
  "month": "07",
  "day": "19",
  "hour": "13",
  "minute": "36",
  "second": "05",
  "microsecond": "474651"
}
```

### Quickstart build / run docker image

Clone project and cd to webapp directory

Build image:

```docker build --tag datewebapp .```

Run image:

```docker run --restart=always --name=datewebapp -d -p 5000:5000 datewebapp```

Navigate to http://localhost:5000 or curl http://localhost:5000

Hosted example located here: http://datewebapp.inmy.coffee

## License
[MIT](https://choosealicense.com/licenses/mit/)