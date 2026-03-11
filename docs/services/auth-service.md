# Auth Service

## Purpose
Auth Service is responsible for user authentication in the system.

## Responsibilities
- validate user credentials
- process login requests
- return authentication response

## How it works
The service receives a username and checks whether the user is allowed to access the system.

## Example flow
1. User sends login request
2. Auth Service checks credentials
3. If valid → access granted
4. If invalid → access denied

## Code Location
src/login.py