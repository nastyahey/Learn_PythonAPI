import json

string_as_json_format = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
json_text = json.loads(string_as_json_format)

print(json_text['messages'][1])