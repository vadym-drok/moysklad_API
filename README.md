Simple API for synchronithation the service https://www.moysklad.ru/ and your MS SQL DB. 

When sending a POST request to .../orders with JSON like:

{
"id": "0ca5t869-e2fe-11eb-0a80-0db456481180",
"sum": 10.0
}

The app connects with MS SQL DB and adds or update data.

When sending a GET request to .../orders, the app connects to "moysklad.ru" and take “Заказы покупателей” for the last week. Verifies with data in the MS SQL and writes / updates them.
