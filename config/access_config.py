BASE_URL = "https://pengate-staging.quarksek.com"
BASE_URL.rstrip('/')

# User config
USERS = [
    {
        "id": "tester1",
        "role": "tester",
        "email": "s.testerpengate+1@gmail.com",
        "password": "Testerpengate11@"
    },
    {
        "id": "tester2",
        "role": "tester",
        "email": "s.testerpengate+2@gmail.com",
        "password": "Testerpengate2@"
    },
    {
        "id": "customer1",
        "role": "customer",
        "email": "s.testerpengate+customer1@gmail.com",
        "password": "Customer1@"
    },
    {
        "id": "customer2",
        "role": "customer",
        "email": "s.testerpengate+customer2@gmail.com",
        "password": "Customer2@"
    }
]

# Resource ownership: user owns it and tester assigned to 
# RESOURCES = {
#     "requests": {
#         "08141060-278c-4a64-9909-1b2108442632": {
#             "access": ["customer2", "tester1"]
#         },
#         "1c809bb8-1c93-4e02-b3f0-057d619fa526": {
#             "access": ["tester1"]
#         },
#         "3a65d016-b458-478b-9f7a-157431e67651": {
#             "access": ["customer1", "tester1"]
#         },
#         "5c41fcca-6f0b-4dfe-be1b-05fa30b5fc46": {
#             "access": ["customer1", "tester2"]
#         },
#         "86f829ca-e1da-4d62-b8c7-a1baa81c7589": {
#             "access": ["customer1", "tester1"]
#         },
#         "8a9d35fa-4484-4d74-b97b-8a4695bc2fd5": {
#             "access": ["customer2", "tester2"]
#         },
#         "e2e72329-089f-4615-b3a9-b217898d5bee": {
#             "access": ["customer2", "tester1"]
#         },
#         "public_id": {
#             "access": ["any"]
#         }
#     }
# }

RESOURCES = {
    "requests": {
        # case 1
        "0c192e29-eed2-4191-8a49-6d9f1b8319ef": {
            "access": ["tester1"]
        },
        "1c809bb8-1c93-4e02-b3f0-057d619fa526": {
            "access": ["customer2", "tester2"]
        },
        
        # case 2
        "f8b19752-5177-4315-baf9-fe393f235640": {
            "access": ["customer2"]
        },
        "86f829ca-e1da-4d62-b8c7-a1baa81c7589": {
            "access": ["customer2", "tester1"]
        },
        
        # case 3
        "3a65d016-b458-478b-9f7a-157431e67651": {
            "access": ["customer1", "tester2"]
        },
        "1c809bb8-1c93-4e02-b3f0-057d619fa526": {
            "access": ["customer2", "tester2"]
        },
        
        # others
        "8a9d35fa-4484-4d74-b97b-8a4695bc2fd5": {
            "access": ["customer1"]
        },
        "5361f016-4327-4453-b2fc-e543407c303c": {
            "access": ["customer2"]
        },
        
        "/": {
            "access": ["any"]
        }
    }
}

ENDPOINTS = {
    "get_request": {
        "method": "GET",
        "path": "/api/requests/{id}",
        "resource_type": "requests",
        "requires_id": True
    },
    "delete_request": {
        "method": "DELETE",
        "path": "/api/requests/{id}",
        "resource_type": "requests",
        "requires_id": True
    },
    "post_request": {
        "method": "POST",
        "path": "/api/requests",
        "resource_type": "requests",
        "requires_id": False
    }
}
# admin > tester > customer. greater the index greater the privilege
ROLE_HIERARCHY = ["customer", "tester", "admin"]