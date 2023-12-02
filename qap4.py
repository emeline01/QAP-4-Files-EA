# QAP 4 
# Written by: Emeline Arklie
# November 29, 2023
# Program for entering & calculating new insurance policy information for customers

from datetime import datetime, timedelta

# User inputs
while True:
    
    def get_customer_info():
        FirstName = input("Enter first name: ").title()
        LastName = input("Enter last name: ").title()
        Address = input("Enter address: ")
        City = input("Enter city: ").title()

        Provinces = ['ON', 'QC', 'BC', 'AB', 'MB', 'SK', 'NS', 'NB', 'NL', 'PE', 'NT', 'NU', 'YT']
        Province = input("Enter province: ").upper()
        while Province not in Provinces:
            Province = input("Invalid province. Please re-enter. ").upper()

        PostCode = input("Enter postal code: ")
        PhoneNum = input("Enter postal code: ")
        NumCars = int(input("Enter number of cars being insured: "))
        ExtraLiability = input("Extra liability coverage? (Y/N): ").upper()
        GlassCov = input("Glass coverage? (Y/N): ").upper()
        LoanerCar = input("Loaner car coverage? (Y/N): ").upper()
        PayMethod = input("Payment method (Full/Monthly/Down Pay): ").capitalize()

    # Downpayment option 

        if PayMethod == "Down Pay":
            DownPayment = float(input("Enter amount of down payment: "))
        else: 
            DownPayment = 0.0
        
        Claims = []
        while True:
            Date = input("Enter date of claim (press Enter to finish): ")
            if not Date:
                break
            Cost = float(input("Enter the cost of claim: "))
            Claims.append((Date, Cost))

        return (FirstName, LastName, Address, City, Province, PostCode, PhoneNum, NumCars, ExtraLiability, GlassCov, LoanerCar, PayMethod, DownPayment, Claims)


    def calculate_premium(NumCars, downpayment, claims):
        # Program constants
        NEXT_POLICY_NUM = 1944
        BASIC_PREMIUM = 869.00
        DISC_RATE = 0.25
        EXTRA_LIABILITY = 130.00
        GLASS_COV = 86.00
        LOANER_CAR_COST = 58.00
        HST = 0.15
        PROCESS_FEE = 39.99
        
        # Calculations

        TotalExtracosts = NumCars * (EXTRA_LIABILITY + GLASS_COV + LOANER_CAR_COST)
        TotalPremium = BASIC_PREMIUM + (NumCars - 1) * BASIC_PREMIUM * DISC_RATE + TotalExtracosts
        Tax = TotalPremium * HST
        TotalCost = TotalPremium + HST

        if downpayment > 0:
            TotalCost -= downpayment

        monthly_payment = (TotalCost + PROCESS_FEE) / 8

        return (NEXT_POLICY_NUM, TotalPremium, TotalExtracosts, Tax, TotalCost, monthly_payment)
    
    # Outputs & program receipt

    def generate_receipt(customer_info, premium_info):
        print("\n---- Insurance Receipt ----")
        print(f"Policy Holder: {customer_info[0]} {customer_info[1]}")
        print(f"Address: {customer_info[2]}, {customer_info[3]}, {customer_info[4]} {customer_info[5]}")
        print(f"Phone Number: {customer_info[6]}")
        print(f"Number of Cars: {customer_info[7]}")
        print(f"Extra Liability: {customer_info[8]}")
        print(f"Glass Coverage: {customer_info[9]}")
        print(f"Loaner Car Coverage: {customer_info[10]}")
        print(f"Payment Method: {customer_info[11]}")
        if customer_info[11] == 'Down Pay':
            print(f"Down Payment: ${customer_info[12]:,.2f}")

        print("\n---- Premium Information ----")
        print(f"Policy Number: {premium_info[0]}")
        print(f"Basic Premium: ${premium_info[1]:,.2f}")
        print(f"Total Extra Costs: ${premium_info[2]:,.2f}")
        print(f"HST (15%): ${premium_info[3]:,.2f}")
        print(f"Total Cost: ${premium_info[4]:,.2f}")

        if customer_info[11] == 'Monthly' or customer_info[11] == 'Down Pay':
            print(f"Monthly Payment: ${premium_info[5]:,.2f}")

    def main():
        customer_info = get_customer_info()
        premium_info = calculate_premium(customer_info[7], customer_info[12], customer_info[13])
        generate_receipt(customer_info, premium_info)

    if __name__ == "__main__":
        main()


    
        



        