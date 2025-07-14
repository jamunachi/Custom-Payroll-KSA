# Custom Payroll KSA (IFRS-Ready)

This ERPNext app provides End of Service Benefit (EOSB) calculation and accounting logic based on IFRS (IAS 19).

## Features
- EOSB base calculation using tagged salary components
- Monthly provision based on straight-line accrual (0.0833 of salary)
- Hooked into Salary Slip generation (before insert)
- Extendable for Journal Entry routing per component

## Installation
```bash
cd frappe-bench/apps/
git clone https://github.com/YOUR_GITHUB_USERNAME/custom_payroll_ksa.git
cd ../../
bench --site yoursite install-app custom_payroll_ksa
```
## Required Custom Fields
- `custom_include_in_eosb` (Checkbox) on Salary Component
- `eosb_amount` (Currency) on Salary Slip
- `eosb_monthly_accrual` (Currency) on Salary Slip

## License
MIT