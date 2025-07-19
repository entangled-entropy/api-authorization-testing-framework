TEST_CASES = [

    # Test Case 1
    {
        "name": "Customer1 attempts vertical escalation on tester1's resource",
        "endpoint": "get_request",
        "resource_id": "0c192e29-eed2-4191-8a49-6d9f1b8319ef",  # only tester1 got access
        "user": "customer1",
        "expected_status": [403, 401, 404, 429, 409]
    },
    {
        "name": "Customer1 attempts vertical escalation on tester2's resource",
        "endpoint": "get_request",
        "resource_id": "1c809bb8-1c93-4e02-b3f0-057d619fa526",  # customer2 + tester2 got access
        "user": "customer1",
        "expected_status": [403, 401, 404, 429, 409]
    },

    # Test Case 2
    {
        "name": "Customer1 attempts horizontal IDOR on Customer2's request",
        "endpoint": "get_request",
        "resource_id": "f8b19752-5177-4315-baf9-fe393f235640",  # customer2
        "user": "customer1",
        "expected_status": [403, 401, 404, 429, 409]
    },
    {
        "name": "Customer1 attempts horizontal IDOR on Customer2's request",
        "endpoint": "get_request",
        "resource_id": "86f829ca-e1da-4d62-b8c7-a1baa81c7589",  # customer2 + tester1
        "user": "customer1",
        "expected_status": [403, 401, 404, 429, 409]
    },
    

    # Test Case 3
    {
        "name": "Tester1 attempts horizontal IDOR on Tester2's resources (customer1)",
        "endpoint": "get_request",
        "resource_id": "3a65d016-b458-478b-9f7a-157431e67651",  # customer1 + tester2
        "user": "tester1",
        "expected_status": [403, 401, 404, 429, 409]
    },
    {
        "name": "Tester1 attempts horizontal IDOR on Tester2's resources (customer2)",
        "endpoint": "get_request",
        "resource_id": "1c809bb8-1c93-4e02-b3f0-057d619fa526",  # customer2 + tester2
        "user": "tester1",
        "expected_status": [403, 401, 404, 429, 409]
    },
]

