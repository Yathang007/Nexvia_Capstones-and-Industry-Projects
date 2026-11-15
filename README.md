
# Nexvia | Capstones & Industry Projects

A collection of hands-on AI/ML capstone projects focused on building practical, data-driven solutions to real-world engineering problems.

This repository brings together project implementations, experiments, datasets, model outputs, evaluation results, and technical reports developed as part of capstone and industry-oriented learning.

## Projects

### AIML-03 — Large-Scale Personalized Recommendation Engine

A two-stage recommendation system designed to generate personalized movie recommendations.

The system follows an approach commonly used in large-scale recommendation platforms:

- **Candidate Retrieval:** Identifies a relevant set of candidate movies efficiently.
- **Ranking:** Scores and ranks the retrieved candidates to produce personalized recommendations.

**Key areas covered:**
- Data exploration and preprocessing
- Collaborative filtering and baseline recommenders
- Two-Tower retrieval architecture
- FAISS-based candidate generation
- Recommendation ranking and evaluation
- Model diagnostics and performance analysis

**Technologies:** Python, TensorFlow, TensorFlow Recommenders, FAISS, Pandas, NumPy, Scikit-learn.

**Dataset:** MovieLens ml-latest-small.

**Project documentation:** [Large-Scale Personalized Recommendation Engine — Project Report](AIML-03/Large-Scale%20Personalized%20Recommendation%20Engine_Report.pdf)

**Project files:** [`AIML-03/`](AIML-03/)

---

### AIML-04 — Autonomous Driving Perception Stack

An autonomous driving perception project focused on understanding road environments through computer vision and deep learning.

The project explores visual perception using road-scene images, object detection, and object tracking.

**Key areas covered:**
- Dataset preparation and preprocessing
- KITTI-based image dataset handling
- YOLO-based object detection
- Model training and validation
- Detection performance evaluation
- Object tracking experiments
- Visualization of predictions and results

**Technologies:** Python, PyTorch, Ultralytics YOLO, OpenCV, NumPy, Computer Vision.

**Dataset:** KITTI-based road-scene data.

**Project documentation:** [Autonomous Driving Perception Stack — Project Report](AIML-04/Autonomous_Driving_Perception_Stack_Project_Report.pdf)

**Project files:** [`AIML-04/`](AIML-04/)

---

## Repository Structure

```text
Nexvia_Capstones-and-Industry-Projects/
│
├── AIML-03/
│   ├── personalized-recommendation-engine/
│   │   ├── data/
│   │   ├── notebook/
│   │   ├── runs/
│   │   ├── app.py
│   │   └── ...
│   └── Large-Scale Personalized Recommendation Engine_Report.pdf
│
├── AIML-04/
│   ├── autonomous-driving-perception-stack/
│   │   ├── data/
│   │   ├── runs/
│   │   └── ...
│   └── Autonomous_Driving_Perception_Stack_Project_Report.pdf
│
├── .gitignore
└── README.md
```

*Note: The structure above highlights the main project directories. Individual project folders contain additional implementation files, notebooks, datasets, and experiment outputs.*

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Nexvia_Capstones-and-Industry-Projects.git
```

### 2. Navigate to the repository

```bash
cd Nexvia_Capstones-and-Industry-Projects
```

### 3. Choose a project

Navigate into the relevant project directory:

```bash
cd AIML-03/personalized-recommendation-engine
```

Or:

```bash
cd AIML-04/autonomous-driving-perception-stack
```

### 4. Set up the environment

Each project may have its own dependencies and execution requirements. Refer to the project files and report for the relevant setup and implementation details.

## Repository Highlights

- Practical implementation of machine learning and deep learning concepts.
- End-to-end workflows covering data preparation, model development, and evaluation.
- Experiment tracking and performance analysis.
- Application of AI/ML techniques to recommendation systems and autonomous driving perception.
- Technical reports documenting project objectives, methodology, implementation, and results.

## Documentation

Each project includes a dedicated PDF report describing its objectives, methodology, implementation, experiments, and outcomes.

For detailed implementation information, refer to the respective project directory and report.

## About

This repository serves as a technical portfolio of capstone and industry-oriented AI/ML projects, demonstrating practical experience in machine learning, deep learning, recommendation systems, and computer vision.

**Focus Areas:** Artificial Intelligence | Machine Learning | Deep Learning | Recommendation Systems | Computer Vision | Autonomous Driving

---

*Built with curiosity, experimentation, and a focus on practical engineering.*
