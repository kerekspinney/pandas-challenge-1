"""Returned Goods."""

# Define a new function called process_claims
def process_claims(claims):
    """
    Calculate the total insurance payout based on a list of claims.
    Args:
        claims (list): A list of claim amounts.
    Returns:
        float: The total insurance payout, which is 30% of the sum of all claims.
    """
    # Create a variable called `total_claims`, that is the sum of all claims
    total_claims = sum(claims)
    
    # Calculate a total payout, which is 30% of total_claims:
    total_payout = 0.3 * total_claims
    
    # Return only the total_payout amount
    return total_payout

def print_total(claims):
    total=process_claims(claims)
    print(f"${total: ,.2f}")


if __name__ == "__main__":
    # Add the weekly claims
    weekly_claims = [5000, 1000, 8000, 10000, 3000, 3500]
    some_other_week_claims = [444, 4444, 8222000, 1440000, 322000, 352200]
    some_other_other_week_claims = [33, 33, 8222022200, 144033000, 343, 343]

    # Create a variable that passes the weekly claims to the function.
    month1=process_claims(weekly_claims)
    month2=process_claims(some_other_week_claims)
    month3=process_claims(some_other_other_week_claims)

    print(month1, month2, month3)
    # Print the total insurance payout to 2 decimal places.
    print_total(weekly_claims)
    print(total)
