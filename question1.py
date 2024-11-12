#question1

# 1. Destinations that both airlines fly to.

# 2. Destinations unique to your airline.

# 3. Whether there are any destinations that neither airline shares.



our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
mutual_destinations = our_routes.intersection(competitor_routes)
print(f"Both airlines travel to these destinations: {mutual_destinations}")

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
unique_to_our_carrier = our_routes.difference(competitor_routes)
print(f"Only our airline travels to these destinations: {unique_to_our_carrier}")


our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
exclusive_destinations = our_routes.symmetric_difference(competitor_routes)
print(f"These destinations are not shared by both airlines: {exclusive_destinations}")