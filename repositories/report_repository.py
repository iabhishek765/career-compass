import json

from src.database.database import get_connection


class ReportRepository:

    @staticmethod
    def save_report(report_data: dict):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO assessment_reports (

                prediction,

                confidence,

                career_report,

                career_path,

                recommended_courses,

                recommended_projects,

                recommended_certifications,

                skills_to_improve,

                student_answers

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (

                report_data["prediction"],

                report_data["confidence"],

                report_data["career_report"],

                json.dumps(report_data["career_path"]),

                json.dumps(report_data["recommended_courses"]),

                json.dumps(report_data["recommended_projects"]),

                json.dumps(report_data["recommended_certifications"]),

                json.dumps(report_data["skills_to_improve"]),

                json.dumps(report_data["student_answers"]),

            ),
        )

        connection.commit()

        report_id = cursor.lastrowid

        connection.close()

        return report_id


    @staticmethod
    def get_all_reports():

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
        SELECT
            id,
            prediction,
            confidence,
            created_at
        FROM assessment_reports
        ORDER BY created_at DESC
        """
        )

        reports = cursor.fetchall()

        connection.close()

        return reports



    @staticmethod
    def get_report_by_id(report_id: int):
    
        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
        SELECT *
        FROM assessment_reports
        WHERE id = ?
        """,
        (report_id,)
    )
        report = cursor.fetchone()

        connection.close()

        if report is None:
            return None


        # Convert sqlite3.Row into a normal dictionary
        report = dict(report)

        report["career_path"] = json.loads(report["career_path"])
        report["recommended_courses"] = json.loads(report["recommended_courses"])
        report["recommended_projects"] = json.loads(report["recommended_projects"])
        report["recommended_certifications"] = json.loads(
            report["recommended_certifications"]
        )

        report["skills_to_improve"] = json.loads(report["skills_to_improve"])
        report["student_answers"] = json.loads(report["student_answers"])

        return report


            



    @staticmethod
    def delete_report(report_id: int):


        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
        DELETE FROM assessment_reports
        WHERE id = ?
        """,
        (report_id,)
        )

        connection.commit()

        connection.close()


    
    

