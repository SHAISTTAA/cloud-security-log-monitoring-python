import pandas as pd

def load_logs(file_path):

    print("Loading log data...")

    df = pd.read_csv(file_path)

    return df


def detect_bruteforce(df):

    print("Analyzing login attempts...")

    failed = df[df["status"] == "failed"]

    suspicious = failed.groupby("ip_address").size()

    suspicious_ips = suspicious[suspicious > 3]

    return suspicious_ips


def main():

    logs = load_logs("logs/server_logs.csv")

    suspicious = detect_bruteforce(logs)

    print("\nSuspicious IP addresses")

    print(suspicious)


if __name__ == "__main__":
    main()
