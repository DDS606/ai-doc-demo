# Payment Service

## Purpose
Payment Service handles payment processing in the system.

## Responsibilities
- process transactions
- validate payment amounts
- return transaction result

## How it works
The service receives payment information and checks whether the transaction is valid.

## Example flow
1. User sends payment request
2. Payment Service validates amount
3. If valid → payment processed
4. If invalid → transaction rejected

## Code Location
src/payment.py