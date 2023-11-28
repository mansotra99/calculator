
#Arithmetic Operations API

This repository contains a set of APIs for performing basic arithmetic operations: addition, subtraction, multiplication, and division. Each operation has its separate API endpoint. The APIs are implemented as AWS Lambda functions, and AWS API Gateway is used to create and deploy these APIs.

APIs
The following APIs are available:

Addition API

Endpoint: /add
Method: POST
Input: JSON object with two numbers { "num1": 5, "num2": 3 }
Output: JSON object with the result { "result": 8 }
Subtraction API

Endpoint: /subtract
Method: POST
Input: JSON object with two numbers { "num1": 10, "num2": 4 }
Output: JSON object with the result { "result": 6 }
Multiplication API

Endpoint: /multiply
Method: POST
Input: JSON object with two numbers { "num1": 7, "num2": 2 }
Output: JSON object with the result { "result": 14 }
Division API

Endpoint: /divide
Method: POST
Input: JSON object with two numbers { "num1": 15, "num2": 3 }
Output: JSON object with the result { "result": 5 }
