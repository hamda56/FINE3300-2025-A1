# FINE 3300 - Assignment 1
# Part 1: MortgagePayment class
# Student : Hamda Yusuf
print("testing")

class MortgagePayment:
    def __init__(self, quoted_rate, amort_years):
        # Convert the annual rate to decimal
        self.quoted_rate = quoted_rate 
        self.amort_years = amort_years

    def pva(self, r, n):
        """The PVA formula"""
        return (1 - (1 + r) ** (-n)) / r

    def payments(self, principal):
        # Convert semiannual rate to an effective monthly rate
        semi_rate = self.quoted_rate / 2
        eff_monthly = (1 + semi_rate) ** (1/6) - 1

        # Identifying the number of payments (n) for each period (excluding accelerated payments)
        n_monthly = self.amort_years * 12
        n_semi_monthly = self.amort_years * 24
        n_biweekly = self.amort_years * 26
        n_weekly = self.amort_years * 52

        # Calculate the rates (r) for the different periods using the effective monthly and semi annual rates
        r_monthly = eff_monthly
        r_semi_monthly = (1 + r_monthly) ** (1/2) - 1
        r_biweekly = (1 + semi_rate) ** (1/13) - 1
        r_weekly = (1 + semi_rate) ** (1/52) - 1

        # Calculate the payments for different periods
        monthly = principal / self.pva(r_monthly, n_monthly)
        semi_monthly = principal / self.pva(r_semi_monthly, n_semi_monthly)
        biweekly = principal / self.pva(r_biweekly, n_biweekly)

        # Weekly = Half of biweekly
        weekly = biweekly / 2

        # Calculate the accelerated payments separately because it's equal to half and one quarter of the monthly payment
        rapid_biweekly = monthly / 2
        rapid_weekly = monthly / 4
        
        return (round(monthly, 2), round(semi_monthly, 2), round(biweekly, 2), round(weekly, 2), round(rapid_biweekly, 2), round(rapid_weekly, 2))
   
if __name__ == "__main__":
    mortgage = MortgagePayment(0.055, 25)
    payments = mortgage.payments(500000)
    print(payments)
