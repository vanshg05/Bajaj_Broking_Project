# Bajaj Broking Trading API – Campus Hiring Assignment

## Overview
This project implements a simplified trading backend using RESTful APIs.
It simulates core trading workflows including instruments, order placement,
trade execution, and portfolio tracking using in-memory storage.

## Technology Stack
- Python
- FastAPI
- In-memory data structures

## Setup Instructions

1. Install dependencies:
   pip install -r requirements.txt

2. Start the server:
   uvicorn main:app --reload

3. Open API documentation:
   http://127.0.0.1:8000/docs

## Supported APIs

GET /api/v1/instruments  
POST /api/v1/orders  
GET /api/v1/orders/{orderId}  
GET /api/v1/trades  
GET /api/v1/portfolio  

## Assumptions
- Single hardcoded user
- Immediate execution of market orders
- No external market integration
- In-memory storage only

## Sample Order Request

{
  "symbol": "TCS",
  "quantity": 10,
  "orderType": "BUY",
  "orderStyle": "MARKET"
}
