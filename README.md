# 3D Rectangular Prism Viewer

This application allows users to visualize and analyze 3D models of rectangular prisms. It uses PyQt5 for the GUI and PythonOCC for 3D CAD visualization.

## Installation

1. Install Anaconda or Miniconda if you haven't already:
   https://docs.conda.io/en/latest/miniconda.html

2. Create a new conda environment:
   ```
   conda create -n prism-viewer python=3.8
   ```

3. Activate the environment:
   ```
   conda activate prism-viewer
   ```

4. Install PythonOCC-Core:
   ```
   conda install -c conda-forge pythonocc-core
   ```

5. Clone this repository:
   ```
   git clone https://github.com/yourusername/RectangularPrismViewer.git
   ```

6. Navigate to the project directory:
   ```
   cd RectangularPrismViewer
   ```

7. Install the remaining required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you've activated the conda environment:
   ```
   conda activate prism-viewer
   ```

2. Run the main application:
   ```
   python main.py
   ```

3. Use the dropdown menu to select a prism.
4. View the calculated surface area and volume.
5. Click the "Visualize 3D Model" button to see the 3D representation of the prism.

## Development

- `main.py`: Contains the main application logic and GUI setup.
- `prism_calculator.py`: Includes the PrismCalculator class for surface area and volume calculations.
- `draw_rectangular_prism.py`: Contains functions for creating 3D prism shapes.
- `prisms.db`: SQLite database storing prism dimensions.

## Creating an Executable

To create an executable, use PyInstaller:

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Create the executable:
   ```
   pyinstaller --onefile --windowed main.py
   ```

The executable will be created in the `dist` directory.

## Troubleshooting

If you encounter any issues with PythonOCC-Core, ensure you're using a compatible version of Python (3.7 or 3.8 are recommended). You may also need to install additional system libraries depending on your operating system.

## License

This project is licensed under the MIT License.
'''
    create_file(os.path.join(project_dir, "README.md"), readme_content)

    print(f"Project structure created in '{project_dir}' directory.")
    print("Please follow the installation instructions in the README.md file.")

if __name__ == "__main__":
    create_project_structure()