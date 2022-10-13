import json
import pandas as pd


def anomalies_helper(data, flag):
    trained_model = {}
    with open("trained_model.txt", "r") as file:
        trained_model = json.loads(file.read())

    flag_analysis = data[data["status"] == flag]
    outliers = flag_analysis[
        flag_analysis["f1_"]
        > trained_model[flag]["Q3"] + 1.5 * trained_model[flag]["IQR"]
    ]["f1_"].count()

    return (flag, outliers >= 1)


def inspect_anomalies(data):
    transactions = pd.read_csv(data)
    denied = anomalies_helper(transactions, "denied")
    reversed = anomalies_helper(transactions, "reversed")
    failed = anomalies_helper(transactions, "failed")
    return [denied, reversed, failed]
