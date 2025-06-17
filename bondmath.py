#!/usr/bin/env python3
"""
TI-84 Style Bond Pricing Calculator
Implements all bond pricing formulas with calculator-style menu interface
"""

import math

def clear_screen():
    """Clear screen for clean display"""
    print("\n" * 50)

def pause():
    """Pause for user to read results"""
    input("\nPress ENTER to continue...")

def get_float_input(prompt, min_val=None, max_val=None):
    """Get validated float input"""
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be >= {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be <= {max_val}")
                continue
            return value
        except ValueError:
            print("Invalid input. Enter a number.")

def get_int_input(prompt, min_val=None, max_val=None):
    """Get validated integer input"""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be >= {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be <= {max_val}")
                continue
            return value
        except ValueError:
            print("Invalid input. Enter an integer.")

def bond_price_annual():
    """Calculate bond price with annual coupon payments"""
    clear_screen()
    print("BOND PRICE - ANNUAL")
    print("=" * 20)
    
    C = get_float_input("Annual Coupon ($): ")
    F = get_float_input("Face Value ($): ")
    y = get_float_input("Yield to Maturity (%): ") / 100
    N = get_int_input("Years to Maturity: ", min_val=1)
    
    # Calculate present value
    pv_coupons = sum(C / (1 + y)**t for t in range(1, N + 1))
    pv_principal = F / (1 + y)**N
    bond_price = pv_coupons + pv_principal
    
    print(f"\nRESULTS:")
    print(f"PV of Coupons: ${pv_coupons:.2f}")
    print(f"PV of Principal: ${pv_principal:.2f}")
    print(f"Bond Price: ${bond_price:.2f}")
    print(f"Current Yield: {(C/bond_price)*100:.2f}%")
    
    pause()
    return bond_price

def bond_price_semi_annual():
    """Calculate bond price with semi-annual coupon payments"""
    clear_screen()
    print("BOND PRICE - SEMI-ANNUAL")
    print("=" * 25)
    
    C = get_float_input("Annual Coupon ($): ")
    F = get_float_input("Face Value ($): ")
    y = get_float_input("Annual Yield to Maturity (%): ") / 100
    N = get_float_input("Years to Maturity: ", min_val=0)
    
    m = 2  # Semi-annual payments
    total_periods = int(N * m)
    coupon_per_period = C / m
    yield_per_period = y / m
    
    # Calculate present value
    pv_coupons = sum(coupon_per_period / (1 + yield_per_period)**t 
                    for t in range(1, total_periods + 1))
    pv_principal = F / (1 + yield_per_period)**total_periods
    bond_price = pv_coupons + pv_principal
    
    print(f"\nRESULTS:")
    print(f"Periods: {total_periods}")
    print(f"Coupon/Period: ${coupon_per_period:.2f}")
    print(f"Yield/Period: {yield_per_period*100:.4f}%")
    print(f"PV of Coupons: ${pv_coupons:.2f}")
    print(f"PV of Principal: ${pv_principal:.2f}")
    print(f"Bond Price: ${bond_price:.2f}")
    
    pause()
    return bond_price

def macaulay_duration():
    """Calculate Macaulay Duration"""
    clear_screen()
    print("MACAULAY DURATION")
    print("=" * 17)
    
    C = get_float_input("Annual Coupon ($): ")
    F = get_float_input("Face Value ($): ")
    y = get_float_input("Annual Yield to Maturity (%): ") / 100
    N = get_float_input("Years to Maturity: ", min_val=0)
    payment_freq = get_int_input("Payments per year (1=annual, 2=semi): ", min_val=1, max_val=12)
    
    m = payment_freq
    total_periods = int(N * m)
    coupon_per_period = C / m
    yield_per_period = y / m
    
    # Calculate bond price first
    bond_price = sum(coupon_per_period / (1 + yield_per_period)**t 
                    for t in range(1, total_periods + 1))
    bond_price += F / (1 + yield_per_period)**total_periods
    
    # Calculate weighted cash flows
    weighted_cf = 0
    for t in range(1, total_periods + 1):
        if t == total_periods:
            cash_flow = coupon_per_period + F  # Final payment includes principal
        else:
            cash_flow = coupon_per_period
        
        pv_cf = cash_flow / (1 + yield_per_period)**t
        weighted_cf += (t / m) * pv_cf  # Convert period to years
    
    mac_duration = weighted_cf / bond_price
    
    print(f"\nRESULTS:")
    print(f"Bond Price: ${bond_price:.2f}")
    print(f"Macaulay Duration: {mac_duration:.4f} years")
    
    pause()
    return mac_duration

def modified_duration():
    """Calculate Modified Duration"""
    clear_screen()
    print("MODIFIED DURATION")
    print("=" * 17)
    
    print("1. Calculate from bond parameters")
    print("2. Calculate from Macaulay Duration")
    choice = get_int_input("Choice (1-2): ", min_val=1, max_val=2)
    
    if choice == 1:
        # Calculate Macaulay Duration first, then Modified
        C = get_float_input("Annual Coupon ($): ")
        F = get_float_input("Face Value ($): ")
        y = get_float_input("Annual Yield to Maturity (%): ") / 100
        N = get_float_input("Years to Maturity: ", min_val=0)
        payment_freq = get_int_input("Payments per year (1=annual, 2=semi): ", min_val=1, max_val=12)
        
        m = payment_freq
        total_periods = int(N * m)
        coupon_per_period = C / m
        yield_per_period = y / m
        
        # Calculate bond price
        bond_price = sum(coupon_per_period / (1 + yield_per_period)**t 
                        for t in range(1, total_periods + 1))
        bond_price += F / (1 + yield_per_period)**total_periods
        
        # Calculate Macaulay Duration
        weighted_cf = 0
        for t in range(1, total_periods + 1):
            if t == total_periods:
                cash_flow = coupon_per_period + F
            else:
                cash_flow = coupon_per_period
            
            pv_cf = cash_flow / (1 + yield_per_period)**t
            weighted_cf += (t / m) * pv_cf
        
        mac_duration = weighted_cf / bond_price
        
    else:
        mac_duration = get_float_input("Macaulay Duration: ", min_val=0)
        y = get_float_input("Annual Yield to Maturity (%): ") / 100
        m = get_int_input("Payments per year: ", min_val=1, max_val=12)
    
    mod_duration = mac_duration / (1 + y/m)
    
    print(f"\nRESULTS:")
    if choice == 1:
        print(f"Bond Price: ${bond_price:.2f}")
        print(f"Macaulay Duration: {mac_duration:.4f} years")
    print(f"Modified Duration: {mod_duration:.4f}")
    
    pause()
    return mod_duration

def price_change_duration():
    """Calculate approximate price change using duration"""
    clear_screen()
    print("PRICE CHANGE - DURATION")
    print("=" * 23)
    
    mod_duration = get_float_input("Modified Duration: ", min_val=0)
    yield_change = get_float_input("Yield Change (%): ") / 100
    current_price = get_float_input("Current Bond Price ($): ", min_val=0)
    
    percent_change = -mod_duration * yield_change
    dollar_change = current_price * percent_change
    new_price = current_price + dollar_change
    
    print(f"\nRESULTS:")
    print(f"Percentage Change: {percent_change*100:.2f}%")
    print(f"Dollar Change: ${dollar_change:.2f}")
    print(f"New Price: ${new_price:.2f}")
    
    pause()

def analytical_convexity():
    """Calculate analytical convexity"""
    clear_screen()
    print("ANALYTICAL CONVEXITY")
    print("=" * 20)
    
    C = get_float_input("Annual Coupon ($): ")
    F = get_float_input("Face Value ($): ")
    y = get_float_input("Annual Yield to Maturity (%): ") / 100
    N = get_float_input("Years to Maturity: ", min_val=0)
    payment_freq = get_int_input("Payments per year (1=annual, 2=semi): ", min_val=1, max_val=12)
    
    m = payment_freq
    total_periods = int(N * m)
    coupon_per_period = C / m
    yield_per_period = y / m
    
    # Calculate bond price
    bond_price = sum(coupon_per_period / (1 + yield_per_period)**t 
                    for t in range(1, total_periods + 1))
    bond_price += F / (1 + yield_per_period)**total_periods
    
    # Calculate convexity
    convexity_sum = 0
    for t in range(1, total_periods + 1):
        if t == total_periods:
            cash_flow = coupon_per_period + F
        else:
            cash_flow = coupon_per_period
        
        convexity_sum += cash_flow * t * (t + 1) / (1 + yield_per_period)**t
    
    convexity = convexity_sum / (bond_price * (1 + yield_per_period)**2)
    
    print(f"\nRESULTS:")
    print(f"Bond Price: ${bond_price:.2f}")
    print(f"Convexity: {convexity:.4f}")
    
    pause()
    return convexity

def approximate_convexity():
    """Calculate approximate convexity using price differences"""
    clear_screen()
    print("APPROXIMATE CONVEXITY")
    print("=" * 21)
    
    print("Enter bond parameters:")
    C = get_float_input("Annual Coupon ($): ")
    F = get_float_input("Face Value ($): ")
    y0 = get_float_input("Current Yield to Maturity (%): ") / 100
    N = get_float_input("Years to Maturity: ", min_val=0)
    payment_freq = get_int_input("Payments per year (1=annual, 2=semi): ", min_val=1, max_val=12)
    delta_y = get_float_input("Yield change for calculation (basis points): ") / 10000
    
    m = payment_freq
    total_periods = int(N * m)
    coupon_per_period = C / m
    
    def calc_bond_price(y):
        yield_per_period = y / m
        price = sum(coupon_per_period / (1 + yield_per_period)**t 
                   for t in range(1, total_periods + 1))
        price += F / (1 + yield_per_period)**total_periods
        return price
    
    # Calculate prices at different yields
    P0 = calc_bond_price(y0)          # Current price
    P_minus = calc_bond_price(y0 - delta_y)  # Price when yield decreases
    P_plus = calc_bond_price(y0 + delta_y)   # Price when yield increases
    
    approx_convexity = (P_minus + P_plus - 2 * P0) / (P0 * delta_y**2)
    
    print(f"\nRESULTS:")
    print(f"P0 (current): ${P0:.4f}")
    print(f"P- (yield down): ${P_minus:.4f}")
    print(f"P+ (yield up): ${P_plus:.4f}")
    print(f"Approximate Convexity: {approx_convexity:.4f}")
    
    pause()
    return approx_convexity

def duration_convexity_adjustment():
    """Calculate price change with duration and convexity adjustment"""
    clear_screen()
    print("DURATION + CONVEXITY")
    print("=" * 20)
    
    current_price = get_float_input("Current Bond Price ($): ", min_val=0)
    mod_duration = get_float_input("Modified Duration: ", min_val=0)
    convexity = get_float_input("Convexity: ")
    yield_change = get_float_input("Yield Change (%): ") / 100
    
    # Duration effect
    duration_effect = -mod_duration * yield_change
    
    # Convexity effect
    convexity_effect = 0.5 * convexity * yield_change**2
    
    # Total percentage change
    total_percent_change = duration_effect + convexity_effect
    
    # Dollar amounts
    duration_dollar = current_price * duration_effect
    convexity_dollar = current_price * convexity_effect
    total_dollar_change = current_price * total_percent_change
    new_price = current_price + total_dollar_change
    
    print(f"\nRESULTS:")
    print(f"Duration Effect: {duration_effect*100:.2f}% (${duration_dollar:.2f})")
    print(f"Convexity Effect: {convexity_effect*100:.2f}% (${convexity_dollar:.2f})")
    print(f"Total Change: {total_percent_change*100:.2f}% (${total_dollar_change:.2f})")
    print(f"New Price: ${new_price:.2f}")
    
    pause()

def main_menu():
    """Main calculator menu"""
    while True:
        clear_screen()
        print("TI-84 BOND CALCULATOR")
        print("=" * 21)
        print("1. Bond Price (Annual)")
        print("2. Bond Price (Semi-Annual)")
        print("3. Macaulay Duration")
        print("4. Modified Duration")
        print("5. Price Change (Duration)")
        print("6. Analytical Convexity")
        print("7. Approximate Convexity")
        print("8. Duration + Convexity")
        print("9. Exit")
        print("=" * 21)
        
        choice = get_int_input("Select option (1-9): ", min_val=1, max_val=9)
        
        if choice == 1:
            bond_price_annual()
        elif choice == 2:
            bond_price_semi_annual()
        elif choice == 3:
            macaulay_duration()
        elif choice == 4:
            modified_duration()
        elif choice == 5:
            price_change_duration()
        elif choice == 6:
            analytical_convexity()
        elif choice == 7:
            approximate_convexity()
        elif choice == 8:
            duration_convexity_adjustment()
        elif choice == 9:
            clear_screen()
            print("Thank you for using TI-84 Bond Calculator!")
            break

if __name__ == "__main__":
    main_menu()
