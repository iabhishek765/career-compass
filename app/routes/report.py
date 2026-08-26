from fastapi import APIRouter

from repositories.report_repository import ReportRepository

router = APIRouter(
    prefix="/reports",
    tags=["Report History"]
)


@router.get("/")
def get_all_reports():
    reports = ReportRepository.get_all_reports()

    return reports

@router.get("/{report_id}")
def get_report(report_id: int):

    report = ReportRepository.get_report_by_id(report_id)

    if report is None:
        return {"message": "Report not found"}

    return report

@router.delete("/{report_id}")
def delete_report(report_id: int):

    ReportRepository.delete_report(report_id)

    return {
        "message": "Report deleted successfully",
        "report_id": report_id
    }