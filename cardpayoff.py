
def card_balance(apr, pmt, *balance):
    """function takes multiple balances and loops through entered
    payment and prints balance till 0. if not 0 function adds
    interest as well as months it takes to pay off each balance
    """
    monthly_interest = round((apr/12), 2)
    accrued_interest = []
    month = 0

    for remainder in balance:
        while remainder > 0:
            remainder -= pmt
            month += 1
            print("-" * 35)

            if remainder <= 0:
                print("Month:", month)
                print(" You're all paid up")
            else:
                print("Month:", month)
                added_interest = round((remainder * monthly_interest)/100, 2)
                remainder = round((remainder + added_interest),2)
                print(" Balance Remaining:", remainder)
                print(" Interest Added:", added_interest)
                accrued_interest.append(added_interest)

    print("-" * 35)
    print(f"Payoff will take {month} months")
    print(f"You will pay {round(sum(accrued_interest),2)} in interest")

card_balance()
