# TI-84 Bond Pricing Calculator

A comprehensive Python implementation of bond pricing formulas with a TI-84 calculator-style menu interface. This program provides all essential bond valuation calculations used in finance and investment analysis.

## 🚀 Features

- **Complete Bond Pricing Suite** - All major bond valuation formulas
- **TI-84 Style Interface** - Familiar calculator menu system
- **Input Validation** - Error checking and range validation
- **Detailed Results** - Shows intermediate calculations
- **Multiple Payment Frequencies** - Annual, semi-annual, and custom periods
- **Professional Accuracy** - Precise financial calculations

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies (uses only built-in libraries)

## 🔧 Installation

1. Download the `bond_calculator.py` file
2. Ensure Python 3.6+ is installed on your system
3. Run the program:
   ```bash
   python bond_calculator.py
   ```

## 📖 Usage

Launch the program and navigate using the numbered menu options. The calculator provides a clean, step-by-step interface similar to TI-84 financial calculators.

### Main Menu Options

| Option | Function | Description |
|--------|----------|-------------|
| **1** | Bond Price (Annual) | Calculate present value with annual coupon payments |
| **2** | Bond Price (Semi-Annual) | Calculate present value with semi-annual payments |
| **3** | Macaulay Duration | Weighted average time to receive cash flows |
| **4** | Modified Duration | Interest rate sensitivity measure |
| **5** | Price Change (Duration) | Estimate price change from yield changes |
| **6** | Analytical Convexity | Formula-based convexity calculation |
| **7** | Approximate Convexity | Price difference method convexity |
| **8** | Duration + Convexity | Combined price change estimation |
| **9** | Exit | Close the calculator |

## 💡 Example Usage

### Basic Bond Pricing
```
Select option: 1 (Bond Price - Annual)
Annual Coupon ($): 50
Face Value ($): 1000
Yield to Maturity (%): 5
Years to Maturity: 10

Results:
PV of Coupons: $386.09
PV of Principal: $613.91
Bond Price: $1000.00
Current Yield: 5.00%
```

### Duration Calculation
```
Select option: 3 (Macaulay Duration)
Annual Coupon ($): 60
Face Value ($): 1000
Yield to Maturity (%): 6
Years to Maturity: 5
Payments per year: 2

Results:
Bond Price: $1000.00
Macaulay Duration: 4.4651 years
```

## 📐 Implemented Formulas

### 1. Bond Price (Present Value)
**Annual:** `PV = Σ[C/(1+y)^t] + F/(1+y)^N`

**Semi-Annual:** `PV = Σ[C/m/(1+y/m)^t] + F/(1+y/m)^(N×m)`

### 2. Macaulay Duration
`MacDur = Σ[t × Ct/(1+y/m)^t] / PV`

### 3. Modified Duration
`ModDur = MacDur / (1 + y/m)`

### 4. Price Change (Duration)
`%ΔPV ≈ -ModDur × Δy`

### 5. Analytical Convexity
`Convexity = [1/(PV×(1+y/m)²)] × Σ[Ct×t×(t+1)/(1+y/m)^t]`

### 6. Approximate Convexity
`Convexity = (PV⁻ + PV⁺ - 2×PV₀) / (PV₀ × (Δy)²)`

### 7. Duration + Convexity Adjustment
`%ΔPV ≈ (-ModDur × Δy) + (0.5 × Convexity × (Δy)²)`

## 🎯 Key Variables

| Symbol | Description | Units |
|--------|-------------|-------|
| **PV** | Present Value (Bond Price) | Dollars |
| **C** | Annual coupon payment | Dollars |
| **F** | Face value (par value) | Dollars |
| **y** | Yield to maturity | Decimal (5% = 0.05) |
| **N** | Years to maturity | Years |
| **m** | Coupon payments per year | Integer |
| **t** | Time period | Periods |

## 🔍 Input Guidelines

- **Monetary Values:** Enter in dollars (e.g., 1000 for $1,000)
- **Percentages:** Enter as whole numbers (e.g., 5 for 5%)
- **Years:** Can be decimal (e.g., 2.5 for 2.5 years)
- **Payment Frequency:** 
  - 1 = Annual
  - 2 = Semi-annual
  - 4 = Quarterly
  - 12 = Monthly

## ⚠️ Important Notes

1. **Yield Conventions:** The calculator converts percentage inputs to decimals automatically
2. **Payment Timing:** Assumes payments at period end (standard bond convention)
3. **Precision:** Results display to 2-4 decimal places for practical use
4. **Error Handling:** Invalid inputs prompt for re-entry with guidance

## 🎓 Educational Use

This calculator is ideal for:
- **Finance Students** - Learning bond valuation concepts
- **Investment Professionals** - Quick calculations and verification
- **Academic Research** - Consistent formula implementation
- **CFA/FRM Exam Prep** - Practice with realistic scenarios

## 📊 Advanced Features

### Duration Analysis
- Calculates both Macaulay and Modified duration
- Supports multiple payment frequencies
- Shows step-by-step calculations

### Convexity Analysis
- Both analytical and approximate methods
- Customizable yield shock scenarios
- Detailed intermediate results

### Price Sensitivity
- Duration-only estimates
- Duration + convexity adjustments
- Comparison of estimation methods

## 🔧 Customization

The program can be easily modified to:
- Add new bond types (zero-coupon, floating rate)
- Include additional risk measures
- Support different day-count conventions
- Export results to files

## 📝 License

This program is provided for educational and professional use. Feel free to modify and distribute as needed.

## 🤝 Contributing

Suggestions for improvements or additional features are welcome. Consider adding:
- Yield-to-call calculations
- Option-adjusted duration
- Credit spread analysis
- Portfolio duration calculations

## 📞 Support

For questions about bond pricing theory or calculator usage, refer to standard finance textbooks or consult with a finance professional.

---

**Version:** 1.0  
**Compatibility:** Python 3.6+  
**Last Updated:** June 2025
