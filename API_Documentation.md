
##  Login API

- ## Endpoint  : POST/api/login


  ## Request Body :

    {
        "username": "megha",
        "password": "123456"
    }

    curl -X POST http://127.0.0.1:8000/api/login/ \
     -H "Content-Type: application/json" \
     -d '{"username": "megha", "password": "123456"}'

 ## Response

    {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOi...",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    }

 ## Refresh Token API

   ## POST /api/token/refresh/

    { 
        "refresh": "<refresh_token>"
    }

    curl -X POST http://127.0.0.1:8000/api/token/refresh/ \
     -H "Content-Type: application/json" \
     -d '{"refresh": "<refresh_token>"}'

  ## Response 
        {
            "access": "<new_access_token>"
        }

 ## Overview API

   ##  GET /api/snippets/overview/

    curl -X GET http://127.0.0.1:8000/api/snippets/overview/ \
     -H "Authorization: Bearer <access_token>"

  ## Response

   "data": {
        "total_snippets": 1,
        "snippets": [
            {
                "id": 1,
                "title": "Test snippet",
                "note": "here my first nippet",
                "created_by": "admin",
                "tag_details": [
                    {
                        "id": 1,
                        "title": "test"
                    }
                ],
                "created_at": "2025-10-29T11:08:33.975367Z",
                "updated_at": "2025-10-29T11:08:33.975556Z"
            }
        ]
    }

## Create Snippet API

 - ## POST /api/snippets/

  ## Request

    {
        "title": "New Snippet",
        "note": "This test snippet",
        "tags": ["django", "api"]
    }

    curl -X POST http://127.0.0.1:8000/api/snippets/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <access_token>" \
     -d '{"title": "New Snippet", "note": "This is my second note", "tags": ["django","api"]}'


   
 ## Response
  
   "data": {
        "id": 2,
        "title": "New Snippet",
        "note": "This is my second note",
        "created_by": "admin",
        "tag_details": [
            {
                "id": 3,
                "title": "api"
            },
            {
                "id": 2,
                "title": "django"
            }
        ],
        "created_at": "2025-10-29T12:33:10.508814Z",
        "updated_at": "2025-10-29T12:33:10.508959Z"
    }


## Detail Snippet API

  - ## GET /api/snippets/{id}/

    curl -X GET http://127.0.0.1:8000/api/snippets/2/ \
     -H "Authorization: Bearer <access_token>"

    "data": {
        "id": 1,
        "title": "Test snippet",
        "note": "here my first nippet",
        "created_by": "admin",
        "tag_details": [
            {
                "id": 1,
                "title": "test"
            }
        ],
        "created_at": "2025-10-29T11:08:33.975367Z",
        "updated_at": "2025-10-29T11:08:33.975556Z"
    }

## Update Snippet API
- ## PUT /api/snippets/{id}/

  ## Request
   
   {
    "title": "Updated Snippet",
    "note": "Modified note text",
    "tags": ["python", "backend"]
    }

    curl -X PUT http://127.0.0.1:8000/api/snippets/2/ \
    -H "Authorization: Bearer <access_token>" \
    -H "Content-Type: application/json" \
    -d '{"title": "Updated Snippet", "note": "Modified note text", "tags": ["python", "backend"]}'

## Response

    {
        "id": 2,
        "title": "Updated Snippet",
        "note": "Modified note text",
        "tag_details": [
            {"id": 3, "title": "python"},
            {"id": 4, "title": "backend"}
        ],
        "created_by": "megha",
        "created_at": "2025-10-29T14:20:00Z",
        "updated_at": "2025-10-29T15:00:00Z"
    }

## Delete Snippet API

  ## DELETE /api/snippets/{id}/

    curl -X DELETE http://127.0.0.1:8000/api/snippets/2/ \
     -H "Authorization: Bearer <access_token>"
     
  ## Response
    Showing currently available snippet

    {
        "id": 1,
        "title": "Test snippet",
        "note": "here my first nippet",
        "created_by": "admin",
        "tag_details": [
            {
                "id": 1,
                "title": "test"
            }
        ],
        "created_at": "2025-10-29T11:08:33.975367Z",
        "updated_at": "2025-10-29T11:08:33.975556Z"
    }

## Tag List API
  
  ## GET /api/tags/

    curl -X GET http://127.0.0.1:8000/api/tags/ \
     -H "Authorization: Bearer <access_token>"

  ## Response

    {
            "id": 3,
            "title": "api"
        },
        {
            "id": 2,
            "title": "django"
        },
        {
            "id": 1,
            "title": "test"
    }

## Tag Detail (Snippets by Tag) API
 
 ## GET /api/tags/{id}/snippets/

    curl -X GET http://127.0.0.1:8000/api/tags/1/snippets/ \
     -H "Authorization: Bearer <access_token>"

  ## Response

    {
        "id": 1,
        "title": "Test snippet",
        "note": "here my first nippet",
        "created_by": "admin",
        "tag_details": [
            {
                "id": 1,
                "title": "test"
            }
        ],
        "created_at": "2025-10-29T11:08:33.975367Z",
        "updated_at": "2025-10-29T11:08:33.975556Z"
    }










