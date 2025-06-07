from _typeshed import Incomplete
from office365.reports.report import Report as Report
from office365.reports.root import ReportRoot as ReportRoot
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.queries.function import FunctionQuery as FunctionQuery

def create_report_query(
    report_root,
    report_name,
    period: Incomplete | None = None,
    return_stream: bool = False,
): ...
