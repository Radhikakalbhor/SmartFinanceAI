# components/calculations.py

def calculate_financial_health(
    income,
    expenses,
    savings,
    monthly_sip,
    monthly_emi
):
    score = 0

    # Savings Ratio (40 Marks)
    if income > 0:
        savings_ratio = (income - expenses) / income
    else:
        savings_ratio = 0

    if savings_ratio >= 0.40:
        score += 40
    elif savings_ratio >= 0.30:
        score += 35
    elif savings_ratio >= 0.20:
        score += 25
    elif savings_ratio >= 0.10:
        score += 15
    else:
        score += 5

    # Emergency Savings (20 Marks)
    if expenses > 0:
        emergency_months = savings / expenses
    else:
        emergency_months = 0

    if emergency_months >= 6:
        score += 20
    elif emergency_months >= 4:
        score += 15
    elif emergency_months >= 2:
        score += 10
    else:
        score += 5

    # Investment Score (20 Marks)
    if income > 0:
        sip_ratio = monthly_sip / income
    else:
        sip_ratio = 0

    if sip_ratio >= 0.20:
        score += 20
    elif sip_ratio >= 0.15:
        score += 15
    elif sip_ratio >= 0.10:
        score += 10
    elif sip_ratio >= 0.05:
        score += 5

    # EMI Score (20 Marks)
    if income > 0:
        emi_ratio = monthly_emi / income
    else:
        emi_ratio = 0

    if emi_ratio <= 0.20:
        score += 20
    elif emi_ratio <= 0.30:
        score += 15
    elif emi_ratio <= 0.40:
        score += 10
    else:
        score += 5

    return round(score, 1)


def financial_status(score):

    if score >= 85:
        return "Excellent", "🟢"

    elif score >= 70:
        return "Good", "🟢"

    elif score >= 55:
        return "Average", "🟡"

    elif score >= 40:
        return "Needs Improvement", "🟠"

    return "Critical", "🔴"


def savings_rate(income, expenses):

    if income == 0:
        return 0

    return round(((income - expenses) / income) * 100, 2)


def investment_rate(income, monthly_sip):

    if income == 0:
        return 0

    return round((monthly_sip / income) * 100, 2)


def debt_ratio(income, monthly_emi):

    if income == 0:
        return 0

    return round((monthly_emi / income) * 100, 2)


def expense_ratio(income, expenses):

    if income == 0:
        return 0

    return round((expenses / income) * 100, 2)


def emergency_fund_months(
    savings,
    expenses
):

    if expenses == 0:
        return 0

    return round(savings / expenses, 1)