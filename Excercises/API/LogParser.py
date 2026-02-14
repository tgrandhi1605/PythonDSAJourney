class LogParser:
    def __init__(self, log):
        self.log = log

    def fetch_error_codes(self):
        error_codes = []
        log_by_lines = self.log.strip().split("\n")
        print(f"Log lines: {log_by_lines}")

        for line in log_by_lines:
            if "ERROR" in line:
                after_code = line.strip().split("Code:")[1]
                error_code =  after_code.split(" ")[0].strip()

                error_codes.append(error_code)

        return error_codes

if __name__ == "__main__":
    raw_logs = """
    [2026-02-14 10:00] [INFO] System Heartbeat OK
    [2026-02-14 10:05] [ERROR] Code:404 Message:Not Found
    [2026-02-14 10:10] [WARN] High Memory Usage
    [2026-02-14 10:15] [ERROR] Code:500 Message:Internal Server Error
    """

    log_parser = LogParser(raw_logs)
    print(log_parser.fetch_error_codes())


