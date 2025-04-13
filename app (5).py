import gradio as gr
import cv2
import numpy as np
import datetime
import random
from fpdf import FPDF
import time

# Quantum Simulation Logic
class QuantumSim:
    def __init__(self):
        self.states = {
            "000": "Payment encrypted & approved",
            "010": "Fraud suspicion: Biometric mismatch",
            "001": "Fraud suspicion: Location tampering"
        }

    def evaluate_transaction(self):
        return random.choice(list(self.states.items()))

# Computer Vision & Damage/Injury Detection
class CVProcessor:
    def extract_vehicle_number(self, image_np):
        # Bypass OCR
        return "DL3CAB1234"  # Dummy number

    def detect_damage_severity(self, image_np):
        if image_np is None:
            return "No image provided"
        damage_score = np.random.randint(1, 10)
        if damage_score > 7:
            return "Severe"
        elif damage_score > 4:
            return "Moderate"
        else:
            return "Minor"

    def detect_person_injury(self, image_np):
        if image_np is None:
            return "No image provided"
        injury_score = np.random.randint(0, 2)
        return "Critical" if injury_score else "Stable"

# Insurance Automation Agent
class InsuranceAgent:
    def __init__(self):
        self.qsim = QuantumSim()
        self.cv = CVProcessor()
        self.reports = []

    def simulate_live_camera_feed(self):
        print("[Agent] Watching live feed... analyzing frame by frame.")
        for i in range(3):  # Simulate 3 frames
            dummy_frame = np.ones((480, 640, 3), dtype=np.uint8) * np.random.randint(0, 255)
            report = self.process_frame(dummy_frame)
            self.reports.append(report)
            time.sleep(2)

    def process_frame(self, frame):
        vehicle_number = self.cv.extract_vehicle_number(frame)
        damage = self.cv.detect_damage_severity(frame)
        injury = self.cv.detect_person_injury(frame)
        q_code, status = self.qsim.evaluate_transaction()

        response = {
            "Time": str(datetime.datetime.now()),
            "Vehicle Number": vehicle_number,
            "Damage Level": damage,
            "Injury Level": injury,
            "Quantum Status": status,
            "Code": q_code,
            "Hospital Notified": "Yes" if damage in ["Severe", "Moderate"] else "No",
            "Tow Vehicle Dispatched": "Yes",
            "IRDA Notified": "Yes" if "Fraud" in status else "No",
            "Final Status": "Auto Approved" if "approved" in status else "Under Investigation"
        }

        self.generate_pdf_report(response)
        self.notify_services(response)
        print("[Debug] Frame Processed:", response)
        return response

    def generate_pdf_report(self, data):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Auto Insurance Claim Report", ln=True, align='C')
        for key, value in data.items():
            pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
        filename = f"Claim_Report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        pdf.output(filename)
        print(f"[Agent] Report generated: {filename}")

    def notify_services(self, data):
        print(f"[Hospital] Emergency Level: {data['Injury Level']} → Ambulance dispatched.")
        print(f"[Tow Vehicle] Vehicle #{data['Vehicle Number']} scheduled for towing.")
        if data["IRDA Notified"] == "Yes":
            print("[IRDA] Fraud suspected. Penalty log initiated.")

# Gradio UI
agent = InsuranceAgent()

def start_agent_simulation():
    print("[Debug] Starting simulation...")
    agent.reports = []
    agent.simulate_live_camera_feed()
    all_reports_text = ""
    for i, report in enumerate(agent.reports):
        all_reports_text += f"--- Report {i+1} ---\n"
        for key, value in report.items():
            all_reports_text += f"{key}: {value}\n"
        all_reports_text += "\n"
    return all_reports_text

with gr.Blocks() as iface:
    gr.Markdown("# No-Ops AI Agent for Road Accident Management")
    with gr.Column():
        start_button = gr.Button("Start Agent Simulation")
        report_output = gr.Textbox(label="Agent Activity and Reports", lines=20)

    start_button.click(start_agent_simulation, outputs=report_output)

iface.launch()
