import { apiRequest } from "./api";
import type { StudentRequest, PredictionResponse } from "../types/api";

export async function predictStudent(
  studentData: StudentRequest
): Promise<PredictionResponse> {
  return apiRequest<PredictionResponse>("/predict", {
    method: "POST",
    body: JSON.stringify(studentData),
  });
}