# Django Backend

This is my first project learning how to build a backend in Python with Django. I had worked on a couple miscellaneous scripts in Python and was curious to see what a backend could look like.

This was originally built to work with a Next.js frontend to process csv's into reports, but I ended up taking a different approach and scrapping the Django backend. However, it was still a great learning experience!

## Usage

```bash
# starts the live server
python manage.py runserver
```

## Key Learning Points

- I found that building this application was pretty similar to a Node.js backend in JavaScript. The general concepts--routes, views, endpoints, etc. were shared among both implementations.
- Learning how to work with CORS when making API calls proved to be rather difficult, as I had to figure out how to send over a CSRF token to the frontend to validate POST requests.

## Authors

[John Gaynor](https://johngaynor.dev) (last updated 10/14/2023)
