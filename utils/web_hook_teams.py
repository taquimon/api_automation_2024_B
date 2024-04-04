import pymsteams

from config.config import WEB_HOOK

teams_message = pymsteams.connectorcard(WEB_HOOK)
with open("../reports/markdown/md_report.md") as report:
    report_message = report.read()

print(report_message)
teams_message.text(report_message)
teams_message.send()

