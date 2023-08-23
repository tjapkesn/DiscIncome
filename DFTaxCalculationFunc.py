import pandas as pd
def ThresholdizeIncome(Income, threshold_list):
    if Income <= threshold_list[0]:
        return [Income]
    amnts = []
    amnts.append(threshold_list[0])
    for i in range(1,len(threshold_list)):
        if Income >= threshold_list[i]:
            amnts.append(threshold_list[i]-threshold_list[i-1])
        else:
            amnts.append(Income - threshold_list[i-1])
            break
    return amnts
def ApplyMarginalRates(ThresholdizedIncome, MR_list):
    tax = 0
    for i in range(len(ThresholdizedIncome)):
        tax += ThresholdizedIncome[i]*MR_list[i]
    return tax
def CalculateTax(country_row, income_find = "decile", threshold_find = "threshold", rate_find = "marginal"):
    working_row = country_row.dropna()
    income_list = working_row[[key for key in working_row.keys if income_find in key]]
    threshold_list = working_row[[key for key in working_row.keys if threshold_find in key]]
    rate_list = working_row[[key for key in working_row.keys if rate_find in key]]
    for key in income_list.keys:
        ti = ThresholdizeIncome(income_list[key], threshold_list= threshold_list)
        tax = ApplyMarginalRates(ti, rate_list)
        country_row[key] = tax
    return country_row

