import http.client
import json 
import urllib.parse

# process_order script
conn = http.client.HTTPSConnection("checkout.api.dev.besimplified.net")
payload = ''
# bearer_token = str(input("Enter the bearer token: "))
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mbyI6eyJpZCI6Ik5qWTJNbUk1TURWaE9UZzVZMkpqTm1Jek5EZzVOR0l6IiwiZmlyc3RfbmFtZSI6IlN5c3RlbSIsIm1pZGRsZV9uYW1lIjoiIiwibGFzdF9uYW1lIjoiVXNlciIsInBlcm1pc3Npb25LZXkiOiJwZXJtaXRfTmpZMk1tSTVNRFZoT1RnNVkySmpObUl6TkRnNU5HSXoifSwib3JnSW5mbyI6eyJvcmdzIjpbIk5qWTJNbUUwWkRrek1UazROREU1T0RZMFptWm1OR0l4Il0sImlkIjoiTmpZMk1tRTBaRGt6TVRrNE5ERTVPRFkwWm1abU5HSXgifSwicmVzZWxsZXJJbmZvIjp7ImlkIjoiTmpZMk1tRTBaRGt6TVRrNE5ERTVPRFkwWm1abU5HSXkifSwiZW1haWwiOiJzeXN0ZW1AYmVzaW1wbGlmaWVkLm5ldCIsImV4cCI6MTc0ODU4ODk0OS43MDE5NzMsImlzcyI6IlNpbXBsaWZpZWQgQWNjb3VudHMiLCJpYXQiOjE3NDczNzkzNDkuNzAxOTc1LCJhZ2VudCI6IndlYiJ9.eEuelP6GL3B3uvBrfxbLHI3k5QwFVptX7fY-n9AelzQ'
}
instance_id = str(input("Enter the instance id: "))
dl_id = str(input("Enter the DL id: "))
where_clause = {
    "where_fields": ["instance_id", "offer_id", "status"],
    "where_values": [
        {"$oid": instance_id},
        dl_id,
        1
    ]
}
where_clause_str = json.dumps(where_clause)
encoded_clause = urllib.parse.quote(where_clause_str)
path = f"/v1/extensions/direct-links/list?debug=yes&where_clause={encoded_clause}"

conn.request("GET", path, payload, headers)
res = conn.getresponse()
data = res.read()
dl_cart_response = data.decode("utf-8")
dl_cart_response = json.loads(dl_cart_response)



conn = http.client.HTTPConnection("localhost", 3002)
initiate_checkout_cart = dl_cart_response["data"]["results"]["results"]["data"][0]["cart"]
payload = json.dumps(initiate_checkout_cart)
headers = {
  'X-identifier': initiate_checkout_cart["instance_identifier"],
  'Content-Type': 'application/json'
}
conn.request("POST", "/v1/checkouts/checkouts/initiateCheckout?debug=yes", payload, headers)
res = conn.getresponse()
data = res.read()
initiate_checkout_response=json.loads(data)


conn = http.client.HTTPConnection("localhost", 3002)
payload = json.dumps({
    "first_name": "abc",
    "last_name": "abc",
    "currency": "USD",
    "phone": "+1 9716578913",
    "email": "abcxy@codeclouds.com",
    "card_name": "abc",
    "credit_card_number": "4111111111111111",
    "expiration_date": "1236",
    "cvv": "111",
    "shipping_id": "68aea6b1fa624f1eac7494c4",
    "ip_address": "122.185.160.34",
    "billing_same_as_shipping": "YES",
    "shipping_address1": "abc",
    "shipping_address2": "abc",
    "shipping_city": "abc",
    "shipping_state": "AL",
    "shipping_zip": "45678",
    "shipping_country": "US",
    "terms_agree": "on",
    "cc_type": "",
    "custom_fields": {}
})
headers = {
  'X-session-uuid': initiate_checkout_response["session_id"],
  'Content-Type': 'application/json',
  'X-Order-Type': 'primitive',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mbyI6eyJpZCI6Ik5qUXlZVGszWW1RNE16a3lOR0kyWXpJM1lUVTBaRGM0IiwiZmlyc3RfbmFtZSI6IktyaXNobmVuZHUiLCJtaWRkbGVfbmFtZSI6IiIsImxhc3RfbmFtZSI6IkJpc3dhcyIsInBlcm1pc3Npb25LZXkiOiJwZXJtaXRfTmpReVlUazNZbVE0TXpreU5HSTJZekkzWVRVMFpEYzQifSwib3JnSW5mbyI6eyJvcmdzIjpbIk5qWTFPRFkyWm1VM09XUTVPRGhqTXpGa1pUbGxOamN3Il0sImlkIjoiTmpZMU9EWTJabVUzT1dRNU9EaGpNekZrWlRsbE5qY3cifSwicmVzZWxsZXJJbmZvIjp7ImlkIjoiTmpZMU9EWTJabVUzT1dRNU9EaGpNekZrWlRsbE5qY3gifSwiZW1haWwiOiJrcmlzaG5lbmR1LmJpc3dhc0Bjb2RlY2xvdWRzLmluIiwiZXhwIjoxNzU0NjM0MTU4LjA5NTExLCJpc3MiOiJTaW1wbGlmaWVkIEFjY291bnRzIiwiaWF0IjoxNzUzNDI0NTU4LjA5NTExMywiYWdlbnQiOiJ3ZWIifQ.HAUHDskj0H5e0FsDrdOkZRVqx9GoTkUBLunSvEOkH5g'
}
conn.request("POST", "/v1/checkouts/process_orders/create?debug=yes", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
