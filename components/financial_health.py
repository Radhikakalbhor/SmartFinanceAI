# utils/financial_health.py

from components.calculations import (
    calculate_financial_health,
    financial_status,
    savings_rate,
    investment_rate,
    debt_ratio,
    expense_ratio,
    emergency_fund_months,
)


def generate_financial_report(
    income,
    expenses,
    savings,
    monthly_sip,
    monthly_emi,
):

    score = calculate_financial_health(
        income,
        expenses,
        savings,
        monthly_sip,
        monthly_emi,
    )

    status, icon = financial_status(score)

    report = {
        "health_score": score,
        "status": status,
        "icon": icon,
        "savings_rate": savings_rate(
            income,
            expenses,
        ),
        "investment_rate": investment_rate(
            income,
            monthly_sip,
        ),
        "debt_ratio": debt_ratio(
            income,
            monthly_emi,
        ),
        "expense_ratio": expense_ratio(
            income,
            expenses,
        ),
        "emergency_months": emergency_fund_months(
            savings,
            expenses,
        ),
    }

    recommendations = []

    if report["expense_ratio"] > 70:
        recommendations.append(
            "Reduce monthly expenses to improve cash flow."
        )

    if report["savings_rate"] < 20:
        recommendations.append(
            "Try to save at least 20% of your monthly income."
        )

    if report["investment_rate"] < 10:
        recommendations.append(
            "Increase SIP investments for long-term wealth creation."
        )

    if report["debt_ratio"] > 35:
        recommendations.append(
            "Reduce EMI burden to improve financial stability."
        )

    if report["emergency_months"] < 6:
        recommendations.append(
            "Build an emergency fund covering at least 6 months of expenses."
        )

    if not recommendations:
        recommendations.append(
            "Excellent financial discipline. Keep maintaining your current habits."
        )

    report["recommendations"] = recommendations

    return report


def get_health_color(score):

    if score >= 85:
        return "green"

    elif score >= 70:
        return "lightgreen"

    elif score >= 55:
        return "orange"

    return "red"


def get_progress(score):

    return min(max(score, 0), 100)


def get_risk_level(score):

    if score >= 85:
        return "Low Risk"

    elif score >= 70:
        return "Moderate Risk"

    elif score >= 55:
        return "Medium Risk"

    return "High Risk"