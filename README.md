# Django Backend

This is my first project learning how to build a backend in Python with Django. I had worked on a couple miscellaneous scripts in Python and was curious to see what a backend could look like.

This was originally built to work with a Next.js frontend to process csv's into reports, but I ended up taking a different approach and scrapping the Django backend. However, it was still a great learning experience!

## Usage

To get started developing:

```bash
# starts the live server
python manage.py runserver
```

Below is some sample code for how to make API calls.

### Backend

This is the setup for how the backend receives requests from the frontend.

```python
### settings.py
# install corsheaders via pip to allow API calls
INSTALLED_APPS = [
    'corsheaders' # and other apps
]

# define middleware for cors
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # DEFAULT (all other middleware)
]

# define allowed origins
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000'
]

# define allowed methods and headers
CORS_ALLOW_METHODS = [
    'POST' # and other methods
]

CORS_ALLOW_HEADERS = [
    'x-csrftoken' # and other headers
]

# add trusted origins and allow credentials
CSRF_TRUSTED_ORIGINS = ['http://localhost:3000']

CORS_ALLOW_CREDENTIALS = True
```

```python
### urls.py
# map urls to views, always end urls (routes) with '/'
urlpatterns = [
    path('testpost/', views.test_post),
    path('testget/', views.test_get),
    path('csrf/', views.csrf),
    path('init/', views.init_upload)
]

### views.py
# define views, map to templates as necessary
def csrf(request):
    return render(request, 'csrf_token_page.html')

def test_get(request):
    return JsonResponse({'success': 'get route works'})

### templates/csrf_token_page.html
<form method="post">
  {% csrf_token %}
  <!-- Other form fields (if applicable) -->
</form>
```

### Frontend

This is an example implementation of a frontend that accesses these routes using axios. In my project I used a custom apiCall function to abstract token retrieval away from the front-facing components.

```javascript
// api.js
// function to simplify API calls, getting a token if it's a POST route
export function apiCall(method, path, data) {
  return new Promise(async (resolve, reject) => {
    const fullPath = "http://localhost:8000/" + path;
    const headers = {};

    if (method.toLowerCase() === "post") {
      const csrf = await getCSRFToken();
      headers["X-CSRFToken"] = csrf;
    }

    return axios[method.toLowerCase()](fullPath, data, {
      headers,
      withCredentials: true,
    })
      .then((res) => {
        return resolve(res.data);
      })
      .catch((err) => {
        if (err && err.response && err.response.data._unauthorized) {
          window.location.reload(false);
        } else if (err.response) {
          return reject(err.response.data.error);
        } else {
          return reject(
            "Error retrieving data from the server. Please try again in a moment."
          );
        }
      });
  });
}

// getCSRFToken()
export function getCSRFToken() {
  return new Promise(async (resolve, reject) => {
    try {
      const response = await axios.get("http://localhost:8000/api/csrf");

      const htmlContent = response.data;
      const match = htmlContent.match(
        /name="csrfmiddlewaretoken" value="(.+?)"/
      );
      const csrfToken = match ? match[1] : null;

      console.log("CRSF TOKEN:", csrfToken);

      // write it to the cookies
      document.cookie = `csrftoken=${csrfToken}; path=/; SameSite=Lax; Secure`;

      resolve(csrfToken);
    } catch (error) {
      reject("Failed to obtain CSRF token");
    }
  });
}

// in one of the front-facing components:
const [num, setNum] = useState(0);

const handlePost = async () => {
  try {
    const response = await apiCall("post", "api/testpost/", {
      data: 2,
      otherData: "test",
    });

    console.log("Post request successful:", response);
    setNum(response.data);
  } catch (error) {
    console.error("Post request failed:", error);
  }
};
```

## Key Learning Points

- I found that building this application was pretty similar to a Node.js backend in JavaScript. The general concepts--routes, views, endpoints, etc. were shared among both implementations.
- Learning how to work with CORS when making API calls proved to be rather difficult, as I had to figure out how to send over a CSRF token to the frontend to validate POST requests. This was accomplished by attaching a template to a 'csrf' request, in which the template contained a token that could be used by the frontend to make a subsequent POST request.

## Authors

[John Gaynor](https://johngaynor.dev) (last updated 10/14/2023)
