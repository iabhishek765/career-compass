import { apiRequest } from "./api";
import type {
  HistoryReport,
  HistoryReportDetail,
} from "../types/history";

export async function getHistoryReports(): Promise<HistoryReport[]> {
  return apiRequest<HistoryReport[]>("/reports", {
    method: "GET",
  });
}

export async function getHistoryReport(
  reportId: number
): Promise<HistoryReportDetail> {
  return apiRequest<HistoryReportDetail>(`/reports/${reportId}`, {
    method: "GET",
  });
}

export async function deleteHistoryReport(
  reportId: number
): Promise<void> {
  await apiRequest(`/reports/${reportId}`, {
    method: "DELETE",
  });
}