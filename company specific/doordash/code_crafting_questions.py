"""
Delivery API
The input is dasherId, and the output is reward. There will be a sample dataset, which is a list where each item is roughly in the format of {dasherId: 1, deliveryId: 1, timestamp: "2024-01-01 00:00:00", status: "ACCEPTED"}. Each delivery will have two records: one for ACCEPTED and another for either CANCELLED or DELIVERED. The reward is calculated based on some predefined formula.

You will need to implement a function that mimics an API endpoint that calls a downstream service which essentially retrieves this JSON.

A follow-up question introduces a rush hour window during which the reward is doubled. The overall logic is simple, but handling timestamps is quite tricky, so it’s best to familiarize yourself with that in advance.

Gift Card API
I was given a set of "APIs" I needed to call to create my own API that would return a specific response body. These were a ConsumerService, a PaymentService and an AddressService. I needed to implement a BootstrapService that would "call" these APIs (in the given exercise just method calls, not actual REST API calls) and return a body containing a consumer ID, the default payment service, gift card credits remaining, and the user's name and address. This body was put together using pieces of responses from the given APIs. The input was a String userId. I needed to also ensure proper error handling - if the userId was invalid, unavailable, return an error, but if the other APIs returned an error the relevant fields should be blank. The code should run and show the correct response (or, ideally, the response should be tested with asserions.)
"""