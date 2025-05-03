import math
import argparse


def calculate_fd_maturity(principal, annual_rate, years, compounding_frequency=1):
    """
    Calculates the maturity amount and total interest earned on a fixed deposit.

    Parameters:
        principal (float): The initial amount deposited.
        annual_rate (float): Annual interest rate (in percentage, e.g., 5 for 5%).
        years (float): Time period in years.
        compounding_frequency (int): Number of times interest is compounded per year (default=1).

    Returns:
        tuple: (maturity_amount, total_interest)
    """
    rate_decimal = annual_rate / 100.0
    maturity_amount = principal * math.pow((1 + rate_decimal / compounding_frequency), compounding_frequency * years)
    total_interest = maturity_amount - principal
    return maturity_amount, total_interest


def run_tests():
    """Basic test cases for calculate_fd_maturity"""
    tests = [
        # (principal, rate, years, freq, expected_amount)
        (1000, 5, 1, 1, 1050.0),            # simple annual
        (1000, 5, 2, 2, 1102.50),           # semi-annual
        (2000, 3, 3, 4, 2185.467),          # quarterly
        (1500, 4, 0.5, 12, 1515.045),       # monthly
    ]
    for P, R, T, n, exp in tests:
        amt, _ = calculate_fd_maturity(P, R, T, n)
        # allow small rounding differences
        assert abs(amt - exp) < 0.01, f"Test failed for {P, R, T, n}: got {amt}, expected {exp}"
    print("All tests passed.")


def main():
    parser = argparse.ArgumentParser(description="Fixed Deposit Maturity Calculator")
    parser.add_argument("-P", "--principal", type=float, required=True,
                        help="Principal amount deposited")
    parser.add_argument("-R", "--rate", type=float, required=True,
                        help="Annual interest rate (in %)")
    parser.add_argument("-T", "--years", type=float, required=True,
                        help="Time period in years")
    parser.add_argument("-n", "--frequency", type=int, default=1,
                        help="Compounding frequency per year (default=1)")
    parser.add_argument("--run-tests", action="store_true",
                        help="Run built-in test suite and exit")
    args = parser.parse_args()

    if args.run_tests:
        run_tests()
        return

    amount, interest = calculate_fd_maturity(
        args.principal, args.rate, args.years, args.frequency
    )

    print("=== Fixed Deposit Maturity Calculator ===")
    print(f"Principal: {args.principal:,.2f}")
    print(f"Annual Rate: {args.rate:.2f}%")
    print(f"Time (years): {args.years}")
    print(f"Compounding Frequency: {args.frequency} per year\n")
    print(f"Maturity Amount: {amount:,.2f}")
    print(f"Total Interest Earned: {interest:,.2f}")

if __name__ == "__main__":
    main()
