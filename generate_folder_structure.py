import os

# Define the folder and file structure
project_structure = {
    "config": ["configuration.py"],
    "entity": ["config_entity.py"],
    "components": [
        "data_ingestion.py",
        "data_validation.py",
        "data_transformation.py",
        "model_trainer.py",
        "model_evaluation.py"
    ],
    "pipeline": [
        "stage_01_data_ingestion.py",
        "stage_02_data_validation.py",
        "stage_03_data_transformation.py",
        "stage_04_model_trainer.py",
        "stage_05_model_evaluation.py"
    ],
    "artifacts": [".gitkeep"],
    "logs": ["running_logs.log"]
}

# Files at the root level
root_files = [
    "schema.yaml",
    "config.yaml",
    "params.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "README.md"
]

def create_structure(base_path="."):
    # Create folders and files
    for folder, files in project_structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, "w") as f:
                f.write("")

    # Create root-level files
    for file in root_files:
        file_path = os.path.join(base_path, file)
        with open(file_path, "w") as f:
            f.write("")

    print("✅ Project structure created successfully.")

if __name__ == "__main__":
    create_structure()
