import analyser.reply_generator as ds

@test
def response_test(test_query):
    ds.get_response(test_query)

response_test("hello")