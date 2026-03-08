from crewai import Crew, Process

from agents import (
    refund_agent,
    logistics_agent,
    pattern_agent,
    marketplace_agent,
    report_agent
)

from tasks import (
    refund_analysis_task,
    logistics_validation_task,
    pattern_detection_task,
    marketplace_investigation_task,
    report_task
)


fraud_detection_crew = Crew(

    agents=[
        refund_agent,
        logistics_agent,
        pattern_agent,
        marketplace_agent,
        report_agent
    ],

    tasks=[
        refund_analysis_task,
        logistics_validation_task,
        pattern_detection_task,
        marketplace_investigation_task,
        report_task
    ],

    process=Process.sequential,

    verbose=True
)