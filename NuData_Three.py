# Numerous components on a network, such as DNS servers, switches, load balancers, 
# and others can generate errors anywhere in the life of a given request. 
# The usual technique for dealing with these error responses in a networked environment 
# is to implement retries in the client application. 
# This technique increases the reliability of the application and 
# reduces operational costs for the developer. 
# Write code that implements automatic retry logic and 
# simulates exponential backoff and jitter. 
# For the purposes of this code test, assume that the code you are writing will retry on server or 
# throttling errors but will halt on client errors.