#!/bin/bash
# Send Header
curl -s -L -H"X-HolbertonSchool-User-Id:98" -H "Origin: HolbertonSchool" -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
